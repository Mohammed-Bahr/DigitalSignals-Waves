---
Created: " 2026-04-28 19:42"
modified: 2026-04-28 19:42
tags:
  - FACL
  - DigitalSignals
  - "#DigitalSignals/FIR"
  - "#DigitalSignals/IIR"
  - "#DigitalSignals/Filters"
Source: https://drive.google.com/file/d/17_X7YAajK7LDmHTjAHeXsKpT7gBaRJHK/view
---
> [!quote] Treat people as if they were what they ought to be and you help them to become what they are capable of being.
> — Johann Wolfgang von Goethe

**"اللهم إني أسألك فهم النبيين، وحفظ المرسلين، والملائكة المقربين، اللهم اجعل ألسنتنا عامرة بذكرك، وقلوبنا بخشيتك، إنك على كل شيء قدير"**

---

## Lecture Overview

This lecture covers **digital filter design fundamentals**, starting from ideal low-pass filters, the practical problem of ==truncation==, windowing methods to mitigate truncation effects, and the two main categories of digital filters: 
1. **FIR (Finite Impulse Response)** 
and 
2. **IIR (Infinite Impulse Response)** .

---

## Section 1: Ideal Low-Pass Filter

### Core Concept
An ideal low-pass filter perfectly passes all frequencies below a cutoff frequency ωc and completely blocks all frequencies above ωc.

### Important Formulas

**Frequency Domain Representation:**
$$H(e^{j\omega}) = \begin{cases} 1, & |\omega| < \omega_c \\ 0, & \text{otherwise} \end{cases}$$

**Time Domain Impulse Response (derived via Inverse DTFT):**
$$h[n] = \frac{1}{2\pi}\int_{-\pi}^{\pi} H(e^{j\omega}) e^{j\omega n} d\omega = \frac{\omega_c}{\pi} \int_{-\omega_c}^{\omega_c} e^{j\omega n} d\omega$$

$$h[n] = \frac{\omega_c}{\pi} \cdot \text{sinc}\left(\frac{\omega_c n}{\pi}\right) = \frac{\sin(\omega_c n)}{\pi n}$$

### Symbol Meanings
| Symbol | Meaning |
|--------|---------|
| $H(e^{j\omega})$ | Frequency response of the filter |
| $\omega_c$ | Cutoff frequency (radians/sample) |
| $h[n]$ | Impulse response in time domain |
| $\text{sinc}(x)$ | Sinc function = $\frac{\sin(\pi x)}{\pi x}$ |

### Intuition / Why It Matters
The ideal low-pass filter has a **rectangular shape** in frequency (perfect brick-wall), but its impulse response is a **sinc function** that extends from $n = -\infty$ to $n = +\infty$. This means:
- Perfect frequency selectivity
- **Infinite duration** → **Non-causal** → **Cannot be implemented in real-time!**

### Visual Description (from your notes)
Your sketch shows:
- **Top plot**: $H(e^{j\omega})$ - rectangular pulses at $\pm\omega_c$, repeating every $2\pi$
- **Bottom plot**: $h[n]$ - sinc-like function centered at $n=0$, oscillating and decaying slowly

---

## ✂️ Section 2: Truncated Ideal Filter & The Windowing Problem

### Core Concept
Since we can't implement an infinite-duration filter, we **truncate** it by multiplying with a finite-length **window function** $w[n]$:

$$h_{truncated}[n] = h_{ideal}[n] \cdot w[n]$$

### The Problem with Simple Truncation (Rectangular Window)

**Time Domain Effect:**
- Truncation = multiplying by rectangular window
- Result: Finite-length sinc function (abruptly cut off)

**Frequency Domain Effect (⚠️ CRITICAL for exams):**
- Multiplication in time $\leftrightarrow$ *Convolution in frequency*
- $H_{truncated}(e^{j\omega}) = H_{ideal}(e^{j\omega}) * W(e^{j\omega})$
- Since $W(e^{j\omega})$ for rectangular window is a **sinc-like function**, convolving creates:
  1. **Ripples in passband** (main lobe region)
  2. **Ripples in stopband** (side lobes)
  3. **Gradual transition** instead of sharp cutoff

### Visual Description
Imagine taking your perfect rectangular frequency response and **smudging/blurring** it - the sharp edges become wavy with ripples spreading into both ==passband== and ==stopband==.

---

## Section 3: Window Functions

### Core Concept
Different window shapes trade off between:
- **Main lobe width** (affects transition bandwidth)
- **Side lobe height** (affects stopband attenuation)

### Common Windows (from your list):

| Window | Characteristics |
|--------|----------------|
| **Rectangular** | Worst side lobes (~ -13 dB), narrowest main lobe |
| **Hanning (Hann)** | Moderate performance |
| **Hamming** | Better side lobe suppression than Hanning |
| **Blackman** | Very good side lobe suppression (~ -58 dB) |
| **Kaiser** | Adjustable parameter β controls trade-off |
| **Triangle** | Simpler alternative |

### Key Metrics :
- **Rectangular**: Side lobes visible, poor stopband attenuation
- **Hamming/Hanning**: Improved, ripples less noticeable
- **Blackman**: ~ **-80 dB** side lobe level (excellent!)
- **Kaiser**: Tunable via β parameter

### Decibel Scale Explanation
$$\text{dB} = 20\log_{10}(|\text{Magnitude}|)$$

**Examples from lecture:**
- -30 dB → Magnitude ≈ $10^{-1.5}$ ≈ 0.0316 (about 3% leakage)
- -40 dB → Better (less leakage)
- -80 dB → Excellent (Blackman window performance)

> **Intuition:** More negative dB = better suppression of unwanted frequencies.

---

## Section 4: Application to Speech Processing (Bonus Context)

### Why This Matters for Speech
Speech signals are **non-stationary** (statistics change over time), so we process them in short segments called **frames**:

### Processing Pipeline:
1. **Segmentation**: Split speech into 20-30 ms frames (≈300-400 samples at typical sampling rates)
2. **Windowing**: Apply Hamming/Hann window to each frame (reduces spectral leakage)
3. **FFT**: Compute spectrum of each windowed frame
4. **Feature Extraction** (MFCC pipeline):
   - Take magnitude (or power = |X|²)
   - Apply **log scale** (matches human hearing perception)
   - Apply **Mel scale** (logarithmic frequency scale - perceptually motivated)
   - **Filter bank**: Group frequencies into ~40 bands (triangular filters on Mel scale)
   - **DCT** (Discrete Cosine Transform): Compress to ~13 coefficients
   - Add deltas (velocity) → **26 features per frame**

### Spectrogram
- **2D representation**: ==Time== (frame number) vs ==Frequency== (Mel bands) vs Magnitude (color/intensity)
- Looks like an **image** → Can use CNN (Convolutional Neural Network) for processing!
- Used in modern ASR (Automatic Speech Recognition) systems

---

## Section 5: FIR Filters (Finite Impulse Response)

### Core Concept
> **FIR filters** have impulse responses of **finite length**. They are essentially truncated (windowed) versions of ideal filters or designed directly with finite coefficients.

### General Form

**Difference Equation (Time Domain):**
$$y[n] = a_0x[n] + a_1x[n-1] + a_2x[n-2] + ... + a_Mx[n-M]$$
$$
 = (a_0 + a_1e^{-j\omega} + a_2e^{-j2\omega} + ... + a_Me^{-jM\omega} )*x[n]
$$
**Frequency Response:**
$$H(e^{j\omega}) = \frac{y^(e^{j\omega})}{x(e^{j\omega})} = a_0 + a_1e^{-j\omega} + a_2e^{-j2\omega} + ... + a_Me^{-jM\omega}$$

**Key Property:** This is a **polynomial** in $e^{-j\omega}$ (not a rational function).

### Input-Output Relation
$$y[n] = x[n] * h[n] \quad \text{(convolution)}$$

---

## 💡 Section 6: Worked Example - Moving Average Filter

### Problem Statement
Given: $y[n] = \frac{1}{2}(x[n] + x[n-1])$

Find: $h[n]$ and $H(e^{j\omega})$

### Solution Step-by-Step

**Step 1: Identify h[n]**
By inspection (or set $x[n] = \delta[n]$):
$$h[n] = \frac{1}{2}(\delta[n] + \delta[n-1])$$

**Impulse Response Plot (from your notes):**
![[FACL/DigitalSignals/Subfiles/LEC-7/Attachments/image-1.png]]
Two impulses: value ½ at n=0, value ½ at n=1

**Step 2: Find H($e^{jω}$) - Method 1 (DTFT of h[n])**
$$H(e^{j\omega}) = \sum_{n=-\infty}^{\infty} h[n]e^{-j\omega n}$$

$$H(e^{j\omega}) = \frac{1}{2}e^{-j\omega \cdot 0} + \frac{1}{2}e^{-j\omega \cdot 1} = \frac{1}{2}(1 + e^{-j\omega})$$

**Step 3: Simplify using Euler's Formula 

**Important Identity (memorize this!):**
$$e^{j\theta} = \cos\theta + j\sin\theta$$

**Trick:** Multiply by $\frac{e^{j\omega/2}}{e^{j\omega/2}} = 1$:

$$H(e^{j\omega}) = \frac{1}{2}(1 + e^{-j\omega}) \cdot \frac{e^{j\omega/2}}{e^{j\omega/2}}$$

$$= \frac{1}{2} \cdot \frac{e^{j\omega/2} + e^{-j\omega/2}}{e^{j\omega/2}}$$

Using identity: $e^{j\theta} + e^{-j\theta} = 2\cos\theta$

$$= \frac{1}{2} \cdot \frac{2\cos(\omega/2)}{e^{j\omega/2}} = \frac{\cos(\omega/2)}{e^{j\omega/2}}$$

$$= e^{-j\omega/2}\cos(\omega/2)$$

**Final Form:**
$$H(e^{j\omega}) = \underbrace{\cos(\omega/2)}_{\text{Magnitude}} \cdot \underbrace{e^{-j\omega/2}}_{\text{Phase}}$$

### Magnitude Response Analysis
$$|H(e^{j\omega})| = |\cos(\omega/2)|$$

**Key Values:**
![[FACL/DigitalSignals/Subfiles/LEC-7/Attachments/image.png]]
- At $\omega = 0$: $|H| = \cos(0) = 1$ ✓ (DC passes fully)
- At $\omega = \pi$: $|H| = \cos(\pi/2) = 0$ ✓ (Nyquist blocked)
- At $\omega = \pi/2$: $|H| = \cos(\pi/4) = \frac{1}{\sqrt{2}} \approx 0.707$ (-3 dB point)

**Shape:** Looks like a *low-pass filter* (but not ideal - gradual rolloff)

**Plot description (from your notes):**
- Starts at 1 when ω=0
- Smoothly decreases following cosine curve
- Reaches 0 at ω=π
- Symmetric around ω=0 (periodic with 2π)

### Phase Response Analysis
$$\angle H(e^{j\omega}) = -\frac{\omega}{2}$$

**Critical Observation:** 
- **Linear phase!** (straight line with slope -½)
- This means **constant group delay** = 0.5 samples
- **No phase distortion** - all frequencies delayed equally!

**General Rule (🌟 EXAM GOLD):**
> **All FIR filters with symmetric/antisymmetric coefficients have linear phase (or generalized linear phase).**

---

## Section 7: IIR Filters (Infinite Impulse Response)

### Core Concept
**IIR filters** have *recursive* structure - output depends on previous outputs AND inputs.

### General Difference Equation
$$y[n] = -a_1y[n-1] - a_2y[n-2] - ... + b_0x[n] + b_1x[n-1] + ...$$

Or equivalently:
$$\sum_{k=0}^{N} a_k y[n-k] = \sum_{m=0}^{M} b_m x[n-m]$$

where $a_0 = 1$ typically.

### Frequency Response
$$H(e^{j\omega}) = \frac{Y(e^{j\omega})}{X(e^{j\omega})} = \frac{b_0 + b_1e^{-j\omega} + ... + b_Me^{-jM\omega}}{1 + a_1e^{-j\omega} + ... + a_Ne^{-jN\omega}}$$

**Key Difference from FIR:** This is a **rational function** (ratio of polynomials), not just a polynomial!

### Example from Lecture
$$y[n] = 0.9y[n-1] + x[n]$$

**Finding H(e^jω):**
Take DTFT of both sides:
$$Y(e^{j\omega}) = 0.9e^{-j\omega}Y(e^{j\omega}) + X(e^{j\omega})$$

$$Y(e^{j\omega})(1 - 0.9e^{-j\omega}) = X(e^{j\omega})$$

$$H(e^{j\omega}) = \frac{1}{1 - 0.9e^{-j\omega}}$$

**Impulse Response:** $h[n] = (0.9)^n u[n]$ (infinite duration!)

### Stability Consideration
For IIR filter to be stable: **all poles must lie inside unit circle** (|pole| < 1)

In our example: pole at $z = 0.9$ → inside unit circle → ✅ **stable**

### Causality Condition
- **Right-sided sequence** (causal): ROC is exterior of circle through outermost pole
- **Left-sided sequence** (anti-causal): ROC is interior of circle through innermost pole
- Initial conditions determine which solution applies

### FIR vs IIR Comparison

| Feature | FIR | IIR |
|---------|-----|-----|
| Impulse Response | Finite | Infinite |
| Structure | Non-recursive (feedforward only) | Recursive (feedback) |
| Stability | Always stable (no poles except at origin) | Must check pole locations |
| Phase | Can achieve exact linear phase | Generally nonlinear phase |
| Order needed for same specs | Higher | Lower (more efficient) |
| Design Methods | Windowing, frequency sampling, optimal | Analog prototype transformation |

---

## Summary of Key Points

### Main Takeaways:
1. **Ideal filters are unrealizable** due to infinite/non-causal impulse response
2. **Truncation causes ripple artifacts** (Gibbs phenomenon) due to convolution with window's spectrum
3. **Window selection trades off** main lobe width vs. side lobe height
4. **FIR filters** = polynomial frequency response, always stable, can have linear phase
5. **IIR filters** = rational frequency response, recursive, need stability check, generally nonlinear phase
6. **Moving average** is simplest FIR low-pass filter (order determines smoothing)
7. **Phase response matters** - linear phase preserves waveform shape

---

## Important Formulas List

### Essential Equations for Exams:

1. **Ideal LPF Impulse Response:**
   $$h_{ideal}[n] = \frac{\sin(\omega_c n)}{\pi n}$$

2. **Truncated Filter:**
   $$h[n] = h_{ideal}[n] \cdot w[n]$$

3. **FIR Difference Equation:**
   $$y[n] = \sum_{k=0}^{M} b_k x[n-k]$$

4. **FIR Frequency Response:**
   $$H(e^{j\omega}) = \sum_{k=0}^{M} b_k e^{-jk\omega}$$

5. **IIR Frequency Response (Rational Function):**
   $$H(e^{j\omega}) = \frac{\sum_{m=0}^{M} b_m e^{-jm\omega}}{1 + \sum_{k=1}^{N} a_k e^{-jk\omega}}$$

6. **Decibel Conversion:**
   $$\text{dB} = 20\log_{10}(|H|)$$

7. **Euler's Identities:**
   $$e^{j\theta} = \cos\theta + j\sin\theta$$
   $$\cos\theta = \frac{e^{j\theta} + e^{-j\theta}}{2}$$
   $$\sin\theta = \frac{e^{j\theta} - e^{-j\theta}}{2j}$$

8. **Moving Average (Order 2):**
   $$H(e^{j\omega}) = e^{-j\omega/2}\cos(\omega/2)$$

---

## ⚠️ **Common Student Mistakes**

1. **Confusing time/frequency domain operations:**
   - ❌ Thinking truncation doesn't affect frequency response
   - ✅ Remember: multiplication in time ↔ convolution in frequency

2. **Forgetting the windowing step:**
   - Just cutting off the sinc function (rectangular window) gives worst ripples
   - Always consider which window to use based on application requirements

3. **Mixing up FIR and IIR properties:**
   - FIR ≠ always better; IIR is more efficient (lower order for same specs)
   - FIR has linear phase advantage; IIR has efficiency advantage

4. **Phase response neglect:**
   - Many students only look at magnitude response
   - Phase distortion can be critical in applications like audio, communications, image processing

5. **Stability oversight in IIR:**
   - Forgetting to check if poles are inside unit circle
   - Not understanding ROC (Region of Convergence) implications

6. **DTFT calculation errors:**
   - Wrong summation limits
   - Sign errors in exponents ($e^{-j\omega n}$ not $e^{+j\omega n}$)
   - Not simplifying using Euler's formulas

7. **Decibel scale confusion:**
   - Using log base e instead of base 10
   - Forgetting factor of 20 (for magnitude) vs 10 (for power)

8. **Moving average misidentification:**
   - Not recognizing it as a low-pass filter
   - Confusing order (number of taps) with cutoff frequency

---

## 📋 **Quiz Questions**

### **Question 1:**
Why can't we implement an ideal low-pass filter in real-time?

**Answer:** Because its impulse response $h[n] = \frac{\sin(\omega_c n)}{\pi n}$ is:
- **Infinite in length** (extends from -∞ to +∞)
- **Non-causal** (non-zero for n < 0, meaning it needs future samples)
Real-time systems require causal, finite-length implementations.

---

### **Question 2:**
What happens in the frequency domain when you multiply an ideal filter's impulse response by a rectangular window?

**Answer:** Convolution occurs in frequency domain:
$$H_{truncated}(e^{j\omega}) = H_{ideal}(e^{j\omega}) * W_{rect}(e^{j\omega})$$
Since $W_{rect}(e^{j\omega})$ is a sinc-like function, this causes:
- Ripples in both passband and stopband
- Gradual transition band instead of sharp cutoff
- This is called **spectral leakage** or **Gibbs phenomenon**

---

### **Question 3:**
For the moving average filter $y[n] = \frac{1}{2}(x[n] + x[n-1])$:
(a) What is the impulse response h[n]?
(b) What is the magnitude at ω = π/2?
(c) Is the phase linear or nonlinear?

**Answer:**
(a) $h[n] = \frac{1}{2}\delta[n] + \frac{1}{2}\delta[n-1]$
(b) $|H(e^{j\pi/2})| = |\cos(\pi/4)| = \frac{1}{\sqrt{2}} \approx 0.707$ (or -3 dB)
(c) **Linear phase**: $\angle H = -\omega/2$ (straight line with slope -0.5)

---

### **Question 4:**
What is the key structural difference between FIR and IIR filters that makes IIR potentially unstable?

**Answer:**
- **FIR**: Has only **zeros** (numerator polynomial). No feedback. Always stable.
- **IIR**: Has both **poles and zeros** (rational function). Uses **feedback** (recursive). If any pole lies on or outside the unit circle ($|p| \geq 1$), the filter is **unstable** (impulse response doesn't decay).

Example: $H(z) = \frac{1}{1 - 1.2z^{-1}}$ has pole at z = 1.2 → **unstable** (output grows infinitely)

---

### **Question 5:**
A speech signal is sampled at 16 kHz. You want to apply a Hamming window of 20 ms duration. How many samples is that? Why do we window speech signals before taking the FFT?

**Answer:**
**Number of samples:**
$$N = \text{duration} \times f_s = 0.02 \times 16000 = 320 \text{ samples}$$

**Reasons for windowing:**
1. **Speech is non-stationary** - statistics change over time, so we analyze short segments where it's approximately stationary (20-30 ms)
2. **Reduce spectral leakage** - abrupt truncation of the segment (equivalent to rectangular window) causes sidelobes in frequency. Hamming/Hanning window tapers the edges smoothly, reducing these artifacts
3. **Consistent frame analysis** - enables frame-by-frame feature extraction (like MFCCs)

---

## 🎯 **Exam Preparation Tips**

### High-Yield Topics:
1. ✅ Deriving h[n] from H(e^jω) for ideal LPF
2. ✅ Understanding windowing effects (time↔frequency duality)
3. ✅ Computing H(e^jω) for given FIR filter (like moving average)
4. ✅ Simplifying using Euler's formulas (the $e^{j\omega/2}$ trick)
5. ✅ Drawing magnitude and phase responses
6. ✅ Distinguishing FIR vs IIR properties
7. ✅ Stability criterion for IIR (poles inside unit circle)
8. ✅ Linear phase concept and its importance

### Quick Reference Card:
```
IDEAL LPF:  h[n] = sin(ωc·n)/(π·n)  →  infinite, non-causal ❌

WINDOWING:  h_trunc[n] = h_ideal[n] · w[n]
            Trade-off: main lobe width ↔ side lobe height

FIR:        y[n] = Σ bₖx[n-k]  
            H(e^jω) = polynomial → always stable, can have linear phase

IIR:        y[n] = Σ bₘx[n-m] - Σ aₖy[n-k]
            H(e^jω) = rational function → need stability check, nonlinear phase

MOVING AVG: H(e^jω) = e^(-jω/2) cos(ω/2)  →  LPF with linear phase
```

Good luck with your studies! 📚✨