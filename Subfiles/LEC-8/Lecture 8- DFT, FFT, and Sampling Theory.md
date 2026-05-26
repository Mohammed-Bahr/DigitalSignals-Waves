---
Created: " 2026-04-29 12:10"
modified: 2026-04-29 12:10
tags:
  - FACL
  - "#DigitalSignals"
Source: https://onedrive.live.com/personal/530e6bf1aa159903/_layouts/15/Doc.aspx?sourcedoc={346a91bf-04b6-4e69-afab-083a67e3126c}&action=view&wd=target%28DSP.one%7Cf049227c-94c0-424e-b849-8dcbc1f52d50%2FUntitled%20Page%7C425dd185-a9e5-3440-8bb2-c11a8f105e79%2F%29&wdorigin=NavigationUrl
---
> [!quote] Good timber does not grow with ease; the stronger the wind, the stronger the trees.
> — J. Willard Marriott

**"اللهم إني أسألك فهم النبيين، وحفظ المرسلين، والملائكة المقربين، اللهم اجعل ألسنتنا عامرة بذكرك، وقلوبنا بخشيتك، إنك على كل شيء قدير"**

---


## Lecture Topic Identified

**Digital Signal Processing (DSP): The Discrete Fourier Transform (DFT), Fast Fourier Transform (FFT), and Sampling Theory**

This lecture covers three main areas:
1. **DFT (Discrete Fourier Transform)** - definition, properties, and differences from DTFT
2. **FFT (Fast Fourier Transform)** - the divide-and-conquer algorithm, butterfly diagrams, and computational complexity
3. **Sampling Theory** - impulse train sampling, aliasing, Nyquist rate, and reconstruction filters


---

## Section 1: Review of Filter Types (Brief Context)

### Main Concept
The professor begins by reviewing two fundamental filter types in DSP before diving into DFT:

- **FIR (Finite Impulse Response) Filters**: Direct relationship between output y[n] and input x[n]. The output is a weighted sum of current and past inputs: y[n] = b₀x[n] + b₁x[n-1] + ... + bₘx[n-M]. Called "polynomial" because it's a finite sum.
- **IIR (Infinite Impulse Response) Filters**: Recursive filters with both numerator and denominator (feedback). Output depends on past outputs too.

### Why It Matters
This sets the stage for understanding why we need frequency-domain tools like DFT to design and analyze filters efficiently.

---

## Section 2: The Discrete Fourier Transform (DFT)

### Main Concept
The DFT is a practical, computable version of the DTFT (Discrete-Time Fourier Transform) that works with **finite-length** signals.

### The Core Equations

**DFT (Analysis Equation):**
$$X[k] = \sum_{n=0}^{N-1} x[n] \cdot e^{-j\frac{2\pi}{N}kn}$$

**Inverse DFT (Synthesis Equation):**
$$x[n] = \frac{1}{N}\sum_{k=0}^{N-1} X[k] \cdot e^{j\frac{2\pi}{N}kn}$$

### Intuition / Simple Understanding
- The DFT takes N samples of a signal and produces N frequency coefficients
- Think of it as "asking" the signal: "How much of each pure frequency (sine/cosine) is present?"
- The frequency index k corresponds to actual frequency: $\omega_k = \frac{2\pi k}{N}$

### Symbol Definitions
| Symbol | Meaning |
|--------|---------|
| $N$ | Number of samples (signal length) |
| $n$ | Time index (sample number), $n = 0, 1, ..., N-1$ |
| $k$ | Frequency index (bin number), $k = 0, 1, ..., N-1$ |
| $x[n]$ | Input signal sample at time n |
| $X[k]$ | DFT coefficient at frequency bin k |
| $\omega_k = \frac{2\pi k}{N}$ | Digital frequency corresponding to bin k |

### Why It Matters
The DFT is what we actually compute in software (MATLAB's `fft()`, Python's `np.fft.fft()`). The DTFT is theoretical (infinite samples, continuous frequency); the DFT is practical (finite samples, discrete frequency).

---

## Section 3: DFT vs. DTFT — Key Differences

### Main Concept
The professor emphasizes three critical differences between DFT and DTFT:

| Feature | DTFT | DFT |
|---------|------|-----|
| **Signal length** | Infinite or finite | Finite (N samples) |
| **Frequency variable** | Continuous ω from -π to +π | Discrete k from 0 to N-1 |
| **Nature** | Theoretical transform | Sampled version of DTFT |
| **Periodicity** | Periodic with 2π | Periodic with N (in k-domain) |
| **Computation** | Integral (theoretical) | Sum (practical) |

### Critical Difference #1: Sampling in Frequency
> "The DFT is a sampled version of the DTFT"

$$X[k] = X(e^{j\omega})\Big|_{\omega = \frac{2\pi k}{N}}$$

We evaluate the DTFT at N equally-spaced frequencies around the unit circle.

### Critical Difference #2: Frequency Range Convention
- **DTFT standard range**: $-\pi \leq \omega < \pi$ (symmetric around zero)
- **DFT standard range**: $0 \leq k < N$ or $0 \leq \omega < 2\pi$

> **Exam Tip**: When plotting DFT spectra, professors often want you to shift the zero-frequency component to the center (using `fftshift`), showing negative frequencies on the left.

### Critical Difference #3: Circular vs. Linear Convolution
| Linear Convolution | Circular Convolution |
|-------------------|----------------------|
| Flip, shift, multiply, sum | "Wrap-around" — signals are treated as periodic |
| Output length: N + M - 1 | Output length: max(N, M) |
| No overlap assumptions | Assumes periodic extension |

### 🔑 KEY EXAM CONCEPT: Zero-Padding
> "If you want linear convolution using DFT/FFT, you MUST zero-pad both signals!"

**Why zero-padding works:**
- If signal A has length N and signal B has length M
- Pad both to length **at least N + M - 1**
- Now circular convolution = linear convolution (for the fundamental period)

**Two benefits of zero-padding:**
1. **Avoids circular convolution artifacts** (wrap-around interference)
2. **Increases frequency resolution** — more DFT points = finer frequency grid (closer to true DTFT)

**Example from lecture:**
- Filter length: 25 or 51 taps
- Computed DFT with 1024 points
- This means: 1024 - 51 = 973 zeros were added
- Result: Fine frequency grid, and linear convolution behavior

---

## Section 4: DFT Computational Complexity & The FFT

### Main Concept
Direct DFT computation is too slow for large N. The FFT algorithm reduces complexity from $O(N^2)$ to $O(N \log N)$.

### Direct DFT Complexity
For each $X[k]$: N multiplications + N-1 additions = **O(N)**
For all N values of k: **O(N²)** total operations

**Example:** N = 1,000,000 → ~1 trillion operations!

### FFT Complexity: O(N log N)
**Example:** N = 1,000,000 → ~20 million operations (50,000× faster!)

### The FFT Algorithm: Divide and Conquer

#### Step 1: Separate Even and Odd Samples
Given N samples (where N is a power of 2):
- **Even-indexed samples**: $x[0], x[2], x[4], ..., x[N-2]$
- **Odd-indexed samples**: $x[1], x[3], x[5], ..., x[N-1]$

Let $M = N/2$

#### Step 2: The Decimation Equation
$$X[k] = \underbrace{\sum_{m=0}^{M-1} x[2m] \cdot e^{-j\frac{2\pi}{M}km}}_{\text{DFT of even samples}} + \underbrace{e^{-j\frac{2\pi}{N}k}}_{\text{Twiddle Factor } W_N^k} \cdot \underbrace{\sum_{m=0}^{M-1} x[2m+1] \cdot e^{-j\frac{2\pi}{M}km}}_{\text{DFT of odd samples}}$$

Or more compactly:
$$\boxed{X[k] = X_{even}[k] + W_N^k \cdot X_{odd}[k]}$$

Where the **Twiddle Factor** is:
$$W_N^k = e^{-j\frac{2\pi k}{N}}$$

#### Step 3: Recursive Decomposition
- Each N-point DFT becomes two N/2-point DFTs
- Each N/2-point DFT becomes two N/4-point DFTs
- Continue until reaching 2-point DFTs (trivial: just addition/subtraction)

**Recursion tree depth:** $\log_2 N$ levels

**Operations per level:** N complex multiplications/additions

**Total:** $N \log_2 N$

### The Twiddle Factor $W_N^k$
This is a complex number on the unit circle:
- Magnitude: always 1
- Angle: $-\frac{2\pi k}{N}$ radians (clockwise rotation)
- **Periodicity**: $W_N^{k+N} = W_N^k$ (repeats every N)
- **Symmetry**: $W_N^{k+N/2} = -W_N^k$ (half-period is negative)

**Visual intuition:** The twiddle factors are N equally-spaced points on the unit circle in the complex plane.

---

## Section 5: The Butterfly Diagram

### Main Concept
The butterfly diagram is a visual representation of the FFT computation flow, showing how data moves and combines.

### Bit-Reversal Permutation
Before computing, the input samples must be reordered by **bit-reversed indices**.

**Example for N = 8 (3 bits):**

| Index | Binary | Bit-Reversed | New Position |
|-------|--------|--------------|--------------|
| 0 | 000 | 000 | 0 |
| 1 | 001 | 100 | 4 |
| 2 | 010 | 010 | 2 |
| 3 | 011 | 110 | 6 |
| 4 | 100 | 001 | 1 |
| 5 | 101 | 101 | 5 |
| 6 | 110 | 011 | 3 |
| 7 | 111 | 111 | 7 |

**Resulting order:** x[0], x[4], x[2], x[6], x[1], x[5], x[3], x[7]

> **Why bit-reversal?** It naturally groups even and odd indices at each recursive split.

### Butterfly Structure (2-point)
```
        X_even[k] ──┬──(+ )── X[k]
                    │
        X_odd[k] ──[×W]──┘
                    │
        X_even[k] ──┬──(- )── X[k+N/2]
                    │
        X_odd[k] ──[×(-W)]─┘
```

**One butterfly = 1 complex multiplication + 2 complex additions**

### Worked Example: N = 4 Signal
Given: x = [3, 1, 2, 5] (after bit-reversal: [3, 2, 1, 5])

**Stage 1 (2-point butterflies):**
- Butterfly 1: x[0]=3, x[2]=1 → (3+1)=4, (3-1)=2
- Butterfly 2: x[1]=2, x[3]=5 → (2+5)=7, (2-5)=-3

**Stage 2 (4-point butterfly, twiddle factors: $W_4^0=1$, $W_4^1=-j$):**
- X[0] = 4 + (1)(7) = 11
- X[1] = 2 + (-j)(-3) = 2 + 3j
- X[2] = 4 - (1)(7) = -3
- X[3] = 2 - (-j)(-3) = 2 - 3j

**Result:** X[k] = [11, 2+3j, -3, 2-3j]

**Verification:** X[1] and X[3] are complex conjugates (symmetry for real input) ✓

---

## Section 6: Inverse FFT (IFFT)

### Main Concept
The inverse DFT uses the same algorithm, just with:
1. **Positive exponent** instead of negative: $e^{+j\frac{2\pi}{N}kn}$
2. **Division by N** at the end

**Practical approach:** Use the same FFT hardware/software with:
- Conjugate the twiddle factors (or input), run FFT, conjugate result, divide by N

---

## Section 7: Sampling Theory

### Main Concept
How do we convert continuous-time (analog) signals to discrete-time (digital) signals? Through **sampling**.

### The Sampling Process
**Mathematical model:**
$$x_s(t) = x_c(t) \cdot p_T(t)$$

Where:
- $x_c(t)$ = continuous-time signal
- $p_T(t)$ = impulse train with period T: $\sum_{n=-\infty}^{\infty} \delta(t - nT)$
- $x_s(t)$ = sampled signal

### Intuition
Think of a switch that closes every T seconds, letting through an instantaneous sample of the signal.

### Frequency Domain Analysis

**Fourier Series of Impulse Train:**
$$p_T(t) = \frac{1}{T}\sum_{k=-\infty}^{\infty} e^{j\frac{2\pi k}{T}t} = \frac{1}{T}\sum_{k=-\infty}^{\infty} e^{j k \omega_s t}$$

Where $\omega_s = \frac{2\pi}{T}$ is the **sampling frequency** (radians/second).

**Sampled Signal Spectrum:**
$$X_s(j\omega) = \frac{1}{T}\sum_{k=-\infty}^{\infty} X_c(j(\omega - k\omega_s))$$

### 🔑 CRITICAL RESULT: Spectrum Replication
> **Sampling in time = Replication in frequency**

The original spectrum $X_c(j\omega)$ is:
1. **Scaled by** $1/T$
2. **Repeated** every $\omega_s$ (sampling frequency)
3. Each copy is centered at $k\omega_s$ for all integers k

### Visual Description (Implied Diagram)
```
Original Spectrum Xc(jω):
    _______
___/       \___
   -B     +B    (bandlimited to B)

Sampled Spectrum Xs(jω):
    ___     ___     ___
___/   \___/   \___/   \___
   -ωs  -B  +B  +ωs   2ωs
      (replicas every ωs)
```

---

## Section 8: Aliasing and the Nyquist Rate

### Main Concept
If spectral replicas overlap, high frequencies "masquerade" as low frequencies — this is **aliasing**.

### When Does Aliasing Occur?
**Aliasing happens when:** $\omega_s < 2B$

Where B = highest frequency in the original signal (bandwidth)

### The Nyquist-Shannon Sampling Theorem

> **Nyquist Rate:** $\omega_s \geq 2B$ (or $f_s \geq 2f_{max}$)

**In terms of sampling period:** $T \leq \frac{1}{2f_{max}} = \frac{\pi}{B}$

### Why It Matters
- If you sample too slowly, you **lose information permanently**
- No post-processing can recover the original signal
- This is why CDs use 44.1 kHz (human hearing ~20 kHz → need >40 kHz)

### 🔑 EXAM FORMULA
$$\boxed{f_s \geq 2f_{max} \text{ (Nyquist Criterion)}}$$

---

## Section 9: Signal Reconstruction

### Main Concept
How do we recover the original continuous signal from samples?

### Ideal Reconstruction Filter
**Frequency response:**
$$H_r(j\omega) = \begin{cases} T & |\omega| \leq \frac{\omega_s}{2} = \frac{\pi}{T} \\ 0 & |\omega| > \frac{\pi}{T} \end{cases}$$

This is a **low-pass filter** with:
- Gain = T (to cancel the 1/T scaling from sampling)
- Cutoff = $\omega_s/2$ (half the sampling frequency, called the **Nyquist frequency**)

### Impulse Response of Ideal Reconstruction Filter
Taking the inverse Fourier transform:
$$h_r(t) = \frac{\sin(\pi t/T)}{\pi t/T} = \text{sinc}\left(\frac{t}{T}\right)$$

Where $\text{sinc}(x) = \frac{\sin(\pi x)}{\pi x}$

### Why This is "Ideal" (and Impractical)
1. **Non-causal**: $h_r(t)$ extends from $t = -\infty$ to $+\infty$ (needs future samples!)
2. **Infinite extent**: Requires infinite computation
3. **Perfect reconstruction**: If implemented perfectly, recovers original exactly

### Practical Reconstruction: Zero-Order Hold (ZOH)

**Time-domain behavior:**
- Hold each sample value constant until the next sample arrives
- Creates a "staircase" waveform

**Impulse response:**
$$h_{ZOH}(t) = \begin{cases} 1 & 0 \leq t < T \\ 0 & \text{otherwise} \end{cases}$$

**Frequency response:**
$$H_{ZOH}(j\omega) = T \cdot \frac{\sin(\omega T/2)}{\omega T/2} \cdot e^{-j\omega T/2} = T \cdot \text{sinc}\left(\frac{\omega T}{2\pi}\right) \cdot e^{-j\omega T/2}$$

**Characteristics:**
- Magnitude: $T \cdot |\text{sinc}(f/f_s)|$
- First null at $\omega = 2\pi/T = \omega_s$ (the sampling frequency)
- Approximate -3dB cutoff around $\omega = \pi/T = \omega_s/2$
- **Not ideal**: Passes some high-frequency "images" (causes staircase artifacts)

### First-Order Hold (Linear Interpolation)

**Time-domain behavior:**
- Connect samples with straight lines
- Better approximation than ZOH
- Requires waiting for next sample (introduces delay)

**Impulse response:** Triangular shape (convolution of two rectangular pulses)

**Frequency response:** $\text{sinc}^2$ shape — falls off faster, better attenuation of images

### Practical Implementation
- **ZOH**: Simple RC circuit (capacitor holds charge, resistor discharges)
- **First-order**: More complex analog circuitry
- **Higher-order**: Digital interpolation filters (used in modern DACs)

---

## Section 10: Up-Sampling and Down-Sampling (Preview)

### Main Concept
The professor mentions changing sampling rates:
- **Down-sampling (decimation)**: Reduce rate by keeping every M-th sample
- **Up-sampling (interpolation)**: Increase rate by inserting zeros, then filtering

**Applications:**
- Audio streaming (different quality levels = different rates)
- Communication systems (adaptive bandwidth)
- Image processing (scaling)

---

# Summary

| Topic | Key Takeaway |
|-------|-------------|
| **DFT** | Practical, finite version of DTFT; N frequency samples from N time samples |
| **FFT** | Divide-and-conquer algorithm; O(N log N) instead of O(N²) |
| **Zero-padding** | Needed for linear convolution with DFT; improves frequency resolution |
| **Sampling** | Multiplication by impulse train in time = spectrum replication in frequency |
| **Nyquist** | Sample at least 2× the highest frequency to avoid aliasing |
| **Reconstruction** | Ideal = sinc interpolation; Practical = ZOH or linear interpolation |

---

# Key Formulas / Rules / Definitions

### DFT Pair
$$X[k] = \sum_{n=0}^{N-1} x[n] \cdot W_N^{kn}, \quad W_N = e^{-j\frac{2\pi}{N}}$$
$$x[n] = \frac{1}{N}\sum_{k=0}^{N-1} X[k] \cdot W_N^{-kn}$$

### FFT Decimation
$$X[k] = X_{even}[k] + W_N^k \cdot X_{odd}[k]$$

### Sampling
$$x_s(t) = x_c(t) \cdot \sum_{n=-\infty}^{\infty} \delta(t-nT)$$
$$X_s(j\omega) = \frac{1}{T}\sum_{k=-\infty}^{\infty} X_c(j(\omega - k\omega_s))$$

### Nyquist Criterion
$$\omega_s \geq 2B \quad \text{or} \quad f_s \geq 2f_{max}$$

### Ideal Reconstruction
$$h_r(t) = \text{sinc}\left(\frac{t}{T}\right), \quad H_r(j\omega) = \begin{cases} T & |\omega| \leq \pi/T \\ 0 & \text{otherwise} \end{cases}$$

### ZOH Frequency Response
$$H_{ZOH}(j\omega) = T \cdot \text{sinc}\left(\frac{\omega T}{2\pi}\right) \cdot e^{-j\omega T/2}$$

---

# Common Mistakes Students Make

1. **Confusing DFT with DTFT**: DFT is for finite signals, discrete frequencies; DTFT is theoretical, continuous frequency
2. **Forgetting the 1/N in IDFT**: The inverse has a division by N; the forward does not
3. **Circular vs. Linear Convolution**: Thinking they're always the same — they're only equal with proper zero-padding
4. **Nyquist Confusion**: Using $f_s = 2f_{max}$ (borderline) instead of $f_s > 2f_{max}$ (safe). At exactly Nyquist, you need ideal filters.
5. **Sampling Frequency vs. Nyquist Frequency**: $\omega_s = 2\pi/T$ is sampling freq; $\omega_s/2 = \pi/T$ is Nyquist freq (the cutoff)
6. **ZOH Gain**: Forgetting the factor of T in reconstruction — the spectrum is scaled by 1/T during sampling, so we need gain T to recover
7. **Bit-reversal**: Applying FFT without reordering input — always bit-reverse first!

---

# 5 Review Questions with Answers

### Q1: Why is the FFT faster than direct DFT computation?
**A:** The FFT uses a divide-and-conquer approach, recursively splitting an N-point DFT into two N/2-point DFTs. This creates a recursion tree of depth log₂N, with N operations per level, giving O(N log N) complexity versus O(N²) for direct computation. For N=1024, that's ~10,000 operations vs. ~1,000,000.

---

### Q2: A signal has maximum frequency 5 kHz. What is the minimum sampling frequency? What happens if you sample at 8 kHz?
**A:** Minimum sampling frequency = 2 × 5 kHz = **10 kHz** (Nyquist rate). If you sample at 8 kHz, which is less than 10 kHz, **aliasing occurs**. Frequencies above 4 kHz (half the sampling rate) will "fold back" and appear as false low frequencies in the sampled signal. The 5 kHz component would alias to 3 kHz (8-5=3).

---

### Q3: You convolve two signals of length 100 and 200 using FFT. What minimum FFT size should you use, and why?
**A:** Minimum FFT size = **100 + 200 - 1 = 299**. Since FFT works best with powers of 2, you'd typically use **512**. Without zero-padding to at least 299, circular convolution would occur, causing time-domain aliasing (wrap-around) where the tail of the convolution result corrupts the beginning.

---

### Q4: What is the twiddle factor $W_N^k$, and what two properties make the FFT efficient?
**A:** $W_N^k = e^{-j\frac{2\pi k}{N}}$ is the complex exponential weighting factor. The two key properties are:
1. **Periodicity**: $W_N^{k+N} = W_N^k$ — values repeat every N
2. **Symmetry**: $W_N^{k+N/2} = -W_N^k$ — half-period points are negatives

These allow the FFT to reuse computations and reduce the total number of operations.

---

### Q5: Compare the ideal reconstruction filter with the zero-order hold. Why can't we build the ideal filter?
**A:** The ideal filter has a perfect rectangular frequency response and a sinc impulse response. The ZOH has a sinc-shaped magnitude response (with sidelobes) and a rectangular impulse response. We can't build the ideal filter because:
1. **Non-causal**: The sinc extends to $t = -\infty$, requiring future knowledge
2. **Infinite length**: Requires infinite computation and delay
3. **Abrupt transitions**: The perfect rectangular frequency response requires unrealizable infinite-order analog components

---

# Quick Revision Sheet

```
┌─────────────────────────────────────────────────────────┐
│  DFT: X[k] = Σ x[n]·e^(-j2πkn/N)   n=0 to N-1          │
│  IDFT: x[n] = (1/N) Σ X[k]·e^(j2πkn/N)  k=0 to N-1    │
├─────────────────────────────────────────────────────────┤
│  FFT Complexity: O(N log₂N)  vs  DFT: O(N²)            │
│  Requirement: N must be power of 2 (for radix-2 FFT)   │
├─────────────────────────────────────────────────────────┤
│  ZERO-PAD for linear convolution!                       │
│  Pad to: N + M - 1 (where N, M = signal lengths)       │
├─────────────────────────────────────────────────────────┤
│  SAMPLING: x_s(t) = x_c(t)·Σδ(t-nT)                    │
│  SPECTRUM: Repeats every ω_s = 2π/T, scaled by 1/T    │
├─────────────────────────────────────────────────────────┤
│  NYQUIST: f_s ≥ 2·f_max                                │
│  ALIASING: Overlapping spectral replicas               │
├─────────────────────────────────────────────────────────┤
│  IDEAL RECONSTRUCTION: h(t) = sinc(t/T)                │
│  ZOH: Staircase, H(jω) = T·sinc(ωT/2π)·e^(-jωT/2)     │
│  FIRST-ORDER: Linear between samples, sinc² response   │
└─────────────────────────────────────────────────────────┘
```

---

**Study Tip from the Professor:** The professor emphasizes that understanding the FFT butterfly diagram and being able to trace through a small example (like N=4 or N=8) is excellent preparation for exams. Practice drawing the flow and computing twiddle factors manually!