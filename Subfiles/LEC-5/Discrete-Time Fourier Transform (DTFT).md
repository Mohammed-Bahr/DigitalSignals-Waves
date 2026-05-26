> [!quote] Conflict is the gadfly of thought. It stirs us to observation and memory. It instigates to invention. It shocks us out of sheeplike passivity, and sets us at noting and contriving.
> — John Dewey

**"اللهم إني أسألك فهم النبيين، وحفظ المرسلين، والملائكة المقربين، اللهم اجعل ألسنتنا عامرة بذكرك، وقلوبنا بخشيتك، إنك على كل شيء قدير"**

---
 
> [!quote]
> The DTFT is not just a formula—it's a lens through which discrete-time signals reveal their frequency character. Every property is a tool; every transform pair is a pattern to recognize. Master these, and you see structure where others see noise.


## Definition

### DTFT — Continuous-Frequency Transform
$$
X(e^{j\omega}) = \sum_{n=-\infty}^{\infty} x[n]e^{-j\omega n}
$$

The **DTFT** transforms a discrete-time signal $x[n]$ into a continuous, periodic function of frequency $X(e^{j\omega})$. It reveals how much of each frequency component is present in the signal.

The DTFT is the fundamental frequency-domain representation for discrete-time signals. Unlike the DFT (which is computable on a computer), the DTFT is a theoretical tool that gives us a complete frequency picture — it's the bridge between continuous-time Fourier analysis and discrete processing. All other discrete transforms (DFT, FFT, Z-transform) are derived from or related to the DTFT.

**How It Works**
- **Input**: Discrete-time signal $x[n]$ (sequence of numbers, possibly infinite-length)
- **Output**: Continuous function $X(e^{j\omega})$ defined for all $\omega \in \mathbb{R}$
- **Computation**: Sum over all $n$ of $x[n]$ weighted by complex exponentials $e^{-j\omega n}$
- **Convergence**: The sum must converge; this imposes conditions on $x[n]$ (absolute summability)

**Concrete Example — Delta Function**
$x[n] = \delta[n]$ (only nonzero at $n=0$)

$$X(e^{j\omega}) = \sum_{n=-\infty}^{\infty} \delta[n]e^{-j\omega n} = e^{-j\omega \cdot 0} = 1$$

**Interpretation**: An impulse contains all frequencies equally — it has a flat spectrum of magnitude 1 at all $\omega$.

> [!tip]- Algorithm — Computing DTFT by Definition
> ```
> Input: x[n] for n = 0, 1, ..., N-1 (or infinite), frequency ω
> Output: X(e^{jω})
> 
> Step 1: Initialize sum = 0
> Step 2: For each n in the sequence:
>           sum += x[n] × e^(-jωn)
> Step 3: Return sum
> ```

> [!warning]- Common Mistakes
> - **Mistake 1** — Forgetting that DTFT is periodic with period $2\pi$. It's easy to think $\omega$ can be any real number without repetition, but the spectrum repeats every $2\pi$.
> - **Mistake 2** — Ignoring convergence. The DTFT doesn't exist for all signals (e.g., $x[n] = 1$ for all $n$ doesn't have a convergent DTFT without using distributions).
> - **Mistake 3** — Mixing up capital/lowercase. $X$ is frequency domain; $x$ is time domain.

This is the foundation for DFT (Discrete Fourier Transform), Inverse DTFT, Convolution Theorem, and is a sampled version of the Continuous-Time Fourier Transform. Related to Z-Transform via $X(e^{j\omega}) = X(z)\big|_{z=e^{j\omega}}$.

---

### DFT — Sampled DTFT
$$
X[k] = X(e^{j\frac{2\pi k}{N}}) = \sum_{n=0}^{N-1} x[n]e^{-j\frac{2\pi}{N}kn}
$$

The **DFT** is the DTFT evaluated at $N$ equally-spaced frequency points: $\omega_k = \frac{2\pi k}{N}$ for $k = 0, 1, \ldots, N-1$. It discretizes the frequency axis, making computation feasible.

The DFT is what computers actually calculate. It transforms a finite-length sequence into a finite-length spectrum. The FFT algorithm computes the DFT efficiently in $O(N \log N)$ time, enabling all of modern digital signal processing — audio compression (MP3), image compression (JPEG), radar, communications, etc.

**How It Works**
- **Input**: Finite sequence $x[n]$ for $n = 0, 1, \ldots, N-1$
- **Output**: $N$ complex values $X[k]$ representing the spectrum at frequencies $\omega_k = \frac{2\pi k}{N}$
- **Key difference from DTFT**: DFT samples the continuous-frequency DTFT at discrete points

**Concrete Example — 4-Point DFT**
Let $x[n] = [1, 0, 0, 0]$ for $n = 0, 1, 2, 3$.

For $k = 0$: $X[0] = \sum_{n=0}^{3} x[n] e^{-j\frac{2\pi}{4}(0)n} = 1 + 0 + 0 + 0 = 1$

For $k = 1$: $X[1] = \sum_{n=0}^{3} x[n] e^{-j\frac{\pi}{2}n} = 1 + 0 + 0 + 0 = 1$

All $X[k] = 1$ — this makes sense because $x[n] = \delta[n]$ (zero-padded) has a flat DTFT!

> [!tip]- Algorithm — Direct DFT Computation
> ```
> Input: x[n] for n = 0, 1, ..., N-1
> Output: X[k] for k = 0, 1, ..., N-1
> 
> Step 1: For k = 0 to N-1:
>           X[k] = 0
>           For n = 0 to N-1:
>             X[k] += x[n] × e^(-j×2π×k×n/N)
> Step 2: Return X[0], X[1], ..., X[N-1]
> ```
	
> [!warning]- Common Mistakes
> - **Mistake 1** — Not realizing DFT is periodic: $X[k] = X[k + N]$. The DFT "wraps around" because it samples a periodic DTFT.
> - **Mistake 2** — Forgetting that the frequency index $k$ corresponds to $\omega_k = \frac{2\pi k}{N}$ radians. $k = 0$ is DC, $k = N/2$ (if N even) is Nyquist frequency.
> - **Mistake 3** — Using the naive DFT algorithm on large $N$. Always use the FFT instead — it's the same result but much faster.


---

## DTFT of Basic Signals

### 1. Impulse Signal

**Impulse**: $\delta[n] = \begin{cases} 1 & n=0 \\ 0 & \text{o.w.} \end{cases}$

$$ X(e^{j\omega}) = \sum_{n=-\infty}^{\infty} \delta[n]e^{-j\omega n} = e^{-j\omega(0)} = 1 $$

$$ \delta[n] \xleftrightarrow{\text{DTFT}} 1 $$

```horizontal 
![[../Attachments/image-6.png]]
$$
\text{TimeDomain}
$$
---
![[../Attachments/image-7.png]]
$$
\text{FrequencyDomain}
$$
```
	
An impulse (Kronecker delta) has a **flat spectrum** — it contains all frequencies with equal magnitude.

This is the frequency-domain characterization of the "perfect test signal." When you excite a system with $\delta[n]$, you're injecting all frequencies simultaneously. The output is the system's impulse response $h[n]$, whose DTFT gives the frequency response $H(e^{j\omega})$.

**How It Works**
- The sum collapses to one term: only $n=0$ contributes
- The complex exponential at $n=0$ is $e^0 = 1$
- Result: $X(e^{j\omega}) = 1$ for all $\omega$

**Concrete Example**
System identification: Feed $\delta[n]$ into an unknown filter. The output $y[n] = h[n]$ (impulse response). Take DTFT of $h[n]$ to get $H(e^{j\omega})$ — the complete frequency characterization of the filter.

> [!warning]- Common Mistakes
> - **Mistake 1** — Confusing $\delta[n]$ (discrete impulse) with $\delta(t)$ (continuous-time Dirac delta). They share the flat-spectrum property but are mathematically different objects.
> - **Mistake 2** — Forgetting that $|X(e^{j\omega})| = 1$ for all $\omega$, meaning the impulse has finite energy only if considered as a single sample.


---

### 2. Right-Sided Exponential

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

A right-sided exponential decays for $n \geq 0$ when $|a| < 1$. Its DTFT is a rational function with one pole. This is one of the most important transform pairs in DSP.

This transform pair appears constantly in system analysis. The impulse response of a first-order IIR filter is exactly $h[n] = a^n u[n]$ for $|a| < 1$. The pole location determines the system's frequency response shape.

**How It Works**
1. Start with the DTFT definition
2. Apply $u[n]$ to limit summation to $n \geq 0$
3. Recognize the infinite geometric series form
4. Convergence requires $|r| = |a e^{-j\omega}| = |a| < 1$
5. Apply geometric series formula


> [!tip]- Algorithm — Verifying DTFT of Exponential
> ```
> Input: pole location a, frequency ω
> Output: X(e^{jω})
> 
> Step 1: Check |a| < 1 (for convergence)
> Step 2: Compute X(e^{jω}) = 1 / (1 - a × e^{-jω})
> Step 3: For verification, sum first M terms:
>         sum = Σ_{n=0}^{M} a^n × e^{-jωn}
> Step 4: Compare sum to closed-form result
> ```

> [!warning]- Common Mistakes
> - **Mistake 1** — Trying to compute the DTFT when $|a| \geq 1$. The sum diverges; no DTFT exists.
> - **Mistake 2** — Forgetting that the pole at $z = a$ (inside the unit circle for $|a| < 1$) determines the frequency response peak location.
> - **Mistake 3** — Not recognizing this as the impulse response of a first-order recursive filter: $y[n] - ay[n-1] = x[n]$.


---

### 3. Left-Sided Exponential

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

A left-sided exponential grows toward $n \to -\infty$ but is truncated to exist only for $n \leq -1$. When $|a| > 1$, the sequence decays as $n \to -\infty$, making it summable.

This is the **non-causal** counterpart to the right-sided exponential. It demonstrates that the same functional form can arise from different time-domain signals with different regions of convergence (ROCs). This concept is crucial for the Z-transform and for understanding stability vs. causality.

**How It Works**
1. The unit step constraint $u[-n-1]$ gives $n \leq -1$
2. Substitute $n$ with negative indices; rewrite in terms of positive exponents
3. Factor out the common term
4. Recognize geometric series, now with $a^{-1}e^{j\omega}$
5. Convergence requires $|a^{-1}e^{j\omega}| = \frac{1}{|a|} < 1 \Rightarrow |a| > 1$

**Key insight**: This is *the same closed-form* as the right-sided exponential case, but with a different ROC ($|a| > 1$ vs. $|a| < 1$). In the Z-transform, these are two different ROCs for the same rational function.

**Code Implementation**

> [!warning]- Common Mistakes
> - **Mistake 1** — Confusing the convergence condition: right-sided needs $|a| < 1$; left-sided needs $|a| > 1$.
> - **Mistake 2** — Not realizing this is a non-causal signal (exists only for $n < 0$). Realizable systems need $h[n] = 0$ for $n < 0$.
> - **Mistake 3** — Thinking the DTFT doesn't exist because the signal grows for $n \to +\infty$. But the signal is zero there — it only exists for $n \leq -1$.


---

### 4. DTFT of Constant Signal $x[n] = 1$

![[FACL/DigitalSignals/Subfiles/Attachments/image.png]]

$$
X(e^{j\omega}) = 2\pi \sum_{k=-\infty}^{\infty}\delta(\omega-2\pi k)
$$

> [!bug] Correction
> **Was:** The original formula used lowercase $x(e^{jw})$ instead of $X(e^{j\omega})$.
> **Why it's wrong:** The DTFT output is always denoted with uppercase $X$, and the standard notation uses $\omega$ (Greek omega) rather than $w$ for the frequency variable.
> **Correct:** $X(e^{j\omega})$ with uppercase $X$ and Greek $\omega$.

A constant signal (DC, all ones for all $n$) has a DTFT consisting of **impulses in frequency** at integer multiples of $2\pi$. This is the dual of the time-domain impulse having a flat frequency spectrum.

This transform pair generalizes: pure DC ($\omega = 0$) in time maps to an impulse at $\omega = 0$ in frequency. Since DTFT is periodic with period $2\pi$, the impulses repeat at $2\pi k$. This establishes the fundamental duality: **localized in time $\leftrightarrow$ spread in frequency, and vice versa.**

**How It Works**
![[FACL/DigitalSignals/Subfiles/Attachments/image.png]]
- $x[n] = 1$ for all $n$ does not have an absolutely summable DTFT
- Using distribution theory, the DTFT becomes a train of frequency-domain impulses
- Each impulse has area $2\pi$, placed at $\omega = 0, \pm 2\pi, \pm 4\pi, \ldots$
- This is the spectral representation of a pure DC signal
	
**Interpretation**: A constant in time is the slowest-varying signal possible (infinite period), so all its "energy" concentrates at $\omega = 0$ (and periodic repetitions at $2\pi k$).

> [!warning]- Common Mistakes
> - **Mistake 1** — Trying to compute the infinite sum directly without using distribution theory. The sum diverges; you need the impulse train interpretation.
> - **Mistake 2** — Forgetting that the impulse areas are $2\pi$, not 1. This factor comes from careful derivation involving the inverse DTFT.
> - **Mistake 3** — Not connecting this to the DFT case: for a finite-length constant signal (all ones for $n = 0, \ldots, N-1$), the DFT is a single impulse at $k = 0$ with magnitude $N$.
 
---

### 5. DTFT of Unit Step $u[n]$

**Trial:**
$$
X(e^{j\omega}) = \sum_{n=-\infty}^{\infty} u[n]e^{-j\omega n}= \sum_{n=0}^{\infty}e^{-j\omega n}= 1+e^{-j\omega}+e^{-j2\omega}+\dots \quad , r = e^{-j\omega} , |r| = 1
$$

The geometric series has $|r| = |e^{-j\omega}| = 1$, so it doesn't converge in the usual sense. We need to use distribution theory.

**Proof:**
![[../Attachments/image-8.png]]
$$
X(e^{j\omega}) = \frac{1}{1-e^{-j\omega}} + \pi \sum^{\infty}_{k=-\infty} \delta(\omega-2\pi k)
$$

The unit step $u[n]$ is the sum of a constant ($\frac{1}{2}$) and a "causal signum" function. Its DTFT has two parts: a **rational continuous part** $\frac{1}{1-e^{-j\omega}}$ and an **impulse train** representing the DC component.

This transform appears frequently when analyzing switched-on signals or systems with DC bias. The decomposition into odd and even parts (constant + step) yields the two spectral components.

**How It Works**
1. The geometric series $\sum_{n=0}^{\infty} e^{-j\omega n}$ doesn't converge because $|e^{-j\omega}| = 1$
2. Decompose: $u[n] = \frac{1}{2} + \frac{1}{2}\text{sgn}[n]$ where $\text{sgn}[n]$ is the signum function
3. The DC term $\frac{1}{2}$ gives the impulse train with strength $\pi$
4. The causal alternating part gives $\frac{1}{1-e^{-j\omega}}$

At $\omega = 0$: The continuous part has a pole (denominator $\to 0$), integrated with the impulse to give a regularized result.

> [!warning]- Common Mistakes
> - **Mistake 1** — Applying the geometric series formula when $|r| = 1$. The formula requires $|r| < 1$; at $|r| = 1$, the series diverges in the ordinary sense.
> - **Mistake 2** — Omitting the impulse train term $\pi \sum_k \delta(\omega - 2\pi k)$. This is essential — without it, the inverse transform wouldn't recover $u[n]$.
> - **Mistake 3** — Expecting the DTFT to be smooth everywhere. It has both continuous and discrete (impulsive) components.


---

## DTFT Properties

## Property 1: DTFT is Periodic with Period $2\pi$

**Proof:**

$$X(e^{j\omega}) = \sum_{n=-\infty}^{\infty} x[n] e^{-j\omega n}$$

$$X(e^{j(\omega + 2\pi)}) = \sum_{n=-\infty}^{\infty} x[n] e^{-j(\omega + 2\pi)n}$$

$$= \sum_{n=-\infty}^{\infty} x[n] e^{-j\omega n} \cdot e^{-j2\pi n}$$
$$
= \sum_{n=-\infty}^{\infty} x[n] e^{-j\omega n} = X(e^{j\omega})
$$
Since $e^{-j2\pi n} = 1$ for all integer $n$, we get $X(e^{j(\omega+2\pi)}) = X(e^{j\omega})$ ∎

The DTFT spectrum repeats every $2\pi$ radians: $X(e^{j\omega}) = X(e^{j(\omega + 2\pi)})$ for all $\omega$. This means the spectrum is fully described by one period, conventionally $\omega \in [-\pi, \pi]$ or $[0, 2\pi]$.

Periodicity simplifies analysis — you never need to consider frequencies outside $[-\pi, \pi]$ because everything repeats. This is fundamentally different from the continuous-time Fourier transform (non-periodic spectrum). The $2\pi$ period comes from the discrete-time nature: the Nyquist-Shannon sampling theorem tells us $2\pi$ radians corresponds to the normalized sampling frequency.

**How It Works**
- The key fact: $e^{-j2\pi n} = \cos(2\pi n) - j\sin(2\pi n) = 1$ for all integer $n$
- When evaluating at $\omega + 2\pi$, the extra term $e^{-j2\pi n}$ always equals 1
- The sum is unchanged; the spectrum is periodic
- Primary period: $\omega \in (-\pi, \pi]$ or $[0, 2\pi)$
	
This periodicity means: if you plot $|X(e^{j\omega})|$ for $\omega \in [-3\pi, 3\pi]$, you'll see three identical copies.

> [!tip]- Algorithm — Exploiting Periodicity
> ```
> Input: X(e^{jω}) for ω ∈ [-π, π]
> Output: X(e^{jω}) for any ω
> 
> Step 1: Given any ω, compute ω_mod = ω mod 2π
> Step 2: If ω_mod > π, set ω_mod = ω_mod - 2π
> Step 3: Now ω_mod ∈ [-π, π]
> Step 4: Return X(e^{jω_mod})
> ```

> [!warning]- Common Mistakes
> - **Mistake 1** — Plotting the spectrum for $|\omega| > \pi$ without realizing it's a repeat. You're showing redundant information.
> - **Mistake 2** — Thinking $f_s/2$ (Nyquist in Hz) corresponds to $2\pi$. No — $\omega = \pi$ is Nyquist; $\omega = 2\pi$ is $f_s$.
> - **Mistake 3** — Forgetting this periodicity when upsampling or downsampling signals. The spectral copies overlap or shift.

---

### Signum Function

$$\frac{1}{2}\text{sgn}(t) \xrightarrow{\text{DTFT}} \frac{2}{1 - e^{j\omega}}$$

$$\text{sgn}[n] \xrightarrow{\text{DTFT}} \frac{2}{1 - e^{j\omega}}$$

> [!bug] Correction
> **Was:** The original had inconsistent notation, mixing $\text{sgn}(t)$ (continuous-time) with discrete-time DTFT.
> **Why it's wrong:** The DTFT applies only to discrete-time signals. For continuous-time, we'd use the Continuous-Time Fourier Transform (CTFT).
> **Correct:** The discrete-time signum is $\text{sgn}[n] = \begin{cases} 1 & n > 0 \\ 0 & n = 0 \\ -1 & n < 0 \end{cases}$

The signum function outputs the sign of its input: +1 for positive, -1 for negative. In discrete time: $\text{sgn}[n] = 1$ for $n > 0$, $-1$ for $n < 0$.

The signum helps construct odd signals and appears when expressing signals as even + odd parts. It's also useful for deriving step functions: $u[n] = \frac{1}{2}(1 + \text{sgn}[n])$.

---

## Property 2: DTFT is Linear

$$\text{DTFT}\{\alpha_1 x_1[n] + \alpha_2 x_2[n]\} = \alpha_1 \text{ DTFT}\{x_1[n]\} + \alpha_2 \text{ DTFT}\{x_2[n]\}$$

$$= \alpha_1 X_1(e^{j\omega}) + \alpha_2 X_2(e^{j\omega})$$

Linearity means the DTFT of a weighted sum equals the weighted sum of the individual DTFTs. This is the most fundamental property — it makes the DTFT a **linear operator**.

Linearity enables Superposition: decompose complex signals into simple ones, transform each, then combine. This is how we analyze complicated systems — break them into parts, handle each part separately, then superimpose the results.

**How It Works**
- The DTFT is defined by a sum, and sums commute with other sums
- Weighting terms can be factored in or out
- This holds for any finite linear combination

> [!warning]- Common Mistakes
> - **Mistake 1** — Not using linearity when you could. If a signal is a sum of known components, don't compute the DTFT from scratch — use known transform pairs and add.
> - **Mistake 2** — Applying linearity to nonlinear operations. DTFT of $x_1[n] \cdot x_2[n]$ is NOT the product of DTFTs (that's a different theorem).

---

## Property 3: Time Shift

$$\text{DTFT}\{x[n-k]\} = \sum_{n=-\infty}^{\infty} x[n-k] e^{-j\omega n}$$

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

##### Explanation

**Why does magnitude stay the same?** $e^{-j\omega k}$ is a complex exponential with magnitude exactly 1 for all $\omega$. Multiplying by it scales nothing — it only rotates the phase.

**Why is the phase shift linear?** The added phase $-\omega k$ is a straight line in $\omega$ with slope $-k$. This means every frequency gets shifted by the same _time delay_ $k$, so the signal's shape is preserved perfectly — just delayed. This is called **linear phase**, and it guarantees **no phase distortion**.

**Contrast with non-linear phase:** if different frequencies were delayed by different amounts, the signal would come out distorted even though the magnitudes are unchanged. Linear phase avoids this entirely.

Delaying a signal by $k$ samples in the time domain multiplies its spectrum by $e^{-j\omega k}$ in the frequency domain. This is purely a **phase shift** with magnitude unchanged — the signal shape is preserved.

This property guarantees that **pure delay is distortionless**. Real-world delays (transmission lines, buffer delays, reverb tails) shift every frequency component by the same time amount, preserving waveform shape. This is why "phase linear" filters are prized in audio — they delay all frequencies equally.

**How It Works**
- Substitute $m = n - k$ in the DTFT sum
- The exponent separates: $-j\omega(m+k) = -j\omega m - j\omega k$
- Factor out the constant $e^{-j\omega k}$
- The remaining sum is the original DTFT

> [!tip]- Algorithm — Applying Time Shift Property
> ```
> Input: Signal x[n] delayed by k samples → x[n-k]
> Output: DTFT of delayed signal
> 
> Step 1: Find DTFT of original signal X(e^{jω})
> Step 2: Multiply by e^{-jωk}
> Step 3: Result is DTFT{x[n-k]}
> 
> For magnitude: |X_delayed| = |X_original| (unchanged)
> For phase: ∠X_delayed = ∠X_original - ωk (linear phase shift)
> ```

> [!warning]- Common Mistakes
> - **Mistake 1** — Confusing the sign: $x[n-k]$ is a delay (positive $k$), yielding multiplication by $e^{-j\omega k}$ (negative sign in exponent).
> - **Mistake 2** — Expecting a magnitude change. The magnitude is unchanged — delay is distortionless.
> - **Mistake 3** — Not recognizing linear phase: the phase $\angle X = \text{original phase} - \omega k$ is a straight line with slope $-k$. This is the hallmark of pure delay.

---
 
## Property 4: Frequency Shift (Modulation)

$$e^{j\omega_0 n} x[n] \xleftrightarrow{\text{DTFT}} X(e^{j(\omega - \omega_0)})$$

> Multiplying by a complex exponential $e^{j\omega_0 n}$ in the **time domain** shifts the spectrum by $\omega_0$ in the **frequency domain**.

---

#### Visualization
![[FACL/DigitalSignals/Subfiles/Attachments/image-1.png]]
**Original spectrum $X(e^{j\omega})$** — centered at $\omega = 0$:

$$\underbrace{\frown}_{-2\omega_0 \quad 0 \quad 2\omega_0}$$

After modulation, the spectrum shifts — one copy moves to $+\omega_0$, one to $-\omega_0$:

$$\underbrace{\frown}_{-\omega_0} \qquad \underbrace{\frown}_{+\omega_0}$$

---

#### Why it works

Starting from the definition:

$$\text{DTFT}\{e^{j\omega_0 n} x[n]\} = \sum_{n=-\infty}^{\infty} x[n] e^{j\omega_0 n} e^{-j\omega n}$$

$$= \sum_{n=-\infty}^{\infty} x[n] e^{-j(\omega - \omega_0)n} = X(e^{j(\omega-\omega_0)})$$

The $e^{j\omega_0 n}$ term simply replaces $\omega$ with $\omega - \omega_0$ inside the DTFT sum — shifting the entire spectrum to the right by $\omega_0$.

---

#### Key takeaway

|Domain|Operation|
|---|---|
|Time|Multiply by $e^{j\omega_0 n}$|
|Frequency|Shift spectrum by $+\omega_0$|

This is the mathematical basis of **modulation** in communications — shifting a baseband signal up to a carrier frequency.

Multiplication by a complex exponential in time shifts the spectrum: $\omega \to \omega - \omega_0$. This is the inverse operation to time shifting: multiply in time domain ↔ shift in frequency domain.

This is the foundation of **modulation** — the technology that lets us send multiple signals over one channel (radio stations, Wi-Fi channels, etc.). Each signal occupies a different frequency band because we shift its spectrum to a different $\omega_0$ carrier frequency. It's also the basis for frequency translation in receivers (heterodyning).

**How It Works**
- Multiply $x[n]$ by $e^{j\omega_0 n} = \cos(\omega_0 n) + j\sin(\omega_0 n)$
- In the DTFT definition, this adds $+j\omega_0 n$ to the exponent
- The argument of the exponential becomes $-j\omega n + j\omega_0 n = -j(\omega - \omega_0)n$
- The resulting spectrum is $X(e^{j(\omega - \omega_0)})$ — shifted right by $\omega_0$


> [!tip]- Algorithm — Spectrum Shifting via Modulation
> ```
> Input: Spectrum X(e^{jω}), desired shift ω₀
> Output: Shifted spectrum X(e^{j(ω-ω₀)})
> 
> Step 1: Multiply x[n] by e^{jω₀n} in time domain
> Step 2: Compute DTFT of result
> 
> Alternative (if starting from spectrum):
>   Step 1: Replace ω with ω - ω₀ everywhere in X(e^{jω})
>   Step 2: This gives X(e^{j(ω-ω₀)})
> ```

> [!warning]- Common Mistakes
> - **Mistake 1** — Getting the sign wrong: multiplication by $e^{j\omega_0 n}$ shifts spectrum to $\omega - \omega_0$ (right), not $\omega + \omega_0$ (left).
> - **Mistake 2** — Forgetting that real signals use cosine modulation, which creates TWO spectral copies (at both $+\omega_0$ and $-\omega_0$), not one. This is because $\cos(\omega_0 n) = \frac{e^{j\omega_0 n} + e^{-j\omega_0 n}}{2}$.
> - **Mistake 3** — Not understanding aliasing: if you shift the spectrum too far (beyond $[-\pi, \pi]$), it wraps around due to periodicity — spectral aliasing.


---

## Property 6 — Energy Conservation (Parseval's Theorem)

The total energy of a discrete-time signal $x[n]$ is defined as:

$$E = \sum_{n=-\infty}^{\infty} |x[n]|^2$$

Parseval's theorem states that this energy can equivalently be computed in the **frequency domain**:

$$E = \frac{1}{2\pi} \int_{-\pi}^{\pi} |X(e^{j\omega})|^2 \, d\omega$$

where $X(e^{j\omega})$ is the DTFT of $x[n]$. The $\frac{1}{2\pi}$ factor accounts for the normalization of the DTFT integral over one period $[-\pi, \pi]$.

**Intuition:** Energy is preserved whether you "look" at the signal in time or in frequency. The squared DTFT magnitude $|X(e^{j\omega})|^2$ is called the **energy spectral density** — it tells you how energy is distributed across frequencies.

Parseval's theorem states that the total energy of a signal is the same whether computed in the time domain (sum of squared samples) or in the frequency domain (integral of squared spectrum magnitude). Energy is **conserved** under the DTFT.

This validates that the DTFT is an energy-preserving transform (up to a normalization constant). It also defines **energy spectral density** $S_{xx}(e^{j\omega}) = |X(e^{j\omega})|^2$ — the distribution of the signal's energy across frequency. This is foundational for power spectrum estimation and signal analysis.

**How It Works**
- Time domain: sum $|x[n]|^2$ over all $n$
- Frequency domain: integrate $|X(e^{j\omega})|^2$ over one period $[-\pi, \pi]$, divide by $2\pi$
- Both give the same number
- The $1/(2\pi)$ factor normalizes for the period length


> [!tip]- Algorithm — Computing Energy via Parseval
> ```
> Input: Signal x[n]
> Output: Total energy E
> 
> Method 1 (Time Domain):
>   Step 1: E = Σ_n |x[n]|²
> 
> Method 2 (Frequency Domain):
>   Step 1: Compute X(e^{jω}) = DTFT{x[n]}
>   Step 2: E = (1/2π) × ∫_{-π}^{π} |X(e^{jω})|² dω
> 
> For discrete (DFT-based) computation:
>   Step 1: X[k] = FFT{x[n]}
>   Step 2: E = (1/N) × Σ_k |X[k]|²
> ```

> [!warning]- Common Mistakes
> - **Mistake 1** — Forgetting the $1/(2\pi)$ factor when using the continuous DTFT formula. The integral of $|X|^2$ over $[-\pi, \pi]$ is NOT the energy — you must divide by $2\pi$.
> - **Mistake 2** — Confusing energy with power. Parseval applies to energy signals (finite total energy). For power signals (infinite energy, finite average power), you need a different formulation.
> - **Mistake 3** — Not verifying numerically. Always check that your time-domain and frequency-domain energies match — if they don't, you have an error somewhere.

---

## Property 7 — Frequency Domain Derivative (Multiplication by n)

Starting from the DTFT definition:

$$X(e^{j\omega}) = \sum_{n=-\infty}^{\infty} x[n] \, e^{-j\omega n}$$

Differentiate both sides with respect to $\omega$:

$$\frac{d}{d\omega} X(e^{j\omega}) = \sum_{n=-\infty}^{\infty} x[n] \cdot (-jn) \, e^{-j\omega n}$$

Factor out $-j$:

$$\frac{d}{d\omega} X(e^{j\omega}) = -j \sum_{n=-\infty}^{\infty} n \cdot x[n] \, e^{-j\omega n} = -j \cdot \text{DTFT}\{n \cdot x[n]\}$$

Rearranging to isolate the DTFT of $n \cdot x[n]$:

$$\boxed{\text{DTFT}\{n^{anything} \cdot x[n]\} = j^{anything} \frac{d}{d\omega} X(e^{j\omega})}$$

**Intuition:** Multiplying a signal by $n$ in the time domain corresponds to differentiating its spectrum with respect to $\omega$ and multiplying by $j$. This is the **dual** of the time-shifting property (shift in time → multiply by complex exponential in frequency).

The key takeaways:
![[FACL/DigitalSignals/Subfiles/Attachments/image-3.png]]

**Parseval:** You never have to sum $|x[n]|^2$ over all $n$ — you can integrate the energy spectral density $|X(e^{j\omega})|^2$ over $[-\pi, \pi]$ instead. Both give the same total energy.

**Derivative property:** The $j$ factor appears because differentiating $e^{-j\omega n}$ with respect to $\omega$ pulls out $-jn$, and when you move the $-j$ to the other side it becomes $+j$. This property is useful for finding the DTFT of signals like $n \cdot u[n]$ or $n \cdot a^n u[n]$ — instead of computing the transform from scratch, you differentiate a known DTFT and multiply by $j$.

Multiplying a signal by $n$ (the time index) corresponds to differentiating its spectrum: $n \cdot x[n] \leftrightarrow j \frac{d}{d\omega} X(e^{j\omega})$. This is the dual of the frequency-shift property.

This property provides a shortcut for computing DTFTs of signals like $x[n] = n \cdot a^n u[n]$ or $x[n] = n \cdot u[n]$. Instead of computing the sum directly, you differentiate a known transform. It also shows that multiplying by $n$ emphasizes later parts of the signal (larger $n$), which corresponds to emphasizing higher frequencies in the spectrum's derivative.

**How It Works**
1. Start with DTFT definition: $X(e^{j\omega}) = \sum_n x[n] e^{-j\omega n}$
2. Differentiate with respect to $\omega$:
   $\frac{dX}{d\omega} = \sum_n x[n] \frac{d}{d\omega}(e^{-j\omega n}) = \sum_n x[n] (-jn) e^{-j\omega n}$
3. Factor out $-j$: $= -j \sum_n n \cdot x[n] e^{-j\omega n}$
4. The sum is the DTFT of $n \cdot x[n]$
5. Solve: DTFT$\{n \cdot x[n]\} = j \frac{dX}{d\omega}$

> [!warning]- Common Mistakes
> - **Mistake 1** — Forgetting the $j$ factor. After differentiation, you MUST multiply by $j$ to get the correct DTFT.
> - **Mistake 2** — Sign errors in differentiation. Remember $\frac{d}{d\omega} e^{-j\omega n} = -jn e^{-j\omega n}$ (there's a $-jn$ factor).
> - **Mistake 3** — Not simplifying the final expression. The derivative often creates opportunities to factor and simplify.



---

## Recap + Property 8 — Symmetry Properties

First, the top line is the DTFT pair from Property 7 (recap):

$$n \cdot x[n] \xleftrightarrow{\text{DTFT}} j\frac{d}{d\omega}X(e^{j\omega})$$

And the two complex conjugate identities shown (used in the proof below):

$$(ab)^* = a^* b^* \qquad (a+b)^* = a^* + b^*$$

---

## Property 8 — Symmetry Properties

#### Definitions
![[FACL/DigitalSignals/Subfiles/Attachments/image-5.png]]

**Conjugate symmetric (even symmetric)** — a signal satisfies:

$$x[n] = x^*[-n]$$

This means if you flip the signal in time AND take its complex conjugate, you get back the same signal. For real signals this reduces to ordinary even symmetry: $x[n] = x[-n]$.

**Conjugate anti-symmetric (odd symmetric)** — a signal satisfies:

$$x[n] = -x^*[-n]$$

Same idea but with a sign flip. For real signals this reduces to odd symmetry: $x[n] = -x[-n]$.

---

#### Key theorem: The DTFT of a real signal is conjugate symmetric (even)

This is the most important result on this slide. If $x[n]$ is real, then:

$$X^*(e^{j\omega}) = X(e^{-j\omega})$$

meaning the spectrum at $+\omega$ is the complex conjugate of the spectrum at $-\omega$. This is why for real signals you only need to look at $\omega \in [0, \pi]$ — the negative-frequency half carries no new information.

---

#### Proof

Start with the DTFT definition:

$$X(e^{j\omega}) = \sum_{n=-\infty}^{\infty} x[n]\, e^{-j\omega n}$$

Since $x[n]$ is real, $x^*[n] = x[n]$. Now take the complex conjugate of the entire DTFT:

$$X(e^{j\omega}) = \sum_{n=-\infty}^{\infty} x[n] \, e^{-j\omega n}$$

Apply $(ab)^* = a^* b^*$ and $(a+b)^* = a^* + b^*$ to distribute the conjugate inside the sum:

$$X(e^{j\omega}) = \sum_{n=-\infty}^{\infty} x[n] \, e^{-j \omega n}$$

Since $x[n]$ is real, replace $x^*[n]$ with $x[n]$:

$$X^*(e^{j\omega}) = \sum_{n=-\infty}^{\infty} x[n] \, e^{+j\omega n} = \sum_{n=-\infty}^{\infty} x[n] \, e^{-j(-\omega)n} = X(e^{-j\omega})$$

$$\boxed{X^*(e^{j\omega}) = X(e^{-j\omega})}$$

This completes the proof.

![[FACL/DigitalSignals/Subfiles/Attachments/image-4.png]]

The practical punchline: whenever you see a spectrum plot of a real-world signal (audio, images, sensor data — all real-valued), the left half is always a mirror of the right half. That's this theorem at work. Engineers exploit it constantly — if you're running an FFT on a real signal with $N$ points, you only need to compute $N/2 + 1$ unique frequency bins.

For **real-valued signals**, the DTFT has built-in symmetry: the spectrum at frequency $\omega$ is the complex conjugate of the spectrum at frequency $-\omega$. This means: $|X(e^{j\omega})|$ is **even** (symmetric about $\omega=0$) and $\angle X(e^{j\omega})$ is **odd** (anti-symmetric about $\omega=0$).

This symmetry means **you only need to analyze half the spectrum** for real signals. The frequency range $[0, \pi]$ contains all unique information; $[-\pi, 0]$ is redundant. This cuts computation and storage in half for FFT implementations on real data. It's the reason real FFT algorithms exist — they exploit this redundancy.

**How It Works**
1. Real signals have $x[n] = x^*[n]$ (since imaginary part is zero)
2. Take the DTFT and conjugate it: $X^*(e^{j\omega})$
3. The conjugate flips the sign in the exponent: $e^{-j\omega n} \to e^{+j\omega n}$
4. Replace $+\omega n$ with $-(-\omega)n$
5. The sum becomes $X(e^{-j\omega})$
6. Result: $X^*(e^{j\omega}) = X(e^{-j\omega})$

**Consequences**
- $|X(e^{j\omega})| = |X(e^{-j\omega})|$ — magnitude is symmetric (even)
- $\angle X(e^{j\omega}) = -\angle X(e^{-j\omega})$ — phase is anti-symmetric (odd)

> [!warning]- Common Mistakes
> - **Mistake 1** — Plotting both positive and negative frequencies for real signals and thinking they contain different information. They're conjugates — you only need half the plot.
> - **Mistake 2** — Not using real FFT (rfft) for real-valued signals. You're computing twice as much as needed.
> - **Mistake 3** — Forgetting that this symmetry holds ONLY for real signals. Complex signals don't have this property — their spectra are generally asymmetric.

---


## Convolution Theorem (DTFT) — Property

### Statement

$$x[n] * h[n] \xleftrightarrow{\text{DTFT}} X(e^{j\omega}) \cdot H(e^{j\omega})$$

Convolution in time domain **=** Multiplication in frequency domain.

---

### Step-by-Step Proof

**Start:** Take the DTFT of the convolution sum.

$$\text{DTFT}\{x[n] * h[n]\} = \sum_{n=-\infty}^{\infty} \left[\sum_{k=-\infty}^{\infty} x[k] h[n-k]\right] e^{-j\omega n}$$

**Step 1 — Swap the order of summation** (both are absolutely convergent):

$$= \sum_{k=-\infty}^{\infty} x[k] \sum_{n=-\infty}^{\infty} h[n-k] e^{-j\omega n}$$

The outer sum over $k$ pulls $x[k]$ out since it doesn't depend on $n$.

**Step 2 — Substitute** $m = n - k$ in the inner sum, so $n = m + k$:

$$\sum_{n=-\infty}^{\infty} h[n-k] e^{-j\omega n} = \sum_{m=-\infty}^{\infty} h[m] e^{-j\omega(m+k)} = e^{-j\omega k} \sum_{m=-\infty}^{\infty} h[m] e^{-j\omega m}$$

The inner sum is exactly $H(e^{j\omega})$ by definition of the DTFT.

$$= e^{-j\omega k} \cdot H(e^{j\omega})$$

**Step 3 — Substitute back:**

$$= \sum_{k=-\infty}^{\infty} x[k] e^{-j\omega k} \cdot H(e^{j\omega})$$

Factor out $H(e^{j\omega})$ since it doesn't depend on $k$:

$$= H(e^{j\omega}) \underbrace{\sum_{k=-\infty}^{\infty} x[k] e^{-j\omega k}}_{X(e^{j\omega})}$$

**Result:**
$$
\text{DTFT}\{x[n] * h[n]\} \longleftrightarrow X(e^{j\omega}) \cdot H(e^{j\omega})
$$

### Why This Matters

|Domain|Operation|
|---|---|
|Time|Convolution $x[n] * h[n]$ (hard, infinite sum)|
|Frequency|Multiplication $X \cdot H$ (easy, pointwise)|

This is the foundation of **LTI system analysis** — instead of convolving a signal with an impulse response, you multiply their spectra in the frequency domain, then IDTFT back if needed.

The convolution theorem states that convolution in one domain equals multiplication in the other. For DTFT: $x[n] * h[n] \leftrightarrow X(e^{j\omega}) \cdot H(e^{j\omega})$. This is perhaps the single most important property for signal processing.

This theorem reduces an $O(N^2)$ convolution operation to an $O(N \log N)$ FFT-based computation: FFT both signals, multiply pointwise, IFFT. It also provides intuition: filtering is multiplication in frequency domain — you attenuate or amplify specific frequencies. Without this theorem, modern signal processing would be computationally infeasible.

**How It Works**
1. Convolution: $y[n] = \sum_k x[k] h[n-k]$ — nested sums, computationally heavy
2. DTFT converts convolution to multiplication: $Y = X \cdot H$
3. Multiplication is much faster: one multiply per frequency point
4. Inverse DTFT recovers $y[n]$ if needed

> [!tip]- Algorithm — Fast Convolution via FFT
> ```
> Input: x[n], h[n] (length N_x and N_h)
> Output: y[n] = x[n] * h[n]
> 
> Step 1: Choose FFT length L ≥ N_x + N_h - 1 (zero-pad)
> Step 2: Compute X[k] = FFT{x[n]} padded to length L
> Step 3: Compute H[k] = FFT{h[n]} padded to length L
> Step 4: Multiply: Y[k] = X[k] × H[k] for all k
> Step 5: Compute y[n] = IFFT{Y[k]}
> Step 6: Trim result to length N_x + N_h - 1
> 
> Complexity: O(L log L) vs. O(N_x × N_h) for direct convolution
> ```

> [!warning]- Common Mistakes
> - **Mistake 1** — Not zero-padding sufficiently. If $L < N_x + N_h - 1$, cyclic convolution occurs and results are wrong due to time-domain aliasing.
> - **Mistake 2** — Forgetting this is the "forward" direction: time-domain convolution → frequency-domain multiplication. The reverse (time-domain multiplication → frequency-domain convolution) is also true and equally important.
> - **Mistake 3** — Using direct convolution for long signals. Always use FFT-based fast convolution when $N$ exceeds a few dozen samples.

---

### Convolution Property
Frequency response of $LTI$ system = $DTFT$ of the impulse Response. 
$$
x[n] * h[n] \xleftrightarrow{\text{DTFT}} X(e^{j\omega})H(e^{j\omega})  
$$

This means:

> [!warning] **Convolution in time domain** becomes **multiplication in frequency domain**.

---

### Effect of Convolution

When multiplying in frequency domain:

- **Magnitude multiplication**
- **Phase addition**

So:

$$
|Y(e^{j\omega})| = |X(e^{j\omega})||H(e^{j\omega})|  
$$
$$
\angle Y(e^{j\omega}) = \angle X(e^{j\omega}) + \angle H(e^{j\omega})  
$$

When signals are convolved (or spectra multiplied), magnitudes multiply and phases add. This is the spectral interpretation of filtering: the output spectrum is the input spectrum weighted by the filter's frequency response.

This property lets us design filters by specifying their frequency response shape. A low-pass filter has $|H(e^{j\omega})| \approx 1$ for $|\omega| < \omega_c$ and $|H| \approx 0$ elsewhere — it "passes" low frequencies and attenuates high ones. The phase response $\angle H$ determines time-domain distortion characteristics.


---

### In LTI Systems

In an **LTI (Linear Time-Invariant) system**, convolution is called:

## Filtering

Because the system changes or filters certain frequencies of the input signal.

---

### Frequency Response of LTI System

The **frequency response** of an LTI system is:

$$
H(e^{j\omega}) = \text{DTFT of } h[n]  
$$

Where:

- $h[n]$ = impulse response of the system
- $H(e^{j\omega})$ = frequency response

---

### System Block Diagram
![[FACL/DigitalSignals/Subfiles/Attachments/image-2.png]]

Input:
$$
x[n] \quad \leftrightarrow \quad X(e^{j\omega})  
$$

Passes through system with impulse response:
$$
h[n]  
$$

Output:
$$
y[n] = x[n] * h[n]  
$$

In frequency domain:
$$
Y(e^{j\omega}) = X(e^{j\omega})H(e^{j\omega})  
$$

---

### Explanation

Imagine you send a signal into a system.

- In **time domain**, the system processes it using **convolution**.
- In **frequency domain**, it simply multiplies frequencies.

That's why frequency domain is easier to analyze.

Example:

- If $H(e^{j\omega})$ removes high frequencies → **Low-pass filter**
- If it removes low frequencies → **High-pass filter**

So convolution = filtering because the system selects frequencies.

In LTI systems, the impulse response $h[n]$ completely characterizes the system. Its DTFT $H(e^{j\omega})$ is the **frequency response** — it tells you how the system responds to each frequency component.

The frequency response is the most intuitive way to understand a system: it answers "what does this filter do?" A plot of $|H(e^{j\omega})|$ vs. $\omega$ shows gain (or attenuation) at each frequency. A plot of $\angle H(e^{j\omega})$ vs. $\omega$ shows phase shift. Together, they fully describe the system's effect on any input signal.

**How It Works**
1. Input $x[n]$ has spectrum $X(e^{j\omega})$
2. Filter has frequency response $H(e^{j\omega})$
3. Output spectrum: $Y(e^{j\omega}) = X(e^{j\omega}) H(e^{j\omega})$
4. Frequency-by-frequency multiplication
5. Inverse DTFT gives $y[n]$

> [!tip]- Algorithm — Analyzing LTI Systems
> ```
> Input: Impulse response h[n], input signal x[n]
> Output: Output signal y[n]
> 
> Step 1: Compute H(e^{jω}) = DTFT{h[n]}
> Step 2: Compute X(e^{jω}) = DTFT{x[n]}
> Step 3: Multiply: Y(e^{jω}) = X(e^{jω}) × H(e^{jω})
> Step 4: Compute y[n] = IDTFT{Y(e^{jω})}
> 
> Alternative (time domain):
>   Compute y[n] = x[n] * h[n] directly
> ```

> [!warning]- Common Mistakes
> - **Mistake 1** — Confusing impulse response $h[n]$ with frequency response $H(e^{j\omega})$. They're a transform pair — each uniquely determines the other, but they describe different things.
> - **Mistake 2** — Not understanding that $|H(e^{j\omega})|$ shows pass/stop bands: values near 1 mean frequencies pass; values near 0 mean frequencies are blocked.
> - **Mistake 3** — Forgetting that the phase response matters for time-domain shape. If you care about preserving waveform shape (not just frequency content), you need both magnitude and phase.


---

### Important Shortcut

Whenever you see:
$$
y[n]=x[n]*h[n]  
$$

Immediately think:
$$
Y(e^{j\omega})=X(e^{j\omega})H(e^{j\omega})  
$$

This is one of the most important ideas in Signals & Systems.

---

## Communication Channel Modeling

- Then this channel, what does it model?
	- at transmitter:
		- filtration
		- delay the signal
		- attenuation
	- at receiver:
		- de-modulation
		- amplify
		- de-attenuation
		- and do nothing for delay

A communication channel can be modeled as an LTI system with impulse response $h_{channel}[n]$ that represents the combined effects of filtering, delay, and attenuation. The received signal is $y[n] = x[n] * h_{channel}[n]$.

Understanding channel effects lets you design equalizers to compensate. Transmitted signals undergo: **filtration** (frequency-dependent attenuation), **delay** (time shift), and **attenuation** (overall magnitude reduction). The receiver must undo these effects: the delay is harmless (linear phase), but filtering and attenuation must be compensated.

**How It Works in the Channel**

|Effect|Time Domain|Frequency Domain|Receiver Compensation|
|---|---|---|---|
|Filtration|Convolution with $h[n]$|Multiplication by $H(e^{j\omega})$|Equalizer filter|
|Delay|Shift by $k$ samples|Multiply by $e^{-j\omega k}$|No action needed (linear phase)|
|Attenuation|Multiply by scalar $a$|Multiply by magnitude $a$|Amplify by $1/a$|

- The receiver does equalization (inverse filtering) to undo filtration
- Amplification compensates for attenuation
- Delay is left as-is (it doesn't distort the signal, just shifts it)


---


## Additional Symmetry Results

### DTFT of Purely Imaginary Signal
Is odd symmetric (conjugate anti-symmetric).

If $x[n]$ is purely imaginary ($x[n] = j\cdot x_I[n]$ where $x_I[n]$ is real), then the DTFT satisfies **conjugate anti-symmetry**: $X^*(e^{j\omega}) = -X(e^{-j\omega})$.

**How It Works**
- Start with $x[n] = j \cdot x_I[n]$ where $x_I[n]$ is real
- The DTFT: $X(e^{j\omega}) = j \cdot \text{DTFT}\{x_I[n]\}$
- Taking conjugate: $X^*(e^{j\omega}) = -j \cdot \text{DTFT}^*\{x_I[n]\} = -j \cdot X_I(e^{-j\omega})$
- But $X(e^{-j\omega}) = j \cdot X_I(e^{-j\omega})$
- Result: $X^*(e^{j\omega}) = -X(e^{-j\omega})$

**Consequences**
- $\text{Re}\{X(e^{j\omega})\}$ is odd (anti-symmetric)
- $\text{Im}\{X(e^{j\omega})\}$ is even (symmetric)
- Opposite of real-signal case


---

### DTFT of Even Symmetric Signal
Is pure real.

If a signal has even symmetry ($x[n] = x[-n]$), then its DTFT is **purely real**: $X(e^{j\omega}) = \text{Re}\{X(e^{j\omega})\}$ with zero imaginary part.

**How It Works**
- For even $x[n]$: $x[n] = x[-n]$
- Each pair $(x[n], x[-n])$ contributes: $x[n] e^{-j\omega n} + x[-n] e^{-j\omega(-n)}$
- Since $x[n] = x[-n]$: $= x[n](e^{-j\omega n} + e^{j\omega n}) = 2x[n]\cos(\omega n)$
- $\cos(\omega n)$ is real → sum is real
- Imaginary part vanishes in pairs

**Example**
$x[n] = \delta[n+1] + \delta[n] + \delta[n-1]$ (even symmetric)

$X(e^{j\omega}) = e^{j\omega} + 1 + e^{-j\omega} = 1 + 2\cos(\omega)$

This is purely real (no imaginary part).


---

### DTFT of Odd Symmetric Signal
Is pure imaginary.

> [!bug] Correction
> **Was:** The original stated "old symmetric" instead of "odd symmetric."
> **Why it's wrong:** "Old" is a typo; the correct term is "odd" (as in odd function symmetry).
> **Correct:** "odd symmetric signal" — a signal with $x[n] = -x[-n]$.

If a signal has odd symmetry ($x[n] = -x[-n]$), then its DTFT is **purely imaginary**: $X(e^{j\omega}) = j \cdot \text{Im}\{X(e^{j\omega})\}$ with zero real part.

**How It Works**
- For odd $x[n]$: $x[n] = -x[-n]$
- Each pair $(x[n], x[-n])$ contributes: $x[n] e^{-j\omega n} + x[-n] e^{-j\omega(-n)}$
- Since $x[-n] = -x[n]$: $= x[n](e^{-j\omega n} - e^{j\omega n}) = -2j\, x[n]\sin(\omega n)$
- This is purely imaginary (no real part)
- Real part vanishes in pairs

**Example**
$x[n] = \delta[n+1] - \delta[n-1]$ (odd symmetric)

$X(e^{j\omega}) = e^{j\omega} - e^{-j\omega} = 2j\sin(\omega)$

This is purely imaginary (no real part).

---

### Summary of Symmetry Properties

| Signal Type | Time Domain Property | Frequency Domain Property |
|-------------|---------------------|--------------------------|
| Real | $x[n] = x^*[n]$ | $X^*(e^{j\omega}) = X(e^{-j\omega})$ (conjugate symmetric) |
| Purely Imaginary | $x[n] = -x^*[n]$ | $X^*(e^{j\omega}) = -X(e^{-j\omega})$ (conjugate anti-symmetric) |
| Even | $x[n] = x[-n]$ | $X(e^{j\omega})$ is purely real |
| Odd | $x[n] = -x[-n]$ | $X(e^{j\omega})$ is purely imaginary |



