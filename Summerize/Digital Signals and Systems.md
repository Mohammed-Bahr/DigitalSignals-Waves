---
Created: " 2026-04-07 22:02"
tags:
  - FACL
  - DigitalSignals
Source:
---

> [!quote] Imagination will often carry us to worlds that never were. But without it we go nowhere.
> — Carl Sagan

**"اللهم إني أسألك فهم النبيين، وحفظ المرسلين، والملائكة المقربين، اللهم اجعل ألسنتنا عامرة بذكرك، وقلوبنا بخشيتك، إنك على كل شيء قدير"**

# 1. Signal Fundamentals

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

# 2. Analog to Digital Conversion (A/D)
$$The Process: x(t) \rightarrow Sampling \rightarrow Quantization \rightarrow \bar{x}[n]$$
$$ x(t) \xrightarrow{\text{Sampling}} x_s(t) \xrightarrow{\text{Quantization}} \bar{x}[n] $$
The conversion process involves two main steps:

### Sampling
$$Continuous \xrightarrow{to} Discrete$$
Converts **continuous time** to **discrete time**
$$x(t) \xrightarrow{\text{Sampling}} x_s(t)$$

Mathematically, ideal sampling uses an impulse train (comb function):
$$p(t) = \sum_{n=-\infty}^{\infty} \delta(t - nT)$$

$$x_s(t) = x(t)p(t) = \sum_{n=-\infty}^{\infty} x(nT)\delta(t - nT)$$

### Quantization
$$Analog \xrightarrow{To} Digital$$
$$x_s(t) \xrightarrow{\text{Quantization}} \bar{x}[n]$$
Converts **analog** (continuous value) to **digital** (discrete value)
- Uses operational amplifiers as comparators
- Compares input signal $V^-$ with reference $V^+$
- **Quantization error** occurs (irreversible loss of information)

---

# 3. Discrete-Time Systems

## Definition
An operation that takes input signals and produces output signals:
$$x[n] \rightarrow \boxed{\text{System } T\{\cdot\}} \rightarrow y[n]$$

$$y[n] = T\{x[n], n\}$$

## Classification of Systems

### 3.1 By I/O Cardinality
- **SISO**: Single Input Single Output
- **SIMO**: Single Input Multiple Output  
- **MISO**: Multiple Input Single Output
- **MIMO**: Multiple Input Multiple Output

### 3.2 By Linearity
A system is **linear** if it satisfies:
1. **Superposition**: $T\{x_1[n] + x_2[n]\} = T\{x_1[n]\} + T\{x_2[n]\}$
2. **Scaling**: $T\{a \cdot x[n]\} = a \cdot T\{x[n]\}$

Combined:
$$T\{a_1x_1[n] + a_2x_2[n]\} = a_1T\{x_1[n]\} + a_2T\{x_2[n]\}$$

> **Note**: Real systems are rarely perfectly linear, but many are approximately linear.

**Non-linear**: Otherwise (e.g., containing higher powers, time-shifting operations)

>[!important] Note : if equation have constant term it will be not linear .

> [!important]+ Linear if:
> - Only **x[n], y[n]** with coefficients
> - No weird operations
> **❌ Immediately NON-LINEAR if you see:**
> 🚫 Powers:
> - $x^2[n],\ y^2[n]$
>     
> - $|x[n]|,\ \sqrt{x[n]}$
>   🚫 Multiplication between signals
$
x[n] \cdot y[n] 
$

### 3.3 By Time Invariance
- **Time Invariant**: $T\{x[n-k]\} = y[n-k]$
  - "Shifting in input leads to same shifting in output"
- **Time Variant**: Otherwise

**Common causes of time variance:**
1. Multiplication by $n$ (time-dependent coefficients)
2. Time scaling (e.g., $x[2n]$)
3. Time shifting operations in the system definition

### 3.4 By Causality
- **Causal**: Output does not depend on future input
- **Anti-causal**: Output depends on future input

**Examples:**
- $y[n] + 3y[n-1] = 2x[n] + 5x[n-4]$ → Linear & Time Invariant (LTI)
- $y[n] + 3y[n-1] = 2x[n] + 5x[n-4] + 7$ → Non-linear (constant term) & Time Invariant
- $y[n] + 3y[n-1] = n \cdot x[n] + 5x[n-4]$ → Linear & Time Varying
- $y[n] + 3y^2[n-1] = x[n] + 5x[n-4]$ → Non-linear & Time Invariant

> **Note**: In LTI systems, we call the shift value the **"order"**.

### 3.5 By Memory
- **Memoryless**: Output depends on current input only
- **Non-memoryless**: Output depends on past/future inputs

### 3.6 By Stability (BIBO)
- **Stable (BIBO)**: Bounded Input → Bounded Output
- **Unstable**: Otherwise
>[!Note] if function multiplied by $n$ it will be not stable .

---

## TRICKS of how to find the system classification :

### 1. Linearity
**Two deal-breakers:**
- ❌ **Constant term** (any standalone number like `+ 5` or `- 3`).  
  *Example:* `y[n] = 2x[n] + 4` → **Non-linear**.
- ❌ **Nonlinear operations on `x[n]` or `y[n]`**: powers (`x²[n]`, `y³[n-1]`), products (`x[n]·x[n-1]`), or transcendentals (`sin(x[n])`).

**✅ Linear if:** The equation is just sums of scaled versions of `x` and `y` at various shifts.  
*Note:* Coefficients like `n` or `n²` in front of `x[n]` are **fine** for linearity (they just affect time invariance).

---

### 2. Time Invariance
**Look for the index `n` appearing *outside* the brackets.**
- ❌ **Multiplication by `n`:** `n·x[n]`, `n·y[n-1]` → **Time-variant**.
- ❌ **Time scaling:** `x[2n]`, `x[n/2]` → **Time-variant**.
- ❌ **Time reversal (if part of system definition):** `x[-n]` → **Time-variant**.
- ❌ **Modulated shifts:** `cos(ωn)·x[n]` → **Time-variant**.

**✅ Time-invariant if:** The only places `n` appears are inside the brackets as `[n - k]` (a pure delay).

---

### 3. Causality
**Look for the largest positive offset on `x` or `y`.**
- ❌ **`x[n + k]` or `y[n + k]` where `k > 0`** → **Non-causal** (needs future input/output).
- ❌ **`y[n]` depends on `x[-n]`** (time reversal) → Usually **non-causal**.
- ❌ **`x[2n]`** (downsampling) → **Non-causal** (needs future samples to compute `y[0]`? Actually depends on context, but generally treated as non-causal in real-time).

**✅ Causal if:** All `x` and `y` terms are indexed as `[n - m]` where `m ≥ 0`.

---

### 4. Memory
**Look for `x[n]` alone.**
- **✅ Memoryless if:** The equation is **exactly** `y[n] = f(x[n])` with no shifts.  
  *Example:* `y[n] = x²[n]` is **memoryless** (non-linear, but still memoryless).
- **❌ Has memory if:** Any `x[n ± k]` with `k ≠ 0` appears, or **any `y[n ± k]` term exists**.

> Trick: If you see a `y` on the right side of the equation (difference equation), it **always** has memory.

---

### 5. Stability (BIBO) – Quick Heuristics
For "just looking" at the equation form (assuming causal LTI difference eq):

- ❌ **Multiplication by `n`:** e.g., `n·x[n]`. Bounded input (like a step) will produce an output that grows linearly → **Unstable**.
- ❌ **Coefficient > 1 in recursive feedback:** `y[n] = 2y[n-1] + x[n]`. The pole is at 2 (outside unit circle) → **Unstable**.
- ✅ **All `y` terms have coefficients < 1 in magnitude?** Not a guarantee (e.g., `y[n] = 0.5y[n-1] - 0.8y[n-2]` can be stable), but usually **stable** if it looks like a simple averaging filter.

> **The "n Rule" :** If `x[n]` or `y[n]` is **multiplied by `n`** (or any growing function of time), the system is **non-linear or time-variant** and **almost certainly unstable**.


---

# 4. Convolution Theory for LTI Systems

## Definition
For an LTI system, the relationship between input $x[n]$ and output $y[n]$ is described by convolution:

$$y[n] = x[n] * h[n] = \sum_{k=-\infty}^{\infty} x[k] \cdot h[n-k]$$

Where $h[n]$ is the **impulse response** of LTI system. (the output when input is $\delta[n]$).

## Finding Impulse Response Examples
Given a difference equation, set $x[n] = \delta[n]$ and solve:

##### **Example 1:**
$$y[n] = 3x[n] - x[n-2] + 4x[n-3]$$
$$h[n] = 3\delta[n] - \delta[n-2] + 4\delta[n-3]$$

Vector form: $h = [3, 0, -1, 4]$

> [!Note]
> we could adding more values at the edges like : $$h = [0,0,0,3,0,-1,4,0,0]$$
> but padding with zeros doesn't change anything so just remove it .

##### **Recursive Example 2:**
**The problem** — We're given a first-order difference equation:

$$y[n] = 1.1 \cdot y[n-1] + x[n]$$

and we want to find the **impulse response** $h[n]$, i.e., the output when the input is $x[n] = \delta[n]$ (a unit impulse), with zero initial conditions.

**The impulse response equation** becomes:

$$h[n] = 1.1 \cdot h[n-1] + \delta[n]$$

**Step 1 — Complementary (homogeneous) solution**

Set all inputs to zero ($\delta[n] = 0$):

$$h[n] - 1.1 \cdot h[n-1] = 0$$

Assume the solution has the form $h[n] = \alpha^n$, so $h[n-1] = \alpha^{n-1}$. Substituting:

$$\alpha^n - 1.1 \cdot \alpha^{n-1} = 0$$

Factor out $\alpha^{n-1}$:

$$\alpha^{n-1}(\alpha - 1.1) = 0$$

Since $\alpha^{n-1} \neq 0$, we get:

$$\alpha = 1.1$$

So the complementary solution is:

$$h_c[n] = A \cdot (1.1)^n$$

where $A$ is a constant determined by initial conditions.

**Step 2 — Finding A**

Apply the initial condition at $n = 0$. At $n = 0$, the impulse $\delta[0] = 1$ fires, and $h[-1] = 0$ (zero initial conditions):

$$h[0] = 1.1 \cdot h[-1] + \delta[0] = 1.1 \cdot 0 + 1 = 1$$

From $h[n] = A \cdot (1.1)^n$:

$$h[0] = A \cdot (1.1)^0 = A = 1$$

So $A = 1$.

**Final answer:**

$$\boxed{h[n] = (1.1)^n \cdot u[n]}$$

where $u[n]$ is the unit step (the solution only exists for $n \geq 0$).
![[FACL/DigitalSignals/Attachments/image.png]]
- **Key observations:**
		
	- Since $\alpha = 1.1 > 1$, the system is **unstable** — the impulse response grows exponentially and never decays.
	- If $\alpha$ were $< 1$ (e.g., $y[n] = 0.9 \cdot y[n-1] + x[n]$), the system would be **stable** and $h[n]$ would decay to zero.
	- The method used here is the **complementary solution** approach . Method 2 mentioned is the **Z-transform / moment generating function** approach, which gives the same answer more systematically.
	
## Proof of the Convolution Theorem

### Setup

We have an **LTI system** (Linear Time-Invariant):

$$x[n] \xrightarrow{\text{LTI}} y[n]$$

We denote the system operator as $\mathcal{T}{\cdot}$, so:

$$y[n] = \mathcal{T}{x[n]}$$

### Step 1 — Define the impulse response

The **impulse response** $h[n]$ is the output when the input is $\delta[n]$:

$$h[n] = \mathcal{T}{\delta[n]}$$
### Step 2 — Time invariance

Since the system is **time-invariant**, shifting the input shifts the output by the same amount:

$$h[n-k] = \mathcal{T}{\delta[n-k]}$$

That is, a delayed impulse $\delta[n-k]$ produces a delayed impulse response $h[n-k]$.

### Step 3 — Linearity (scaling)

Since the system is **linear**, we can scale both sides by any constant. Scaling by $x[k]$:

$$x[k]\cdot h[n-k] = \mathcal{T}{x[k]\cdot\delta[n-k]}$$

Here $x[k]$ is just a constant with respect to $n$, so it factors out of the operator.

### Step 4 — Linearity (superposition / summation)

Since the system is **linear**, we can sum over all values of $k$:

$$
\sum_{k=-\infty}^{\infty} x[k] \cdot h[n-k] = \mathcal{T}\left\{ \sum_{k=-\infty}^{\infty} x[k] \cdot \delta[n-k] \right\}
$$

### Step 5 — Simplify the right-hand side

Now use the **sifting property** of the impulse:

$$\sum_{k=-\infty}^{\infty} x[k]\cdot\delta[n-k] = x[n]$$

because $\delta[n-k] = 1$ only when $k = n$, and $0$ otherwise. So:
$$
\mathcal{T}\left\{ x[n] \right\} = y[n]
$$

### Step 6 — Conclusion

Putting it all together:

$$\sum_{k=-\infty}^{\infty} x[k]\cdot h[n-k] = \mathcal{T}{x[n]} = y[n]$$

Therefore:

$$\boxed{y[n] = x[n] * h[n] = \sum_{k=-\infty}^{\infty} x[k]\cdot h[n-k]}$$

This is the **convolution sum**, and it proves that **any LTI system is completely characterized by its impulse response** $h[n]$. Given $h[n]$, you can compute the output for _any_ input $x[n]$.

- Here's a flowchart summarizing the entire logical chain of the proof:**The big takeaway** is that the proof relies on exactly two properties of the system — and nothing else:
	![[FACL/DigitalSignals/Attachments/image-1.png]]
	- **Time invariance** lets you generalize from one impulse to a shifted impulse.
	- **Linearity** (scaling + superposition) lets you build any arbitrary signal $x[n]$ as a weighted sum of shifted impulses, and pass that sum through the system.

> The sifting property of $\delta[n]$ is what ties it together: any signal $x[n]$ can always be written as $\sum_{k} x[k],\delta[n-k]$, so the LTI machinery immediately gives you the convolution sum. Click any node to dive deeper into that step.

## Causality Condition for LTI
An LTI system is causal if:
$$h[n] = 0 \quad \text{for all } n < 0$$

**Proof:**
$$y[n] = \sum_{k=-\infty}^{\infty} h[k]x[n-k]$$
If $h[k] = 0$ for $k < 0$, then:
$$y[n] = h[0]x[n] + h[1]x[n-1] + h[2]x[n-2] + \dots$$
Output depends only on present and past inputs.

## BIBO Stability Condition
An LTI system is BIBO stable if:
$$\sum_{k=-\infty}^{\infty} |h[k]| < \infty \quad \text{(finite)}$$
>[!Note] if function multiplied by $n$ it will be not stable .

---

# 5. Properties of Convolution

## 1. Commutative (تبادلي)
$$x[n] * h[n] = h[n] * x[n]$$
$$\sum_{k=-\infty}^{\infty} x[k]h[n-k] = \sum_{k=-\infty}^{\infty} h[k]x[n-k]$$
> Any linear operation commutes with convolution (e.g., delay operations).
## 2. Associative (ترابطي)
$$(x[n] * h_1[n]) * h_2[n] = x[n] * (h_1[n] * h_2[n])$$

**Interpretation**: Cascaded systems can be combined into a single system with impulse response $h_1[n] * h_2[n]$.

## 3. Distributive over Addition
$$x[n] * (h_1[n] + h_2[n]) = x[n] * h_1[n] + x[n] * h_2[n]$$

**Interpretation**: Parallel systems can be combined by adding their impulse responses.

## 4. Identity Element
$$x[n] * \delta[n] = x[n]$$

---

# 6. Linear vs Circular Convolution

## Linear Convolution
Standard convolution for aperiodic signals:
$$y[n] = \sum_{k=-\infty}^{\infty} x[k]h[n-k]$$

>[!warning] **Size Rule**: If $x$ has length $N$ and $h$ has length $M$, then $y$ has length $N + M - 1$.


### Circular Convolution
Used for periodic/$DFT$ analysis:
$$x[n] * h[n] = \sum_{k=0}^{N-1} x[k]\cdot h[ \text{ }(n-k) \bmod N \text{ }]$$

**Calculation method**: Flip (reverse), shift circularly, multiply and sum.

---

# 7. Frequency Analysis

### Periodic Discrete-Time Signals
A signal $x[n]$ is periodic with period $N$ if:
$$x[n+N] = x[n] \quad \text{for some integer } N$$
>[!warning] The **fundamental period** is the least value of N.

- **Notes** :
	- to be periodic we should have $\pi$ as a factor .
		
	- $N=\frac{2\pi k}{w}$ should be an integer 
		
	- if signal starts form zero we can't say it is periodic it could be ==semi-periodic==. 
		
#### Periodicity Condition for Sinusoids:

> First what is **Sinusoids**  ?  $\longrightarrow$  it is like $Sin(wn)$ and $Cos(wn)$ or $e^{jwn} = cos(wn) + j \text{ }  sin(wn)$

For $\sin(\omega n)$ or $e^{j\omega n}$ to be periodic:
$$N = \frac{2\pi k}{\omega} \text{ must be an integer for some } k \in \mathbb{Z}$$
> [!note] **Note**: Not all continuous-time periodic signals remain periodic when discretized.

### Aliasing of DT Frequency
$$\sin(\omega n) = \sin(n(\omega + 2\pi k)) \quad \text{for all } k,n \in Z $$
Therefore: $\omega \equiv \omega + 2\pi k$

**Implication**: Frequencies are indistinguishable modulo $2\pi$. In DSP, we restrict analysis to:
$$\omega \in [-\pi, \pi]$$

> [!important] C/D Conversion in Frequency Domain
Sampling in time domain ($t = nT$) leads to periodicity in frequency domain with period $\Omega_s = \frac{2\pi}{T}$.																		


### Continuous to Discrete Conversion in Frequency Domain

Remember: C/D in ==time domain== involves:
$$x_s(t) = x(t) \cdot P(t) = \sum_{n=-\infty}^{\infty} x(nT) \cdot \delta(t - nT)$$

In ==Frec domain== :The Fourier transform of the sampled signal:
$$X_s(j\Omega) = \int_{-\infty}^{\infty} x_s(t) e^{-j\Omega t} dt$$


---

# 8. Transforms

## Fourier Transform of Basic Signals

#### 1. Impulse: $\delta[n]$
$$X(e^{j\omega}) = \sum_{n=-\infty}^{\infty} \delta[n] e^{-j\omega n} = e^{-j\omega(0)} = 1$$

#### 2. Right-sided Exponential: $x[n] = a^n u[n]$

$$X(e^{j\omega}) = \sum_{n=0}^{\infty} a^n e^{-j\omega n} = \frac{1}{1 - ae^{-j\omega}}, \quad |a| < 1$$

#### 3. Left-sided Exponential: $x[n] = -a^n u[-n-1]$

$$X(e^{j\omega}) = \frac{-ae^{j\omega}}{1 - ae^{j\omega}} = \frac{1}{1 - ae^{-j\omega}}, \quad |a| > 1$$


---
#### 4. Unit Step: $u[n]$

$$X(e^{j\omega}) = \sum_{n=0}^{\infty} e^{-j\omega n} = \frac{1}{1 - e^{-j\omega}} + \pi \sum_{k=-\infty}^{\infty} \delta(\omega - 2\pi k)$$

#### 5. Cosine: $\cos(\omega_0 n)$

$$X(e^{j\omega}) = \pi \sum_{k=-\infty}^{\infty} [\delta(\omega - \omega_0 - 2\pi k) + \delta(\omega + \omega_0 - 2\pi k)]$$

#### 6. Sine: $\sin(\omega_0 n)$

$$X(e^{j\omega}) = \frac{\pi}{j} \sum_{k=-\infty}^{\infty} [\delta(\omega - \omega_0 - 2\pi k) - \delta(\omega + \omega_0 - 2\pi k)]$$

---

## DTFT (Discrete-Time Fourier Transform)
DTFT of a discrete time signal $x[n]$ is given by:
$$Time \xrightarrow{to} Frequency $$
$$X(e^{j\omega}) = \sum_{n=-\infty}^{\infty} x[n]e^{-j\omega n}$$
>[!Warning] Using the **inverse DTFT** pair: $$\frac{1}{1 - ae^{-j\omega}} \xrightarrow{\mathcal{F}^{-1}} a^n u[n]$$

**Relationship to continuous FT**:
$$X(e^{j\omega}) = X_s(j \text{ } \frac{\omega}{T} ) \quad \text{where } \omega = \Omega T$$
 
 - Relation with Continuous-Time Fourier Transform
	- Discrete in time domain → Continuous in frequency domain
	- Continuous in time domain → Discrete in frequency domain

**Key Points**:
- $t$: time (continuous)
- $n$: time index (discrete, "normalized time")
- $\Omega$: angular frequency (rad/second) $\quad \text{where } \omega = \Omega T$
- $\omega$: radian frequency (normalized, rad/sample)
![[FACL/DigitalSignals/Attachments/image-2.png]]

### DTFT Properties

#### 1. Periodicity
$$X(e^{j(\omega + 2\pi)}) = X(e^{j\omega})$$

#### 2. Linearity
If $x[n] = \alpha_1 x_1[n] + \alpha_2 x_2[n]$, then:
$$X(e^{j\omega}) = \alpha_1 X_1(e^{j\omega}) + \alpha_2 X_2(e^{j\omega})$$

#### 3. Time Shift
$$x[n-k] \xrightarrow{DTFT}e^{-j\omega k} X(e^{j\omega})$$

This causes a **linear phase shift** (no phase distortion).

#### 4. Frequency Shift (Modulation)
$$e^{j \omega_0 n} x[n] \xleftarrow{\text{DTFT}} X(e^{j(\omega - \omega_0)})$$

This is used for modulation, where $f = \omega_0$ is the corner frequency.

#### 5. Convolution in Time Domain (Filtering)
If $y[n] = x[n] * h[n]$, then:
$$Y(e^{j\omega}) = X(e^{j\omega}) \cdot H(e^{j\omega})$$

This means: Convolution in time domain = Multiplication in frequency domain.
 
$$
x[n] * h[n] \longleftrightarrow X(e^{j\omega}) H(e^{j\omega})
$$

- $\rightarrow$ Noise is usually of higher frequency, so we use low-pass filter to remove noise.  
	
- $\rightarrow$ We pass signals on a low-pass filter before modulation so that multiple carrier frequencies won’t overlap.  

- **Effect of Convolution** $\rightarrow$ 
	- magnitude multiplication  
	- phase addition.  
	
> So, in LTI system, Convolution is called "*Filtering*".  
- Frequency response of LTI system = DTFT of impulse response $g$.

$$
\begin{array}{ccc}
x[n] & \longrightarrow & 
\boxed{\begin{array}{c} \text{LTI} \\ \text{system} \end{array}} \longrightarrow & y[n] = x[n] * h[n] \\[2em]
X(e^{j\omega}) & & & Y(e^{j\omega}) = X(e^{j\omega}) \cdot H(e^{j\omega})
\end{array}
$$
$\rightarrow$ If the phase of $H(e^{j\omega})$ is not linear, it will cause phase distortion which is an undesirable property.  
	
A **Channel** is :
```horizontal
- Delay 
---
- Filtertion
---
- Attenuation 
```

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
- **Imaginary signal** → DTFT is conjugate anti-sy
---

## DFT (Discrete Fourier Transform)
Since $\omega$ is continuous and $DTFT$ can be computed on computers, we use $DFT$.

In $DFT$, frequency is sampled. If the number of samples needed is N, the obtained frequencies are:
$$\omega_k = \frac{2\pi}{N}k, \quad k = 0, 1, 2, \ldots, N-1$$

To make frequency discrete for computer processing:

$$X[k] = X(e^{j\frac{2\pi k}{N}}) = \sum_{n=0}^{N-1} x[n]e^{-j\frac{2\pi}{N}kn}$$

Where:
- $N$ = number of frequency samples
- $k = 0, 1, 2, \dots, N-1$
- Frequencies obtained: $0, \frac{2\pi}{N}, \frac{4\pi}{N}, \dots, \frac{2\pi(N-1)}{N}$

**Note**: $x[n]$ is assumed non-zero only over $[0, N-1]$.
> To summarize it we now have a recorded voice in X[n] samples, and now we want to give it to user by DFT.
> 
> We using DFT over DTFT Because computers can't handle the continuous components of the DTFT.
---
### FFT (Fast Fourier Transform)
An algorithm to compute DFT with complexity $O(N \log N)$ instead of $O(N^2)$.

---

# Summary Table: System Properties

| Property | Condition |
|----------|-----------|
| **Linear** | Satisfies superposition and scaling |
| **Time Invariant** | $T\{x[n-k]\} = y[n-k]$ |
| **Causal** | $h[n] = 0$ for $n < 0$ |
| **Stable (BIBO)** | $\sum_{n=-\infty}^{\infty} \|h[n]\| < \infty$ |
| **Memoryless** | Output depends only on current input |

---