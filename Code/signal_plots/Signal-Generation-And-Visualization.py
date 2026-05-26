import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.size': 12,
    'axes.titlesize': 16,
    'axes.titleweight': 'bold',
    'axes.labelsize': 13,
    'axes.labelweight': 'bold',
    'axes.spines.top': False,
    'axes.spines.right': False,
    'figure.facecolor': '#fafafa',
    'axes.facecolor': '#ffffff',
})

OUTPUT_DIR = Path(__file__).parent / "signal_plots"
OUTPUT_DIR.mkdir(exist_ok=True)

BANNER_PROPS = dict(boxstyle='round,pad=0.4', facecolor='#1f77b4', edgecolor='none', alpha=0.9)

def add_title_banner(ax, text, sub_text=None):
    ax.text(0.5, 1.08, text, transform=ax.transAxes, fontsize=17,
            fontweight='bold', color='white', ha='center', va='bottom',
            bbox=BANNER_PROPS)
    if sub_text:
        ax.text(0.5, 1.02, sub_text, transform=ax.transAxes, fontsize=10,
                color='gray', ha='center', va='bottom', style='italic')

def unit_impulse(n, n0=0):
    n = np.asarray(n)
    return (n == n0).astype(float)

def unit_step(n, n0=0):
    n = np.asarray(n)
    return (n >= n0).astype(float)

def ramp(n, slope=1.0, n0=0):
    n = np.asarray(n)
    return slope * np.maximum(0, n - n0)

def exponential(n, a):
    n = np.asarray(n)
    return np.power(a, n)

def sinusoid(n, omega, phase=0.0, amplitude=1.0):
    n = np.asarray(n)
    return amplitude * np.cos(omega * n + phase)

def complex_exponential(n, omega):
    n = np.asarray(n)
    return np.exp(1j * omega * n)

def quantize(x, levels):
    x_min, x_max = x.min(), x.max()
    if x_min == x_max:
        return np.zeros_like(x)
    bins = np.linspace(x_min, x_max, levels)
    indices = np.digitize(x, bins) - 1
    indices = np.clip(indices, 0, levels - 1)
    return bins[indices]

def plot_discrete(n, x, title, subtitle, filename, analog_n=None, analog_x=None,
                  ylabel='Amplitude'):
    fig, ax = plt.subplots(figsize=(11, 4.5))
    add_title_banner(ax, title, subtitle)
    if analog_n is not None and analog_x is not None:
        ax.plot(analog_n, analog_x, 'cornflowerblue', linewidth=2, alpha=0.5, label='Analog')
    markerline, stemlines, baseline = ax.stem(n, x, linefmt='#d62728', markerfmt='D',
                                               basefmt='#cccccc', label='Discrete')
    plt.setp(markerline, markersize=5)
    ax.set_xlabel('Sample Index (n)', fontsize=12)
    ax.set_ylabel(ylabel, fontsize=12)
    ax.set_xlim(n[0] - 1, n[-1] + 1)
    y_margin = 0.15 * (max(x) - min(x)) if max(x) != min(x) else 0.5
    ax.set_ylim(min(x) - y_margin, max(x) + y_margin)
    ax.grid(True, alpha=0.25, linestyle='--')
    ax.legend(fontsize=11, loc='upper right', framealpha=0.9, edgecolor='#dddddd')
    plt.subplots_adjust(top=0.80, bottom=0.14, left=0.10, right=0.95)
    plt.savefig(OUTPUT_DIR / filename, dpi=150, bbox_inches='tight')
    plt.close()

def generate_all_signals(n_range=(-5, 20), omega=0.5, a=0.8):
    n = np.arange(n_range[0], n_range[1] + 1)

    plot_discrete(n, unit_impulse(n, n0=3), 'Unit Impulse Signal',
                  'δ[n − 3] — Non-zero at exactly one index', 'impulse.png')
    plot_discrete(n, unit_step(n, n0=5), 'Unit Step Signal',
                  'u[n − 5] — Turns on at n = 5 and stays on', 'step.png')
    plot_discrete(n, ramp(n, slope=2.0, n0=2), 'Ramp Signal',
                  '2 · max(0, n − 2) — Linearly increasing from n = 2', 'ramp.png')
    plot_discrete(n, exponential(n, a), 'Exponential Signal',
                  f'{a}^n — Decays geometrically (|a| < 1)', 'exponential.png')
    plot_discrete(n, sinusoid(n, omega, phase=0), 'Sinusoidal Signal',
                  f'cos({omega} · n) — Discrete-time oscillation', 'sine.png')

    ce = complex_exponential(n, omega)
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(11, 6.5))
    add_title_banner(ax1, 'Complex Exponential Signal',
                     f'e^(j{omega}n) — Real and Imaginary Parts')
    m1, s1, b1 = ax1.stem(n, ce.real, linefmt='#1f77b4', markerfmt='D',
                           basefmt='#cccccc', label='Real Part')
    plt.setp(m1, markersize=4)
    ax1.set_ylabel('Amplitude', fontsize=12)
    ax1.set_xlim(n[0] - 1, n[-1] + 1)
    ax1.grid(True, alpha=0.25, linestyle='--')
    ax1.legend(fontsize=11, loc='upper right', framealpha=0.9, edgecolor='#dddddd')

    m2, s2, b2 = ax2.stem(n, ce.imag, linefmt='#d62728', markerfmt='D',
                           basefmt='#cccccc', label='Imaginary Part')
    plt.setp(m2, markersize=4)
    ax2.set_xlabel('Sample Index (n)', fontsize=12)
    ax2.set_ylabel('Amplitude', fontsize=12)
    ax2.set_xlim(n[0] - 1, n[-1] + 1)
    ax2.grid(True, alpha=0.25, linestyle='--')
    ax2.legend(fontsize=11, loc='upper right', framealpha=0.9, edgecolor='#dddddd')

    plt.subplots_adjust(top=0.90, bottom=0.10, left=0.10, right=0.95, hspace=0.35)
    plt.savefig(OUTPUT_DIR / 'complex_exponential.png', dpi=150, bbox_inches='tight')
    plt.close()

def plot_sampling_comparison(t_range=(0, 1), f_signal=5, f_samples=20, levels=8):
    t = np.linspace(t_range[0], t_range[1], 1000)
    x_analog = np.cos(2 * np.pi * f_signal * t)

    n = np.arange(0, int((t_range[1] - t_range[0]) * f_samples) + 1)
    t_samples = n / f_samples
    x_sampled = np.cos(2 * np.pi * f_signal * t_samples)
    x_quantized = quantize(x_sampled, levels)

    fig, ax = plt.subplots(figsize=(13, 5))
    add_title_banner(ax, 'Sampling & Quantization Comparison',
                     f'f_signal = {f_signal} Hz  |  f_s = {f_samples} Hz  |  {levels} quantization levels')
    ax.plot(t, x_analog, color='cornflowerblue', linewidth=2.5, alpha=0.35, label='Analog (continuous)')
    m3, s3, b3 = ax.stem(t_samples, x_sampled, linefmt='#2ca02c', markerfmt='D',
                     basefmt='#cccccc', label='Sampled')
    plt.setp(m3, markersize=5)
    ax.step(t_samples, x_quantized, '#d62728', linewidth=2, where='mid', alpha=0.85,
            label=f'Quantized ({levels} levels)')
    ax.set_xlabel('Time (s)', fontsize=12)
    ax.set_ylabel('Amplitude', fontsize=12)
    ax.set_xlim(t_range[0], t_range[1])
    ax.grid(True, alpha=0.25, linestyle='--')
    ax.legend(fontsize=11, loc='upper right', framealpha=0.9, edgecolor='#dddddd')
    plt.subplots_adjust(top=0.80, bottom=0.14, left=0.08, right=0.95)
    plt.savefig(OUTPUT_DIR / 'sampling_comparison.png', dpi=150, bbox_inches='tight')
    plt.close()

def plot_omega_variation(omegas=[0.1, 0.5, 1.0, 2.0]):
    n = np.arange(0, 20)
    fig, axes = plt.subplots(len(omegas), 1, figsize=(11, 9))
    add_title_banner(axes[0], 'Effect of Varying Angular Frequency (ω)',
                     'cos(ωn) for different values of ω')
    for ax, omega in zip(axes, omegas):
        x = sinusoid(n, omega)
        m4, s4, b4 = ax.stem(n, x, linefmt='#1f77b4', markerfmt='D',
                                basefmt='#cccccc')
        plt.setp(m4, markersize=4.5)
        ax.text(0.02, 0.88, f'ω = {omega}', transform=ax.transAxes, fontsize=13,
                fontweight='bold', color='#1f77b4', va='top',
                bbox=dict(boxstyle='round,pad=0.3', facecolor='#eef4fb', edgecolor='#1f77b4', alpha=0.8))
        ax.set_ylabel('Amplitude', fontsize=11)
        ax.set_xlim(n[0] - 1, n[-1] + 1)
        ax.set_ylim(-1.6, 1.6)
        ax.grid(True, alpha=0.25, linestyle='--')
    axes[-1].set_xlabel('Sample Index (n)', fontsize=12)
    plt.subplots_adjust(top=0.93, bottom=0.06, left=0.09, right=0.95, hspace=0.45)
    plt.savefig(OUTPUT_DIR / 'omega_variation.png', dpi=150, bbox_inches='tight')
    plt.close()

if __name__ == '__main__':
    print(f"Generating styled signal plots → {OUTPUT_DIR}/")
    generate_all_signals()
    plot_sampling_comparison()
    plot_omega_variation()
    print("Done — all images saved with title banners and padded layouts.")