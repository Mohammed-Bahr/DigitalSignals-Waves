---
Created: " 2026-04-21 08:23"
modified: 2026-04-28 04:56
tags:
  - FACL
  - DigitalSignals
Source:
---
> [!quote] Real magic in relationships means an absence of judgement of others.
> — Wayne Dyer

**"اللهم إني أسألك فهم النبيين، وحفظ المرسلين، والملائكة المقربين، اللهم اجعل ألسنتنا عامرة بذكرك، وقلوبنا بخشيتك، إنك على كل شيء قدير"**

---
> **Conclusion:** DTFT is not just a mathematical formula — it's a tool for understanding signals and systems. Every property has direct application in signal processing and communications. A good understanding of these fundamentals makes it easier to understand advanced topics like Sampling, Filtering, and Modulation.
	
## Overview

This lecture covers one of the most important mathematical tools in digital signal processing: the Discrete-Time Fourier Transform (DTFT). This transform allows us to analyze discrete-time digital signals from the Time Domain to the Frequency Domain, revealing their frequency content and how they interact with different systems. We will study the transform definition, basic signal transforms, important mathematical properties, and the most significant application: the Convolution Theorem, which forms the foundation for analyzing communication systems and filtering.

---

## Detailed Explanation

### 1. Introduction: Difference Between DTFT and DFT

#### Discrete-Time Fourier Transform (DTFT)

The mathematical formula:

$$X(e^{j\omega}) = \sum_{n=-\infty}^{\infty} x[n]e^{-j\omega n}$$

Components:

- $x[n]$: Discrete-time signal (a sequence of numbers)
- $e^{-j\omega n}$: Complex exponential (rotating phasor) used to "probe" each frequency
- $\omega$: Continuous frequency (radians/sample), not discrete
- $X(e^{j\omega})$: Frequency spectrum (continuous complex-valued function)

Why continuous frequency? Because $e^{-j\omega n}$ is defined for any real value of $\omega$. We are not sampling the frequency axis; we are computing the complete theoretical spectrum. This gives us a full frequency picture, but it cannot be directly computed on a computer because it requires infinite values of $\omega$.

#### Discrete Fourier Transform (DFT)

To make computation possible on a computer, we do two things:

1. **Sample** the frequency: $\omega_k = \frac{2\pi k}{N}$
2. **Limit** the sum to N samples

Formula:

$$X[k] = X(e^{j\frac{2\pi k}{N}}) = \sum_{n=0}^{N-1} x[n]e^{-j\frac{2\pi}{N}kn}$$

Key difference:

| | DTFT | DFT |
|---|---|
| Frequency | Continuous ($\omega$ any real value) | Discrete ($N$ points: $k = 0, 1, \ldots, N-1$) |
| Signal | Can be infinite | Must be finite (length $N$) |
| Use | Theoretical - for analysis | Practical - for computer computation |

Practical example: If we have $x[n] = [1, 0, 0, 0]$ of length 4, the DFT of this signal is $X[k] = 1$ for all $k$, because the signal is a delta padded with zeros.

> **Important note about DFT:** When computing DFT, the signal must be finite. If the signal is infinite, we perform "Truncation" by multiplying it with a rectangular window, which may cause slight frequency distortion.

---

### 2. DTFT of Basic Signals

#### (a) Delta Function (Impulse) $\delta[n]$

$$\delta[n] = \begin{cases} 1 & n=0 \\ 0 & \text{else} \end{cases}$$

$$X(e^{j\omega}) = \sum_{n=-\infty}^{\infty} \delta[n]e^{-j\omega n} = e^{-j\omega(0)} = 1$$

$$\boxed{\delta[n] \xleftrightarrow{\text{DTFT}} 1}$$

**Explanation:**

- In time: Very short spike at $n=0$
- In frequency: Flat spectrum (all frequencies present equally)

**Why?** The sum collapses to a single term ($n=0$ only), and $e^{-j\omega \cdot 0} = 1$.

**Physical meaning:** The delta is the "perfect test signal" — it contains all frequencies equally, like white light containing all colors. That's why, when we input $\delta[n]$ into a system, the output reveals the complete frequency response of the system.

---

#### (b) Right-Sided Exponential

$$x[n] = a^n u[n]$$

where $a$ is a complex constant.

$$X(e^{j\omega}) = \sum_{n=-\infty}^{\infty} a^n u[n] e^{-j\omega n} = \sum_{n=0}^{\infty} a^n e^{-j\omega n}$$

$$= 1 + a e^{-j\omega} + a^2 e^{-j2\omega} + \dots$$

Using the geometric series:

$$1 + r + r^2 + \dots = \frac{1}{1-r} \quad \text{when} |r| < 1$$

**Convergence condition:** $|a e^{-j\omega}| < 1$ means $|a| \cdot |e^{-j\omega}| < 1$, and since $|e^{-j\omega}| = 1$, the condition is $|a| < 1$.

**Result:**

$$X(e^{j\omega}) = \frac{1}{1 - ae^{-j\omega}}, \quad |a| < 1$$

$$\boxed{a^n u[n] \xleftrightarrow{\text{DTFT}} \frac{1}{1 - ae^{-j\omega}}, \quad |a| < 1}$$

**Explanation:**

- $u[n]$ makes the sum start from $n=0$ to $\infty$
- The result is an infinite geometric series
- Convergence condition: $|a| < 1$ — if $|a| \geq 1$, the sum diverges and DTFT does not exist

**Physical meaning:** This is the impulse response of a first-order IIR filter. The pole at $z = a$ (inside the unit circle) determines the frequency response shape. Smaller $|a|$ → faster decay → wider bandwidth.

---

#### (c) Left-Sided Exponential

$$x[n] = -a^n u[-n-1]$$

Since $u[-n-1]$ gives $-n - 1 \geq 0$ i.e. $-n \geq 1$ i.e. $n \leq -1$:

$$X(e^{j\omega}) = \sum_{n=-\infty}^{-1} -a^n e^{-j\omega n}$$

$$= -\left[a^{-1}e^{j\omega} + a^{-2}e^{j2\omega} + \cdots\right]$$

$$= -a^{-1}e^{j\omega} \left[1 + a^{-1}e^{j\omega} + a^{-2}e^{j2\omega} + \cdots\right]$$

**Convergence condition:** $|a^{-1}e^{j\omega}| < 1$ i.e. $|a| > 1$.

**Result (after simplification):**

$$X(e^{j\omega}) = \frac{1}{1 - ae^{-j\omega}}, \quad |a| > 1$$

$$\boxed{-a^n u[-n-1] \xleftrightarrow{\text{DTFT}} \frac{1}{1 - ae^{-j\omega}}, \quad |a| > 1}$$

**Remarkable result:** Same formula, but different condition!

**Deep insight:** The same rational function $\frac{1}{1-ae^{-j\omega}}$ can represent two completely different signals depending on the Region of Convergence (ROC). This is the foundation of the Z-transform's power.

---

#### (d) Constant Signal $x[n] = 1$

$$X(e^{j\omega}) = 2\pi \sum_{k=-\infty}^{\infty} \delta(\omega - 2\pi k)$$

**Explanation:**

- Constant signal in time = zero frequency only (DC)
- Since DTFT is periodic with $2\pi$, we get impulse trains at every $2\pi k$
- Each impulse has height $2\pi$

**Duality principle:**

This principle is universal: **localized in one domain → spread in the other domain**.

---

#### (e) Unit Step $u[n]$

$$X(e^{j\omega}) = \frac{1}{1-e^{-j\omega}} + \pi \sum_{k=-\infty}^{\infty} \delta(\omega - 2\pi k)$$

**Why two parts:** We write $u[n] = \frac{1}{2} + \frac{1}{2}\text{sgn}[n]$:

- DC part → impulses at $2\pi k$
- The other part → $\frac{1}{1-e^{-j\omega}}$

**Why not use geometric series directly?** Because $|e^{-j\omega}| = 1$ — at the boundary of convergence. We need distribution theory to handle this.

**Common mistake:** Writing $\frac{1}{1-e^{-j\omega}}$ only, without the impulse train! This is wrong because the inverse transform won't recover $u[n]$.

---

### 3. DTFT Properties

#### Property 1: Periodicity

$$X(e^{j(\omega + 2\pi)}) = X(e^{j\omega})$$

**Proof:**

$$X(e^{j\omega}) = \sum_{n=-\infty}^{\infty} x[n] e^{-j\omega n}$$

Substituting: $X(e^{j(\omega + 2\pi)}) = sum_{n=-\infty}^{\infty} x[n] e^{-j(\omega + 2\pi)n}$

$$= \sum_{n=-\infty}^{\infty} x[n] e^{-j\omega n} \cdot e^{-j2\pi n}$$

Since $e^{-j2\pi n} = 1$ for all integers:

$$= \sum_{n=-\infty}^{\infty} x[n] e^{-j\omega n} = X(e^{j\omega})$$

**Why?** Because $e^{-j2\pi n} = \cos(2\pi n) - j\sin(2\pi n) = 1$ for any integer. The phasor completes full rotations and returns to the same point.

**Practical consequences:**

- We only need to look at $\omega \in [-\pi, \pi]$ or $[0, 2\pi]$
- Everything outside is a repeated copy

**Important frequency mapping:**

| Frequency | Meaning |
|---|---|
| $\omega = 0$ | DC (zero frequency) |
| $\omega = \pi$ | Nyquist frequency (highest representable) |
| $\omega = 2\pi$ | Sampling frequency (same as $\omega = 0$) |

---

#### Property 2: Linearity

$$\text{DTFT}\{\alpha_1 x_1[n] + \alpha_2 x_2[n]\} = \alpha_1 \text{DTFT}\{x_1[n]\} + \alpha_2 \text{DTFT}\{x_2[n]\}$$

In shorthand:

$$\alpha_1 x_1[n] + \alpha_2 x_2[n] \xleftrightarrow{\text{DTFT}} \alpha_1 X_1(e^{j\omega}) + \alpha_2 X_2(e^{j\omega})$$

**Why?** DTFT is defined by a sum, and sums commute with linear combinations. Constants can be factored out.

**How to use it:** If your signal is $x[n] = 3\delta[n] + 2(0.5)^n u[n]$, don't compute DTFT from scratch — transform each part separately and add the results.

---

#### Property 3: Time Shift

$$x[n-k] \xleftrightarrow{\text{DTFT}} e^{-j\omega k} X(e^{j\omega})$$

**Proof:**

$$\text{DTFT}\{x[n-k]\} = \sum_{n=-\infty}^{\infty} x[n-k] e^{-j\omega n}$$

Letting $m = n - k$ (i.e., $n = m + k$):

$$= \sum_{m=-\infty}^{\infty} x[m] e^{-j\omega(m+k)}$$

$$= e^{-j\omega k} \sum_{m=-\infty}^{\infty} x[m] e^{-j\omega m} = e^{-j\omega k} X(e^{j\omega})$$

**Implications:**

- **Magnitude effect:** $|e^{-j\omega k}| = 1$ — unchanged!
- **Phase effect:** $\angle e^{-j\omega k} = -\omega k$ — linear shift

$$\boxed{|X_{delayed}| = |X_{original}|} \quad \boxed{\angle X_{delayed} = \angle X_{original} - \omega k}$$

**Why is linear phase important?**

- Linear phase shift means all frequencies are delayed by the same time amount $k$
- This preserves the signal shape (No Phase Distortion)
- If the shift were nonlinear, the signal shape would change

> **Key takeaway:** Pure delay is the **only** operation that changes phase without changing magnitude!

---

#### Property 4: Frequency Shift (Modulation)

$$e^{j\omega_0 n} x[n] \xleftrightarrow{\text{DTFT}} X(e^{j(\omega - \omega_0)})$$

**Proof:**

$$\text{DTFT}\{e^{j\omega_0 n} x[n]\} = \sum_{n=-\infty}^{\infty} x[n] e^{j\omega_0 n} e^{-j\omega n}$$

$$= \sum_{n=-\infty}^{\infty} x[n] e^{-j(\omega - \omega_0)n} = X(e^{j(\omega-\omega_0)})$$

**Summary:**

| Domain | Operation |
|---|---|
| Time | Multiply by $e^{j\omega_0 n}$ |
| Frequency | Shift spectrum by $+\omega_0$ |

**This is the basis of Modulation in communications:**

1. Audio signal at $\omega = 0$ (baseband)
2. Multiply by $e^{j\omega_0 n}$ → spectrum shifts to $\omega_0$ (carrier frequency)
3. Transmit through air
4. Receiver multiplies by $e^{-j\omega_0 n}$ → returns spectrum to baseband
5. Low-pass filter → recovers original signal

---

#### Property 5: Convolution Theorem

$$x[n] * h[n] \xleftrightarrow{\text{DTFT}} X(e^{j\omega}) \cdot H(e^{j\omega})$$

**Step-by-step proof:**

$$\text{DTFT}\{x[n]*h[n]\} = \sum_n \left[\sum_k x[k]h[n-k]\right] e^{-j\omega n}$$

**Step 1:** Swap summation order:

$$= \sum_k x[k] \sum_n h[n-k] e^{-j\omega n}$$

**Step 2:** Let $m = n-k$ in the inner sum:

$$\sum_n h[n-k] e^{-j\omega n} = \sum_m h[m] e^{-j\omega(m+k)} = e^{-j\omega k} \underbrace{\sum_m h[m] e^{-j\omega m}}_{H(e^{j\omega})}$$

**Step 3:** Substitute back:

$$= \sum_k x[k] e^{-j\omega k} \cdot H(e^{j\omega}) = H(e^{j\omega}) \underbrace{\sum_k x[k] e^{-j\omega k}}_{X(e^{j\omega})}$$

$$\boxed{= X(e^{j\omega}) \cdot H(e^{j\omega})}$$

**Why this matters:**

| Domain | Operation | Complexity |
|---|---|---|
| Time | Convolution $x[n]*h[n]$ | $O(N^2)$ (hard!) |
| Frequency | Multiplication $X \cdot H$ | $O(N)$ (easy!) |

**Speed:** Direct convolution = $O(N^2)$. FFT-based convolution = $O(N \log N)$. For $N = 10^6$, this is the difference between hours and seconds!

**Concept:** Convolution → Filtering. $|H|$ acts as a frequency-dependent volume knob, $\angle H$ adds frequency-dependent delay.

**Filter types:**

```
Low-pass:     ████░░░░     Passes low frequencies, blocks high
High-pass:   ░░░░████     Passes high frequencies, blocks low
Band-pass:   ░░████░░     Passes a specific band only
```

---

#### Property 6: Parseval's Theorem — Energy Conservation

$$\sum_{n=-\infty}^{\infty} |x[n]|^2 = \frac{1}{2\pi} \int_{-\pi}^{\pi} |X(e^{j\omega})|^2 d\omega$$

**Explanation:**

- Total energy of a signal is the same in time or frequency
- $|X(e^{j\omega})|^2$ is called the **Energy Spectral Density**
- The factor $\frac{1}{2\pi}$ accounts for the change in the integration variable

**Example with delta:**

- Time: $\sum |\delta[n]|^2 = 1$
- Frequency: $\frac{1}{2\pi} \int_{-\pi}^{\pi} |1|^2 d\omega = \frac{1}{2\pi} \cdot 2\pi = 1$

---

#### Property 7: Frequency Domain Derivative (Multiplication by n)

$$n \cdot x[n] \xleftrightarrow{\text{DTFT}} j\frac{d}{d\omega} X(e^{j\omega})$$

**Proof:**

$$\frac{d}{d\omega} X(e^{j\omega}) = \sum_n x[n] \cdot (-jn) e^{-j\omega n}$$

$$\Rightarrow \text{DTFT}\{n \cdot x[n]\} = j\frac{d}{d\omega} X(e^{j\omega})$$

**Practical use:** Instead of computing $\sum_n n \cdot a^n e^{-j\omega n}$ from scratch, differentiate known result $\frac{1}{1-ae^{-j\omega}}$ and multiply by $j$.

**Example:**
DTFT of $n \cdot a^n u[n]$:

$$j \cdot \frac{d}{d\omega} \left[\frac{1}{1-ae^{-j\omega}}\right] = j \cdot \frac{-ae^{-j\omega} \cdot (-j)}{(1-ae^{-j\omega})^2} = \frac{-ae^{-j\omega}}{(1-ae^{-j\omega})^2}$$

---

#### Property 8: Symmetry Properties

**Definitions:**

- **Conjugate Symmetric:** $x[n] = x^*[-n]$
- **Conjugate Anti-symmetric:** $x[n] = -x^*[-n]$

**Important theorem:** If $x[n]$ is real, then:

$$X^*(e^{j\omega}) = X(e^{-j\omega})$$

**Proof:**

$$X(e^{j\omega}) = \sum_n x[n] e^{-j\omega n}$$

Taking the complex conjugate:

$$X^*(e^{j\omega}) = \left[\sum_n x[n] e^{-j\omega n}\right]^* = \sum_n x[n]^* e^{+j\omega n}$$

Since $x[n]$ is real: $= \sum_n x[n] e^{-j(-\omega)n} = X(e^{-j\omega})$

$$\boxed{X^*(e^{j\omega}) = X(e^{-j\omega})}$$

**Consequences:**

- $|X(e^{j\omega})|$ is even — symmetric about $\omega = 0$
- $\angle X(e^{j\omega})$ is odd — anti-symmetric about $\omega = 0$

**Practical benefit:** For real signals, we only need to compute half the spectrum ($\omega \in [0, \pi]$)!

**Symmetry summary:**

| Time Domain Signal | Frequency Domain Spectrum |
|---|---|
| Real | $X^*(e^{j\omega}) = X(e^{-j\omega})$ |
| Real + Even | Pure Real |
| Real + Odd | Pure Imaginary |
| Pure Imaginary | Conjugate Anti-symmetric |

---

### 4. Communication Channel Model

As an LTI system, the channel affects the signal in three ways:

| Effect | Time Domain | Frequency Domain | Receiver Fix |
|---|---|---|---|
| **Filtration** | Convolution | Multiply by $H(e^{j\omega})$ | Equalizer |
| **Delay** | Shift by $k$ | Multiply by $e^{-j\omega k}$ | Do nothing (linear phase = harmless) |
| **Attenuation** | Scale by $\alpha$ | Scale by $\alpha$ | Amplify by $1/\alpha$ |

**Key insight:** Delay is the **only** effect that doesn't need correction. This is why we require communication channels to have **linear phase** — any nonlinear phase distortion cannot be undone by simple amplification.

---

### 5. Practical Examples

#### Example 1: DTFT of $\cos(\omega_0 n)$

Using Euler's identity:

$$\cos(\omega_0 n) = \frac{1}{2}e^{j\omega_0 n} + \frac{1}{2}e^{-j\omega_0 n}$$

Using the frequency shift property:

$$X(e^{j\omega}) = \pi \sum_{k=-\infty}^{\infty} [\delta(\omega - \omega_0 - 2\pi k) + \delta(\omega + \omega_0 - 2\pi k)]$$

**Explanation:**

- Two impulses at $\pm\omega_0$ (repeated every $2\pi$)
- Each impulse has height $\pi$
- Spectrum is **real** (because cosine is even)

---

#### Example 2: DTFT of $\sin(\omega_0 n)$

$$\sin(\omega_0 n) = \frac{1}{2j}e^{j\omega_0 n} - \frac{1}{2j}e^{-j\omega_0 n}$$

$$X(e^{j\omega}) = \frac{\pi}{j} \sum_{k=-\infty}^{\infty} [\delta(\omega - \omega_0 - 2\pi k) - \delta(\omega + \omega_0 - 2\pi k)]$$

**Explanation:**

- Two impulses at $\pm\omega_0$ with opposite signs
- Spectrum is **pure imaginary** (because sine is odd)

---

## Key Points for Exam

### Important Definitions

1. **DTFT:** $X(e^{j\omega}) = \sum_{n=-\infty}^{\infty} x[n]e^{-j\omega n}$
2. **DFT:** $X[k] = \sum_{n=0}^{N-1} x[n]e^{-j\frac{2\pi}{N}kn}$
3. **Convolution:** $y[n] = x[n] * h[n] = \sum_k x[k]h[n-k]$
4. **Linear phase:** $\angle e^{-j\omega k} = -\omega k$ — straight line in $\omega$

### Important Properties

1. **Periodicity:** $X(e^{j(\omega+2\pi)}) = X(e^{j\omega})$
2. **Linearity:** $\alpha_1 x_1 + \alpha_2 x_2 \leftrightarrow \alpha_1 X_1 + \alpha_2 X_2$
3. **Time shift:** $x[n-k] \leftrightarrow e^{-j\omega k} X(e^{j\omega})$
4. **Frequency shift:** $e^{j\omega_0 n}x[n] \leftrightarrow X(e^{j(\omega-\omega_0)})$
5. **Convolution:** $x[n]*h[n] \leftrightarrow X(e^{j\omega})H(e^{j\omega})$
6. **Parseval:** $\sum |x[n]|^2 = \frac{1}{2\pi}\int |X|^2 d\omega$
7. **Derivative:** $n \cdot x[n] \leftrightarrow j\frac{dX}{d\omega}$
8. **Symmetry:** If $x[n]$ real: $X^*(e^{j\omega}) = X(e^{-j\omega})$

### Transform Pairs to Memorize

| Signal $x[n]$ | DTFT $X(e^{j\omega})$ | Condition |
|---|---|---|
| $\delta[n]$ | $1$ | Always |
| $a^n u[n]$ | $\frac{1}{1-ae^{-j\omega}}$ | $|a| < 1$ |
| $-a^n u[-n-1]$ | $\frac{1}{1-ae^{-j\omega}}$ | $|a| > 1$ |
| $1$ | $2\pi\sum_k \delta(\omega-2\pi k)$ | Distributions |
| $u[n]$ | $\frac{1}{1-e^{-j\omega}} + pi\sum_k \delta(\omega-2\pi k)$ | Distributions |
| $\cos(\omega_0 n)$ | $\pi[\delta(\omega-\omega_0) + \delta(\omega+\omega_0)]$ | + copies |
| $\sin(\omega_0 n)$ | $\frac{\pi}{j}[\delta(\omega-\omega_0) - \delta(\omega+\omega_0)]$ | + copies |

---

## Simplified for Beginners

### What is DTFT?

Imagine you're listening to a song. In the **time domain**, you hear the wave evolve second by second. But what if you wanted to know **which frequencies** (bass, treble, voice) are present and **how much** of each?

DTFT does exactly that — takes a sequence of samples and decomposes it into a **continuous spectrum of frequencies**. It answers: "How much of each frequency is in this signal?"

### Why do we need continuous frequency?

Because $e^{-j\omega n}$ is defined for any real $\omega$. We don't sample the frequency axis; we compute the complete theoretical spectrum. This gives us a full picture, but it can't be computed on a computer because it requires infinite values of $\omega$.

### How do we compute it on a computer?

We use DFT — we sample the frequency at N equally-spaced points: $\omega_k = \frac{2\pi k}{N}$. This makes computation possible!

### Simple example — Delta

Delta $\delta[n]$ is a single spike at $n=0$.

- In time: one spike
- In frequency: flat spectrum = 1 for all frequencies

Why? Because it contains all frequencies equally!

### Why does convolution matter?

Convolution in time = multiplication in frequency.

This means:

- Instead of expensive summation, we multiply — which is easy!
- This is the foundation of all communication systems and filtering

### Delaying a signal

When we delay a signal by $k$ samples:

- Magnitude doesn't change! $|e^{-j\omega k}| = 1$
- Phase changes linearly: $-\omega k$

This is important — delay doesn't distort the signal!

---

## Review Questions

### Question 1

**What is the difference between DTFT and DFT? When do we use each?**

DTFT is a theoretical transform that gives a continuous spectrum for potentially infinite signals, but cannot be computed on a computer because it requires infinite frequency values. DFT is a practical version that samples the DTFT spectrum at discrete points, making it computable. We use DTFT for theoretical analysis and DFT for actual computation.

### Question 2

**What is the convergence condition for DTFT of $a^n u[n]$? Explain why.**

$|a| < 1$. Because DTFT uses the geometric series $\sum (ae^{-j\omega})^n$, which converges only when $|ae^{-j\omega}| < 1$. Since $|e^{-j\omega}| = 1$, the condition becomes $|a| < 1$. If $|a| \geq 1$, the sum diverges and DTFT does not exist.

### Question 3

**Prove that DTFT is periodic with period $2\pi$.**

$e^{-j(\omega+2\pi)n} = e^{-j\omega n} \cdot e^{-j2\pi n} = e^{-j\omega n} \cdot 1 = e^{-j\omega n}$. Therefore $X(e^{j(\omega+2\pi)}) = X(e^{j\omega})$. The $2\pi$ period comes from the discrete-time nature.

### Question 4

**Explain the time shift property and its effect on magnitude and phase.**

$x[n-k] \leftrightarrow e^{-j\omega k} X(e^{j\omega})$. Magnitude doesn't change because $|e^{-j\omega k}| = 1$. Phase changes linearly: $-\omega k$ — this means all frequencies are delayed by the same amount, hence no distortion!

### Question 5

**What is Modulation? How is it used in communications?**

Modulation is multiplying the signal by $e^{j\omega_0 n}$, which shifts its spectrum to $\omega_0$. In communications: we multiply the baseband signal by a high-frequency carrier for transmission, then multiply again to recover it at the receiver.

### Question 6

**Prove the Convolution Theorem: $x[n]*h[n] \leftrightarrow X(e^{j\omega})H(e^{j\omega})$.**

We start from the DTFT definition of convolution: $\sum_n [\sum_k x[k]h[n-k]] e^{-j\omega n}$. We swap the order of summation, then let $m = n-k$ in the inner sum. After simplification, we get $X(e^{j\omega})H(e^{j\omega})$.

### Question 7

**Explain why real signals have conjugate symmetric spectra.**

If $x[n]$ is real: $X^*(e^{j\omega}) = X(e^{-j\omega})$. This means the spectrum at $+\omega$ is the complex conjugate of the spectrum at $-\omega$. Therefore $|X|$ is even and $\angle X$ is odd. So we only need half the spectrum!

### Question 8

**What is the difference between low-pass and high-pass filters?**

Low-pass passes low frequencies and blocks high ones. High-pass does the opposite. Both depend on $|H(e^{j\omega})|$ — if close to 1 for low frequencies = low-pass; if close to 1 for high frequencies = high-pass.

### Question 9

**What is the importance of Parseval's Theorem?**

It states that signal energy is conserved: $\sum |x[n]|^2 = \frac{1}{2\pi}\int |X|^2 d\omega$. Energy can be computed in time or frequency — both give the same result.

### Question 10

**How does a channel affect a signal in communications?**

The channel (as an LTI system) affects the signal in three ways: Filtration (frequency-dependent attenuation), Delay (time shift), and Attenuation (magnitude reduction). The receiver performs: De-modulation, Amplification, and Equalization. Delay alone doesn't need correction!

---

## Quick Summary Before Exam

1. **DTFT = theoretical** with continuous frequency; **DFT = practical** for computers
2. **Periodicity = $2\pi$** — no need to look outside $[-\pi, \pi]$
3. **Convolution in time = multiplication in frequency** — most important property!
4. **Delay = multiply by $e^{-j\omega k}$** — doesn't distort because magnitude is constant!
5. **Modulation = spectrum shifting** — foundation of communications
6. **Real signal = symmetric spectrum** — compute only half!
7. **Parseval = energy conservation**
8. **Symmetry:** Even → Real spectrum; Odd → Imaginary!

---
