"""
Interactive DSP Signal Explorer
================================
Full GUI using matplotlib widgets — sliders, radio buttons, tabs.
Every parameter change updates the plot live in the same window.

Requirements:
    pip install numpy matplotlib
Run:
    python signal_explorer.py
"""

import matplotlib.gridspec as gridspec
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyBboxPatch
from matplotlib.widgets import Button, CheckButtons, RadioButtons, Slider

# ──────────────────────────────────────────────
#  Signal generators
# ──────────────────────────────────────────────


def unit_impulse(n, n0=0):
    return (n == n0).astype(float)


def unit_step(n, n0=0):
    return (n >= n0).astype(float)


def ramp(n, slope=1.0, n0=0):
    return slope * np.maximum(0, n - n0)


def exponential(n, a):
    if a == 0:
        return np.where(n == 0, 1.0, 0.0)
    return np.power(a, n.astype(float))


def sinusoid(n, omega, phase=0.0, amplitude=1.0):
    return amplitude * np.cos(omega * n + phase)


def complex_exponential_real(n, omega):
    return np.cos(omega * n)


def complex_exponential_imag(n, omega):
    return np.sin(omega * n)


def quantize(x, levels):
    levels = max(2, int(levels))
    x_min, x_max = x.min(), x.max()
    if x_min == x_max:
        return np.zeros_like(x)
    bins = np.linspace(x_min, x_max, levels)
    indices = np.digitize(x, bins) - 1
    indices = np.clip(indices, 0, levels - 1)
    return bins[indices]


# ──────────────────────────────────────────────
#  Color palette
# ──────────────────────────────────────────────
BG = "#0f1117"
PANEL = "#1a1d27"
ACCENT = "#7c6af7"
ACCENT2 = "#f97316"
GREEN = "#22c55e"
RED = "#ef4444"
TEXT = "#e2e8f0"
GRIDCOL = "#2a2d3e"
SLIDER_BG = "#252836"

plt.rcParams.update(
    {
        "figure.facecolor": BG,
        "axes.facecolor": PANEL,
        "axes.edgecolor": GRIDCOL,
        "axes.labelcolor": TEXT,
        "xtick.color": TEXT,
        "ytick.color": TEXT,
        "text.color": TEXT,
        "grid.color": GRIDCOL,
        "grid.linestyle": "--",
        "grid.alpha": 0.5,
        "font.family": "monospace",
    }
)

# ──────────────────────────────────────────────
#  Figure layout
# ──────────────────────────────────────────────
fig = plt.figure(figsize=(16, 9), facecolor=BG)
fig.canvas.manager.set_window_title("⚡ DSP Signal Explorer — Bahr")

# Main plot area: top-left 2/3
ax_main = fig.add_axes([0.04, 0.34, 0.62, 0.54])
# Secondary (for complex exp): bottom-left
ax_sub = fig.add_axes([0.04, 0.06, 0.62, 0.24])
# Info panel
ax_info = fig.add_axes([0.68, 0.54, 0.30, 0.34], facecolor=PANEL)

for ax in [ax_main, ax_sub, ax_info]:
    ax.grid(True)
    ax.tick_params(labelsize=8)

ax_info.set_xticks([])
ax_info.set_yticks([])

# ──────────────────────────────────────────────
#  Widget axes (right column + bottom strip)
# ──────────────────────────────────────────────
ax_radio = fig.add_axes([0.69, 0.27, 0.28, 0.28], facecolor=PANEL)
ax_sn0 = fig.add_axes([0.69, 0.20, 0.28, 0.03], facecolor=SLIDER_BG)
ax_somega = fig.add_axes([0.69, 0.15, 0.28, 0.03], facecolor=SLIDER_BG)
ax_sa = fig.add_axes([0.69, 0.10, 0.28, 0.03], facecolor=SLIDER_BG)
ax_sphase = fig.add_axes([0.69, 0.05, 0.28, 0.03], facecolor=SLIDER_BG)
ax_schk = fig.add_axes(
    [0.04, 0.06, 0.10, 0.26], facecolor=PANEL
)  # overlap handled by zorder

# Sampling / quantization extra sliders (shown only for that mode)
ax_sfs = fig.add_axes([0.04, 0.01, 0.28, 0.02], facecolor=SLIDER_BG, visible=False)
ax_sqlevs = fig.add_axes([0.35, 0.01, 0.28, 0.02], facecolor=SLIDER_BG, visible=False)

# Reset button
ax_reset = fig.add_axes([0.69, 0.01, 0.13, 0.03], facecolor=SLIDER_BG)

# ──────────────────────────────────────────────
#  Widgets
# ──────────────────────────────────────────────
SIGNALS = [
    "Unit Impulse",
    "Unit Step",
    "Ramp",
    "Exponential",
    "Sinusoid",
    "Complex Exp",
    "Sampling/Quant",
    "Omega Variation",
]

radio = RadioButtons(
    ax_radio,
    SIGNALS,
    active=4,
    activecolor=ACCENT,
)
for label in radio.labels:
    label.set_fontsize(8.5)
    label.set_color(TEXT)
# Radio buttons use scatter PathCollection in matplotlib>=3.7
radio.set_radio_props({"s": 64})

sl_n0 = Slider(ax_sn0, "n₀", -10, 20, valinit=0, valstep=1, color=ACCENT)
sl_omega = Slider(ax_somega, "ω", 0.05, np.pi, valinit=0.5, color=ACCENT2)
sl_a = Slider(ax_sa, "a", -1.5, 1.5, valinit=0.8, color=GREEN)
sl_phase = Slider(ax_sphase, "phase", -np.pi, np.pi, valinit=0.0, color=RED)
sl_fs = Slider(ax_sfs, "f_s (Hz)", 5, 100, valinit=20, valstep=1, color=ACCENT)
sl_qlevs = Slider(ax_sqlevs, "Q levels", 2, 64, valinit=8, valstep=1, color=ACCENT2)

for sl in [sl_n0, sl_omega, sl_a, sl_phase, sl_fs, sl_qlevs]:
    sl.label.set_color(TEXT)
    sl.label.set_fontsize(8)
    sl.valtext.set_color(ACCENT)
    sl.valtext.set_fontsize(8)

chk_show_analog = CheckButtons(ax_schk, ["Show\nAnalog"], [False])
for lbl in chk_show_analog.labels:
    lbl.set_fontsize(7)
    lbl.set_color(TEXT)

btn_reset = Button(ax_reset, "↺ Reset", color=SLIDER_BG, hovercolor=ACCENT)
btn_reset.label.set_color(TEXT)
btn_reset.label.set_fontsize(9)

# ──────────────────────────────────────────────
#  State
# ──────────────────────────────────────────────
state = {"signal": SIGNALS[4]}


# ──────────────────────────────────────────────
#  Draw helpers
# ──────────────────────────────────────────────
def stem_plot(ax, n, x, color=ACCENT, label="x[n]"):
    markerline, stemlines, baseline = ax.stem(
        n, x, linefmt="-", markerfmt="o", basefmt="-", label=label
    )
    markerline.set_color(color)
    markerline.set_markersize(5)
    # In matplotlib >=3.7, stemlines is a LineCollection (not a list of lines)
    if hasattr(stemlines, "set_color"):
        stemlines.set_color(color)
        stemlines.set_alpha(0.7)
    else:
        for line in stemlines:
            line.set_color(color)
            line.set_alpha(0.7)
    baseline.set_color(GRIDCOL)


def update_info(lines):
    ax_info.clear()
    ax_info.set_facecolor(PANEL)
    ax_info.set_xticks([])
    ax_info.set_yticks([])
    ax_info.set_title("  Signal Info", loc="left", fontsize=9, color=ACCENT, pad=6)
    y = 0.90
    for line in lines:
        ax_info.text(
            0.05,
            y,
            line,
            transform=ax_info.transAxes,
            fontsize=8.5,
            color=TEXT,
            va="top",
            family="monospace",
        )
        y -= 0.13


# ──────────────────────────────────────────────
#  Main update
# ──────────────────────────────────────────────
def update(_=None):
    sig = state["signal"]
    n0 = int(sl_n0.val)
    omega = sl_omega.val
    a = sl_a.val
    phase = sl_phase.val
    fs = int(sl_fs.val)
    qlevs = int(sl_qlevs.val)
    show_analog = chk_show_analog.get_status()[0]

    # Show/hide sampling sliders
    ax_sfs.set_visible(sig == "Sampling/Quant")
    ax_sqlevs.set_visible(sig == "Sampling/Quant")

    ax_main.clear()
    ax_main.grid(True)
    ax_sub.clear()
    ax_sub.grid(True)

    n = np.arange(-10, 41)

    # ── Per-signal logic ──────────────────────
    if sig == "Unit Impulse":
        x = unit_impulse(n, n0)
        stem_plot(ax_main, n, x)
        ax_main.set_title(f"Unit Impulse  δ[n - {n0}]", color=TEXT, fontsize=11)
        update_info(
            [
                f"Type   : δ[n - n₀]",
                f"n₀     : {n0}",
                f"Range  : n ∈ [-10, 40]",
                f"Peak   : 1 at n = {n0}",
                f"Energy : 1",
            ]
        )
        ax_sub.set_visible(False)

    elif sig == "Unit Step":
        x = unit_step(n, n0)
        stem_plot(ax_main, n, x, color=GREEN)
        ax_main.set_title(f"Unit Step  u[n - {n0}]", color=TEXT, fontsize=11)
        update_info(
            [
                f"Type   : u[n - n₀]",
                f"n₀     : {n0}",
                f"0 for n < {n0}",
                f"1 for n ≥ {n0}",
            ]
        )
        ax_sub.set_visible(False)

    elif sig == "Ramp":
        x = ramp(n, slope=a, n0=n0)
        stem_plot(ax_main, n, x, color=ACCENT2)
        ax_main.set_title(f"Ramp  {a:.2f}·max(0, n−{n0})", color=TEXT, fontsize=11)
        update_info(
            [
                f"Type   : slope·max(0, n-n₀)",
                f"n₀     : {n0}",
                f"slope  : {a:.3f}  (use 'a' slider)",
                f"0 for n < {n0}",
            ]
        )
        ax_sub.set_visible(False)

    elif sig == "Exponential":
        x = exponential(n, a)
        color = GREEN if abs(a) < 1 else RED
        stem_plot(ax_main, n, x, color=color)
        stability = (
            "Stable (|a|<1)"
            if abs(a) < 1
            else ("Unstable (|a|>1)" if abs(a) > 1 else "Marginal")
        )
        ax_main.set_title(f"Exponential  a^n,  a = {a:.3f}", color=TEXT, fontsize=11)
        x_abs_max = np.max(np.abs(x[np.isfinite(x)]))
        y_limit = min(max(x_abs_max * 1.2, 1), 1e6)
        ax_main.set_ylim(-y_limit, y_limit)
        update_info(
            [
                f"Type   : a^n",
                f"a      : {a:.4f}",
                f"Status : {stability}",
                f"x[0]   : 1",
                f"x[5]   : {a**5:.4f}",
            ]
        )
        ax_sub.set_visible(False)

    elif sig == "Sinusoid":
        x = sinusoid(n, omega, phase, amplitude=1.0)
        stem_plot(ax_main, n, x, color=ACCENT2)
        if show_analog:
            t = np.linspace(n.min(), n.max(), 1000)
            ax_main.plot(
                t,
                np.cos(omega * t + phase),
                color=ACCENT2,
                alpha=0.25,
                lw=1.5,
                label="analog envelope",
            )
        period_str = f"{2 * np.pi / omega:.2f}" if omega != 0 else "∞"
        ax_main.set_title(
            f"Sinusoid  cos({omega:.3f}·n + {phase:.2f})", color=TEXT, fontsize=11
        )
        update_info(
            [
                f"Type   : A·cos(ωn + φ)",
                f"ω      : {omega:.4f} rad",
                f"φ      : {phase:.4f} rad",
                f"Period : {period_str} samples",
                f"Max    : 1.00",
            ]
        )
        ax_sub.set_visible(False)

    elif sig == "Complex Exp":
        ax_sub.set_visible(True)
        re = complex_exponential_real(n, omega)
        im = complex_exponential_imag(n, omega)
        stem_plot(ax_main, n, re, color=ACCENT, label="Re{e^(jωn)}")
        stem_plot(ax_sub, n, im, color=ACCENT2, label="Im{e^(jωn)}")
        ax_main.set_title(
            f"Complex Exponential  e^(j·{omega:.3f}·n)  — Real", color=TEXT, fontsize=11
        )
        ax_sub.set_title("Imaginary Part", color=ACCENT2, fontsize=9)
        ax_sub.grid(True)
        ax_sub.legend(fontsize=8, facecolor=PANEL, labelcolor=TEXT)
        period_ratio = omega / (2 * np.pi)
        is_periodic = np.abs(period_ratio - np.round(period_ratio)) < 1e-9
        period_str = f"{2 * np.pi / omega:.2f}" if is_periodic and omega != 0 else "aperiodic (discrete)"
        update_info(
            [
                f"Type   : e^(jωn)",
                f"ω      : {omega:.4f} rad",
                f"Re     : cos(ωn)",
                f"Im     : sin(ωn)",
                f"Period : {period_str} samples",
            ]
        )

    elif sig == "Sampling/Quant":
        ax_sub.set_visible(True)
        f_sig = 5
        t = np.linspace(0, 1, 2000)
        x_analog = np.cos(2 * np.pi * f_sig * t)

        t_s = np.arange(0, fs + 1) / fs
        x_s = np.cos(2 * np.pi * f_sig * t_s)
        x_q = quantize(x_s, qlevs)

        ax_main.plot(t, x_analog, color=ACCENT, alpha=0.3, lw=1.5, label="Analog")
        stem_plot(ax_main, t_s, x_s, color=GREEN, label="Sampled")
        ax_main.set_title(
            f"Sampling  f_signal={f_sig}Hz  f_s={fs}Hz", color=TEXT, fontsize=11
        )
        ax_main.set_xlabel("Time (s)", color=TEXT, fontsize=9)
        ax_main.legend(fontsize=8, facecolor=PANEL, labelcolor=TEXT)

        ax_sub.plot(t, x_analog, color=ACCENT, alpha=0.2, lw=1)
        ax_sub.step(
            t_s,
            x_q,
            color=RED,
            lw=1.8,
            where="mid",
            label=f"Quantized ({qlevs} levels)",
        )
        ax_sub.legend(fontsize=8, facecolor=PANEL, labelcolor=TEXT)
        ax_sub.set_title("Quantization", color=RED, fontsize=9)
        ax_sub.grid(True)

        snr_approx = 6.02 * np.log2(qlevs) + 1.76
        update_info(
            [
                f"f_signal : {f_sig} Hz",
                f"f_s      : {fs} Hz",
                f"Ratio    : {fs / f_sig:.1f}×",
                f"Q levels : {qlevs}",
                f"Est SNR  : {snr_approx:.1f} dB",
                f"Nyquist  : {'OK' if fs >= 2 * f_sig else 'ALIASING!'}",
            ]
        )

    elif sig == "Omega Variation":
        ax_sub.set_visible(True)
        omegas = [omega * 0.25, omega * 0.5, omega, omega * 2]
        colors = [ACCENT, GREEN, ACCENT2, RED]
        n_short = np.arange(0, 30)
        for i, (om, col) in enumerate(zip(omegas, colors)):
            x = sinusoid(n_short, om)
            offset = i * 2.5
            markerline, stemlines, baseline = ax_main.stem(
                n_short,
                x + offset,
                linefmt="-",
                markerfmt="o",
                basefmt="-",
                label=f"ω={om:.2f}",
            )
            markerline.set_color(col)
            markerline.set_alpha(0.6)
            if hasattr(stemlines, "set_color"):
                stemlines.set_color(col)
                stemlines.set_alpha(0.6)
            else:
                for line in stemlines:
                    line.set_color(col)
                    line.set_alpha(0.6)
            baseline.set_color(GRIDCOL)
        ax_main.set_title(
            f"Omega Variation  (base ω={omega:.3f})", color=TEXT, fontsize=11
        )
        ax_main.legend(fontsize=7, facecolor=PANEL, labelcolor=TEXT)

        # Frequency-domain magnitude sketch
        freqs = np.linspace(0, np.pi, 500)
        for om, col in zip(omegas, colors):
            resp = np.abs(np.sin(freqs - om + 0.001) / (freqs - om + 0.001))
            resp = resp / resp.max()
            ax_sub.plot(freqs, resp, color=col, alpha=0.7, lw=1.2, label=f"ω={om:.2f}")
        ax_sub.set_title("Approximate Frequency Spread", color=TEXT, fontsize=9)
        ax_sub.set_xlabel("ω (rad)", color=TEXT, fontsize=8)
        ax_sub.legend(fontsize=7, facecolor=PANEL, labelcolor=TEXT)
        ax_sub.grid(True)
        update_info(
            [
                f"base ω  : {omega:.4f}",
                f"ω×0.25 : {omega * 0.25:.4f}",
                f"ω×0.5  : {omega * 0.5:.4f}",
                f"ω×2.0  : {omega * 2:.4f}",
            ]
        )

    # ── Common styling ──────────────────────
    ax_main.set_xlabel("n (samples)", color=TEXT, fontsize=9)
    ax_main.legend(fontsize=8, facecolor=PANEL, labelcolor=TEXT, loc="best")
    ax_main.tick_params(colors=TEXT, labelsize=8)

    if ax_sub.get_visible():
        ax_sub.set_xlabel("n / t", color=TEXT, fontsize=8)
        ax_sub.tick_params(colors=TEXT, labelsize=8)

    fig.canvas.draw_idle()


# ──────────────────────────────────────────────
#  Callbacks
# ──────────────────────────────────────────────
def on_radio(label):
    state["signal"] = label
    update()


def on_reset(_):
    sl_n0.reset()
    sl_omega.reset()
    sl_a.reset()
    sl_phase.reset()
    sl_fs.reset()
    sl_qlevs.reset()
    update()


radio.on_clicked(on_radio)
for sl in [sl_n0, sl_omega, sl_a, sl_phase, sl_fs, sl_qlevs]:
    sl.on_changed(update)
chk_show_analog.on_clicked(update)
btn_reset.on_clicked(on_reset)

# ──────────────────────────────────────────────
#  Title banner
# ──────────────────────────────────────────────
fig.text(
    0.50,
    0.985,
    "⚡  DSP Signal Explorer",
    ha="center",
    va="top",
    fontsize=14,
    color=ACCENT,
    fontweight="bold",
    family="monospace",
)
fig.text(
    0.50,
    0.955,
    "Use the radio buttons & sliders on the right to explore each signal in real-time",
    ha="center",
    va="top",
    fontsize=7.5,
    color=TEXT,
    alpha=0.7,
)

# ──────────────────────────────────────────────
#  Initial draw
# ──────────────────────────────────────────────
ax_sub.set_visible(True)
update()
plt.show()
