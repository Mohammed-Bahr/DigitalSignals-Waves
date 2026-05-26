---
Created: " 2026-04-08 10:37"
tags:
  - FACL
Source:
---
> [!quote] I have just three things to teach: simplicity, patience, compassion. These three are your greatest treasures.
> — Lao Tzu

**"اللهم إني أسألك فهم النبيين، وحفظ المرسلين، والملائكة المقربين، اللهم اجعل ألسنتنا عامرة بذكرك، وقلوبنا بخشيتك، إنك على كل شيء قدير"**

### **Question 1 Solution**

**a) System Classification**

- **(i)** $y[n] = 1 + 0.9x[n] + 0.1 \sum_{k=-\infty}^{n-3} y[k]$: This system is **non-linear** because it contains a constant term ('1'). It is also **time-varying** because the constant addition does not scale with input shifts.
- **(ii)** $y[n] + 3x[-n-1] = 0 \Rightarrow y[n] = -3x[-n-1]$: This system is **linear** as it satisfies scaling and superposition. However, it is **time-varying** due to the time-reversal $-n$ in the input.
- **(iii)** $y[n] - 2y[n-1] + x[n] = 0$: This is a linear difference equation with constant coefficients, making it a **Linear Time-Invariant (LTI)** system.

**b) Linear Convolutions** Given $x[n] = \delta[n] - 2\delta[n-1] + 3\delta[n-3]$, $y[n] = \delta[n] - 2\delta[n-2]$, and $h[n] = 0.5^n u[n]$.

- **(i)** $x[n] * y[n]$: Representing signals as vectors: $x = [1, -2, 0, 3]$ and $y = [1, 0, -2]$.
    - $k=0: 1 \cdot 1 = 1$
    - $k=1: 1 \cdot (-2) + 0 \cdot 1 = -2$
    - $k=2: 1 \cdot 0 + 0 \cdot (-2) + (-2) \cdot 1 = -2$
    - $k=3: 1 \cdot 3 + 0 \cdot 0 + (-2) \cdot (-2) = 7$
    - $k=4: 0 \cdot 3 + (-2) \cdot 0 = 0$
    - $k=5: (-2) \cdot 3 = -6$
    - **Result:** $x[n] ∗ y[n] = [1, -2, -2, 7, 0, -6]$.
- **(ii)** $h[n] * x[n]$: Using the distributive property and the identity $x[n] * \delta[n-k] = x[n-k]$:
    - $h[n] * \delta[n] - 2(h[n] * \delta[n-1]) + 3(h[n] * \delta[n-3])$
    - **Result:** $y[n] = 0.5^n u[n] - 2(0.5^{n-1} u[n-1]) + 3(0.5^{n-3} u[n-3])$.

---

### **Question 2 Solution**

**a) DTFT Calculation**

- **(i)** $x_1[n] = 0.2^n u[n] - 3^n u[-n-1]$:
    - Using standard pairs: $0.2^n u[n] \to \frac{1}{1-0.2e^{-j\omega}}$.
    - Using the left-sided exponential pair: $-3^n u[-n-1] \to \frac{1}{1-3e^{-j\omega}}$.
    - **Result:** $X_1(e^{j\omega}) = \frac{1}{1-0.2e^{-j\omega}} + \frac{1}{1-3e^{-j\omega}}$.
- **(ii)** $x_2[n] = 4^n u[-n] + 0.3^n u[n-1]$:
    - $4^n u[-n] = 4^n \delta[n] + 4^n u[-n-1] = 1 - ( -4^n u[-n-1] ) \to 1 - \frac{1}{1-4e^{-j\omega}} = \frac{-4e^{-j\omega}}{1-4e^{-j\omega}}$.
    - $0.3^n u[n-1] = 0.3(0.3^{n-1} u[n-1]) \to \frac{0.3e^{-j\omega}}{1-0.3e^{-j\omega}}$.
    - **Result:** $X_2(e^{j\omega}) = \frac{-4e^{-j\omega}}{1-4e^{-j\omega}} + \frac{0.3e^{-j\omega}}{1-0.3e^{-j\omega}}$.

**b) z-transform and ROC** (Using the principles detailed in)

- **(i)** $x_3[n] = 0.5^n u[n-1] - 3^n u[-n]$:
    - $0.5^n u[n-1] \to \frac{0.5z^{-1}}{1-0.5z^{-1}}$, ROC: $|z| > 0.5$.
    - $-3^n u[-n] = -1 - 3^n u[-n-1] \to -1 + \frac{1}{1-3z^{-1}} = \frac{3z^{-1}}{1-3z^{-1}}$, ROC: $|z| < 3$.
    - **Result:** $X_3(z) = \frac{0.5z^{-1}}{1-0.5z^{-1}} + \frac{3z^{-1}}{1-3z^{-1}}$, **ROC: $0.5 < |z| < 3$**.

---

### **Question 3 Solution**

**a) Impulse Response Analysis** Given $h[n] = \delta[n+1] - \delta[n-1]$.

- **(i) Spectra:** $H(e^{j\omega}) = e^{j\omega} - e^{-j\omega} = 2j \sin(\omega)$.
    - **Magnitude:** $|H(e^{j\omega})| = 2|\sin(\omega)|$.
    - **Phase:** Since $2j \sin(\omega) = 2\sin(\omega)e^{j\pi/2}$, the phase is **$\pi/2$** (for $\sin(\omega) > 0$).
- **(ii) Output for $x[n] = e^{j \frac{\pi}{4} n}$:** $y[n] = x[n] \cdot H(e^{j\omega})|_{\omega = \pi/4}$.
    - $H(e^{j\pi/4}) = 2j \sin(\pi/4) = j\sqrt{2}$.
    - **Result:** $y[n] = \sqrt{2} e^{j(\frac{\pi}{4} n + \frac{\pi}{2})}$.

**b) Frequency Response Analysis**

- **(i) Impulse Response:** $H(e^{j\omega}) = \frac{1}{(1-0.6e^{-j\omega})(1-0.9e^{-j\omega})}$. Using partial fractions:
    - $H(e^{j\omega}) = \frac{-2}{1-0.6e^{-j\omega}} + \frac{3}{1-0.9e^{-j\omega}}$.
    - **Result:** $h[n] = [3(0.9)^n - 2(0.6)^n] u[n]$. The system is **causal** because $h[n]=0$ for $n < 0$.
- **(ii) Output for $x[n] = \delta[n] - \delta[n-1]$:**
    - **Result:** $y[n] = h[n] - h[n-1]$.

