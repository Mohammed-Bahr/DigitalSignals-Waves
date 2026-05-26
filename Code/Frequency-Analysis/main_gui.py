"""
main_gui.py
-----------
Main PyQt5 application window.

Layout overview
───────────────
┌──────────────────────────────────────────────────────────────────┐
│  DSP Visualizer                                   [dark header]  │
├──────────────────────────────────────────────────────────────────┤
│  LEFT PANEL (controls)   │  RIGHT PANEL (tab plots)             │
│  ─────────────────────   │  ┌─────────────────────────────────┐ │
│  Signal Type   [combo]   │  │ DTFT │ DFT │ FFT │ Compare │    │ │
│  Frequency     [slider]  │  │                                 │ │
│  Amplitude     [slider]  │  │   Matplotlib canvas here        │ │
│  Sampling Freq [slider]  │  │                                 │ │
│  Num Samples   [slider]  │  └─────────────────────────────────┘ │
│  Phase         [slider]  │                                       │
│  ─────────────────────   │                                       │
│  Custom Signal [text]    │                                       │
│  [Update] [Export]       │                                       │
│  DFT/FFT timing label    │                                       │
└──────────────────────────────────────────────────────────────────┘
"""

import sys
import os
import time
import numpy as np

from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout,
    QLabel, QComboBox, QSlider, QPushButton, QTabWidget,
    QTextEdit, QGroupBox, QSplitter, QFileDialog, QMessageBox,
    QSizePolicy
)
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QFont, QPalette, QColor

from signal_generator import SignalGenerator
from fourier_transforms import FourierTransforms
from plot_manager import PlotManager, ComparisonPlotManager


# ── Stylesheet ─────────────────────────────────────────────────────────────────

DARK_STYLE = """
QMainWindow, QWidget {
    background-color: #0f0f1a;
    color: #e0e0f0;
    font-family: "Segoe UI", "Ubuntu", sans-serif;
    font-size: 12px;
}

QGroupBox {
    border: 1px solid #2a2a4a;
    border-radius: 6px;
    margin-top: 10px;
    padding: 8px;
    font-weight: bold;
    color: #00d4ff;
}
QGroupBox::title {
    subcontrol-origin: margin;
    left: 10px;
    padding: 0 4px;
}

QLabel {
    color: #b0b0d0;
}
QLabel#value_label {
    color: #00d4ff;
    font-weight: bold;
    min-width: 60px;
}

QSlider::groove:horizontal {
    height: 4px;
    background: #2a2a4a;
    border-radius: 2px;
}
QSlider::handle:horizontal {
    width: 14px; height: 14px;
    border-radius: 7px;
    background: #00d4ff;
    margin: -5px 0;
}
QSlider::sub-page:horizontal {
    background: #006688;
    border-radius: 2px;
}

QComboBox {
    background-color: #16213e;
    border: 1px solid #2a2a4a;
    border-radius: 4px;
    padding: 4px 8px;
    color: #e0e0f0;
}
QComboBox::drop-down { border: none; }
QComboBox QAbstractItemView {
    background-color: #16213e;
    selection-background-color: #006688;
    color: #e0e0f0;
}

QPushButton {
    background-color: #16213e;
    border: 1px solid #00d4ff;
    border-radius: 5px;
    padding: 6px 14px;
    color: #00d4ff;
    font-weight: bold;
}
QPushButton:hover  { background-color: #006688; color: #ffffff; }
QPushButton:pressed { background-color: #004455; }

QPushButton#run_btn {
    background-color: #004455;
    border-color: #06ffa5;
    color: #06ffa5;
}
QPushButton#run_btn:hover { background-color: #006644; }

QTabWidget::pane {
    border: 1px solid #2a2a4a;
    background-color: #0f0f1a;
}
QTabBar::tab {
    background: #16213e;
    border: 1px solid #2a2a4a;
    padding: 6px 16px;
    color: #888;
    border-top-left-radius: 5px;
    border-top-right-radius: 5px;
    margin-right: 2px;
}
QTabBar::tab:selected {
    background: #0f0f1a;
    color: #00d4ff;
    border-bottom-color: #0f0f1a;
    font-weight: bold;
}

QTextEdit {
    background-color: #16213e;
    border: 1px solid #2a2a4a;
    border-radius: 4px;
    color: #e0e0f0;
    font-family: "Consolas", "Courier New", monospace;
    font-size: 11px;
}

QScrollBar:vertical {
    background: #16213e;
    width: 8px;
}
QScrollBar::handle:vertical { background: #2a2a4a; border-radius: 4px; }
"""

# ── Helper widget ──────────────────────────────────────────────────────────────

class LabelledSlider(QWidget):
    """
    A horizontal slider with a label on the left and a value readout on the right.
    Internally stores floats by mapping to an integer range.
    """

    def __init__(self, label: str, min_val: float, max_val: float,
                 initial: float, step: float = 1.0, decimals: int = 0,
                 callback=None, parent=None):
        super().__init__(parent)
        self._min = min_val
        self._max = max_val
        self._step = step
        self._decimals = decimals
        self._callback = callback

        # Integer range derived from float range / step
        int_range = int(round((max_val - min_val) / step))

        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)

        self.name_label = QLabel(label)
        self.name_label.setFixedWidth(110)
        layout.addWidget(self.name_label)

        self.slider = QSlider(Qt.Horizontal)
        self.slider.setRange(0, int_range)
        self.slider.setValue(int(round((initial - min_val) / step)))
        self.slider.valueChanged.connect(self._on_change)
        layout.addWidget(self.slider)

        self.val_label = QLabel(self._fmt(initial))
        self.val_label.setObjectName("value_label")
        self.val_label.setFixedWidth(65)
        self.val_label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        layout.addWidget(self.val_label)

    def _fmt(self, v):
        return f"{v:.{self._decimals}f}"

    def _on_change(self, int_val):
        v = self._min + int_val * self._step
        self.val_label.setText(self._fmt(v))
        if self._callback:
            self._callback(v)

    def value(self) -> float:
        return self._min + self.slider.value() * self._step

    def set_value(self, v: float):
        self.slider.setValue(int(round((v - self._min) / self._step)))


# ── Main Window ────────────────────────────────────────────────────────────────

class DSPMainWindow(QMainWindow):
    """
    Top-level application window.

    Responsibilities:
    - Build the full UI layout.
    - Wire controls to signal/transform computation.
    - Delegate plot updates to PlotManager instances.
    """

    def __init__(self):
        super().__init__()
        self.setWindowTitle("DSP Visualizer — DTFT · DFT · FFT")
        self.resize(1400, 820)
        self.setStyleSheet(DARK_STYLE)

        # ── Core objects ────────────────────────────────────────────────────
        self.generator = SignalGenerator(
            frequency=5.0, amplitude=1.0, fs=100.0,
            n_samples=128, phase=0.0, duty_cycle=0.5
        )
        self.ft = FourierTransforms()

        # Current signal arrays (updated on every change)
        self._t = np.array([])
        self._x = np.array([])

        # ── Build UI ────────────────────────────────────────────────────────
        central = QWidget()
        self.setCentralWidget(central)
        root_layout = QHBoxLayout(central)
        root_layout.setContentsMargins(8, 8, 8, 8)
        root_layout.setSpacing(8)

        # Left control panel
        left = self._build_control_panel()
        left.setFixedWidth(300)
        root_layout.addWidget(left)

        # Right tab area
        right = self._build_tab_area()
        root_layout.addWidget(right, stretch=1)

        # ── Initial render ───────────────────────────────────────────────────
        self._update_all()

    # ================================================================ UI builders

    def _build_control_panel(self):
        panel = QWidget()
        layout = QVBoxLayout(panel)
        layout.setSpacing(10)

        # --- Signal type ---
        grp_type = QGroupBox("Signal Type")
        grp_layout = QVBoxLayout(grp_type)
        self.signal_combo = QComboBox()
        self.signal_combo.addItems(
            ["Sine Wave", "Cosine Wave", "Square Wave", "Impulse", "Random Signal", "Custom"]
        )
        self.signal_combo.currentIndexChanged.connect(self._on_signal_changed)
        grp_layout.addWidget(self.signal_combo)
        layout.addWidget(grp_type)

        # --- Parameters ---
        grp_params = QGroupBox("Signal Parameters")
        p_layout = QVBoxLayout(grp_params)

        self.sl_freq = LabelledSlider("Frequency (Hz)", 0.5, 50.0, 5.0,
                                      step=0.5, decimals=1,
                                      callback=lambda v: self._set_param("frequency", v))
        self.sl_amp  = LabelledSlider("Amplitude",      0.1, 5.0,  1.0,
                                      step=0.1, decimals=1,
                                      callback=lambda v: self._set_param("amplitude", v))
        self.sl_fs   = LabelledSlider("Sampling Fs (Hz)", 10, 500, 100,
                                      step=10, decimals=0,
                                      callback=lambda v: self._set_param("fs", v))
        self.sl_N    = LabelledSlider("Num Samples",    16, 512, 128,
                                      step=16, decimals=0,
                                      callback=lambda v: self._set_param("n_samples", int(v)))
        self.sl_phase = LabelledSlider("Phase (°)",     -180, 180, 0,
                                       step=5, decimals=0,
                                       callback=lambda v: self._set_param(
                                           "phase", float(v) * np.pi / 180))

        for sl in [self.sl_freq, self.sl_amp, self.sl_fs, self.sl_N, self.sl_phase]:
            p_layout.addWidget(sl)
        layout.addWidget(grp_params)

        # --- Custom signal input ---
        grp_custom = QGroupBox("Custom Signal Values")
        c_layout = QVBoxLayout(grp_custom)
        c_layout.addWidget(QLabel("Comma-separated samples:"))
        self.custom_edit = QTextEdit()
        self.custom_edit.setPlaceholderText("e.g.  1, 0.5, 0, -0.5, -1, -0.5, 0, 0.5")
        self.custom_edit.setFixedHeight(60)
        c_layout.addWidget(self.custom_edit)
        layout.addWidget(grp_custom)

        # --- Buttons ---
        grp_btn = QGroupBox("Actions")
        b_layout = QVBoxLayout(grp_btn)

        btn_update = QPushButton("⟳  Update Plots")
        btn_update.clicked.connect(self._update_all)
        b_layout.addWidget(btn_update)

        btn_compare = QPushButton("⏱  Run DFT vs FFT Timing")
        btn_compare.setObjectName("run_btn")
        btn_compare.clicked.connect(self._run_comparison)
        b_layout.addWidget(btn_compare)

        btn_export = QPushButton("💾  Export Plots (PNG)")
        btn_export.clicked.connect(self._export_plots)
        b_layout.addWidget(btn_export)

        layout.addWidget(grp_btn)

        # --- Timing readout ---
        grp_time = QGroupBox("Transform Timing")
        t_layout = QVBoxLayout(grp_time)
        self.lbl_dft_time = QLabel("DFT time: —")
        self.lbl_fft_time = QLabel("FFT time: —")
        self.lbl_speedup  = QLabel("Speedup:  —")
        for lbl in [self.lbl_dft_time, self.lbl_fft_time, self.lbl_speedup]:
            lbl.setStyleSheet("color: #06ffa5; font-family: monospace;")
            t_layout.addWidget(lbl)
        layout.addWidget(grp_time)

        layout.addStretch()
        return panel

    def _build_tab_area(self):
        self.tabs = QTabWidget()

        # Create one PlotManager per tab
        self.pm_dtft    = PlotManager(transform_label="DTFT")
        self.pm_dft     = PlotManager(transform_label="DFT")
        self.pm_fft     = PlotManager(transform_label="FFT")
        self.pm_compare = ComparisonPlotManager()

        for pm, label in [(self.pm_dtft, "📈 DTFT"),
                          (self.pm_dft,  "📊 DFT"),
                          (self.pm_fft,  "⚡ FFT"),
                          (None,         "⏱ Compare")]:
            page = QWidget()
            page_layout = QVBoxLayout(page)
            page_layout.setContentsMargins(4, 4, 4, 4)

            if pm is not None:
                page_layout.addWidget(pm.toolbar)
                page_layout.addWidget(pm.canvas)
            else:
                page_layout.addWidget(self.pm_compare.toolbar)
                page_layout.addWidget(self.pm_compare.canvas)
                # Instruction label
                info = QLabel(
                    "Click  ⏱ Run DFT vs FFT Timing  in the left panel\n"
                    "to benchmark manual DFT against NumPy FFT for various N."
                )
                info.setAlignment(Qt.AlignCenter)
                info.setStyleSheet("color: #888; font-size: 11px;")
                page_layout.addWidget(info)

            self.tabs.addTab(page, label)

        return self.tabs

    # ================================================================ slot helpers

    def _set_param(self, attr: str, value):
        """Update one attribute on the generator then refresh all plots."""
        setattr(self.generator, attr, value)
        self._update_all()

    def _on_signal_changed(self, idx):
        """Called when the signal-type combo changes."""
        self._update_all()

    # ================================================================ core update

    def _get_signal(self):
        """Dispatch to the correct generator method based on the combo selection."""
        sig_type = self.signal_combo.currentText()
        if sig_type == "Sine Wave":
            return self.generator.sine_wave()
        elif sig_type == "Cosine Wave":
            return self.generator.cosine_wave()
        elif sig_type == "Square Wave":
            return self.generator.square_wave()
        elif sig_type == "Impulse":
            return self.generator.impulse()
        elif sig_type == "Random Signal":
            return self.generator.random_signal()
        elif sig_type == "Custom":
            text = self.custom_edit.toPlainText().strip()
            if not text:
                return self.generator.sine_wave()   # fallback
            try:
                return self.generator.custom_signal(text)
            except ValueError:
                QMessageBox.warning(self, "Parse Error",
                                    "Could not parse custom signal.\n"
                                    "Use comma-separated numbers, e.g. 1, 0.5, -1")
                return self.generator.sine_wave()
        return self.generator.sine_wave()

    def _update_all(self):
        """Recompute signal and all three transforms, then refresh every canvas."""
        t, x = self._get_signal()
        self._t, self._x = t, x

        N  = len(x)
        fs = self.generator.fs

        # ── DTFT ────────────────────────────────────────────────────────────────
        omega, X_dtft = self.ft.dtft(x, num_freq_points=1024)
        omega_pi = omega / np.pi      # normalise to [0, 2) so axis reads "×π rad/s"
        mag_dtft   = self.ft.magnitude(X_dtft) * N   # un-normalise for visual clarity
        phase_dtft = self.ft.phase(X_dtft)

        self.pm_dtft.update_time(t, x)
        self.pm_dtft.update_magnitude(omega_pi, mag_dtft, xlabel="ω / π  (rad/sample)")
        self.pm_dtft.update_phase(omega_pi, phase_dtft, xlabel="ω / π  (rad/sample)")
        self.pm_dtft.refresh()

        # ── DFT (manual) ────────────────────────────────────────────────────────
        freqs_hz, half = self.ft.freq_axis_hz(N, fs)
        _, X_dft, dft_elapsed = self.ft.dft_manual(x)
        mag_dft   = self.ft.magnitude(X_dft)[:half]
        phase_dft = self.ft.phase(X_dft)[:half]

        self.pm_dft.update_time(t, x)
        self.pm_dft.update_magnitude(freqs_hz, mag_dft, xlabel="Frequency (Hz)")
        self.pm_dft.update_phase(freqs_hz, phase_dft, xlabel="Frequency (Hz)")
        self.pm_dft.refresh()

        # ── FFT (numpy) ──────────────────────────────────────────────────────────
        _, X_fft, fft_elapsed = self.ft.fft_numpy(x)
        mag_fft   = self.ft.magnitude(X_fft)[:half]
        phase_fft = self.ft.phase(X_fft)[:half]

        self.pm_fft.update_time(t, x)
        self.pm_fft.update_magnitude(freqs_hz, mag_fft, xlabel="Frequency (Hz)")
        self.pm_fft.update_phase(freqs_hz, phase_fft, xlabel="Frequency (Hz)")
        self.pm_fft.refresh()

        # ── Timing labels ────────────────────────────────────────────────────────
        speedup = dft_elapsed / fft_elapsed if fft_elapsed > 0 else float("inf")
        self.lbl_dft_time.setText(f"DFT time:  {dft_elapsed*1000:.2f} ms")
        self.lbl_fft_time.setText(f"FFT time:  {fft_elapsed*1000:.4f} ms")
        self.lbl_speedup.setText( f"Speedup:   {speedup:.1f}×")

    # ================================================================ compare tab

    def _run_comparison(self):
        """
        Benchmark DFT vs FFT for a range of N values and plot the results
        in the Compare tab.
        """
        sizes = [16, 32, 64, 128, 256, 512]
        dft_times, fft_times = [], []

        for N in sizes:
            rng = np.random.default_rng(0)
            x = rng.standard_normal(N)

            # DFT
            _, _, dt = self.ft.dft_manual(x)
            dft_times.append(dt)

            # FFT (run multiple times and take min to reduce noise)
            best_fft = min(self.ft.fft_numpy(x)[2] for _ in range(5))
            fft_times.append(best_fft)

        self.pm_compare.plot(sizes, dft_times, fft_times)
        # Switch to Compare tab
        self.tabs.setCurrentIndex(3)

    # ================================================================ export

    def _export_plots(self):
        path, _ = QFileDialog.getExistingDirectory(
            self, "Choose export folder", os.path.expanduser("~")
        ) if hasattr(QFileDialog, 'getExistingDirectory') else (None, None)

        # Simpler call for PyQt5
        path = QFileDialog.getExistingDirectory(self, "Choose export folder",
                                                os.path.expanduser("~"))
        if not path:
            return

        ts = int(time.time())
        for pm, name in [(self.pm_dtft, "DTFT"), (self.pm_dft, "DFT"),
                         (self.pm_fft, "FFT"), (self.pm_compare, "Compare")]:
            fname = os.path.join(path, f"DSP_{name}_{ts}.png")
            pm.figure.savefig(fname, dpi=150, facecolor=pm.figure.get_facecolor())

        QMessageBox.information(self, "Export Complete",
                                f"4 PNG files saved to:\n{path}")


# ── Entry point ────────────────────────────────────────────────────────────────

def main():
    app = QApplication(sys.argv)
    app.setStyle("Fusion")           # base style — our stylesheet overrides it

    # Force dark palette as a fallback
    palette = QPalette()
    palette.setColor(QPalette.Window,          QColor(15, 15, 26))
    palette.setColor(QPalette.WindowText,      QColor(224, 224, 240))
    palette.setColor(QPalette.Base,            QColor(22, 33, 62))
    palette.setColor(QPalette.AlternateBase,   QColor(15, 15, 26))
    palette.setColor(QPalette.ToolTipBase,     QColor(0, 0, 0))
    palette.setColor(QPalette.ToolTipText,     QColor(224, 224, 240))
    palette.setColor(QPalette.Text,            QColor(224, 224, 240))
    palette.setColor(QPalette.Button,          QColor(22, 33, 62))
    palette.setColor(QPalette.ButtonText,      QColor(224, 224, 240))
    palette.setColor(QPalette.Highlight,       QColor(0, 100, 136))
    palette.setColor(QPalette.HighlightedText, QColor(255, 255, 255))
    app.setPalette(palette)

    window = DSPMainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
