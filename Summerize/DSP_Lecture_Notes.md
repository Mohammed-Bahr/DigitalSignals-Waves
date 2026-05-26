---
Created: " 2026-04-07 21:12"
tags:
  - FACL
  - DigitalSignals
Source:
---
> [!quote] To be great is to be misunderstood.
> — Ralph Emerson

**"اللهم إني أسألك فهم النبيين، وحفظ المرسلين، والملائكة المقربين، اللهم اجعل ألسنتنا عامرة بذكرك، وقلوبنا بخشيتك، إنك على كل شيء قدير"**

---
## Signal Fundamentals

### Definition
A **signal** is a physical quantity changing with time (or any independent variable). Mathematically, it's a function:
- $x: \mathbb{R} \rightarrow \mathbb{R}$ (real-valued)
- $x: \mathbb{R} \rightarrow \mathbb{C}$ (complex-valued)

Real numbers include both rational and irrational numbers.

### Signal Classification

Signals can be categorized into four types based on time and value:

| Type | Time | Value | Description |
|------|------|-------|-------------|
| 1 | Continuous | Continuous | Analog signals (e.g., $x(t)$ continuous wave) |
| 2 | Continuous | Discrete | Sampled signals |
| 3 | Discrete | Continuous | Discrete-time analog |
| 4 | Discrete | Discrete | **Digital signals** (limited by quantization levels) |

> **Note**: Discrete time & discrete value is the only type of signal that works on computers.

**Key distinctions:**
- **Continuous value** → Analog signals
- **Discrete value** → Digital signals

---

## Analog to Digital Conversion
$$The Process: x(t) \rightarrow Sampling \rightarrow Quantization \rightarrow \bar{x}[n]$$
$$ x(t) \xrightarrow{\text{Sampling}} x_s(t) \xrightarrow{\text{Quantization}} \bar{x}[n] $$
### Sampling
$$Continuous \xrightarrow{to} Discrete$$
Converts *continuous* time to *discrete* time.
The sampled signal can be expressed as:
$$\bar{x}(t) = \sum_{n=-\infty}^{\infty} x[n] \cdot \bar{\delta}(t - nT)$$

### Quantization
$$Analog \xrightarrow{To} Digital$$
Quantization error is irreversible. When quantizing to levels (e.g., 100 levels), each level has a quantization step of 0.15.

---

## Discrete-Time Systems

**Definition**: An operation that can take input signal(s) and produce output signal(s).
$$x[n] \longrightarrow \boxed{\text{System } T()} \longrightarrow y[n]$$
$$y[n] = T[x[n] , n]$$

### System Classification Based on Linearity
>in real life there is no linear system but it is almost linear 

**Linear System**: Satisfies superposition and scaling
$$ T[\alpha_1 x_1[n] + \alpha_2 x_2[n]] = \alpha_1 T[x_1[n]] + \alpha_2 T[x_2[n]]$$

**Non-linear System**: Does not satisfy linearity (otherwise)

### Time Invariance

If input shift leads to output shift by the same value:
$$y[n - n_0] = T[x[n - n_0]]$$

#### Examples:
- $y[n] = 3n^2 \times [n]$ → Linear, Time-varying
- $y[n] = 3x[n] - 2x[n-5]$ → Linear, Time-invariant
- $y[n] = 3x^2[n] - 2x^3[n-5]$ → Non-linear, Time-invariant
- $y[n] = 3x[-n] - 2x[n-5]$ → Non-linear, Time-varying

## Discrete Time System Classification :
### According to I/O Cordinality :
1. `SISO` $\rightarrow$ Single Input Single Output
2. `SIMO` $\rightarrow$ Single Input Multiple Output
3. `MISO` $\rightarrow$ Multiple Input Single Output
4. `MIMO` $\rightarrow$ Multiple Input Multiple Output

### Linear Time-Invariant (LTI) Systems

- Described by difference equations that are linear with constant coefficients
- **Homogeneous** property

>Systems will never be linear if it have higher power time shifting .

### System Properties Based on Causality

- **Causal**: Output doesn't depend on future input
- **Non-causal**: Output depends on future input

Examples:
- $y[n] = 3x[n+5]$ → Non-causal
- $y[n+1] = 3x[n]$ → Causal
- $5y[n] = 4x[n-3]$ → Causal

### Memory-Based Classification

- **Memoryless**: Output only depends on current input
- **With Memory**: Output depends on past/future inputs

Example: A channel between 2 devices is an LTI system
$$y[n] = E_n / E_1 = 2 \times [n - k]$$

Ideal Channel is LTI-Causal, Memoryless

### Stability (BIBO Sense)

A system is stable if: **Bounded Input → Bounded Output**

---

## Convolution Theory of LTI Systems

The relationship between output and input of LTI systems can be described by convolution:

$$y[n] = x[n] * h[n] = \sum_{k=-\infty}^{\infty} x[k] \cdot h[n-k]$$

where $h[n]$ is the **impulse response** of the LTI system.

### Impulse Response

The impulse response of a system is the output when the input is an impulse $\delta[n]$.

### Finding Impulse Response

**Example 1:**
Given: $y[n] = 3x[n] - x[n-2] - 1 \cdot x[n-3]$

The impulse response:
$$h[n] = 3\delta[n] - \delta[n-2] - 1 \cdot \delta[n-3]$$
$$h = [3, 0, -1, -1]$$

**Example 2:**
System: $y[n] = 1.1 y[n-1] + x[n]$

Assuming the system is initially at rest:

The homogeneous relation: $h[n] = 1.1 h[n-1] + \delta[n]$

Using the recurrence:
- $h[0] = 1.1 h[-1] + \delta[0] = 1.1(0) + 1 = 1$
- $h[1] = 1.1 h[0] + \delta[1] = 1.1(1) + 0 = 1.1$
- $h[2] = 1.1 h[1] + \delta[2] = 1.1(1.1) + 0 = (1.1)^2$

Solution: $h[n] = (1.1)^n$

### Properties of Convolution

1. **Commutative**: $x[n] * h[n] = h[n] * x[n]$

2. **Associative**: $x[n] * (h_1[n] * h_2[n]) = (x[n] * h_1[n]) * h_2[n]$

3. **Distributive over addition**: $x[n] * (h_1[n] + h_2[n]) = x[n] * h_1[n] + x[n] * h_2[n]$

4. **Identity**: $x[n] * \delta[n] = x[n]$

### Extension of Commutative Property

Any linear operation is commutative with convolution:
$$x[n] * \delta[n-k] = x[n-k]$$

---

## Frequency Analysis of Signals and Systems

### Periodic Signals

A signal $x[n]$ is periodic with period $N$ if:
$$x[n + N] = x[n]$$

The **fundamental period** is the least value of N.

### Periodicity of Sinusoids

$\sin(\omega n)$ is periodic if we can find $N = 2\pi k/\omega$ such that k and N are integers.

**Example**: Is $x[n] = \sin(\frac{\pi}{9} n)$ periodic?

For $x[n + kN] = x[n]$ to equal $x[n]$:
$$\frac{\pi}{9} kN \text{ should be a multiple of } 2\pi$$

The least value of $kN$ is 18. Therefore, the fundamental period is 18.

### Aliasing of Discrete-Time Frequencies

Note: $\sin(\omega n + 2\pi kn) = \sin(\omega n)$ for all $k, n \in \mathbb{Z}$

Therefore: $\omega \equiv \omega + 2\pi k$

In DSP, frequency analysis is restricted to frequencies from $-\pi$ to $\pi$:
$$\omega \in [-\pi, \pi]$$

---

## Continuous to Discrete Conversion in Frequency Domain

Remember: C/D in time domain involves:
$$x_s(t) = x(t) \cdot P(t) = \sum_{n=-\infty}^{\infty} x(nT) \cdot \delta(t - nT)$$

The Fourier transform of the sampled signal:
$$X_s(j\Omega) = \int_{-\infty}^{\infty} x_s(t) e^{-j\Omega t} dt$$

---

## Discrete-Time Fourier Transform (DTFT)

For a discrete-time signal $x[n]$:

$$X(e^{j\omega}) = \sum_{n=-\infty}^{\infty} x[n] e^{-j\omega n}$$

where $\omega \in [-\pi, \pi]$

### Relation with Continuous-Time Fourier Transform

- Discrete in time domain → Continuous in frequency domain
- Continuous in time domain → Discrete in frequency domain

Notations:
- $t$: time (continuous)
- $n$: time index (discrete, "normalized time")
- $\Omega$: angular frequency (rad/second)
- $\omega$: radian frequency (normalized, rad/sample)

### Discrete Fourier Transform (DFT)

Since $\omega$ is continuous and DTFT can be computed on computers, we use DFT.

In DFT, frequency is sampled. If the number of samples needed is N, the obtained frequencies are:
$$\omega_k = \frac{2\pi}{N}k, \quad k = 0, 1, 2, \ldots, N-1$$

### Fourier Transform of Basic Signals

#### 1. Impulse: $\delta[n]$
$$X(e^{j\omega}) = \sum_{n=-\infty}^{\infty} \delta[n] e^{-j\omega n} = e^{-j\omega(0)} = 1$$

#### 2. Right-sided Exponential: $x[n] = a^n u[n]$

$$X(e^{j\omega}) = \sum_{n=0}^{\infty} a^n e^{-j\omega n} = \frac{1}{1 - ae^{-j\omega}}, \quad |a| < 1$$

#### 3. Left-sided Exponential: $x[n] = -a^n u[-n-1]$

$$X(e^{j\omega}) = \frac{-ae^{j\omega}}{1 - ae^{j\omega}} = \frac{1}{1 - ae^{-j\omega}}, \quad |a| > 1$$

#### 4. Unit Step: $u[n]$

$$X(e^{j\omega}) = \sum_{n=0}^{\infty} e^{-j\omega n} = \frac{1}{1 - e^{-j\omega}} + \pi \sum_{k=-\infty}^{\infty} \delta(\omega - 2\pi k)$$

#### 5. Cosine: $\cos(\omega_0 n)$

$$X(e^{j\omega}) = \pi \sum_{k=-\infty}^{\infty} [\delta(\omega - \omega_0 - 2\pi k) + \delta(\omega + \omega_0 - 2\pi k)]$$

#### 6. Sine: $\sin(\omega_0 n)$

$$X(e^{j\omega}) = \frac{\pi}{j} \sum_{k=-\infty}^{\infty} [\delta(\omega - \omega_0 - 2\pi k) - \delta(\omega + \omega_0 - 2\pi k)]$$

### DTFT Properties

#### 1. Periodicity
$$X(e^{j(\omega + 2\pi)}) = X(e^{j\omega})$$

#### 2. Linearity
If $x[n] = \alpha_1 x_1[n] + \alpha_2 x_2[n]$, then:
$$X(e^{j\omega}) = \alpha_1 X_1(e^{j\omega}) + \alpha_2 X_2(e^{j\omega})$$

#### 3. Time Shift
If $x[n-k] \xrightarrow{DTFT} X(e^{j\omega})$, then:
$$e^{-j\omega k} X(e^{j\omega})$$

This causes a **linear phase shift** (no phase distortion).

#### 4. Frequency Shift (Modulation)
$$e^{j \omega_0 n} x[n] \xleftarrow{\text{DTFT}} X(e^{j(\omega - \omega_0)})$$

This is used for modulation, where $f = \omega_0$ is the corner frequency.

#### 5. Convolution in Time Domain (Filtering)
If $y[n] = x[n] * h[n]$, then:
$$Y(e^{j\omega}) = X(e^{j\omega}) \cdot H(e^{j\omega})$$

This means: Convolution in time domain = Multiplication in frequency domain.

#### 6. Multiplication in Time Domain (Windowing)
If $y[n] = x[n] \cdot w[n]$, then:
$$Y(e^{j\omega}) = \frac{1}{2\pi} X(e^{j\omega}) * W(e^{j\omega})$$

#### 7. Energy Conservation (Parseval's Theorem)
Signal energy: $E = \sum_{n=-\infty}^{\infty} |x[n]|^2 = \frac{1}{2\pi} \int_{-\pi}^{\pi} |X(e^{j\omega})|^2 d\omega$

#### 8. Derivative in Frequency Domain
$$\frac{d}{d\omega} X(e^{j\omega}) = -j \sum_{n=-\infty}^{\infty} n \cdot x[n] e^{-j\omega n}$$

#### 9. Symmetry Properties

- **Real even signal** → DTFT is pure real and even
- **Real odd signal** → DTFT is pure imaginary and odd
- **Real signal** → DTFT is conjugate symmetric (even)
- **Imaginary signal** → DTFT is conjugate anti-symmetric (odd)

---

## Filter Types and Classification

### Ideal Filters

An ideal filter multiplies pass-band components by 1 and stop-band components by 0.

**Ideal Low-Pass Filter**:
$$H(e^{j\omega}) = \begin{cases} 1 & |\omega| \leq \omega_c \\ 0 & \omega_c < |\omega| \leq \pi \end{cases}$$

The impulse response (sinc function):
$$h[n] = \frac{\sin(\omega_c n)}{\pi n}$$

This filter is **ideal but anti-causal** with infinite support.

### Practical Filters

#### Finite Impulse Response (FIR) Filters

- Used to approximate ideal filters
- Non-recursive
- Linear phase possible
- Output: $y[n] = \sum_{k=0}^{M} a_k x[n-k]$

**Example - Moving Average Filter (order 2)**:
$$y[n] = \frac{1}{2}(x[n] + x[n-1])$$

The impulse response:
$$h[n] = \frac{1}{2} \delta[n] + \frac{1}{2} \delta[n-1]$$

**Frequency Response**:
$$H(e^{j\omega}) = \frac{1}{2}(1 + e^{-j\omega}) = e^{-j\omega/2} \cos(\omega/2)$$

This has **linear phase** (no phase distortion).

#### Infinite Impulse Response (IIR) Filters

- Recursive filters (can continue until infinity)
- Frequency response appears as a rational function
- Can achieve same performance with lower order than FIR
- **Disadvantage**: Nonlinear phase change, linear only in limited frequency

**Example**:
$$y[n] = 0.9 y[n-1] + x[n]$$

Taking DTFT:
$$Y(e^{j\omega}) = 0.9 e^{-j\omega} Y(e^{j\omega}) + X(e^{j\omega})$$

$$H(e^{j\omega}) = \frac{1}{1 - 0.9e^{-j\omega}}$$

### Windowing Functions for FIR Design

- Rectangular window
- Hanning window
- Hamming window
- Blackman window
- Raised cosine, Triangle, etc.

### Speech Processing Application

Speech is a non-stationary random signal. To analyze it:
1. **Segmentation** through windowing (frames of ~20-30ms where signal is stationary)
2. Use **Hamming window** instead of rectangular to avoid spectral distortion

**Feature Extraction Methods**:
- Filter Bank
- Mel-Frequency Cepstral Coefficients (MFCC)
- Log Scale spectrogram

---

## Sampling Theory

### Ideal Sampling

Given continuous signal $x_c(t)$, the sampled signal:
$$x_s(t) = x_c(t) \cdot P(t) = x_c(t) \sum_{n=-\infty}^{\infty} \delta(t - nT)$$

### Fourier Series Representation of Impulse Train

The impulse train $P(t) = \sum_{k=-\infty}^{\infty} \delta(t - nT)$ is periodic with period T.

Using Fourier series:
$$P(t) = \sum_{k=-\infty}^{\infty} c_k e^{-j\frac{2\pi k t}{T}}$$

where $c_k = \frac{1}{T}$ for all k.

Therefore:
$$X_s(j\Omega) = \frac{1}{T} \sum_{k=-\infty}^{\infty} X_c(j(\Omega - \frac{2\pi k}{T}))$$

### Nyquist-Shannon Sampling Theorem

For no aliasing (overlap) to occur:
$$\Omega_s = \frac{2\pi}{T} \geq 2\Omega_m$$

where $\Omega_m$ is the maximum frequency in the signal (bandwidth B).

**Critical Sampling Frequency (Nyquist Rate)** = $2 \times$ maximum frequency

If sampling rate < Nyquist rate, the signal will be distorted (aliasing occurs).

### Signal Recovery (D/C Conversion)

To recover continuous signal from sampled signal, use an **Ideal Recovery Filter**:

$$H_r(j\Omega) = \begin{cases} T & |\Omega| < \frac{\pi}{T} \\ 0 & \text{otherwise} \end{cases}$$

The impulse response:
$$h_r(t) = \frac{\sin(\pi t/T)}{\pi t/T} = \text{sinc}(t/T)$$

This is ideal but **anti-causal** with infinite response.

### Practical Interpolation Methods

When sampling rate is very small (< 2× Nyquist):
- Zero-order hold interpolator
- First-order hold interpolator
- Other interpolation methods

---

## Fast Fourier Transform (FFT)

### DFT Definition

For an N-point sequence:
$$X[k] = \sum_{n=0}^{N-1} x[n] e^{-j\frac{2\pi}{N}kn}$$

Frequency indices: $\omega_k = \frac{2\pi}{N}k$

Inverse DFT:
$$x[n] = \frac{1}{N} \sum_{k=0}^{N-1} X[k] e^{j\frac{2\pi}{N}kn}$$

### DFT vs DTFT

1. **DTFT is continuous** in frequency; **DFT is sampled** at specific points
2. **DFT range**: $\omega = 0$ to $2\pi$; **DTFT range**: $\omega = -\pi$ to $\pi$
3. **DFT**: Circular convolution in time ≡ Multiplication in frequency
4. **DTFT**: Linear convolution in time ≡ Multiplication in frequency

### FFT Complexity

- **Direct computation**: $O(N^2)$
- **FFT algorithm** (when N is power of 2): $O(N \log N)$

### FFT Algorithm (Radix-2 Decimation-in-Time)

For N = 2, 4, 8, 16, 32, 64, ...

The N-point DFT can be split into:
$$X[k] = \sum_{n=0}^{N-1} x[n] e^{-j\frac{2\pi}{N}kn}$$

Split into even and odd indexed samples:

**Even samples**: $n = 2m$
**Odd samples**: $n = 2m + 1$

$$X[k] = \sum_{m=0}^{M-1} x[2m] e^{-j\frac{2\pi}{M}km} + e^{-j\frac{2\pi}{N}k} \sum_{m=0}^{M-1} x[2m+1] e^{-j\frac{2\pi}{M}km}$$

where $M = N/2$

### Butterfly Diagram

The butterfly operation is the basic computation unit in FFT:
$$e^{-j\frac{2\pi}{N}k} = W_N^k$$

For inverse FFT, use $(W_N^k)^*$

### 8-Point FFT Example

Given: $x = [3, 2, 1, 8, ...]$

The butterfly diagram computes the transform iteratively.

---

## Summary Table: DTFT of Basic Signals

| Signal | $x[n]$ | $X(e^{j\omega})$ | Condition |
|--------|--------|-------------------|-----------|
| Impulse | $\delta[n]$ | 1 | - |
| Right-sided exponential | $a^n u[n]$ | $\frac{1}{1 - ae^{-j\omega}}$ | $|a| < 1$ |
| Left-sided exponential | $-a^n u[-n-1]$ | $\frac{1}{1 - ae^{-j\omega}}$ | $|a| > 1$ |
| Unit step | $u[n]$ | $\frac{1}{1 - e^{-j\omega}} + \pi\sum\delta(\omega - 2\pi k)$ | - |
| Cosine | $\cos(\omega_0 n)$ | $\pi\sum[\delta(\omega - \omega_0 - 2\pi k) + \delta(\omega + \omega_0 - 2\pi k)]$ | - |
| Sine | $\sin(\omega_0 n)$ | $\frac{\pi}{j}\sum[\delta(\omega - \omega_0 - 2\pi k) - \delta(\omega + \omega_0 - 2\pi k)]$ | - |

---

## Inverse DTFT Using Partial Fractions

### Method

For rational functions $X(e^{j\omega}) = \frac{P(e^{j\omega})}{Q(e^{j\omega})}$:

1. Factor the denominator
2. Express as sum of partial fractions
3. Find coefficients using residue method
4. Apply inverse DTFT to each term

### Example

$$X(e^{j\omega}) = \frac{3 + e^{-j\omega}}{1 - 0.75e^{-j\omega} + 0.125e^{-j2\omega}}$$

Factor:
$$= \frac{3 + e^{-j\omega}}{(1 - 0.5e^{-j\omega})(1 - 0.25e^{-j\omega})}$$

Partial fraction expansion:
$$\frac{A}{1 - 0.5e^{-j\omega}} + \frac{B}{1 - 0.25e^{-j\omega}}$$

Find A and B, then apply inverse transform to get:
$$x[n] = 10(0.5)^n u[n] - 7(0.25)^n u[n]$$

---

## Important Formulas Reference

### Convolution
$$y[n] = x[n] * h[n] = \sum_{k=-\infty}^{\infty} x[k] \cdot h[n-k]$$

### DTFT
$$X(e^{j\omega}) = \sum_{n=-\infty}^{\infty} x[n] e^{-j\omega n}$$

### IDFT
$$x[n] = \frac{1}{2\pi} \int_{-\pi}^{\pi} X(e^{j\omega}) e^{j\omega n} d\omega$$

### DFT
$$X[k] = \sum_{n=0}^{N-1} x[n] e^{-j\frac{2\pi}{N}kn}$$

### IDFT
$$x[n] = \frac{1}{N} \sum_{k=0}^{N-1} X[k] e^{j\frac{2\pi}{N}kn}$$

### Parseval's Theorem
$$\sum_{n=-\infty}^{\infty} |x[n]|^2 = \frac{1}{2\pi} \int_{-\pi}^{\pi} |X(e^{j\omega})|^2 d\omega$$

### Geometric Series
$$\sum_{n=0}^{\infty} a^n = \frac{1}{1-a}, \quad |a| < 1$$

---

**Note**: This document contains lecture notes from a DSP course. Some content may include OCR artifacts or unclear text that has been interpreted to the best ability. For precise definitions and derivations, refer to standard DSP textbooks like Oppenheim & Schafer's "Discrete-Time Signal Processing."