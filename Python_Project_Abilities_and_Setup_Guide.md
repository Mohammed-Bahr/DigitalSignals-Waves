# Python Project Abilities and Setup Guide for This Digital Signals Directory

This directory is mainly an Obsidian knowledge base for Digital Signal Processing
(DSP). It is not yet a structured Python project, but it has enough material to
build a strong Python project around DSP simulation, visualization, audio
processing, and exam practice.

## 1. What I Found in This Directory

### Main content groups

| Area | Files/directories | Useful project material |
|---|---|---|
| Signal basics and systems | `Subfiles/1. Signal Fundamentals.md`, `Summerize/Digital Signals and Systems.md` | Signal classification, sampling, quantization, system properties, causality, memory, stability |
| Convolution and LTI systems | `Subfiles/2 Convolution Theory for LTI Systems.md`, exam solutions | Linear convolution, circular convolution, impulse response, causality and BIBO stability |
| DTFT, DFT, FFT | `Subfiles/3. Frequency Analysis & Transforms.md`, `Subfiles/LEC-5/*`, `Subfiles/LEC-8/*` | DTFT properties, DFT equations, FFT algorithm, zero padding, spectral analysis |
| Filters | `Subfiles/LEC-7/Ideal Low-Pass Filters, Windowing Techniques, FIR & IIR Filters.md` | Ideal filters, windowing, FIR filters, IIR filters, moving average filters, stability |
| Sampling and resampling | `Subfiles/LEC-8/*`, `Subfiles/LEC-9/LEC9.md` | Nyquist theorem, reconstruction, ZOH, FOH, upsampling, downsampling |
| Z-transform | `Subfiles/LEC-9/LEC9.md`, `Fatma/Fatma 1 to 10 DSP.md` | Z-transform pairs, ROC, poles, stability, transfer functions |
| Exam material | `Exams/Questions&Answers.md`, `Exams/2025 mid/2025 solution.md` | Worked questions for system classification, convolution, DTFT, z-transform, frequency response |
| Existing Python code | `Subfiles/LEC-7/audio1.py` | Prototype audio recorder/player and high-pass FIR filtering with `numpy` and `pyaudio` |

### Current Python status

The directory currently has only one Python script:

`Subfiles/LEC-7/audio1.py`

It can:

- Record microphone audio using `pyaudio`.
- Convert raw audio bytes to a NumPy array.
- Design a windowed sinc high-pass filter.
- Convolve the audio with that filter.
- Play the filtered audio back through speakers.

It is useful as a prototype, but it is not yet a reusable project because:

- It has no `requirements.txt` or `pyproject.toml`.
- It has no package structure.
- Functions are mixed with script execution.
- It does not save plots, audio files, or test results.
- It has no tests.
- It depends on microphone/speaker hardware, which makes it hard to test.

## 2. Best Python Project Idea

The best project for this directory is:

**DSP Python Lab**

A Python package and optional app that turns the notes into runnable tools:

- Generate and plot digital signals.
- Demonstrate sampling, quantization, aliasing, and reconstruction.
- Compute linear and circular convolution.
- Analyze DTFT, DFT, FFT, and frequency responses.
- Design FIR and IIR filters.
- Process audio files or microphone input.
- Simulate upsampling and downsampling.
- Plot z-plane poles and zeros.
- Create exam-style practice tools using the existing notes.

Recommended project folder:

```text
DigitalSignals/
  Python_Project_Abilities_and_Setup_Guide.md
  dsp_python_lab/
    pyproject.toml
    README.md
    src/
      dsp_lab/
        __init__.py
        signals.py
        systems.py
        convolution.py
        transforms.py
        filters.py
        sampling.py
        resampling.py
        ztransform.py
        audio.py
        plots.py
    examples/
      01_signal_basics.py
      02_convolution.py
      03_fft_analysis.py
      04_filter_audio.py
      05_resampling.py
    notebooks/
      01_sampling_and_aliasing.ipynb
      02_dft_fft.ipynb
      03_fir_iir_filters.ipynb
    tests/
      test_convolution.py
      test_transforms.py
      test_filters.py
```

Keeping the Python project inside `dsp_python_lab/` avoids disturbing the
Obsidian notes, PDFs, and attachments.

## 3. Available Abilities You Can Build

### Ability 1: Signal generation and visualization

Source notes:

- `Subfiles/1. Signal Fundamentals.md`
- `Summerize/DSP_Lecture_Notes.md`

What to build:

- Generate impulse, step, ramp, exponential, sine, cosine, and complex exponential signals.
- Plot discrete-time stem plots.
- Plot continuous-like sampled signals.
- Compare analog, sampled, and quantized versions.

Useful functions:

```python
unit_impulse(n, n0=0)
unit_step(n, n0=0)
exponential(n, a)
sinusoid(n, omega, phase=0)
quantize(x, levels)
plot_discrete(n, x)
```

Useful libraries:

- `numpy`
- `matplotlib`

Example project output:

- A script that shows how `cos(omega*n)` changes when `omega` changes.
- A plot showing sampled vs quantized versions of the same signal.

### Ability 2: System classification helper

Source notes:

- `Subfiles/1. Signal Fundamentals.md`
- `Exams/2025 mid/2025 solution.md`

What to build:

- A rule-based helper that checks common signs of:
  - Linearity
  - Time invariance
  - Causality
  - Memory
  - BIBO stability
- It can start as a manual checklist, then later become a parser.

Practical first version:

- User enters a description like `y[n] = 2*x[n] + x[n-1]`.
- Program asks guiding questions or checks simple patterns.
- Program outputs likely classification and explanation.

Suggested scope:

- Do not try to perfectly parse all math at first.
- Start with common exam patterns:
  - Constant term means non-linear.
  - `x[n+k]` means non-causal.
  - `n*x[n]` means time-varying.
  - Any shifted `x` or recursive `y` usually means memory.

Useful libraries:

- Basic Python strings for first version.
- `sympy` later if you want symbolic parsing.

### Ability 3: Linear and circular convolution calculator

Source notes:

- `Subfiles/2 Convolution Theory for LTI Systems.md`
- `Subfiles/LEC-8/Lecture 8- DFT, FFT, and Sampling Theory.md`
- `Exams/2025 mid/2025 solution.md`

What to build:

- Compute linear convolution.
- Compute circular convolution.
- Show zero-padding rule: output length is `N + M - 1`.
- Compare direct convolution with FFT-based convolution.
- Visualize flip, shift, multiply, sum.

Useful functions:

```python
linear_convolution(x, h)
circular_convolution(x, h, N=None)
fft_convolution(x, h)
required_linear_conv_length(len_x, len_h)
```

Useful libraries:

- `numpy`
- `scipy.signal`
- `matplotlib`

Tests to add:

- `linear_convolution([1, -2, 0, 3], [1, 0, -2])` should return
  `[1, -2, -2, 7, 0, -6]`, based on the 2025 mid solution.

### Ability 4: DTFT, DFT, and FFT analyzer

Source notes:

- `Subfiles/3. Frequency Analysis & Transforms.md`
- `Subfiles/LEC-5/DTFT.md`
- `Subfiles/LEC-8/Lecture 8- DFT, FFT, and Sampling Theory.md`
- `Malak/MD format of Malak summary.md`
- `Fatma/Fatma 1 to 10 DSP.md`

What to build:

- Compute DFT using direct matrix multiplication.
- Compute FFT using `numpy.fft.fft`.
- Compare direct DFT complexity with FFT.
- Plot magnitude and phase.
- Use `fftshift` to show frequency from `-\pi` to `+\pi`.
- Demonstrate that DFT samples the DTFT.

Useful functions:

```python
dft_direct(x)
idft_direct(X)
fft_spectrum(x, fs=1.0)
plot_magnitude_phase(freq, X)
compare_dft_fft_runtime(N_values)
```

Useful libraries:

- `numpy`
- `matplotlib`
- `time` or `timeit`

Example project output:

- A plot of a signal made of two sinusoids and its FFT.
- A table showing direct DFT time vs FFT time.
- A visualization of zero-padding improving frequency-grid resolution.

### Ability 5: FIR filter design with windows

Source notes:

- `Subfiles/LEC-7/Ideal Low-Pass Filters, Windowing Techniques, FIR & IIR Filters.md`
- `Subfiles/LEC-7/audio1.py`

What to build:

- Design low-pass, high-pass, band-pass, and band-stop FIR filters.
- Use sinc impulse responses.
- Apply windows:
  - Rectangular
  - Hann
  - Hamming
  - Blackman
  - Kaiser
- Plot impulse response, magnitude response, phase response, and dB response.
- Apply filters to test signals and audio.

Useful functions:

```python
ideal_lowpass(cutoff, num_taps)
fir_lowpass(cutoff, num_taps, window="hamming")
fir_highpass(cutoff, num_taps, window="hamming")
frequency_response(b, a=None, worN=1024)
apply_fir(x, b)
```

Useful libraries:

- `numpy`
- `scipy.signal`
- `matplotlib`

How this connects to `audio1.py`:

- Move the filter design code out of the script and into `filters.py`.
- Move microphone/audio logic into `audio.py`.
- Keep examples in `examples/04_filter_audio.py`.

### Ability 6: IIR filter analysis

Source notes:

- `Subfiles/LEC-7/Ideal Low-Pass Filters, Windowing Techniques, FIR & IIR Filters.md`
- `Subfiles/LEC-9/LEC9.md`
- `Exams/Questions&Answers.md`

What to build:

- Represent IIR filters using numerator `b` and denominator `a`.
- Compute frequency response.
- Plot poles and zeros.
- Check stability: all poles must be inside the unit circle.
- Simulate recursive difference equations.

Useful functions:

```python
iir_frequency_response(b, a)
poles_zeros(b, a)
is_stable_iir(a)
apply_iir(x, b, a)
```

Useful libraries:

- `numpy`
- `scipy.signal`
- `matplotlib`

Example:

For:

```text
y[n] = 0.9*y[n-1] + x[n]
```

Use:

```python
b = [1.0]
a = [1.0, -0.9]
```

The pole is at `0.9`, so the system is stable.

### Ability 7: Sampling, quantization, aliasing, and reconstruction simulator

Source notes:

- `Subfiles/1. Signal Fundamentals.md`
- `Subfiles/LEC-8/Lecture 8- DFT, FFT, and Sampling Theory.md`
- `Subfiles/LEC-9/LEC9.md`

What to build:

- Generate a continuous-looking signal.
- Sample it at different sampling frequencies.
- Show aliasing when `fs < 2*fmax`.
- Quantize with different bit depths.
- Reconstruct using:
  - Ideal sinc interpolation
  - Zero-order hold
  - First-order hold

Useful functions:

```python
sample_signal(func, fs, duration)
quantize_uniform(x, bits)
zero_order_hold(samples, up_factor)
first_order_hold(samples, up_factor)
sinc_reconstruct(samples, fs, t_new)
```

Useful libraries:

- `numpy`
- `matplotlib`
- `scipy.interpolate`

Example project output:

- One figure with original signal, sampled points, quantized points, and reconstructed signal.
- A warning label when the selected sampling rate violates Nyquist.

### Ability 8: Upsampling and downsampling lab

Source notes:

- `Subfiles/LEC-9/LEC9.md`
- `Fatma/Fatma 1 to 10 DSP.md`

What to build:

- Upsample by inserting zeros.
- Apply anti-imaging filter after upsampling.
- Downsample by keeping every M-th sample.
- Apply anti-aliasing filter before downsampling.
- Plot the signal and spectrum before and after.

Useful functions:

```python
upsample(x, M)
downsample(x, M)
anti_imaging_filter(M, num_taps)
anti_aliasing_filter(M, num_taps)
resample_rational(x, up, down)
```

Useful libraries:

- `numpy`
- `scipy.signal`
- `matplotlib`

Important rules:

- Upsampling by `M`: filter after inserting zeros, cutoff `\pi/M`, gain `M`.
- Downsampling by `M`: filter before keeping every M-th sample, cutoff `\pi/M`.

### Ability 9: Z-transform and pole-zero visualizer

Source notes:

- `Subfiles/LEC-9/LEC9.md`
- `Fatma/Fatma 1 to 10 DSP.md`
- `Exams/2025 mid/2025 solution.md`

What to build:

- Enter numerator and denominator coefficients.
- Plot poles and zeros on the z-plane.
- Draw unit circle.
- Check if DTFT exists by checking whether the unit circle is in the ROC.
- Check stability for causal systems.
- Show common z-transform pairs.

Useful functions:

```python
plot_zplane(b, a)
is_stable_from_poles(poles)
z_transform_pair_lookup(name)
partial_fraction_expansion(b, a)
```

Useful libraries:

- `numpy`
- `scipy.signal`
- `scipy.interpolate`
- `matplotlib`
- `sympy` for symbolic work, if needed

### Ability 10: Audio DSP tools

Source notes:

- `Subfiles/LEC-7/audio1.py`
- `Subfiles/LEC-7/Ideal Low-Pass Filters, Windowing Techniques, FIR & IIR Filters.md`

What to build:

- Load `.wav` files.
- Record microphone audio if hardware is available.
- Save filtered audio.
- Plot waveform and spectrum.
- Apply low-pass, high-pass, and band-pass filters.
- Compare original and filtered audio.
- Build a spectrogram viewer.

Recommended improvement over current script:

- Prefer file-based audio first because it is easier to test.
- Keep microphone support optional.
- Use `sounddevice` and `soundfile` or keep `pyaudio` if it already works on your machine.

Useful functions:

```python
read_wav(path)
write_wav(path, fs, x)
record_audio(seconds, fs=44100)
play_audio(x, fs=44100)
plot_spectrogram(x, fs)
```

Useful libraries:

- `numpy`
- `scipy.io.wavfile`
- `soundfile`
- `sounddevice`
- `matplotlib`

### Ability 11: Speech feature extraction mini-project

Source notes:

- `Subfiles/LEC-7/Ideal Low-Pass Filters, Windowing Techniques, FIR & IIR Filters.md`

What to build:

- Split speech into 20-30 ms frames.
- Apply Hamming or Hann window.
- Compute FFT per frame.
- Show spectrogram.
- Optional advanced step: compute simple Mel filter-bank features.

Useful functions:

```python
frame_signal(x, frame_ms, hop_ms, fs)
apply_window(frames, window="hamming")
stft(frames)
power_spectrogram(X)
```

Useful libraries:

- `numpy`
- `scipy.signal`
- `matplotlib`
- `librosa` for advanced audio features

### Ability 12: Exam practice and verification tool

Source notes:

- `Exams/Questions&Answers.md`
- `Exams/2025 mid/2025 solution.md`

What to build:

- Store known exercise inputs and expected outputs.
- Randomize similar convolution and transform questions.
- Verify numerical answers using Python.
- Generate plots for exam explanations.

Example:

```python
def check_convolution_answer(x, h, student_answer):
    expected = np.convolve(x, h)
    return np.allclose(expected, student_answer), expected
```

This helps turn the notes into an active study tool.

## 4. Recommended Development Roadmap

### Phase 1: Create the project skeleton

Commands:

```bash
mkdir -p dsp_python_lab/src/dsp_lab
mkdir -p dsp_python_lab/examples
mkdir -p dsp_python_lab/notebooks
mkdir -p dsp_python_lab/tests
touch dsp_python_lab/src/dsp_lab/__init__.py
```

Create `dsp_python_lab/pyproject.toml`:

```toml
[project]
name = "dsp-python-lab"
version = "0.1.0"
description = "Python DSP lab based on the DigitalSignals Obsidian notes"
requires-python = ">=3.10"
dependencies = [
  "numpy",
  "scipy",
  "matplotlib",
  "sympy",
]

[project.optional-dependencies]
audio = [
  "sounddevice",
  "soundfile",
]
notebooks = [
  "jupyter",
  "ipykernel",
]
app = [
  "streamlit",
]
dev = [
  "pytest",
]

[build-system]
requires = ["setuptools>=68"]
build-backend = "setuptools.build_meta"
```

### Phase 2: Create and activate a virtual environment

From inside `dsp_python_lab/`:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev,notebooks]"
```

For audio support:

```bash
python -m pip install -e ".[audio]"
```

For a simple web app:

```bash
python -m pip install -e ".[app]"
```

### Phase 3: Implement the core DSP modules

Start with modules that do not need hardware.

Recommended order:

1. `signals.py`
2. `convolution.py`
3. `transforms.py`
4. `filters.py`
5. `sampling.py`
6. `resampling.py`
7. `ztransform.py`
8. `audio.py`

This order is best because each later module depends on earlier concepts.

### Phase 4: Add examples

Each example should be short and visual:

```text
examples/01_signal_basics.py
examples/02_convolution.py
examples/03_fft_analysis.py
examples/04_filter_audio.py
examples/05_resampling.py
examples/06_zplane.py
```

Run examples like:

```bash
python examples/02_convolution.py
```

### Phase 5: Add tests

Tests should confirm the math matches known DSP rules.

Useful tests:

- Unit impulse convolution returns the original signal.
- Linear convolution length equals `N + M - 1`.
- Direct DFT matches `numpy.fft.fft`.
- IDFT reverses DFT.
- FFT convolution matches `numpy.convolve`.
- FIR filter coefficients are symmetric for linear phase.
- IIR stability check correctly detects poles outside the unit circle.

Run tests:

```bash
pytest
```

### Phase 6: Add notebooks or a Streamlit app

For learning, notebooks are easiest:

```bash
jupyter notebook
```

For an interactive tool, use Streamlit:

```bash
streamlit run app.py
```

Possible app tabs:

- Signal Generator
- Sampling and Aliasing
- Convolution
- FFT Analyzer
- FIR/IIR Filters
- Audio Filter
- Z-Plane

## 5. First Minimal Implementation Plan

If you want the smallest useful version, build only these files first:

```text
dsp_python_lab/
  pyproject.toml
  src/dsp_lab/
    __init__.py
    signals.py
    convolution.py
    transforms.py
    plots.py
  examples/
    01_signal_basics.py
    02_convolution.py
    03_fft_analysis.py
  tests/
    test_convolution.py
    test_transforms.py
```

Minimum abilities:

- Generate simple signals.
- Plot discrete signals.
- Compute convolution.
- Compute direct DFT and FFT.
- Compare output against NumPy.

This creates a solid base before adding filters, audio, and z-transform tools.

## 6. Example Code Design

### `signals.py`

```python
import numpy as np


def unit_impulse(n, n0=0):
    n = np.asarray(n)
    return (n == n0).astype(float)


def unit_step(n, n0=0):
    n = np.asarray(n)
    return (n >= n0).astype(float)


def sinusoid(n, omega, phase=0.0, amplitude=1.0):
    n = np.asarray(n)
    return amplitude * np.cos(omega * n + phase)


def exponential(n, a):
    n = np.asarray(n)
    return np.power(a, n)
```

### `convolution.py`

```python
import numpy as np


def linear_convolution(x, h):
    x = np.asarray(x)
    h = np.asarray(h)
    y = np.zeros(len(x) + len(h) - 1)
    for n in range(len(y)):
        total = 0.0
        for k in range(len(x)):
            h_index = n - k
            if 0 <= h_index < len(h):
                total += x[k] * h[h_index]
        y[n] = total
    return y


def circular_convolution(x, h, N=None):
    x = np.asarray(x)
    h = np.asarray(h)
    if N is None:
        N = max(len(x), len(h))
    x_pad = np.pad(x, (0, N - len(x)))
    h_pad = np.pad(h, (0, N - len(h)))
    y = np.zeros(N)
    for n in range(N):
        for k in range(N):
            y[n] += x_pad[k] * h_pad[(n - k) % N]
    return y
```

### `transforms.py`

```python
import numpy as np


def dft_direct(x):
    x = np.asarray(x, dtype=complex)
    N = len(x)
    n = np.arange(N)
    k = n.reshape((N, 1))
    W = np.exp(-2j * np.pi * k * n / N)
    return W @ x


def idft_direct(X):
    X = np.asarray(X, dtype=complex)
    N = len(X)
    k = np.arange(N)
    n = k.reshape((N, 1))
    W = np.exp(2j * np.pi * n * k / N)
    return (W @ X) / N
```

## 7. How to Convert the Existing Audio Script

Current file:

`Subfiles/LEC-7/audio1.py`

Recommended split:

```text
src/dsp_lab/audio.py
src/dsp_lab/filters.py
examples/04_filter_audio.py
```

### `audio.py`

Put only input/output operations here:

```python
def record_audio(seconds, fs=44100):
    ...


def play_audio(x, fs=44100):
    ...


def read_wav(path):
    ...


def write_wav(path, fs, x):
    ...
```

### `filters.py`

Put only DSP math here:

```python
def fir_highpass(cutoff_hz, fs, num_taps, window="hamming"):
    ...


def apply_fir(x, taps):
    ...
```

### `examples/04_filter_audio.py`

Use the reusable functions:

```python
from dsp_lab.audio import read_wav, write_wav
from dsp_lab.filters import fir_highpass, apply_fir


fs, x = read_wav("input.wav")
taps = fir_highpass(cutoff_hz=2000, fs=fs, num_taps=51)
y = apply_fir(x, taps)
write_wav("output_highpass.wav", fs, y)
```

This makes the project cleaner and testable.

## 8. Recommended Libraries

| Library | Use |
|---|---|
| `numpy` | Arrays, signals, FFT, math |
| `scipy` | Signal processing, filters, convolution, frequency response |
| `matplotlib` | Plots |
| `sympy` | Symbolic formulas, partial fractions, optional z-transform help |
| `pytest` | Tests |
| `jupyter` | Interactive notebooks |
| `soundfile` | Read/write audio files |
| `sounddevice` | Record/play audio |
| `streamlit` | Optional web interface |
| `librosa` | Advanced audio and speech features, optional |

## 9. Good Project Names

Possible names:

- `dsp-python-lab`
- `digital-signals-lab`
- `fcl-dsp-toolkit`
- `signals-and-systems-python`
- `dsp-exam-helper`

Best name:

`dsp-python-lab`

It is short, clear, and matches the directory content.

## 10. Suggested Final Project Features

A polished final version could include:

1. Signal generator with plots.
2. Sampling and quantization simulator.
3. Convolution calculator with step-by-step visualization.
4. DFT/FFT analyzer with magnitude and phase plots.
5. FIR filter designer with window comparison.
6. IIR stability checker with pole-zero plot.
7. Audio filtering demo.
8. Upsampling/downsampling demo.
9. Z-transform visualizer.
10. Exam practice checker.

## 11. Suggested Milestones

### Milestone 1: Basic package

Goal:

- Create package structure.
- Add signal generation.
- Add convolution.
- Add direct DFT and IDFT.
- Add tests.

Deliverable:

- `pytest` passes.
- Example scripts generate plots.

### Milestone 2: Frequency analysis

Goal:

- Add FFT plots.
- Add zero-padding demo.
- Add magnitude and phase plotting.

Deliverable:

- A working `examples/03_fft_analysis.py`.

### Milestone 3: Filters

Goal:

- Add FIR low-pass and high-pass filters.
- Add window comparison.
- Add frequency response plots.

Deliverable:

- A script that designs a Hamming-window FIR filter and plots its response.

### Milestone 4: Sampling and resampling

Goal:

- Add sampling, quantization, ZOH, FOH.
- Add upsampling and downsampling.

Deliverable:

- A notebook showing aliasing and anti-aliasing filters.

### Milestone 5: Audio

Goal:

- Convert `audio1.py` into reusable functions.
- Add file-based audio filtering.
- Add optional microphone demo.

Deliverable:

- Input `.wav` -> filter -> output `.wav`.

### Milestone 6: Z-transform and exam helper

Goal:

- Add pole-zero plotting.
- Add stability checks.
- Add known exam examples as tests.

Deliverable:

- A z-plane plot and automated verification for at least three exam problems.

## 12. Important Engineering Advice

### Keep notes and code separate

This directory is an Obsidian vault. Do not scatter Python files across lecture
folders. Put the real project in one folder like `dsp_python_lab/`.

### Start with file-based audio

Microphone and speaker code depends on hardware and drivers. Start with `.wav`
files first, then add live microphone support later.

### Test math before building UI

Build and test the core DSP functions before making notebooks or a web app.
Otherwise, visual bugs and math bugs become mixed together.

### Use SciPy for production functions, but implement basics manually for learning

For learning:

- Implement direct convolution.
- Implement direct DFT.
- Implement simple FIR design.

For real use:

- Use `numpy.fft.fft`.
- Use `scipy.signal.convolve`.
- Use `scipy.signal.freqz`.
- Use `scipy.signal.lfilter`.

### Make every example match a lecture concept

Example mapping:

| Example | Related note |
|---|---|
| Signal generation | `Subfiles/1. Signal Fundamentals.md` |
| Convolution | `Subfiles/2 Convolution Theory for LTI Systems.md` |
| DFT and FFT | `Subfiles/LEC-8/Lecture 8- DFT, FFT, and Sampling Theory.md` |
| FIR/IIR filters | `Subfiles/LEC-7/Ideal Low-Pass Filters, Windowing Techniques, FIR & IIR Filters.md` |
| Resampling | `Subfiles/LEC-9/LEC9.md` |
| Z-transform | `Subfiles/LEC-9/LEC9.md` |

## 13. Recommended First Task

Start by creating the package and implementing:

1. `unit_impulse`
2. `unit_step`
3. `linear_convolution`
4. `circular_convolution`
5. `dft_direct`
6. `idft_direct`

Then add tests for these functions.

After this works, add filters and audio.

## 14. Summary

This directory can support a complete Python DSP learning project. The strongest
abilities available from the notes are:

- Signal generation and plotting.
- System classification.
- Linear and circular convolution.
- DTFT/DFT/FFT analysis.
- FIR and IIR filter design.
- Sampling, quantization, aliasing, and reconstruction.
- Upsampling and downsampling.
- Z-transform and pole-zero analysis.
- Audio filtering.
- Exam-practice verification.

The best implementation strategy is to create a clean `dsp_python_lab/` package
inside this directory, then build the project in phases from basic signal tools
to filters, audio, and exam helpers.
