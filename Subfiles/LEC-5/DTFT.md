---
Created: " 2026-04-26 21:01"
modified: 2026-04-26 21:01
tags:
  - FACL
Source:
---
> [!quote] Watch the little things; a small leak will sink a great ship.
> — Benjamin Franklin

**"اللهم إني أسألك فهم النبيين، وحفظ المرسلين، والملائكة المقربين، اللهم اجعل ألسنتنا عامرة بذكرك، وقلوبنا بخشيتك، إنك على كل شيء قدير"**

---
# The Discrete-Time Fourier Transform (DTFT)
## A Complete, Intuitive Walkthrough

---

## 🎯 The Big Picture

Imagine you're listening to a song. In the **time domain**, you hear the sound wave evolving second by second. But what if you wanted to know *which frequencies* (bass, treble, vocals) are present and *how much* of each?

That's exactly what the **DTFT** does — it takes a sequence of discrete samples (numbers) and decomposes them into a **continuous spectrum of frequencies**. It answers:

> *"How much of each frequency lives inside this signal?"*

The entire lecture builds one idea on top of another:

```
DTFT (theory) → Basic Signals (building blocks) → Properties (shortcuts) → Convolution (the crown jewel) → Real Applications (filters, communications)
```

---

## 1. The DTFT — Definition & Intuition

### The Formula
$$X(e^{j\omega}) = \sum_{n=-\infty}^{\infty} x[n] \, e^{-j\omega n}$$

### Breaking It Down

| Piece | What It Is | Why It Matters |
|-------|-----------|----------------|
| $x[n]$ | Your discrete signal (a sequence of numbers) | This is the **input** — the data you're analyzing |
| $e^{-j\omega n}$ | A complex exponential (a rotating phasor) | This is the **probe** — it "tests" how much frequency $\omega$ exists |
| $\omega$ | Continuous frequency variable (radians/sample) | Unlike DFT, this is **not discrete** — it's a smooth continuum |
| $X(e^{j\omega})$ | The output spectrum (complex-valued function) | Gives you **magnitude + phase** at every frequency |
| The sum | Correlation of the signal with each frequency probe | Higher output = more of that frequency is present |

### WHY Continuous Frequency?
Because $e^{-j\omega n}$ is defined for **any** real $\omega$. We're not sampling the frequency axis — we're computing the *full* theoretical spectrum. This gives us a complete picture, but it's **not computable on a computer** (infinite frequencies to evaluate).

### The Bridge to DFT
Since computers can't handle continuous $\omega$, we **sample** the frequency axis at $N$ equally-spaced points:

$$\omega_k = \frac{2\pi k}{N}, \quad k = 0, 1, \ldots, N-1$$

This gives us the **DFT**:
$$X[k] = \sum_{n=0}^{N-1} x[n] \, e^{-j\frac{2\pi}{N}kn}$$

> **Key distinction:** DTFT = theoretical (continuous frequency, possibly infinite-length signal). DFT = practical (discrete frequency, finite-length signal). The DFT is simply **samples of the DTFT**.

---

## 2. DTFT of Basic Signals — The Building Blocks

These five transform pairs are the "multiplication table" of signal processing. Memorize them — everything else is derived from these using properties.

### 2.1 The Impulse $\delta[n]$

**Impulse**: $\delta[n] = \begin{cases} 1 & n=0 \\ 0 & \text{o.w.} \end{cases}$

$$ X(e^{j\omega}) = \sum_{n=-\infty}^{\infty} \delta[n]e^{-j\omega n} = e^{-j\omega(0)} = 1 $$

$$\delta[n] \xleftrightarrow{\text{DTFT}} 1$$

**Time domain:** A single spike at $n=0$, zero everywhere else.
**Frequency domain:** Flat spectrum of magnitude 1 at all frequencies.

**WHY?** The sum collapses to a single term ($n=0$ only), and $e^{-j\omega \cdot 0} = 1$.

**Intuition:** An impulse is the "perfect test signal." It contains **all frequencies equally** — like white light containing every color. That's why injecting $\delta[n]$ into a system reveals its complete frequency response.

```horizontal 
![[image-6.png]]
$$
\text{TimeDomain}
$$
---
![[image-7.png]]
$$
\text{FrequencyDomain}
$$
```
	
```
Time:      ▲
           │ █
           │ █
           └─┴─▶ n
              0

Frequency:  │ ████
           │ ████  (flat at 1 for all ω)
           └─────▶ ω
```

---

### 2.2 Right-Sided Exponential $a^n u[n]$

$$ x[n] = a^n u[n] $$

$a$ is a complex quantity (constant).

$$ X(e^{j\omega}) = \sum_{n=-\infty}^{\infty} a^n u[n] e^{-j\omega n} $$

> [!note] **Geometric Series Reference**
> $$ 1 + r + \dots + r^n = \frac{1 - r^{n+1}}{1 - r} $$
> if $|r| < 1$ and $n \to \infty$
> $$ 1 + r + \dots = \frac{1}{1 - r} $$

$$ = \sum_{n=0}^{\infty} a^n e^{-j\omega n} = 1 + a e^{-j\omega} + a^2 e^{-j2\omega} + \dots $$

The ==DTFT is defined only when==: $|a e^{-j\omega}| < 1$

$$ |a| \cdot |e^{-j\omega}| < 1 $$
$$ (|a| < 1) $$

In this case:
$$ X(e^{j\omega}) = \frac{1}{1 - a e^{-j\omega}} $$

$$
a^n .e^{-j\omega} \xleftrightarrow{\text{DTFT}} \frac{1}{1 - a e^{-j\omega}}, \quad \text{when } |a| < 1
$$

**WHY the condition $|a| < 1$?** The geometric series formula $\sum r^n = \frac{1}{1-r}$ only converges when $|r| < 1$. Here $r = ae^{-j\omega}$, and $|e^{-j\omega}| = 1$, so we need $|a| < 1$.

**Physical meaning:** This is the **impulse response of a first-order IIR filter**. The pole at $z = a$ (inside the unit circle) determines the frequency response shape. Smaller $|a|$ → faster decay → wider bandwidth.

---

### 2.3 Left-Sided Exponential $-a^n u[-n-1]$

$$
x[n] = -a^n u[-n-1]
$$

$$
X(e^{j\omega}) = \sum_{n=-\infty}^{\infty} -a^n u[-n-1] e^{-j\omega n}
$$

Since $u[-n-1]$:
$$
-n - 1 \geq 0
$$
$$
-n \geq 1
$$
$$
\boxed{n \leq -1}
$$

Then:
$$
X(e^{j\omega}) = \sum_{n=-\infty}^{-1} -a^n e^{-j\omega n}
$$

$$
= -\left[a^{-1}e^{j\omega} + a^{-2}e^{j2\omega} + \cdots \right]
$$

$$
= -a^{-1}e^{j\omega} \left[1 + a^{-1}e^{j\omega} + a^{-2}e^{j2\omega} + \cdots \right]
$$

DTFT exists only if:
$$
|a^{-1}e^{j\omega}| < 1
$$

Since:
$$
|e^{j\omega}| = 1
$$
Then:
$$
|a^{-1}| < 1 \Rightarrow |a| > 1
$$
 
In this case: (Multiply by $-a.e^{-jw}$ in nominator and denominator )

$$ X(e^{j\omega}) = \frac{-a^{-1}e^{j\omega}}{1 - a^{-1}e^{j\omega}} = \frac{1}{-a e^{-j\omega} + 1} = \frac{1}{1 - a e^{-j\omega}} $$

$$ -a^n u[-n-1] \xleftrightarrow{\text{DTFT}} \frac{1}{1 - a e^{-j\omega}} \quad \text{when } |a| > 1 $$

**The astonishing result:** Same formula, different condition!

**WHY?** The signal exists only for $n \leq -1$, so we rewrite in terms of positive exponents and get a geometric series with ratio $a^{-1}e^{j\omega}$. Convergence now requires $|a^{-1}| < 1$, i.e., $|a| > 1$.

**Deep insight:** The same rational function $\frac{1}{1-ae^{-j\omega}}$ can represent **two completely different signals** depending on the Region of Convergence. This is the foundation of the Z-transform's power — the ROC carries critical information about causality and stability.

```
Right-sided (|a| < 1):        Left-sided (|a| > 1):
  ▲                               ▲
  │█                              █│
  │ █                            █ │
  │  █                          █  │
  └──┴─▶ n                     ─┴──▶ n
   0  n                      -n  0
```

---

### 2.4 Constant Signal $x[n] = 1$

![[FACL/DigitalSignals/Subfiles/Attachments/image.png]]


$$X(e^{j\omega}) = 1 \xleftrightarrow{\text{DTFT}} 2\pi \sum_{k=-\infty}^{\infty} \delta(\omega - 2\pi k)$$

**WHY impulses in frequency?** A constant signal varies infinitely slowly (infinite period = zero frequency). So ALL its energy concentrates at $\omega = 0$. The $2\pi k$ repetitions come from DTFT periodicity.

**WHY the factor $2\pi$?** Comes from careful derivation using the inverse DTFT integral — it's a normalization factor, not arbitrary.

**Duality with the impulse:** 
- Impulse in time → flat in frequency
- Flat in time → impulse in frequency

This is a universal principle: **localized in one domain → spread in the other**.

---

### 2.5 Unit Step $u[n]$
**Trial:**
$$
X(e^{j\omega}) = \sum_{n=-\infty}^{\infty} u[n]e^{-j\omega n}= \sum_{n=0}^{\infty}e^{-j\omega n}= 1+e^{-j\omega}+e^{-j2\omega}+\dots \quad , r = e^{-j\omega} , |r| = 1
$$

$$u[n] \xleftrightarrow{\text{DTFT}} \frac{1}{1-e^{-j\omega}} + \pi \sum_{k=-\infty}^{\infty} \delta(\omega - 2\pi k)$$

**WHY two parts?** Decompose $u[n] = \frac{1}{2} + \frac{1}{2}\text{sgn}[n]$:
- The DC part $\frac{1}{2}$ → impulse train with strength $\pi$
- The causal alternating part → $\frac{1}{1-e^{-j\omega}}$

**WHY can't we use the geometric series directly?** Because the ratio is $e^{-j\omega}$ with $|e^{-j\omega}| = 1$ — right on the boundary of convergence. We need distribution theory (generalized functions) to handle this.

> **Common trap:** Don't just write $\frac{1}{1-e^{-j\omega}}$ and forget the impulse train. Without it, the inverse transform won't recover $u[n]$.

---

## 3. Properties — The Shortcuts

Properties let you **avoid computing sums from scratch**. They're the "algebra rules" of the frequency domain.

### 3.1 Periodicity: $X(e^{j(\omega+2\pi)}) = X(e^{j\omega})$

**Proof:**

$$X(e^{j\omega}) = \sum_{n=-\infty}^{\infty} x[n] e^{-j\omega n}$$

$$X(e^{j(\omega + 2\pi)}) = \sum_{n=-\infty}^{\infty} x[n] e^{-j(\omega + 2\pi)n}$$

$$= \sum_{n=-\infty}^{\infty} x[n] e^{-j\omega n} \cdot e^{-j2\pi n}$$
$$
= \sum_{n=-\infty}^{\infty} x[n] e^{-j\omega n} = X(e^{j\omega})
$$
Since $e^{-j2\pi n} = 1$ for all integer $n$, we get $X(e^{j(\omega+2\pi)}) = X(e^{j\omega})$ ∎

**Proof in one line:** $e^{-j(\omega+2\pi)n} = e^{-j\omega n} \cdot e^{-j2\pi n} = e^{-j\omega n} \cdot 1 = e^{-j\omega n}$

**WHY?** Because $e^{-j2\pi n} = \cos(2\pi n) - j\sin(2\pi n) = 1$ for any integer $n$. The phasor completes full rotations and returns to the same point.

**Practical consequence:** You only ever need to look at $\omega \in [-\pi, \pi]$ or $[0, 2\pi]$. Everything outside is a copy.

**Important mapping:**

| Frequency       | Meaning                                   |
| --------------- | ----------------------------------------- |
| $\omega = 0$    | DC (zero frequency)                       |
| $\omega = \pi$  | Nyquist frequency (highest representable) |
| $\omega = 2\pi$ | Sampling frequency (same as $\omega = 0$) |


---

### 3.2 Linearity

$$\text{DTFT}\{\alpha_1 x_1[n] + \alpha_2 x_2[n]\} = \alpha_1 \text{ DTFT}\{x_1[n]\} + \alpha_2 \text{ DTFT}\{x_2[n]\}$$

$$= \alpha_1 X_1(e^{j\omega}) + \alpha_2 X_2(e^{j\omega})$$
**in one line** :
$$\alpha_1 x_1[n] + \alpha_2 x_2[n] \xleftrightarrow{\text{DTFT}} \alpha_1 X_1(e^{j\omega}) + \alpha_2 X_2(e^{j\omega})$$

**WHY?** The DTFT is defined by a sum, and sums commute with linear combinations. Constants factor out.

**How to use it:** If your signal is $x[n] = 3\delta[n] + 2(0.5)^n u[n]$, don't compute the $DTFT$ from scratch — transform each part separately and add.

> **Used in practice:** The unit step derivation used linearity: $u[n] = \frac{1}{2} + \frac{1}{2}\text{sgn}[n]$, transform each part, add.

---

### 3.3 Time Shift: Delay → Linear Phase

$$\text{DTFT}\{x[n-k]\} = \sum_{n=-\infty}^{\infty} x[n-k] e^{-j\omega k}$$
$$
\text{DTFT}\{x[n+k]\} = \sum_{n=-\infty}^{\infty} x[n-k] e^{+j\omega k}
$$


Let $m = n - k \quad \therefore n = m + k$

- As $n \to -\infty,\quad m \to -\infty$
- As $n \to +\infty,\quad m \to +\infty$

$$\text{DTFT}\{x[n-k]\} = \sum_{m=-\infty}^{\infty} x[m] e^{-j\omega(m+k)}$$

$$= e^{-j\omega k} \sum_{m=-\infty}^{\infty} x[m] e^{-j\omega m} = e^{-j\omega k} X(e^{j\omega})$$

#### Time Shift Property — Implications

$$x[n-k] \xleftrightarrow{\text{DTFT}} e^{-j\omega k} X(e^{j\omega})$$

↑ _delay in time domain_

##### Magnitude
> [!note] Magintude $e^{-j\omega k}$ = 1

$$|e^{-j\omega k} \cdot X(e^{j\omega})| = |X(e^{j\omega})| \quad \text{(no change)}$$

##### Phase

$$\angle\left[e^{-j\omega k} \cdot X(e^{j\omega})\right]$$

$$= \angle e^{-j\omega k} + \angle X(e^{j\omega})$$

$$= -\omega k + \angle X(e^{j\omega})$$

**(linear phase shift — no phase distortion)**

**WHY is this profound?** Pure delay is the **only** operation that changes phase without changing magnitude. The phase shift $-\omega k$ is a straight line with slope $-k$ — this is **linear phase**, and it guarantees **zero phase distortion**.

**Real-world meaning:** When a signal travels through a cable, it gets delayed. But delay doesn't distort the signal — every frequency is shifted by the same *time amount* $k$. The waveform shape is perfectly preserved.

**Contrast:** If different frequencies were delayed by different amounts (non-linear phase), the signal would arrive distorted even though all frequencies are present. This is why "phase-linear" filters are prized in audio.

---

### 3.4 Frequency Shift: Modulation
![[FACL/DigitalSignals/Subfiles/Attachments/image-1.png]]
$$e^{j\omega_0 n} \cdot x[n] \xleftrightarrow{\text{DTFT}} X(e^{j(\omega - \omega_0)})$$

**This is the dual of time shift:**

| Domain       | Time Shift                   | Frequency Shift               |
| ------------ | ---------------------------- | ----------------------------- |
| Operation    | Delay by $k$                 | Multiply by $e^{j\omega_0 n}$ |
| Other domain | Multiply by $e^{-j\omega k}$ | Shift by $\omega_0$           |


**WHY does this matter?** This is the mathematical foundation of **modulation** — the technology behind ALL wireless communications.

**How a radio works (simplified):**
```
1. Your voice signal X(ω) is centered at ω = 0 (baseband)
2. Multiply by e^(jω₀n) → spectrum shifts to ω₀ (carrier frequency)
3. Transmit at ω₀ → signal travels through air
4. Receiver multiplies by e^(-jω₀n) → spectrum shifts back to baseband
5. Low-pass filter → recover original signal
```

**Critical detail for real signals:** Since $\cos(\omega_0 n) = \frac{e^{j\omega_0 n} + e^{-j\omega_0 n}}{2}$, real modulation creates **two** spectral copies — one at $+\omega_0$ and one at $-\omega_0$. Not one.

---

### 3.5 The Convolution Theorem — The Crown Jewel

$$x[n] * h[n] \xleftrightarrow{\text{DTFT}} X(e^{j\omega}) \cdot H(e^{j\omega})$$
	
> [!warning] **Convolution in time domain** becomes **multiplication in frequency domain**.
	
#### The Proof (step-by-step)

$$\text{DTFT}\{x[n]*h[n]\} = \sum_n \left[\sum_k x[k]h[n-k]\right] e^{-j\omega n}$$

**Step 1:** Swap summation order (justified by absolute convergence):
$$= \sum_k x[k] \sum_n h[n-k] e^{-j\omega n}$$

**Step 2:** Substitute $m = n-k$ in the inner sum:
$$\sum_n h[n-k] e^{-j\omega n} = \sum_m h[m] e^{-j\omega(m+k)} = e^{-j\omega k} \underbrace{\sum_m h[m] e^{-j\omega m}}_{H(e^{j\omega})}$$

**Step 3:** Substitute back:
$$= \sum_k x[k] \, e^{-j\omega k} \, H(e^{j\omega}) = H(e^{j\omega}) \underbrace{\sum_k x[k] e^{-j\omega k}}_{X(e^{j\omega})}$$

$$\boxed{= X(e^{j\omega}) \cdot H(e^{j\omega})}$$

**Result:**
$$
\text{DTFT}\{x[n] * h[n]\} \longleftrightarrow X(e^{j\omega}) \cdot H(e^{j\omega})
$$

#### WHY is this the most important result?

**Computational revolution:** Direct convolution costs $O(N^2)$. FFT-based convolution costs $O(N \log N)$. For $N = 10^6$, that's the difference between hours and seconds.

```
Fast Convolution Algorithm:
1. Pad x[n] and h[n] to length L ≥ N₁ + N₂ - 1
2. X[k] = FFT{x[n]}
3. H[k] = FFT{h[n]}
4. Y[k] = X[k] × H[k]          ← pointwise multiply (CHEAP!)
5. y[n] = IFFT{Y[k]}
```

**Conceptual revolution:** Filtering becomes intuitive. Instead of thinking about convolution (hard), you think about multiplication in frequency (easy):
- Want to remove high frequencies? Make $|H(\omega)| = 0$ for high $\omega$
- Want to boost bass? Make $|H(\omega)|$ large for low $\omega$

---

### 3.6 Convolution's Effect: Magnitude × Magnitude, Phase + Phase

When you multiply two spectra:

$$|Y(e^{j\omega})| = |X(e^{j\omega})| \cdot |H(e^{j\omega})|$$
$$\angle Y(e^{j\omega}) = \angle X(e^{j\omega}) + \angle H(e^{j\omega})$$

**This is filtering in a nutshell:**
- $|H|$ acts as a **frequency-dependent volume knob** — turn it up or down at each frequency
- $\angle H$ adds **frequency-dependent delay** — if linear, no distortion; if non-linear, distortion

---

### 3.7 LTI Systems = Filters

For an $LTI$ system with impulse response $h[n]$:

$$\boxed{H(e^{j\omega}) = \text{DTFT}\{h[n]\}}$$
	
```
          ┌─────────┐
x[n] ──→  │ h[n]    │ ──→ y[n] = x[n] * h[n]
          │ (LTI)   │
          └─────────┘

In frequency domain:

X(e^{jω}) ──→ [× H(e^{jω})] ──→ Y(e^{jω}) = X(e^{jω}) · H(e^{jω})
```
	
**Filter types by $|H(e^{j\omega})|$ shape:**
```
Low-pass:      ████░░░░     Passes low ω, blocks high ω
               0   ωc  π

High-pass:     ░░░░████     Passes high ω, blocks low ω
               0   ωc  π

Band-pass:     ░░████░░     Passes a band, blocks rest
               0        π
```

---

### 3.8 Communication Channel Modeling

A channel is an LTI system that does three things:

| Effect | Time Domain | Frequency Domain | Fix at Receiver |
|--------|------------|-----------------|-----------------|
| **Filtering** | Convolution with $h[n]$ | Multiply by $H(e^{j\omega})$ | Equalizer (inverse filter) |
| **Delay** | Shift by $k$ | Multiply by $e^{-j\omega k}$ | Do nothing (linear phase = harmless) |
| **Attenuation** | Scale by $\alpha < 1$ | Scale by $\alpha$ | Amplify by $1/\alpha$ |

> **Key insight:** Delay is the *only* effect that doesn't need correction. This is why we require communication channels to have **linear phase** — any non-linear phase distortion cannot be undone by simple amplification.

---

### 3.9 Parseval's Theorem — Energy Conservation

$$\sum_{n=-\infty}^{\infty} |x[n]|^2 = \frac{1}{2\pi} \int_{-\pi}^{\pi} |X(e^{j\omega})|^2 \, d\omega$$

**WHY?** The $DTFT$ is a *unitary transformation* (up to the $1/(2\pi)$ factor) — it preserves energy. The total "energy" of the signal is the same whether you compute it sample-by-sample in time or frequency-by-frequency in the spectral domain.

**The term $|X(e^{j\omega})|^2$** is the ==Energy Spectral Density== — it tells you how much energy resides at each frequency.

**Concrete check with $\delta[n]$:**
- Time: $\sum|\delta[n]|^2 = 1$
- Frequency: $\frac{1}{2\pi}\int_{-\pi}^{\pi}|1|^2\,d\omega = \frac{1}{2\pi} \cdot 2\pi = 1$ ✓

---

### 3.10 Frequency Domain Derivative

$$n \cdot x[n] \xleftrightarrow{\text{DTFT}} j\frac{d}{d\omega}X(e^{j\omega})$$

**WHY?** Differentiate the DTFT definition:
$$\frac{d}{d\omega}\sum_n x[n]e^{-j\omega n} = \sum_n x[n](-jn)e^{-j\omega n} = -j \cdot \text{DTFT}\{n \cdot x[n]\}$$

Solve for the DTFT of $n \cdot x[n]$:
$$\text{DTFT}\{n \cdot x[n]\} = j\frac{d}{d\omega}X(e^{j\omega})$$

**Practical use:** Instead of computing $\sum_n n \cdot a^n e^{-j\omega n}$ from scratch, differentiate the known result $\frac{1}{1-ae^{-j\omega}}$ and multiply by $j$.

**Example:** DTFT of $n \cdot a^n u[n]$:
$$j \cdot \frac{d}{d\omega}\left[\frac{1}{1-ae^{-j\omega}}\right] = j \cdot \frac{-ae^{-j\omega} \cdot (-j)}{(1-ae^{-j\omega})^2} = \frac{-ae^{-j\omega}}{(1-ae^{-j\omega})^2}$$

---

### 3.11 Symmetry for Real Signals

**If $x[n]$ is real, then:**
$$X^*(e^{j\omega}) = X(e^{-\omega})$$

**Proof:**
$$X^*(e^{j\omega}) = \left[\sum_n x[n]e^{-j\omega n}\right]^* = \sum_n x[n]^* e^{+j\omega n} = \sum_n x[n] e^{-j(-\omega)n} = X(e^{-j\omega})$$

(Since $x[n]$ is real, $x^*[n] = x[n]$)

**Consequences:**
- $|X(e^{j\omega})|$ is **even** — symmetric about $\omega = 0$ (mirror image)
- $\angle X(e^{j\omega})$ is **odd** — anti-symmetric about $\omega = 0$ (flipped sign)

```
Magnitude (even):          Phase (odd):
    │  /│\                   │    /
    │ / │ \                  │   /
    │/  │  \                 │  /
────┼───┼───┼──── ω      ────┼──┼───┼──── ω
   -ω₀  0  ω₀             -ω₀ 0  ω₀
```

**Massive practical benefit:** For real signals, you only need to compute/store **half the spectrum** ($\omega \in [0, \pi]$). The other half is redundant. This is why "real $FFT$" algorithms exist — they're ~2× faster than complex $FFTs$.

---

## 4. How Everything Connects

```
                        ┌─────────────────────────┐
                        │     DTFT Definition      │
                        │  Σ x[n] e^{-jωn}        │
                        └────────────┬────────────┘
                                     │
                    ┌────────────────┼────────────────┐
                    ▼                ▼                ▼
            ┌──────────────┐ ┌──────────────┐ ┌──────────────┐
            │ Basic Signals│ │  Properties  │ │ Periodicity  │
            │ δ[n] → 1     │ │ Linearity    │ │ X(ω+2π)=X(ω)│
            │ aⁿu[n] → ... │ │ Time Shift   │ │ Only need    │
            │ 1 → 2πΣδ(ω) │ │ Freq Shift   │ │ [-π, π]      │
            │ u[n] → ...   │ │ Convolution  │ └──────────────┘
            └──────┬───────┘ │ Parseval     │
                   │         │ Derivative   │
                   │         │ Symmetry     │
                   │         └──────┬──────┘
                   │                │
                   └────────┬───────┘
                            ▼
                 ┌─────────────────────┐
                 │   Convolution Thm   │
                 │ x*h ↔ X·H          │
                 └──────────┬──────────┘
                            │
              ┌─────────────┼─────────────┐
              ▼             ▼             ▼
      ┌──────────────┐ ┌──────────┐ ┌──────────────┐
      │ LTI Filtering│ │ Fast     │ │Modulation &  │
      │ Y = X·H      │ │Convolution│ │ Communications│
      │ Low-pass     │ │ FFT→×→IFFT│ │ Freq Shift   │
      │ High-pass    │ │ O(NlogN)  │ │ Channel Model│
      └──────────────┘ └──────────┘ └──────────────┘
                            │
                            ▼
                   ┌──────────────────┐
                   │      DFT         │
                   │ Sampled DTFT     │
                   │ What computers   │
                   │ actually compute │
                   └──────────────────┘
```

---

## 5. Summary — The Essential Takeaways

### Transform Pairs to Remember

| Signal $x[n]$ | DTFT $X(e^{j\omega})$ | Condition |
|---------------|----------------------|-----------|
| $\delta[n]$ | $1$ | Always |
| $a^n u[n]$ | $\frac{1}{1-ae^{-j\omega}}$ | $\|a\| < 1$ |
| $-a^n u[-n-1]$ | $\frac{1}{1-ae^{-j\omega}}$ | $\|a\| > 1$ |
| $1$ | $2\pi \sum_k \delta(\omega - 2\pi k)$ | Distribution |
| $u[n]$ | $\frac{1}{1-e^{-j\omega}} + \pi\sum_k\delta(\omega-2\pi k)$ | Distribution |

### Properties to Remember

| Property | Time Domain | Frequency Domain |
|----------|------------|-----------------|
| Periodicity | — | $X(\omega+2\pi) = X(\omega)$ |
| Linearity | $\alpha_1 x_1 + \alpha_2 x_2$ | $\alpha_1 X_1 + \alpha_2 X_2$ |
| Time Shift | $x[n-k]$ | $e^{-j\omega k}X(\omega)$ |
| Freq Shift | $e^{j\omega_0 n}x[n]$ | $X(\omega - \omega_0)$ |
| Convolution | $x[n]*h[n]$ | $X(\omega) \cdot H(\omega)$ |
| Parseval | $\sum\|x[n]\|^2$ | $\frac{1}{2\pi}\int\|X(\omega)\|^2 d\omega$ |
| n-Mult | $n \cdot x[n]$ | $j\frac{d}{d\omega}X(\omega)$ |
| Real Signal | $x[n] \in \mathbb{R}$ | $X^*(\omega) = X(-\omega)$ |

### The Three Deep Insights

1. **Duality:** Localized in time ↔ spread in frequency, and vice versa. The impulse/constant pair is the extreme case.

2. **Convolution = Filtering:** The hardest operation in time (convolution) becomes the easiest in frequency (multiplication). This single fact enables all of modern DSP.

3. **Linear Phase = No Distortion:** A delay shifts phase linearly with frequency, preserving waveform shape. This is why we design phase-linear filters and require linear-phase communication channels.