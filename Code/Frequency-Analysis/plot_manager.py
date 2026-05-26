"""
plot_manager.py
---------------
Manages all Matplotlib figures embedded inside the PyQt5 window.

Design:
  - One PlotManager per transform tab (DTFT / DFT / FFT).
  - Each manager owns a Figure with 3 subplots stacked vertically:
      [0] Time-domain signal
      [1] Magnitude spectrum
      [2] Phase spectrum
  - clear() + redraw() pattern keeps the axes fresh on every update.
"""

import numpy as np
import matplotlib
matplotlib.use("Qt5Agg")                          # render into Qt widgets

from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar


# ── colour palette (dark theme) ────────────────────────────────────────────────
DARK_BG     = "#1a1a2e"    # figure / axes background
PANEL_BG    = "#16213e"    # slightly lighter for axes face
GRID_COLOR  = "#2a2a4a"
TEXT_COLOR  = "#e0e0f0"

SIGNAL_COLOR = "#00d4ff"   # cyan  — time domain
MAG_COLOR    = "#ff6b6b"   # coral — magnitude
PHASE_COLOR  = "#ffd166"   # amber — phase
ACCENT       = "#06ffa5"   # green — comparison highlight


def _style_axes(ax, title: str, xlabel: str, ylabel: str):
    """Apply dark-theme styling to a single Axes object."""
    ax.set_facecolor(PANEL_BG)
    ax.set_title(title, color=TEXT_COLOR, fontsize=10, pad=6)
    ax.set_xlabel(xlabel, color=TEXT_COLOR, fontsize=8)
    ax.set_ylabel(ylabel, color=TEXT_COLOR, fontsize=8)
    ax.tick_params(colors=TEXT_COLOR, labelsize=7)
    ax.grid(True, color=GRID_COLOR, linewidth=0.5, linestyle="--")
    for spine in ax.spines.values():
        spine.set_edgecolor(GRID_COLOR)


class PlotManager:
    """
    Creates and manages a Matplotlib canvas with three stacked subplots.

    Parameters
    ----------
    parent : QWidget
        The Qt parent widget (the tab page).
    transform_label : str
        Short label used in subplot titles (e.g. "DTFT", "DFT", "FFT").
    """

    def __init__(self, parent=None, transform_label: str = "Transform"):
        self.transform_label = transform_label

        # --- Matplotlib Figure ---
        self.figure = Figure(figsize=(9, 7), facecolor=DARK_BG, tight_layout=True)
        self.canvas = FigureCanvas(self.figure)
        self.canvas.setParent(parent)

        # Navigation toolbar gives zoom / pan / save for free
        self.toolbar = NavigationToolbar(self.canvas, parent)
        self.toolbar.setStyleSheet("background-color: #1a1a2e; color: #e0e0f0;")

        # Create 3 subplots
        self.ax_time, self.ax_mag, self.ax_phase = self.figure.subplots(
            3, 1, sharex=False
        )
        self._init_axes()

    # ------------------------------------------------------------------ init
    def _init_axes(self):
        _style_axes(self.ax_time,  "Time-Domain Signal",     "Time (s)",       "Amplitude")
        _style_axes(self.ax_mag,   f"{self.transform_label} – Magnitude",  "Frequency",  "|X|")
        _style_axes(self.ax_phase, f"{self.transform_label} – Phase",       "Frequency",  "Phase (°)")

    # ------------------------------------------------------------------ update
    def update_time(self, t: np.ndarray, x: np.ndarray):
        """Plot the time-domain signal."""
        self.ax_time.cla()
        _style_axes(self.ax_time, "Time-Domain Signal", "Time (s)", "Amplitude")
        self.ax_time.plot(t, x, color=SIGNAL_COLOR, linewidth=1.2, label="x[n]")
        self.ax_time.axhline(0, color=GRID_COLOR, linewidth=0.5)
        # Mark individual samples as dots
        self.ax_time.scatter(t, x, color=SIGNAL_COLOR, s=10, zorder=3, alpha=0.7)
        self.ax_time.legend(fontsize=7, facecolor=PANEL_BG, labelcolor=TEXT_COLOR,
                            edgecolor=GRID_COLOR)

    def _styled_stem(self, ax, freq, values, color):
        """
        Draw a stem plot and style it in a way compatible with both older
        Matplotlib (stemlines is a list of Line2D) and newer versions
        (stemlines is a LineCollection).
        """
        container = ax.stem(freq, values, linefmt=color, markerfmt="o", basefmt=" ")
        markerline, stemlines, _ = container
        markerline.set_color(color)
        markerline.set_markersize(3)
        # stemlines is a LineCollection in Matplotlib ≥ 3.5
        try:
            stemlines.set_color(color)
            stemlines.set_linewidth(0.8)
        except AttributeError:
            # older API: iterable of Line2D
            for line in stemlines:
                line.set_color(color)
                line.set_linewidth(0.8)

    def update_magnitude(self, freq: np.ndarray, mag: np.ndarray,
                         xlabel: str = "Frequency"):
        """Plot the magnitude spectrum."""
        self.ax_mag.cla()
        _style_axes(self.ax_mag, f"{self.transform_label} – Magnitude Spectrum",
                    xlabel, "|X| (normalised)")
        self._styled_stem(self.ax_mag, freq, mag, MAG_COLOR)

    def update_phase(self, freq: np.ndarray, phase: np.ndarray,
                     xlabel: str = "Frequency"):
        """Plot the phase spectrum."""
        self.ax_phase.cla()
        _style_axes(self.ax_phase, f"{self.transform_label} – Phase Spectrum",
                    xlabel, "Phase (°)")
        self._styled_stem(self.ax_phase, freq, phase, PHASE_COLOR)

    def refresh(self):
        """Redraw the canvas after all data has been set."""
        self.figure.tight_layout(pad=1.5)
        self.canvas.draw()


# ── Comparison plot (DFT vs FFT timing) ───────────────────────────────────────

class ComparisonPlotManager:
    """
    A standalone Figure that shows DFT vs FFT computation-time comparison
    as a bar chart over a range of signal lengths.
    """

    def __init__(self, parent=None):
        self.figure = Figure(figsize=(9, 4), facecolor=DARK_BG, tight_layout=True)
        self.canvas = FigureCanvas(self.figure)
        self.canvas.setParent(parent)
        self.toolbar = NavigationToolbar(self.canvas, parent)
        self.toolbar.setStyleSheet("background-color: #1a1a2e; color: #e0e0f0;")
        self.ax = self.figure.add_subplot(1, 1, 1)
        _style_axes(self.ax, "DFT vs FFT — Execution Time", "Signal Length (N)",
                    "Time (ms)")

    def plot(self, sizes, dft_times, fft_times):
        self.ax.cla()
        _style_axes(self.ax, "DFT vs FFT — Execution Time Comparison",
                    "Signal Length (N)", "Time (ms)")
        x = np.arange(len(sizes))
        width = 0.35
        self.ax.bar(x - width / 2, [t * 1000 for t in dft_times],
                    width, label="Manual DFT  O(N²)", color=MAG_COLOR, alpha=0.85)
        self.ax.bar(x + width / 2, [t * 1000 for t in fft_times],
                    width, label="NumPy FFT   O(N log N)", color=ACCENT, alpha=0.85)
        self.ax.set_xticks(x)
        self.ax.set_xticklabels([str(s) for s in sizes], color=TEXT_COLOR, fontsize=8)
        self.ax.legend(fontsize=8, facecolor=PANEL_BG, labelcolor=TEXT_COLOR,
                       edgecolor=GRID_COLOR)
        self.figure.tight_layout(pad=1.5)
        self.canvas.draw()
