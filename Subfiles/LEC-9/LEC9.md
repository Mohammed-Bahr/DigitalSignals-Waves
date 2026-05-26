---
Created: " 2026-05-11 11:24"
modified: 2026-05-11 11:24
tags:
  - FACL
  - DigitalSignals
Doc Lec order: LEC 9
Source:
---
> [!quote] A jug fills drop by drop.
> — Buddha

**"اللهم إني أسألك فهم النبيين، وحفظ المرسلين، والملائكة المقربين، اللهم اجعل ألسنتنا عامرة بذكرك، وقلوبنا بخشيتك، إنك على كل شيء قدير"**

---
 I'll analyze this Arabic lecture transcript on digital signal processing. Let me break down what the professor is teaching and explain it clearly.

## Overview
This is a **Digital Signal Processing (DSP)** lecture covering:
1. **Sampling Theory Review** (from previous lecture)
2. **Upsampling & Downsampling** (digital resampling)
3. **Z-Transform** (discrete-time equivalent of Laplace transform)

---

## Part 1: Sampling Theory Review (0:00 - 9:00)

### Ideal Sampling Recap
The professor starts by reviewing **ideal sampling**:

$$x_s(t) = x(t) \cdot \sum_{n=-\infty}^{\infty} \delta(t - nT) = \sum_{n=-\infty}^{\infty} x(nT)\delta(t-nT)$$

**Key insight**: Sampling is just multiplication by an impulse train.

### Frequency Domain Effect
In frequency domain, sampling causes **spectral repetition** (aliasing copies):

$$X_s(j\omega) = \frac{1}{T}\sum_{k=-\infty}^{\infty} X\left(j\left(\omega - \frac{2\pi k}{T}\right)\right)$$

The professor draws this: if original signal has bandwidth B, after sampling, copies appear at multiples of $\omega_s = \frac{2\pi}{T}$.

### Recovery Filter
To recover the original signal, we use a **reconstruction filter** (recovery filter):
- In frequency domain: $H_r(j\omega) = T$ for $|\omega| < \frac{\pi}{T}$ (Nyquist frequency), zero otherwise
- In time domain: This is a **sinc function** — $h_r(t) = \text{sinc}\left(\frac{\pi t}{T}\right)$

**Problem**: The sinc filter is **non-causal and infinitely long** (extends from $-\infty$ to $+\infty$), so it's not physically realizable.

### Practical Interpolators
Instead of ideal sinc, we use approximations:
- **Zero-Order Hold (ZOH)**: Repeats each sample value until next sample
- **First-Order Hold**: Linear interpolation between samples

---

## Part 2: Upsampling (Interpolation) — Starting at 9:00
![[Screenshot_20260511-120045.png]]
### What is Upsampling?
Upsampling by factor **M** means inserting M-1 zeros between samples.

**Example** (M=2):
- Original $x[n]$: [1, 2, 0.5, 1.5]
- After upsampling: [1, **0**, 2, **0**, 0.5, **0**, 1.5, **0**]

The equation: $y[n] = x[n/M]$ when n is multiple of M, else 0.

### Frequency Domain Effect
![[Screenshot_20260511-120624.png]]
The professor derives:
$$Y(e^{j\omega}) = X(e^{j\omega M})$$

**What happens?**
- The spectrum **compresses** by factor M
- Bandwidth shrinks from B to B/M
- **More aliasing copies appear** in the baseband [-π, π]

### The Need for Interpolation Filter
After upsampling, we need a **low-pass digital filter** to remove the spectral images (aliases) and "fill in" the zeros with interpolated values.

- Cutoff frequency: $\omega_c = \frac{\pi}{M}$
- Gain: M (to compensate for energy loss)
- This is called an **anti-imaging filter** or **interpolation filter**

### Practical Interpolation
The ideal filter would be a sinc in time domain — again, not realizable. So we use:
- **Zero-Order Interpolator**: Just repeat each sample M times
- **First-Order (Linear) Interpolator**: Connect samples with straight lines

**Real-world analogy**: The professor mentions audio "slow-down" effect and **super-resolution** in image processing — same mathematical concept.

---

## Part 3: Downsampling (Decimation) — Starting at 44:00

### What is Downsampling?
Downsampling by factor **M** means keeping every M-th sample and discarding the rest.

**Example** (M=2):
- Original: [1, 2, 0.5, 1.5, 1, ...]
- After downsampling: [1, 0.5, 1, ...]

The equation: $y[n] = x[nM]$

### The Critical Problem: Aliasing
Downsampling **stretches** the spectrum by factor M. If the original bandwidth is too large, the stretched copies **overlap** (aliasing distortion).

**Condition to avoid aliasing**: Original signal bandwidth must satisfy $B < \frac{\pi}{M}$

### Anti-Aliasing Filter (Pre-filtering)
**BEFORE** downsampling, we MUST apply a **low-pass filter**:
- Cutoff: $\omega_c = \frac{\pi}{M}$
- This removes frequencies that would alias after downsampling

### Complete Decimation System
1. **Anti-aliasing filter** (digital low-pass, cutoff π/M)
2. **Downsampler** (keep every M-th sample)

**Real-world analogy**: Audio "fast-forward" — voice sounds chipmunk-like because pitch increases (spectrum stretches).

---

## Part 4: Z-Transform — Starting at 1:23:42

### Definition
The **Z-Transform** is the discrete-time equivalent of Laplace transform:

$$\boxed{X(z) = \sum_{n=-\infty}^{\infty} x[n]z^{-n}}$$

Compare to DTFT: $X(e^{j\omega}) = \sum x[n]e^{-j\omega n}$

So: $z = e^{j\omega}$ on the unit circle.

### Why Z-Transform?
The professor explains two main purposes (same as Laplace):
1. **Time response**: How fast does the system respond? (speed of response)
2. **Stability**: Is the system stable or unstable?

### Inverse Z-Transform
$$x[n] = \frac{1}{2\pi j}\oint_C X(z)z^{n-1}dz$$

Integration around a closed contour in the complex z-plane.

### Region of Convergence (ROC)
Critical concept: The sum may or may not converge depending on |z|.

---

## Part 5: Key Z-Transform Pairs (1:32:00 onwards)

| Signal $x[n]$ | Z-Transform $X(z)$ | ROC |
|---------------|-------------------|-----|
| $\delta[n]$ | 1 | All z |
| $u[n]$ (unit step) | $\frac{1}{1-z^{-1}}$ | $\|z\| > 1$ |
| $a^n u[n]$ (right-sided) | $\frac{1}{1-az^{-1}}$ | $\|z\| > \|a\|$ |
| $-a^n u[-n-1]$ (left-sided) | $\frac{1}{1-az^{-1}}$ | $\|z\| < \|a\|$ |

**Important insight**: Same algebraic expression can have different ROCs → different signals!

### The Z-Plane
- **Unit circle** ($|z| = 1$): Boundary between stable/unstable
- **Outside unit circle** ($|z| > 1$): Right-sided signals
- **Inside unit circle** ($|z| < 1$): Left-sided signals

### Signals with NO Z-Transform
- Constant signal $x[n] = 1$ (two-sided, no overlapping ROC)
- Two-sided exponential $a^{|n|}$
- Sine/cosine without windowing (infinite in both directions)

**Why?** No region where the sum converges.

---

## Part 6: Z-Transform Properties (1:51:30 onwards)

| Property | Time Domain | Z-Domain |
|----------|------------|----------|
| **Linearity** | $a x_1[n] + b x_2[n]$ | $a X_1(z) + b X_2(z)$ |
| **Time Shift** | $x[n-k]$ | $z^{-k}X(z)$ |
| **Multiplication by n** | $n \cdot x[n]$ | $-z\frac{dX(z)}{dz}$ |
| **Convolution** | $x[n] * h[n]$ | $X(z) \cdot H(z)$ |

### The Convolution Property (Most Important!)
$$\boxed{x[n] * h[n] \xleftrightarrow{\mathcal{Z}} X(z) \cdot H(z)}$$

This is why Z-transform is powerful — **convolution becomes multiplication**.

### Transfer Function
For an LTI system:
- Impulse response: $h[n]$
- Transfer function: $H(z) = \mathcal{Z}\{h[n]\}$

Three equivalent representations:
1. **Time domain**: $h[n]$ (impulse response)
2. **Frequency domain**: $H(e^{j\omega})$ (frequency response)
3. **Z-domain**: $H(z)$ (transfer function)

---

## Summary Table: Upsampling vs Downsampling

| Aspect | Upsampling (Interpolation) | Downsampling (Decimation) |
|--------|---------------------------|--------------------------|
| **Factor M** | Expand by M | Compress by M |
| **Time effect** | Insert M-1 zeros | Keep every M-th sample |
| **Frequency effect** | Spectrum compresses | Spectrum stretches |
| **Filter needed?** | **AFTER** (anti-imaging) | **BEFORE** (anti-aliasing) |
| **Filter cutoff** | $\pi/M$ | $\pi/M$ |
| **Filter gain** | M | 1 |
| **Real-world** | Slow audio, super-resolution | Fast audio, data compression |

---

## Key Takeaways

1. **Sampling is multiplication by impulses** in time → **spectral repetition** in frequency

2. **Upsampling** needs **post-filtering** (interpolation) to smooth zeros and remove spectral images

3. **Downsampling** needs **pre-filtering** (anti-aliasing) to prevent overlap of stretched spectra

4. **Z-Transform** generalizes DTFT — analyzes system **stability** and **time response**

5. **ROC is crucial** — same formula, different ROC = different signal

6. **Convolution ↔ Multiplication** in Z-domain makes system analysis tractable