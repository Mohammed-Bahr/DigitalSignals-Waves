---
Created: " 2026-05-06 14:39"
modified: 2026-05-06 14:39
tags:
  - FACL
  - DigitalSignals
Source:
---
> [!quote] To fly as fast as thought, you must begin by knowing that you have already arrived.
> — Richard Bach

**"اللهم إني أسألك فهم النبيين، وحفظ المرسلين، والملائكة المقربين، اللهم اجعل ألسنتنا عامرة بذكرك، وقلوبنا بخشيتك، إنك على كل شيء قدير"**

---

 I'll analyze your DSP notes and rewrite them as clean, comprehensive text without any drawings or charts.

---

# Digital Signal Processing (DSP) - Lectures 1-10

## Signal Classification

A signal is defined by its time and value characteristics:

| Time | Value | Signal Type |
|------|-------|-------------|
| Discrete | Discrete | Digital |
| Discrete | Continuous | Sampled (read by computer) |
| Continuous | Discrete | — |
| Continuous | Continuous | Analog (natural signal) |

**Key Rule:** Any signal with discrete values is called **digital**; any signal with continuous values is called **analog**.

---

## Analog-to-Digital Conversion (ADC)

ADC involves two main steps:

1. **Continuous to Discrete** — Sampling
2. **Analog to Digital** — Quantization

**Process:**
- Analog signal x(t) → Sampled signal xₛ(t) → Quantized (digital) signal x̂(n) = x(n)

**Quantization Error:** Quantized value − Sampled value

**Important:** Quantization error is irreversible.

### Sampling
- Implemented using a switch or amplifier with clock signal (0 or V)
- The value taken is the mean of the sample over the sampling period
- **Ideal Sample:** Uses delta function δ(t) — not practical because δ(t) = ∞
- In practice, δ(t) tends to ∞ but has area = 1 (sifting property)

### Quantization
- Done using operational amplifiers as **comparators**
- Comparator logic:
  - If V⁺ = V⁻, output = 0
  - If V⁺ > V⁻, output = 1
  - If V⁺ < V⁻, output = 0

---

## Ideal Sampling (Mathematical Model)

The sampled signal is modeled as:
$$x_s(t) = x(t) \cdot p(t) = x(t) \cdot \sum_{n=-\infty}^{\infty} \delta(t-nT) = \sum_{n=-\infty}^{\infty} x(nT)\delta(t-nT) = \sum_{n=-\infty}^{\infty} x(n)\delta(t-nT)$$

Where p(t) is the impulse train (comb function):
$$p(t) = \sum_{n=-\infty}^{\infty} \delta(t-nT)$$

---

## Classification of Signals

### A. Based on Cardinality (I/O)
- **SISO:** Single Input, Single Output
- **SIMO:** Single Input, Multiple Output
- **MIMO:** Multiple Input, Multiple Output
- **MISO:** Multiple Input, Single Output

### B. Based on Linearity

A system T is linear if:
$$T\{a_1x_1(t) + a_2x_2(t)\} = a_1T\{x_1(t)\} + a_2T\{x_2(t)\}$$

**Linearity Check:**
- Output y must depend on x (all terms must contain x)
- All x terms must be first-order (no x², constants, fractions, or second-order terms)

### C. Time Invariance Check

A system is time-invariant if:
$$T\{x(t-t_0)\} = y(t-t_0)$$

**Rule:** The variable n can only have coefficient ±1. Not allowed: -n, 2n, n², etc. (first degree only)

**LTI Systems:** We focus on Linear Time-Invariant systems, described by difference equations with homogeneous coefficients (all terms with same constant degree).

---

## Convolution

### Discrete Convolution
$$y(n) = x(n) * h(n) = \sum_{k=-\infty}^{\infty} x(k)h(n-k)$$

**Example 1:**
- x(n) = 3ⁿu(n), h(n) = δ(n) − δ(n−1)
- y(n) = 3ⁿu(n) * [δ(n) − δ(n−1)] = 3ⁿu(n) − 3ⁿ⁻¹u(n−1)

**Example 2:**
- x(n) = δ(n) + 3δ(n−1) + 2δ(n−2) + δ(n−3)
- h(n) = δ(n) − δ(n−2)
- Solution: y(n) = [1, 3, 1, −2, −2, −1]

**Solution Methods:**
1. **Graphical/Shift Method:** Shift h(−n) by one and compute dot products
2. **Matrix Method:** Construct Toeplitz matrix from h(n) and multiply by x(n) vector

**Example 3:**
- x(n) = 2ⁿu(n), h(n) = (0.3)ⁿu(n)
- Using geometric series: y(n) = (0.3)ⁿ · [1 − (20/3)ⁿ⁺¹] / [1 − (20/3)]

---

## Circular Convolution

$$x(n) \circledast_N h(n) = \sum_{k=0}^{N-1} x(k) \cdot h((n-k) \mod N)$$

**Key Points:**
- Pad signals with zeros to convert linear convolution to circular convolution
- For signals of length N, circular convolution produces N output points

**Example:**
- x(n) = [3, 2, 0, 4], h(n) = [1, −2, 0, 1]
- Circular convolution result: y(n) = [5, −6, −2, 3]

---

## Fourier Analysis

### Periodic Signals

A signal x(n) is periodic with period N if:
$$x(n+N) = x(n)$$

Where N is the fundamental period.

**Condition for Periodicity:** x(n) = sin(ωn) is periodic if ω/2π is rational.

$$N = \frac{2\pi k}{\omega}$$

If ω = 7π/9, then N = 18k/7. Starting from k = 7, N becomes integer (periodic with period 18).

---

## Aliasing of Discrete-Time Frequency

$$\sin(\omega n + 2\pi kn) = \sin(\omega n)$$

This identity shows that discrete-time frequencies are periodic with period 2π. The main alias region is [−π, π].

$$\sin(\omega n) = \frac{e^{j\omega n} - e^{-j\omega n}}{2j}$$

---

## Continuous-to-Discrete Transform (C/D)

For continuous signals, we apply sampling:
$$x_s(t) = x(t) \cdot p_T(t) = x(t) \cdot \sum_{n=-\infty}^{\infty} \delta(t-nT) = \sum_{n=-\infty}^{\infty} x(nT)\delta(t-nT) = \sum_{n=-\infty}^{\infty} x(n)\delta(t-nT)$$

---

## Continuous-Time Fourier Transform (CTFT) to DTFT

$$X_s(j\Omega) = \int_{-\infty}^{\infty} x_s(t)e^{-j\Omega t}dt = \sum_{n=-\infty}^{\infty} x(n)e^{-j\Omega nT}$$

Let ω = ΩT (frequency scaling):
$$X_s(e^{j\omega}) = \sum_{n=-\infty}^{\infty} x(n)e^{-j\omega n}$$

**Scaling Relationship:**
- Continuous frequency Ω ranges from −Ωₘ to +Ωₘ
- Discrete frequency ω ranges from −ΩₘT to +ΩₘT
- The spectrum repeats every ω = 2π (or Ωₛ = 2π/T)

---

## DTFT (Discrete-Time Fourier Transform)

$$X(e^{j\omega}) = \sum_{n=-\infty}^{\infty} x(n)e^{-j\omega n}$$

**Characteristics:**
- ω is still continuous in [−π, π]
- Computers cannot read continuous ω

---

## DFT (Discrete Fourier Transform)

To make ω discrete, we sample the frequency:
$$\omega_k = \frac{2\pi k}{N}, \quad k = 0, 1, 2, ..., N-1$$

**Analysis Equation:**
$$X(k) = \sum_{n=0}^{N-1} x(n)e^{-j\frac{2\pi k}{N}n}$$

**Synthesis Equation:**
$$x(n) = \frac{1}{N}\sum_{k=0}^{N-1} X(k)e^{j\frac{2\pi k}{N}n}$$

**Signal Processing Chain:**
Signal (Continuous) → CTFT → DTFT → DFT → Output (Digital)

**Computational Complexity:**
- DFT: O(n²)
- FFT (Fast Fourier Transform): O(n log n)

---

## DTFT of Basic Signals

### 1. Impulse δ(n)
$$\delta(n) = \begin{cases} 1 & n=0 \\ 0 & \text{otherwise} \end{cases}$$

$$X(e^{j\omega}) = \sum_{n=-\infty}^{\infty} \delta(n)e^{-j\omega n} = e^{-j\omega \cdot 0} = 1$$

### 2. Right-Sided Exponential: x(n) = aⁿu(n)
$$X(e^{j\omega}) = \sum_{n=0}^{\infty} a^n e^{-j\omega n} = \sum_{n=0}^{\infty} (ae^{-j\omega})^n = \frac{1}{1-ae^{-j\omega}}, \quad |a| < 1$$

### 3. Left-Sided Exponential: x(n) = −aⁿu(−n−1)
$$X(e^{j\omega}) = \frac{1}{1-ae^{-j\omega}}, \quad |a| > 1$$

---

## DTFT Properties

### 1. Convolution in Time Domain
$$x(n) * h(n) \xrightarrow{DTFT} X(e^{j\omega}) \cdot H(e^{j\omega})$$

H(e^{jω}) is the **frequency response** (impulse response in frequency domain).

**Filters:**
- **Low-pass filter:** Passes low frequencies, stops high frequencies
- **High-pass filter:** Stops low frequencies, passes high frequencies
- Used for noise cancellation (noise commonly in high frequencies)

**Key Insight:** Convolution in time domain ≡ Filtering ≡ Multiplication in frequency domain

### 2. Parseval's Relation (Energy Conservation)
$$\sum_{n=-\infty}^{\infty} |x(n)|^2 = \frac{1}{2\pi}\int_{-\pi}^{\pi} |X(e^{j\omega})|^2 d\omega$$

### 3. Derivative in Frequency Domain
$$\frac{d}{d\omega}X(e^{j\omega}) = \sum_{n=-\infty}^{\infty} x(n)(-jn)e^{-j\omega n}$$

$$\frac{-1}{j}\frac{d}{d\omega}X(e^{j\omega}) \xrightarrow{IDTFT} n \cdot x(n)$$

Derivative in frequency domain ≡ Multiplication by n in time domain

### 4. Symmetry Properties
- **Even signal:** x(n) = x*(−n) → X(e^{jω}) = X(e^{−jω}) (real)
- **Odd signal:** x(n) = −x*(−n)
- DTFT of pure imaginary signal is odd
- DTFT of even symmetric signal is real

**Example:** DTFT of cos(ω₀n)
$$\text{DTFT}\{\cos(\omega_0 n)\} = \frac{1}{2}\text{DTFT}\{e^{j\omega_0 n}\} + \frac{1}{2}\text{DTFT}\{e^{-j\omega_0 n}\}$$
$$= \frac{1}{2} \cdot 2\pi \sum_{k=-\infty}^{\infty} \delta(\omega - \omega_0 - 2\pi k) + \frac{1}{2} \cdot 2\pi \sum_{k=-\infty}^{\infty} \delta(\omega + \omega_0 - 2\pi k)$$

---

## Ideal Filters

An ideal filter passes some frequency components and stops others.

**Ideal Low-Pass Filter:**
$$H(e^{j\omega}) = \begin{cases} 1 & |\omega| < \omega_c \\ 0 & \text{otherwise} \end{cases}$$

Where $ω_c$ is the cutoff frequency.

**Impulse Response of Ideal Low-Pass:**
$$h(n) = \frac{1}{2\pi}\int_{-\omega_c}^{\omega_c} e^{j\omega n} d\omega = \frac{\sin(\omega_c n)}{\pi n} = \frac{\omega_c}{\pi} \text{sinc}\left(\frac{\omega_c n}{\pi}\right)$$

**Characteristics of Ideal Filters:**
- Anti-causal (non-causal)
- Infinite impulse response
- Not practically realizable

---

## Practical Approximations: ZOH and FOH

### Zero-Order Hold (ZOH)
- Holds the sample value constant over the entire sampling period [0, T]
- h_z(t) = 1 for 0 ≤ t ≤ T, 0 otherwise
- Frequency response: H_z(jΩ) = T · sinc(ΩT/2π) · e^{−jΩT/2}

### First-Order Hold (FOH)
- Interpolates between samples with straight lines
- Produces triangular waveform between samples

---

## DFT and FFT

### DFT Equations
**Analysis:** $X(k) = \sum_{n=0}^{N-1} x(n)e^{-j\frac{2\pi k}{N}n}$

**Synthesis:** $x(n) = \frac{1}{N}\sum_{k=0}^{N-1} X(k)e^{j\frac{2\pi k}{N}n}$

### Differences Between DFT and DTFT

| Property | DFT | DTFT |
|----------|-----|------|
| Frequency | Discrete (ω_k = 2πk/N) | Continuous (ω ∈ [−π, π]) |
| Spectrum range | 0 to 2π | −π to π |
| Time domain convolution | Circular | Linear |
| Frequency domain operation | Multiplication | Multiplication |

### FFT Algorithm
- Works when N is a power of 2 (2, 4, 8, 16, ...)
- Uses symmetry and periodicity of twiddle factors: $W_N = e^{-j\frac{2\pi}{N}}$
- Key symmetry: $e^{-j\frac{2\pi}{N}(\frac{N}{2}+k)} = -e^{-j\frac{2\pi}{N}k}$
- Algorithm divides DFT into even and odd parts recursively (divide-and-conquer)
- Complexity reduces from O(N²) to O(N log N)

**Bit-Reversal:** Input samples are reordered by reversing binary indices.

---

## Sampling Theory and Recovery

### Nyquist-Shannon Sampling Theorem
To avoid aliasing (spectral overlap):
$$\Omega_s = \frac{2\pi}{T} \geq 2B$$

Where B is the signal bandwidth (double bandwidth).

### Ideal Recovery Filter (Discrete to Analog)
$$H_r(j\Omega) = \begin{cases} T & |\Omega| < \frac{\pi}{T} \\ 0 & \text{otherwise} \end{cases}$$

**Impulse response:**
$$h_r(t) = \text{sinc}\left(\frac{t}{T}\right) = \frac{\sin(\pi t/T)}{\pi t/T}$$

### Recovery Process
1. Apply ideal low-pass filter to remove aliases
2. Multiply by T (gain compensation)

---

## Up-Sampling and Down-Sampling

### Up-Sampling (Expansion)
- Insert M−1 zeros between samples
- y(n) = x(n/M) when n is multiple of M, 0 otherwise
- **Effect:** Spectrum compressed by factor M, more aliases added
- **Application:** Used to slow down a signal
- **Post-processing:** Apply digital low-pass filter with cutoff π/M and gain = 1 to remove aliases

**Interpolation filters:**
- Zero-order interpolation (sample and hold)
- First-order interpolation (linear interpolation between midpoints)

### Down-Sampling (Decimation)
- Keep every M-th sample: y(n) = x(nM)
- **Application:** Used to make voice faster
- **Pre-processing:** Apply anti-aliasing filter before down-sampling to minimize bandwidth and prevent overlapping

**Anti-aliasing filter:** Low-pass with cutoff π/M and gain M

---

## Z-Transform

The Z-transform is the discrete-time equivalent of the Laplace transform.

**Uses:**
- Test system response speed
- Determine system stability

### Definition
**Analysis:** $X(z) = \sum_{n=-\infty}^{\infty} x(n)z^{-n}$

**Synthesis:** $x(n) = \frac{1}{2\pi j}\oint_c X(z)z^{n-1}dz$

Where c is a contour in the Region of Convergence (ROC).

**Important:** X(z) is only defined (finite) within its ROC.

### Z-Transforms of Basic Signals

| Signal | Z-Transform | ROC |
|--------|-------------|-----|
| δ(n) | 1 | All z (entire plane) |
| u(n) | 1/(1−z⁻¹) | \|z\| > 1 |
| −u(−n−1) | 1/(1−z⁻¹) | \|z\| < 1 |
| aⁿu(n) | 1/(1−az⁻¹) | \|z\| > \|a\| |
| −aⁿu(−n−1) | 1/(1−az⁻¹) | \|z\| < \|a\| |

**Note:** Two-sided signals (e.g., aⁿ without u(n)) do not have a Z-transform because no ROC exists.

---

## Z-Transform Properties

### 1. Linearity
$$\mathcal{Z}\{a_1x_1(n) + a_2x_2(n)\} = a_1X_1(z) + a_2X_2(z)$$
ROC: ROC₁ ∩ ROC₂

### 2. Time Shift
$$\mathcal{Z}\{x(n-k)\} = z^{-k}X(z)$$
ROC: Same as X(z)

### 3. Multiplication by n (Derivative in z)
$$\mathcal{Z}\{n \cdot x(n)\} = -z\frac{d}{dz}X(z)$$
ROC: Same as X(z) (except possible pole/zero cancellation)

### 4. Convolution in Time Domain
$$\mathcal{Z}\{x(n) * h(n)\} = X(z) \cdot H(z)$$
ROC: ROC₁ ∩ ROC₂

### 5. Multiplication by aⁿ
$$\mathcal{Z}\{a^n x(n)\} = X\left(\frac{z}{a}\right)$$
ROC: Scaled version of original ROC

### 6. Final Value Theorem
$$\lim_{n\to\infty} x(n) = \lim_{z\to 1} (1-z^{-1})X(z)$$

For steady-state analysis.

---

## Inverse Z-Transform

Methods:
1. **Contour integration** (using Cauchy's residue theorem)
2. **Partial fraction expansion** (most common)
3. **Power series expansion**
4. **Using properties**

**Cauchy's Theorem:** $\oint_c f(z)dz = 2\pi j \cdot \sum(\text{residues at poles inside c})$

---

## Partial Fraction Expansion Examples

**Example 1:**
$$X(z) = \frac{1}{1-0.5z^{-1}+0.06z^{-2}} = \frac{1}{(1-0.3z^{-1})(1-0.2z^{-1})}, \quad \text{ROC: } |z| > 0.3$$

$$X(z) = \frac{3}{1-0.3z^{-1}} - \frac{2}{1-0.2z^{-1}}$$

Since ROC is outside both poles → right-sided:
$$x(n) = 3(0.3)^n u(n) - 2(0.2)^n u(n)$$

**Example 2:** Same X(z), ROC: 0.2 < |z| < 0.3
- Pole at 0.3 → left-sided: −3(0.3)ⁿu(−n−1)
- Pole at 0.2 → right-sided: −2(0.2)ⁿu(n)

**Example 3:** Same X(z), ROC: |z| < 0.2
- Both poles → left-sided:
$$x(n) = -3(0.3)^n u(-n-1) + 2(0.2)^n u(-n-1)$$

**Example 4:**
$$X(z) = \frac{1}{1-z^{-2}}, \text{ find all ROCs and realizations}$$

Poles: z = ±j (magnitude = 1, on unit circle)

**ROC 1:** |z| > 1 (right-sided)
$$x(n) = 0.5(-j)^n u(n) + 0.5(j)^n u(n)$$

**ROC 2:** |z| < 1 (left-sided)
$$x(n) = -0.5(-j)^n u(-n-1) - 0.5(j)^n u(-n-1)$$

Simplified for ROC 1:
$$x(n) = \begin{cases} (-1)^{n/2} & n \text{ even} \\ 0 & n \text{ odd} \end{cases} = \begin{cases} -1 & n = 2, 6, 10, ... \\ 1 & n = 0, 4, 8, ... \\ 0 & n \text{ odd} \end{cases}$$

---

## Z-Transform for LTI Systems

H(z) = Z{h(n)} is the **transfer function**.

### Stability Criteria:

1. **Stable:** ROC contains the unit circle (|z| = 1)
2. **Marginally Stable (Oscillatory):** 
   - Pole lies on unit circle
   - Pole is not repeated (multiplicity = 1)
   - Unit circle is on the boundary of ROC
3. **Unstable:**
   - Repeated pole on unit circle, OR
   - ROC does not contain unit circle

**Key Relationship:** Stability is equivalent to DTFT existence.
- DTFT is obtained by setting z = e^{jω}
- If system is marginally stable, DTFT differs from Z-transform

**Example 1:**
$$H(z) = \frac{1}{1-0.5z^{-1}}, \quad \text{ROC: } |z| > 0.5$$
- Stable (contains unit circle)
- h(n) = (0.5)ⁿu(n)
- H(e^{jω}) exists

**Example 2:**
$$H(z) = \frac{1}{1-0.5z^{-1}}, \quad \text{ROC: } |z| < 0.5$$
- Unstable (does not contain unit circle)
- h(n) = −(0.5)ⁿu(−n−1)
- DTFT does not exist

**Example 3:**
$$H(z) = \frac{1}{1-z^{-1}}, \quad \text{ROC: } |z| > 1$$
- Marginally stable (pole on unit circle, multiplicity 1)
- In DTFT: $H(e^{j\omega}) = \frac{1}{1-e^{-j\omega}} + \pi\sum_{k=-\infty}^{\infty}\delta(\omega-2\pi k)$

**Example 4:**
$$H(z) = \frac{1}{(1-z^{-1})^2}$$
- Pole at z=1 with multiplicity 2
- Unstable (no DTFT)

---

## Finding Stable Realization

**Problem:** Find ROC of stable realization of:
$$H(z) = \frac{1}{1-4.5z^{-1}+2z^{-2}} = \frac{1}{(1-0.5z^{-1})(1-4z^{-1})}$$

Poles: z = 0.5, z = 4

**Stable ROC:** 0.5 < |z| < 4 (annular region containing unit circle)

Partial fractions:
$$H(z) = \frac{-1/7}{1-0.5z^{-1}} + \frac{8/7}{1-4z^{-1}}$$

- Pole at 0.5 → right-sided: −(1/7)(0.5)ⁿu(n)
- Pole at 4 → left-sided: (8/7)(4)ⁿu(−n−1)

$$h(n) = -\frac{1}{7}(0.5)^n u(n) + \frac{8}{7}(4)^n u(-n-1)$$

---

## FIR Filters Example

**Moving Average Filter:**
$$y(n) = \frac{1}{2}[x(n) + x(n-1)]$$

Find h(n):
- h(n) is system response when input is impulse δ(n)
- h(n) = (1/2)[δ(n) + δ(n−1)]

Frequency response:
$$H(e^{j\omega}) = \text{DTFT}\{h(n)\} = \frac{1}{2}(1 + e^{-j\omega})$$

This is a simple digital filter of order 2.

---

## System Processing Chain Summary

**Analog → Digital:**
Analog → CTFT → DTFT → DFT → Digital Signal

**With practical improvements:**
Analog → CTFT → DTFT → DFT (via FFT) → Digital Signal + Filters (FIR, IIR)

**Digital → Analog:**
Digital → IDFT → IDTFT → Recovery Filter (ideal, ZOH, or FOH) → Analog

---

## Key Relationships Summary

| Operation | Time Domain | Frequency Domain |
|-----------|-------------|------------------|
| Convolution | x(n) * h(n) | X(·) · H(·) |
| Multiplication | x(n) · h(n) | X(·) ⊛ H(·) |
| Time shift | x(n−k) | e^{−jωk}X(e^{jω}) or z^{−k}X(z) |
| Frequency shift | e^{jω₀n}x(n) | X(e^{j(ω−ω₀)}) |
| Time reversal | x(−n) | X(e^{−jω}) or X(z^{−1}) |
| Differentiation (freq) | n·x(n) | j dX/dω or −z dX/dz |

---

## Important Notes

1. **Causal LTI System:** ROC is the outermost region (extends to ∞)
2. **Two-sided signals** don't have Z-transforms (no valid ROC)
3. **Complex conjugate poles** on same circle → two solutions (right/left-sided combinations)
4. **Non-conjugate poles** on different circles → three solutions (both right, both left, or mixed)
5. **ZOH in frequency domain:** Sinc-like response with linear phase
6. **Window functions** are used in filter design to truncate infinite impulse responses

---

*End of DSP Lectures 1-10 Summary*