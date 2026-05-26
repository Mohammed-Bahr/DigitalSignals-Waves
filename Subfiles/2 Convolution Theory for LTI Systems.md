---
Created: " 2026-04-18 17:45"
tags:
  - FACL
  - DigitalSignals
Source:
Doc Lec order: LEC 2
---
> [!quote] One who is too insistent on his own views, finds few to agree with him.
> — Lao Tzu

**"اللهم إني أسألك فهم النبيين، وحفظ المرسلين، والملائكة المقربين، اللهم اجعل ألسنتنا عامرة بذكرك، وقلوبنا بخشيتك، إنك على كل شيء قدير"**

---

## Definition
For an $LTI$ system, the relationship between input $x[n]$ and output $y[n]$ is described by convolution:

$$y[n] = x[n] * h[n] = \sum_{k=-\infty}^{\infty} x[k] \cdot h[n-k]$$

Where $h[n]$ is the **impulse response** of $LTI$ system. (the output when input is $\delta[n]$).

## Finding Impulse Response Examples
Given a difference equation, set $x[n] = \delta[n]$ and solve:

##### **Example 1:**
Find the impulse Response of the System
![[Screenshot_20260506-144543.png]]
$$y[n] = 3x[n] - x[n-2] + 4x[n-3]$$
$$h[n] = 3\delta[n] - \delta[n-2] + 4\delta[n-3]$$

Vector form: $h = [3, 0, -1, 4]$

> [!Note]
> we could adding more values at the edges like : $$h = [0,0,0,3,0,-1,4,0,0]$$
> but padding with zeros doesn't change anything so just remove it .

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

# Properties of Convolution

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

# Linear vs Circular Convolution

## Linear Convolution
Standard convolution for aperiodic signals:
$$y[n] = \sum_{k=-\infty}^{\infty} x[k]h[n-k]$$

>[!warning] **Size Rule**: If $x$ has length $N$ and $h$ has length $M$, then $y$ has length $N + M - 1$.


## Circular Convolution
Used for periodic/$DFT$ analysis:
$$x[n] * h[n] = \sum_{k=0}^{N-1} x[k]\cdot h[ \text{ }(n-k) \bmod N \text{ }]$$

**Calculation method**: Flip (reverse), shift circularly, multiply and sum.
**Key Points:**
- Pad signals with zeros to convert linear convolution to circular convolution
- For signals of length N, circular convolution produces N output points

---

