# DSP Visualizer — DTFT · DFT · FFT

A complete Python desktop application for interactive Digital Signal Processing (DSP) education and visualization.

---

## 🚀 Quick Start

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

> Python 3.8+ recommended. All packages are cross-platform (Windows / macOS / Linux).

### 2. Run the application

```bash
python main_gui.py
```

That's it. A dark-themed GUI window will open.

---

## 📁 Project Structure

```
dsp_app/
├── main_gui.py           ← Entry point + full PyQt5 GUI (window, controls, layout)
├── signal_generator.py   ← Generates all discrete-time signals
├── fourier_transforms.py ← DTFT, manual DFT, and NumPy FFT implementations
├── plot_manager.py       ← Matplotlib canvas management (3 subplots per tab)
├── requirements.txt      ← Python package dependencies
└── README.md             ← This file
```

### Class Roles

| Class | File | Purpose |
|-------|------|---------|
| `SignalGenerator` | signal_generator.py | Generates sine, cosine, square, impulse, random, and custom signals |
| `FourierTransforms` | fourier_transforms.py | Implements DTFT, manual DFT (O(N²)), and FFT via NumPy |
| `PlotManager` | plot_manager.py | Manages a 3-subplot Matplotlib canvas (time + magnitude + phase) |
| `ComparisonPlotManager` | plot_manager.py | Bar-chart canvas for DFT vs FFT timing benchmark |
| `DSPMainWindow` | main_gui.py | Main PyQt5 window; wires all controls to transforms and plots |
| `LabelledSlider` | main_gui.py | Reusable slider widget with float mapping |

---

## 🎛️ Features

| Feature | Details |
|---------|---------|
| Signal types | Sine, Cosine, Square (adjustable duty cycle), Impulse, White noise, Custom |
| Parameters | Frequency (0.5–50 Hz), Amplitude (0.1–5), Sampling Fs (10–500 Hz), N samples (16–512), Phase (±180°) |
| Transforms | DTFT (1024-point approximation), DFT (manual O(N²)), FFT (numpy) |
| Plots | Time domain, Magnitude spectrum, Phase spectrum — all in-window |
| Navigation | Zoom, pan, save via Matplotlib toolbar on every tab |
| Benchmark | Compare DFT vs FFT execution time across N = 16 to 512 |
| Export | Save all 4 plots as PNG files |
| Custom input | Type your own comma-separated sample values |

---

## 📐 Mathematical Background

### 1. DTFT — Discrete-Time Fourier Transform

$$X(e^{j\omega}) = \sum_{n=0}^{N-1} x[n]\, e^{-j\omega n}, \quad \omega \in [0, 2\pi)$$

- Input: discrete-time signal x[n]  
- Output: **continuous** function of angular frequency ω  
- We approximate it by evaluating at 1024 equally-spaced ω values  
- Result: a smooth spectrum showing all frequencies (good for understanding)  
- Not directly computable on a computer (infinite sum in theory; finite here because our signal is finite-length)

### 2. DFT — Discrete Fourier Transform

$$X[k] = \sum_{n=0}^{N-1} x[n]\, e^{-j\frac{2\pi k n}{N}}, \quad k = 0, 1, \ldots, N-1$$

- Both time and frequency are **discrete**  
- Produces exactly N complex values X[k]  
- Equivalent to sampling the DTFT at ω_k = 2πk/N  
- Implemented here with a **naive double loop**: O(N²) — slow but educational  
- Each X[k] is a dot product of x with a complex sinusoid of frequency k/N cycles/sample

### 3. FFT — Fast Fourier Transform (Cooley-Tukey)

$$X[k] = X_{\text{even}}[k] + W_N^k \cdot X_{\text{odd}}[k]$$

- **Mathematically identical** to the DFT — same X[k] values  
- Uses a divide-and-conquer strategy (split even/odd samples recursively)  
- Complexity: **O(N log N)** vs O(N²) — ~100× faster for N = 1024  
- Implemented here via `numpy.fft.fft` (optimised C code under the hood)  
- For large N the speedup is dramatic — see the Compare tab for proof

### Key Differences at a Glance

| Property | DTFT | DFT | FFT |
|----------|------|-----|-----|
| Frequency axis | Continuous ω ∈ [0, 2π) | Discrete k = 0..N-1 | Discrete k = 0..N-1 |
| Computation | Approximated (sampled) | O(N²) exact | O(N log N) exact |
| Output | Smooth spectrum | N complex values | Same N complex values |
| Typical use | Theory, understanding | Small N, teaching | All practical applications |

---

## 📦 Libraries & Why

| Library | Role | Why Chosen |
|---------|------|-----------|
| **PyQt5** | GUI framework | Cross-platform, mature, excellent Matplotlib integration |
| **NumPy** | Numerical arrays, FFT, math | The standard for scientific computing in Python |
| **Matplotlib** | All plotting inside the window | Most flexible Python plotting; supports embedded Qt canvases |
| **SciPy** | (available, not used directly) | Could be used for advanced filter design in extensions |

---

## 💡 Tips

- **Real-time updates**: every slider change instantly recomputes and redraws all three transforms.  
- **Nyquist check**: keep the signal frequency below Fs/2 to avoid aliasing artifacts.  
- **Custom signal**: switch to "Custom" in the combo box and type your own samples, then click Update Plots.  
- **Zoom & Pan**: use the Matplotlib toolbar (🔍🖐️) on any tab to zoom in or pan around.  
- **Benchmark**: click "Run DFT vs FFT Timing" — for N = 512 the FFT can be 100–1000× faster.
