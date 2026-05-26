---
Created: " 2026-04-08 08:50"
tags:
  - FACL
  - DigitalSignals
Source: "[[Malak-DSP.pdf]]"
---
> [!quote] Fate is in your hands and no one elses
> — Byron Pulsifer

**"اللهم إني أسألك فهم النبيين، وحفظ المرسلين، والملائكة المقربين، اللهم اجعل ألسنتنا عامرة بذكرك، وقلوبنا بخشيتك، إنك على كل شيء قدير"**

---
# DSP - Digital Signal Processing Lecture Notes

---

## Page 1

**Page: DSP (lec) Date: 10 / 2 /2026**

Actuator (Sender)  Sensor (Receiver)  
  → Electric Signal  

From Ware  → in Channel (up)  

Analog & Analog System is also  

All Analog Systems were also → linear Circuits  
                 → Analog Electronics  

× Denoising (Filtering)  
× Modulation high Frequency cuts Signal & Signal loss  
× Amplification  
× Transmission System  

Digital Signal  → sampled & Quantized at finite  
         A of levels  

Digital Filters can be slow  

→ DSP is also useful in (automatic) Control.  
→ " " in Error detection & Correction. Programming wise  
→ " Storage & Processing & Compressed  
→ " Data Rate & Bits Modification  
→ " Transcription & Translation  

Nawar

---

## Page 2

**Page: Lec. Date: 10/ 2/ 2026**

→ Frequency Analysis (Spectral Analysis)  
[Arabic text, likely "تطبيقات تحليل التردد (تحليل الطيف)"]  
[Arabic text, likely "مثال: تحليل صوت"]  

Speech Recognition  
[Arabic text, likely "تطبيقات:"]  
$S_{\log_{10}}$ $S_{\log_{10}}$  

Signals → DSP → Image Processing → Computer Vision.  

# Python  
[Arabic text, likely "مثال:"]  

* Brain Signal & Speech Recog.  
  → Grad project  
  [Arabic text, likely "مشروع تخرج"]  
  - Networks are low level Signal Processing.  
  → Chat Bot Speech Recognition & generation.  

Nawar

---

## Page 3

**Page: Lec.  Date: 10/2 /2026**

\* lecture 1  

\rightarrow Signal : A physical quantity changing with time (or any independent variable).  

\circ It is a function, e.g. \( x(t) \).  
\( x : \mathbb{R} \rightarrow \mathbb{R} \)  
or  
\( x : \mathbb{R} \rightarrow \mathbb{C} \) (1)  

\circ Could be:  
\rightarrow Continuous time, Continuous Value (1)  
\rightarrow Discrete Time, Continuous Value (2)  
\rightarrow Continuous Time, Discrete Value (3)  
\rightarrow Discrete Time, Discrete Value (4)  

[Diagram: (2) shows vertical lines at \( t = 1, 2, 3, 4 \) (discrete time, continuous value); (3) shows rectangular pulses (continuous time, discrete value); (1) shows "Quantum Levels" with discrete vertical lines (continuous time, discrete value)]  

(4) \(\leftarrow\) "التحليل الرقمي للإشارات" (Digital Signal Analysis) \(\rightarrow\) (2)  
(1) \(\leftarrow\) "الإشارة الطبيعية" (Natural Signal)  
(3) \(\leftarrow\) "Communication"  

\rightarrow Discrete Value \(\rightarrow\) Digital  
\rightarrow Continuous Value \(\rightarrow\) Analog  

\* we are Concerned with discrete time signals  
\& systems (2) (4)  

Nawar

---

## Page 4

Page: Lec.  
Date: 10/ 2/ 2026  

→ Analog to digital Conversion  
# Continous to discrete (Sampling)  
# Analog to Digital (Quantization)  

$x(t) \rightarrow$ [Sampling] $\rightarrow$ [Quantization] $\rightarrow \tilde{x}[n]$  
$x_s(t)$ $x$  
$x[n]$  

* Sampling:  
$x(t) \rightarrow \bigotimes \rightarrow x_s(t)$  
$c(t)$  

[Diagram: Graph showing "Coch signal" (continuous signal) on the left, "Quantized Sampled Signal" in the middle with "approximation" (red text) and "x" markers, and "x[n]" on the right with n-axis labeled 0,1,2,3,4...]  

[Diagram: "Practical Sampler" with square pulses; "Ideal (Clock) Sampler" with arrows and a clock symbol]  

* Quantization is done using operational amplifiers or Comparators:  
[Diagram: Comparator symbol with $v^+$, $v^-$ inputs; output conditions: $v^+ = v^- \rightarrow \text{output} = 0$; $v^+ > v^- \rightarrow \text{output} \approx \infty$; $v^+ < v^- \rightarrow \text{output} \approx -\infty$]  

* Quantization error is irreversible.  

[Arabic text: "خطأ الكميّة غير قابلة للإلغاء (لأنه لا يمكن استعادة الإشارة الأصلية من مستويات الكميّة) ← 1 = output من Comparator عند مرجع من transistor" (Translation: "Quantization error is irreversible (because the original signal cannot be recovered from quantization levels) ← 1 = output from Comparator when reference from transistor")]  

[Arabic text: "مراجع الكميّة" (Translation: "Quantization references")]  

Nawar

---

## Page 5

**Page: Lec. Date: 10/2/2026.**

\* Ideal Sampling  
\( x(t) \rightarrow ( \times ) \rightarrow x_s(t) = \uparrow \uparrow \uparrow \uparrow \uparrow - - \)  
\(-2T\) \(-T\) \(0\) \(T\) \(2T\)  
Comb function  
impulse Train.  

\( p(t) = \sum_{n=-\infty}^{\infty} \delta(t - nT) \)  

\( x_s(t) = x(t)p(t) = x(t) \sum_{n=-\infty}^{\infty} \delta(t - nT) \)  
\( = \sum_{n=-\infty}^{\infty} x(nT) \delta(t - nT) \)  
\( = \sum_{n=-\infty}^{\infty} x[n] \delta(t - nT) \)  
\(\uparrow \uparrow \uparrow - \uparrow\)  
\(0\) \(T\) \(2T\) \(3T\)  
\(\to\) discrete time signal.  


\* Discrete Time System  
\(\to\) An operation that can take input signal(s) & produce output signal(s)  
Transformer  
\( x[n] \rightarrow T(\cdot) \rightarrow y[n] \)  

\( y[n] = T(x[n], \cdot) \).  


\(\to\) Classification of Systems:  
1) Based on Cardinality of I/O:  
\(\to\) SISO  
\(\to\) SIMO  
\(\to\) MISO  
\(\to\) MIMO.  

2) Based on linearity \(\to\) linear: \( T\{ \alpha_1 x_1(t) + \alpha_2 x_2(t) \} = \alpha_1 T x_1(t) + \alpha_2 x_2(t) \)  
\(\to\) Non - linear.  

\(\to\) in Nature even linear systems have a certain Threshold, where it is linear.  

Nawar

---

## Page 6

Page: Lec  
Date: 10/ 2 / 2026  

* Neural Networks are Piecewise Linear Systems  

* Properties of Linearity = Scaling & Superposition  

[3] Based on Time Invariance  
→ Time Invariant \( T[x(t-t_0)] = [x(t)]_0 \)  
→ Time Variant \( T[x(t), t] \neq \)  

* Examples:-  
\( y[n] = 3x[n] - 2x[n-5] \).  
\( y(t) = T[x(t)] \)  
Linear iff \( x \) up/down = yf  
\( y(t-t_0) = T[x(t-t_0)] \)  
→ Linear & Time invariant.  
Any input shift leads to output shift by the same value.  
b's obj "system"  
Test is \( x \to y \)  

\( y[n] = 3n^2 x[n] \rightarrow \) Linear, Time varying  

\( y[n] = 3x[n] - 2x[n-5] + 1 \rightarrow \) Non Linear, Time invariant  

\( y[n] = 3x^2[n] - 2x^3[n-5] \rightarrow \) non Linear & Time invariant  

\( y[n] = 3x[-n] - 2x[n-5] + 1 \rightarrow \) Non Linear & Time Varying.  

* in our Course, we consider only : LTI Systems  
(Linear & time invariant) Systems.  

* LTI System is described by difference equations  
that are linear with constant coefficients, &  
Homogenous.  

Nawar

---

## Page 7

Page: Lec  
Date: 10/2/2026  

→ Based on Causality → Causal : output doesn’t depend future input  
→ anti Causal or w.  

→ Based on Memorylessness → Memoryless : output only depends on current input.  
→ Memory or w.  

→ Based on Invertibility → Invertible Bijective  
→ Not  

*Function  
Injective one to one function  
Surjective m → ∴ Codomain ∫ f(x)  

→ Based on Stability → BIBO  

[Diagram: (No explicit diagram, but faint hand-drawn sketches appear on the lower half of the page, likely related to function or system concepts, though not clearly defined.)]  

Nawar

---

## Page 8

**Page: DSP (Dec) Date: 17 / 2 / 2026**

* Lecture 2  
→ Last lecture  
a Discrete Time System Classifications  

1 According to I/O Cardinality → SISO  
  ↳ SIMO  
  ↳ MISO  
  ↳ MIMO  

2 According to the linearity → linear (Superposition & Scaling)  
  ↳ Non-linear  

3 According to Time Invariance → time invariant  
  ↳ time Varying  

x[n] ⇒ x[n−k] then y[n] ⇒ y[n−k]  

Ex:- y[n] = 3x[n²]  
First:- y₃[n] = 3x[n²−k]  
Second:- y[n−k] = 3x[(n−k)²] ≠  
  then the system is time varying  

Ex:- y[n] + 3y[n−1] = 2x[n] + 5x[n−4]  

→ is a linear system & it is a time invariant system.  

y[n] + 3y[n−1] = 2x[n] + 5x[n−4] + 7.  

→ is non-linear & time invariant.  

y[n] + 3y[n−1] = n x[n] + 5x[n−4].  

→ is linear & Time varying.  

y[n] + 3y²[n−1] = x[n] + 5x[n−4].  

→ nonlinear & time invariant.  

Nawar

---

## Page 9

**Page:  Date: / /**

4 Causality → Causal: output doesn't depend on future input  
↳ antiCausal.  

Ex: \( y[n] = 3x[n+5] \) → non Causal  
\( 3y[n+1] = 3y[n] \) → Causal.  
\( 5y[n] = 4x[n] + 4x[n-3] \) → Causal.  

order, [illegible] LTI systems [illegible] Shift [illegible] [illegible] ←  
\( x \) [illegible] order [illegible] [illegible] \( y \) [illegible] order [illegible] [illegible]  

5 According to Memorylessness → Memoryless output only depends on  
↳ Non-Memoryless. current input  

An Example: Channel Between 2 Devices is an LTI System  
\( y[n] = a \cdot x[n-k] \)  
Ideal Channel is a LTI, Causal, Memoryless  

6 According to Stability → Stable. (BIBO Sense)  
↳ Unstable  
Bounded Input Bounded Output  
→ [illegible]  

* Convolution Theory of LTI Systems  
→ The relation between output & input of LTI  
Systems Could be described by a Convolution:  
\( y[n] = x[n] * h[n] \)  
\( = \sum_{k=-\infty}^{\infty} x[k] \cdot h[n-k] \)  
\( \sum_{-\infty}^{\infty} x[k] \cdot h[n+k] \) → Correlation.  

where \( h[n] \) is the impulse response of the LTI system.  

Nawar

---

## Page 10

Page: Lec  
Date: 17 / 2 / 2026  

→ Impulse response of a System is the output of the System when the input is an impulse.  

e.g: Find the Impulse response of the System:  
\( y[n] = 3x[n] - x[n-2] + 1x[n-3] \).  
\( h[n] = 3\delta[n] - \delta[n-2] + 1\delta[n-3] \).  

\( h = [3 \ 0 \ -1 \ 1] \)  
[Diagram: A graph with \( n \) on the x-axis and \( h[n] \) on the y-axis, showing a vertical line at \( n=0 \) with height 3, a vertical line at \( n=2 \) with height -1, and a vertical line at \( n=3 \) with height 1.]  


Ex2: Find the impulse response of the System:  
\( y[n] = 1.1y[n-1] + 2x[n] \).  

# Assuming the System is initially at rest  

\( h[n] = 1.1h[n-1] + \delta[n] \) ← Recursive Relation  

→ Solution ①  
\( h[0] = 1.1h[-1] + \delta[0] \)  
\( 1.1(0) + 1 = 1 \)  

\( h[1] = 1.1h[0] + \delta[1] \)  
\( 1.1(1) + 0 = 1.1 \)  

\( h[2] = 1.1h[1] + \delta[2] \)  
\( 1.1(1.1) + 0 = (1.1)^2 \)  

\( h[3] = 1.1h[2] + \delta[3] \)  
\( 1.1(1.21) + 0 = (1.1)^3 \)  

\( h[n] = (1.1)^n \)  


Nawar

---

## Page 11

**Page: Date: 17/2/2026**
Solution ① - Moment generating function.  
\( y[n] = 1.1 y[n-1] + x[n] \)  
\( h[n] = 1.1 h[n-1] + \delta[n] \)  

First Step: Complementary Solution, all inputs are set to zeros.  
\( h[n] - 1.1 h[n-1] = 0 \)  

* Set \( h[n] = \alpha^n \) where \( \alpha \) is constant.  
Then \( h[n-1] = \alpha^{n-1} \)  
\( \alpha^n - 1.1 \alpha^{n-1} = 0 \)  
\( \alpha^{n-1} (\alpha - 1.1) = 0 \)  
\( \alpha = 1.1 \)  

\( h_{cs}[n] = A \alpha^n \)  

Second Step - Particular Solution.  
\( y[n] = 1.1 y[n-1] + x[n] \)  
\( h[n] = 1.1 h[n-1] + \delta[n] \)  

Trial: \( h[n] = C \), \( h[n-1] = C \)  

\( C = 1.1 C + \delta[n] \)  

for \( n > 0 \), \( \Rightarrow \delta[n] = 0 \)  
\( C = 1.1 C \Rightarrow (1 - 1.1) C = 0 \)  
or \( C = 0 \)  
so \( h_{ps}[n] = 0 \), for \( n > 0 \), \( \Rightarrow h_{ps}[n] = \delta[n] \)  

Finally: \( h[n] = h_{cs}[n] + h_{ps}[n] \)  

\( h[n] = A (1.1)^n \)  

to get \( A \):  
\( h[0] = A (1.1)^0 \) \( A = h[0] = 1 \) so \( h[n] = (1.1)^n \)  

Nawar

---

## Page 12

**Page: Lec.  Date: 17/2/2026.**

Ex3: \( y[n] = 0.5 y[n-1] - 0.06 y[n-2] + x[n] \).  

# Assuming the system is initially at rest.  

*Solution:*  
→ Complementary Solution: \( y[n] - 0.5 y[n-1] + 0.06 y[n-2] = 0 \).  
\( y[n] = \alpha^n \)  
\( y[n-1] = \alpha^{n-1} \)  
\( y[n-2] = \alpha^{n-2} \)  

\( \alpha^n - 0.5 \alpha^{n-1} + 0.06 \alpha^{n-2} = 0 \).  
\( \alpha^{n-2} [\alpha^2 - 0.5 \alpha + 0.06] = 0 \).  

\( \alpha^2 - 0.5 \alpha + 0.06 = 0 \).  
\( (\alpha - 0.2)(\alpha - 0.3) \).  
\( \alpha_1 = 0.2 \), \( \alpha_2 = 0.3 \).  

\( y_{c.s}[n] = A (0.2)^n + B (0.3)^n \).  

→ Particular solution:  
\( y_{p.s}[n] = a n + b \)  
\( y_{p.s}[n-1] = a(n-1) + b \)  
\( y_{p.s}[n-2] = a(n-2) + b \)  

\( a n + b = 0.5(a(n-1) + b) - 0.06(a(n-2) + b) + \delta[n] \).  
Find \( a \) & \( b \).  
\( (a - 0.5a + 0.06a)n + (b + 0.5 - 0.5b - 0.12a + 0.06b) = \delta[n] \).  

Nawar

---

## Page 13

**Page: Lec. Date: 17/2/2026.**
where n=0:  
b + 0.5a = 0.5b - 0.12a + 0.06b = 1  
0.56b - 0.38a = 1 → □  

when n=-1:  
-a + 0.5a  

× Proof of Convolution theory.  
x[n] → [LTI] → y[n]  
y[n] = T{ x[n] }  
∴ h[n] = T{ δ[n] }  
∴ h[n-k] = T{ δ[n-k] } → bec. the system is Time invariant.  
∴ x[k] h[n-k] = T{ x[k] δ[n-k] } → bec the system is linear.  
∞  
∑ x[k] h[n-k] = T{ ∑ x[k] δ[n-k] }  
k=-∞ k=-∞  
= T{ x[n] }  
x[n] → [LTI] → ∞  
system. ∑ x[k] h[n-k] = y[n]  
k=-∞  
# y[n] = x[n] * h[n] = ∑ x[k] h[n-k]  
k=-∞  

Nawar

---

## Page 14

**Page: Date: 17/2/2026**

\* Properties of Convolution  

① Commutative: \( x[n] * h[n] = h[n] * x[n] \)  
\[
\sum_{-\infty}^{\infty} x[k] h[n-k] = \sum_{-\infty}^{\infty} h[k] x[n-k]
\]  

② Associative: \( (x[n] * h_1[n]) * h_2[n] = x[n] * (h_1[n] * h_2[n]) \)  
[Diagram: \( x[n] \rightarrow [h_1[n]] \rightarrow [h_2[n]] \equiv x[n] \rightarrow [h_1[n] * h_2[n]] \rightarrow y[n] \)]  

③ Distributive over addition:  
\( x[n] * (h_1[n] + h_2[n]) = x[n] * h_1[n] + x[n] * h_2[n] \)  
[Diagram: \( x[n] \rightarrow [h_1[n] + h_2[n]] \rightarrow y[n] \equiv x[n] \rightarrow [h_1[n]] \rightarrow (+) \rightarrow y[n] \) and \( x[n] \rightarrow [h_2[n]] \rightarrow (+) \rightarrow y[n] \)]  

④ Identity:  
\( x[n] * \delta[n] = x[n] \)  

Extension of property ①:  
→ Any linear operation is commutative with the Convolution.  

Example: \( x[n] * \delta[n-3] = \left[ x[n] * \delta[n] \right]_{n \rightarrow n-3} \)  
\[
= x[n-3] * \delta[n] = x[n-3]
\]  

Nawar

---

## Page 15

**Page: DSP (lec) Date: 24/2/2026**

Lecture (3)  
Previously on...  

Discrete time LTI Systems:  
\[ x[n] \rightarrow [h[n]] \rightarrow y[n] = x[n] * h[n] \]  

\[ x[n] * h[n] = \sum_{k=-\infty}^{\infty} x[k] h[n-k] \]  

\* its properties \*  

① Commutative:  
\[ x[n] * h[n] = h[n] * x[n] = \sum_{-\infty}^{\infty} h[k] * x[n-k] \]  

② Associative:  
\[ x[n] \rightarrow [h_1[n]] \rightarrow [h_2[n]] \rightarrow y[n] \]  
\[ \Rightarrow (x[n] * h_1[n]) * h_2[n] \]  
\[ x[n] \rightarrow [h_1[n] * h_2[n]] \rightarrow y[n] \]  
\[ \Rightarrow \text{Closure property} \]  
\[ x[n] * (h_1[n] * h_2[n]) \]  

③ Distributive over addition:  
\[ x[n] * (h_1[n] + h_2[n]) \]  
\[ = x[n] * h_1[n] + x[n] * h_2[n] \]  

[Diagram: \( x[n] \) splits into two paths: one through \( [h_1[n]] \), one through \( [h_2[n]] \), both outputs summed at \( \oplus \) to give \( y[n] \)]  

\[ \equiv \]  

[Diagram: \( x[n] \rightarrow [h_1[n] + h_2[n]] \rightarrow y[n] \)]  

Nawar

---

## Page 16

**Page: DSP Dec Date: 24/2/2026**

④ Identity element :  
$\delta[n] * x[n] = x[n]$  

⑤ Extension of Commutative Property & Associative Property :  
$\Rightarrow$ It extends to any linear operation  

$\star$ linear operations in Continuous time : $\frac{d}{dt}$, $\int$  

$\star$ linear operations in Discrete time : $+$, $\phi$ shifting  


$\star$ Example :  
$\square$ $x[n] = 3^n u[n]$, $h[n] = \delta[n] - \delta[n-1]$  
$\rightarrow$ Find : $x[n] * h[n]$  

$3^n u[n] * (\delta[n] - \delta[n-1])$  
$= 3^n u[n] * \delta[n] - 3^n u[n] * \delta[n-1]$  
$= 3^n u[n] - 3^{n-1} u[n-1]$  

other form :  
$\rightarrow = \delta[n] + 3^n u[n-1] - 3^{n-1} u[n-1]$  
$\rightarrow = \delta[n] + 3^{n-1} u[n-1] (3 - 1)$  
$= \delta[n] + 2 \cdot 3^{n-1} u[n-1]$  


[Diagram: A discrete-time signal $h[n]$ with two impulses: one at $n=0$ (value 1) and one at $n=1$ (value -1), labeled $h(n)$]  

Nawar

---

## Page 17

**Page: DSP (Dec) Date: 24/2/2026.**

2 \( x[n] = \delta[n] + 3\delta[n-1] + 2\delta[n-2] + \delta[n-3] \)  
\( h[n] = \delta[n] - \delta[n-2] \)  
→ Find: \( x[n] * h[n] \)  

Solution:  
\( x = [1, 3, 2, 1] \) (applying the rule)  
\( h = [1, 0, -1] \)  

\( x = [1, 3, 2, 1] \)  
\( [-1, 0, 1] \rightarrow [1, 3, 2, 1] \)  
\( [-1, 0, 0, 1] \)  

\( y[0] = 1 \times 1 = 1 \)  
\( y[1] = 1 \times 3 + 0 \times 1 = 3 \)  
\( y[2] = -1 + 0 + 2 = 1 \)  
\( y[3] = -3 + 0 + 1 = -2 \)  
\( y[4] = 6 \times 1 + (-1) \times 2 = -2 \)  
\( y[5] = 1 \times -1 = -1 \)  

\( y = [1, 3, 1, -2, -2, -1] \)  

Size(y) = Size(x) + Size(h) - 1  

\[ \begin{bmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ -1 & 0 & 1 & 0 \\ 0 & -1 & 0 & 1 \\ 0 & 0 & -1 & 0 \\ 0 & 0 & 0 & -1 \end{bmatrix} \begin{bmatrix} 1 \\ 3 \\ 2 \\ 1 \end{bmatrix} = \begin{bmatrix} 1 \\ 3 \\ 1 \\ -2 \\ -2 \\ -1 \end{bmatrix} \]  

[Diagram: A linear convolution diagram with "All possible shifts" and "Linear Convolution" labeled, showing a matrix multiplication structure for convolution.]  

Nawan

---

## Page 18

**Page: DSP Lec, Date: 24/2/2016**

- Output is longer than input → System has inertia  
- System has short term Memory.  

- Point Space Function  

[Boxed "B"] \( x[n] = 2^n u[n] \), \( h[n] = 0.3^n u[n] \).  
→ Find \( y[n] = x[n] * h[n] \)  

\( x[n] * h[n] = \sum_{k=-\infty}^{\infty} x[k] h[n-k] \)  

\( = \sum_{k=-\infty}^{\infty} 2^k u[k] \cdot 0.3^{n-k} u[n-k] \).  
[Boxed "k ≥ 0"] [Boxed "k ≤ n"]  

\( y[n] = \left( \sum_{k=0}^{n} 2^k \cdot 0.3^{n-k} \right) \cdot u[n] \).  

\( = 0.3^n \sum_{k=0}^{n} \left( \frac{2}{0.3} \right)^k \cdot u[n] \).  

\( (0.3)^n \left[ 1 + \frac{2}{3} + \left( \frac{2}{3} \right)^2 + \cdots + \left( \frac{2}{3} \right)^n \right] \cdot u[n] \).  

[Red hash] \( 1 + r + r^2 + \cdots + r^n = \frac{1 - r^{n+1}}{1 - r} \)  
→ \( |r| < 0 = \frac{1}{1 - r} \)  

\( y[n] = (0.3)^n \cdot \frac{1 - \left( \frac{2}{3} \right)^{n+1}}{1 - \frac{2}{3}} \cdot u[n] \).  


[Diagram: None]  
[Signature: Nawar]

---

## Page 19

**Page: DSP Lec. Date: 24/2/2026.**

\* Circular Convolution  

\[ x[n] \circledast_N h[n] = \sum_{k=0}^{N-1} x[k] \cdot h[(n-k) \mod N] \]  

Number of output elements  

\( 3 \mod 5 = 3 \)  
\( 7 \mod 5 = 2 \)  
\( -1 \mod 5 = 4 \)  
\( \to (-1) + 5 \mod 5 = 4 \)  

\* Example:  

\( x[n] = 3\delta[n] + 2\delta[n-1] + 1\delta[n-3] \)  
\( h[n] = 5\delta[n] - 2\delta[n-2] + 5\delta[n-3] \)  

\( \to \) Find:  

\( x[n] \circledast_4 h[n] \)  

[Diagram: A rectangular box with "3 2 0 4" (labeled as \( x[n] \)) and another box with "3 2 0 4" (labeled as \( h[n] \)), with a note "Elements: 4 = N" and a circular arrow indicating periodicity]  

\( y[0] = 1 \times 3 + 0 \times 4 + (-2) \times 0 + 2 \times 1 = 5 \)  
\( y[1] = 2 \times 1 + 0 \times 3 + (-2) \times 4 + 1 \times 0 = -6 \)  
\( y[2] = 1 \times 0 + 0 \times 2 + (-2) \times 3 + 1 \times 4 = -2 \)  
\( y[3] = 1 \times 4 + 0 \times 0 + (-2) \times 2 + 1 \times 3 = 3 \)  

\( \# \) Stop  

\( y = [5, -6, -2, 3] \)  

Elements: \( 4 = N \) (as circularity \( k \))

---

## Page 20

**Page: DSP Date: 24/2/2026**

-20 + (2 G 4) → then Shift outer Ring anti clockwise.  

\( y[0] = 1 \times 3 + 2 \times 0 + -2 \times 0 + 2 \times 1 = 5 \)  
\( y[1] = 0 \times 3 + 2 \times -2 + 0 \times 1 + 1 \times 2 = -6 \)  
\( y[2] = -2 \times 3 + 1 \times 4 + 0 \times 2 + 1 \times 0 = -2 \)  
\( y[3] = 1 \times 3 + -2 \times 2 + 1 \times 4 + 0 \times 0 = 3 \)  

Discrete Fourier & Circular Convolution of \( g \) & \( h \)  

* An LTI System is Causal if \( h[n] = 0 \) for all \( n < 0 \).  
Proof:  
\( y[n] = \sum_{k=-\infty}^{\infty} h[k] x[n-k] \)  
\( \because h[k] = 0 \) for \( k < 0 \)  
\( \therefore y[n] = \sum_{k=0}^{\infty} h[k] x[n-k] \)  
\( y[n] = h[0]x[n] + h[1]x[n-1] + h[2]x[n-2] + \dots \)  
\( \therefore y[n] \) does not depend on future \( x[n] \).  

* An LTI System is Stable if \( \sum_{k=-\infty}^{\infty} |h[k]| \) is finite.  

* An LTI System is Memoryless if \( h[n] = \delta[n] \).  

\( |f| = 1 \)  

[Diagram: A circular diagram with a ring (labeled "2 G 4") and an arrow indicating "Shift outer Ring anti clockwise".]  

Nawar

---

## Page 21

**Page: Dsp (lec) Date: 24/2/2026**

* Frequency Analysis of Signals & Systems  

* Periodic Signal:  
A signal \( x[n] \) is periodic with period \( N \) if:  
\( x[n+N] = x[n] \), for some integer \( N \)  
\( N \): Periodic length  
(we use the least value of \( N \) as the fundamental period)  

→ by recursion:  
\( x[n+2N] = x[n+N] = x[n] \)  

In general: \( x[n+kN] = x[n] \)  

Note: Some Continuous Periodic Signals are not periodic for the sampling rate choices.  

Ex: \( x[n] = \sin\left(\frac{7}{9}\pi n\right) \)  

→ Is \( x[n] \) periodic? What is its fundamental period?  

\( x[n+kN] = \sin\left(\frac{7}{9}\pi (n + kN)\right) \)  
\( = \sin\left(\frac{7}{9}\pi n + \frac{7kN}{9}\right) \)  

For \( x[n+kN] \) to be equal to \( x[n] \):  
\( \frac{7}{9}\pi kN \) should be a multiple of \( 2\pi \).  

→ The least value of \( kN \) is 18  
→ Fundamental period is \( \frac{18}{3} \).  

Nawar

---

## Page 22

**Page: DSP (lec) Date: 24/2/2026.**

General Rule:  
To be periodic, $\omega$ should have $2\pi$ as a factor.  
$N = \frac{2\pi k}{\omega}$ should be an integer.  
So, find $k$ such that $\frac{2\pi k}{\omega}$ is integer.  

$x[n] = \sin\left(\frac{\pi}{9} n\right)$  

$\omega = \frac{\pi}{9} \pi$  
$N = \frac{2\pi k}{\frac{\pi}{9}} = \frac{18k}{\pi}$  
$\rightarrow$ the least $k$ that gives integer $N$ is $7$.  
$\rightarrow$ so $N = 18$.  

[Diagram: None]  

Nawar

---

## Page 23

**Page: Dsp  (dec) Date: 3/3/2026**

\* Frequency Analysis of Signals & Systems  

\* Periodic Signal:  
is a Signal satisfying \( x[n+N] = x[n] \)  

Periodic \( \exists k \) such that \( \omega = 2\pi k \). Here \( \omega \) is signal frequency. Semi-Periodic \( \exists k \) such that...  

Examples:  
\( \sin \omega n \)  
\( \cos \omega n \)  
\( j = \sqrt{-1} \)  
\( e^{j\omega n} = \cos \omega n + j \sin \omega n \).  

\( \rightarrow \) Not in Real life alot  
But used to Simplify Analysis  

\* Periodicity of Sinusoids (discrete versions):  

\( \sin(\omega n) \) is Periodic if:  
we can find \( N = \frac{2\pi k}{\omega} \) such that \( k \) and \( N \) are integers. Its Periodic length is  
\( N = \frac{2\pi k_{\text{min}}}{\omega} \) where \( k \) is the least integer giving \( N \).  

\* Periodic length \( \equiv \) Fundamental Period.  

[Diagram: None]  

Nawar

---

## Page 24

**Page: DSP (dec) Date: 3 / 3 / 2026.**

\(\boldsymbol{\star}\) Aliasing of discrete Time Frequencies  

Note: \(\sin(\omega n + 2\pi k n) = \sin(\omega n) \quad \forall n \in \mathbb{Z}\)  

\(\rightarrow\) This means: \(\sin((\omega + 2\pi k)n) = \sin(\omega n)\).  
From this: \(\omega + 2\pi k \equiv \omega\), \(k \in \mathbb{Z}\).  

For example: the frequency \(\omega = \frac{7\pi}{4}\) rad is equivalent to \(\omega = \frac{7\pi}{4} + 2\pi = \frac{15\pi}{4}\).  
\(\boldsymbol{\oint}\) Also equivalent to \(\omega = \frac{7\pi}{4} + 4\pi = \frac{23\pi}{4}\), etc.  

In DSP, we restrict Frequency Analysis to Frequencies from \(-\pi\) to \(\pi\).  
\(\boldsymbol{\Rightarrow} \omega \in [-\pi, \pi]\). [Diagram: A horizontal axis labeled \(-\pi\), \(0\), \(\pi\) with a shaded region between \(-\pi\) and \(\pi\)]  

(quick justification of -ve frequencies)  
\(e^{j\omega n}\), \(j\) plus/minus sign  

\(\rightarrow \sin\omega n = \frac{e^{j\omega n} - e^{-j\omega n}}{2j}\)  

[Diagram: A horizontal axis labeled \(-2\pi\), \(-\pi\), \(0\), \(\pi\), \(2\pi\) with shaded regions at \(-2\pi\) to \(-\pi\) and \(\pi\) to \(2\pi\), and an arrow pointing left]  

From Fourier Series, Any Signal is a Superposition of \(\sin\) & \(\cos\).  

So, Aliasing can be done on any Signal.  

Nawar

---

## Page 25

**Page: DSP Lec₃ Date: 3/3/2026.**
* C/D Conversion in Frequency domain  
* Remember C/D in time domain  

[Diagram: Block diagram showing \( x(t) \) → (arrow) → \( x_s(t) \), with "Clock with Period \( T_s \)" labeled between \( x(t) \) and \( x_s(t) \).]  

\( x_s(t) = x(t) P(t) \)  
where \( P(t) = \sum_{n=-\infty}^{\infty} \delta(t - nT) \)  

[Diagram: Plot of \( x(t) \) (continuous wave) with \( t \) on x-axis, and \( x_s(t) \) (sampled impulses) with \( t \) on x-axis, labeled "Sample".]  

\( x_s(t) = x(t) \sum_{n=-\infty}^{\infty} \delta(t - nT) \)  
\( = \sum_{n=-\infty}^{\infty} x(nT) \cdot \delta(t - nT) \). \( \phi \) ideal sampling  

In Conclusion:  
\( x_s(t) = \sum_{n=-\infty}^{\infty} x[n] \delta(t - nT) \)  

* Taking Fourier Transform (CTFT)  
\( X_s(j\Omega) = \int_{-\infty}^{\infty} x_s(t) e^{-j\Omega t} dt \)  

\( = \int_{-\infty}^{\infty} \sum_{n=-\infty}^{\infty} x[n] \delta(t - nT) \cdot e^{-j\Omega t} dt \)  

\( = \sum_{n=-\infty}^{\infty} x[n] \int_{-\infty}^{\infty} \delta(t - nT) \cdot e^{-j\Omega t} dt \). \( \rightarrow \) Shifting Property  

Any integral contain \( \delta \) will be equal to one value.  

Nawar

---

## Page 26

**Page: DSP. (lec) Date: 3/ 3/ 2026**

$$= \sum_{n=-\infty}^{\infty} x[n] \cdot e^{j\omega n T} = X_s(j\Omega)$$  

$\rightarrow$ Setting $\omega = \Omega T$  

$$X_s(e^{j\omega}) = X_s\left(j\frac{\omega}{T}\right) = \sum_{n=-\infty}^{\infty} x[n] e^{-j\omega n}$$  

$\rightarrow$ Discrete Time Fourier Transform (DTFT) of $x[n]$.  

Scaled frequency $\omega$ is $\frac{\omega}{T}$ (scale $\rightarrow 1$) $\leftarrow$  
Version  

[Diagram: Sketch of frequency spectra with labels $-\Omega_m$, $\Omega_m$, $\Omega_s = \frac{2\pi}{T}$, $-\Omega_m T$, $\Omega_m T$, $2\pi$, "Continuous version" $X_s(e^{j\omega})$, "Discrete version" $f$, and arrows indicating scaling between continuous and discrete domains]  

$\ast$ DTFT  
$$X(e^{j\omega}) = \sum_{n=-\infty}^{\infty} x[n] e^{-j\omega n}$$  

$\ast$ Relation with the Continuous time case:  
Discrete $\omega = \Omega T \rightarrow$ in Frequency domain  
$t = nT \rightarrow$ in time domain  
Continuous $\rightarrow$ Discrete  

$n$: time index (normalized time)  
$\omega$: Rad frequency or Angular frequency or Normalized frequency.  

[Signature: "DSP Openheim" with arrow]  
Nawar

---

## Page 27

**Page: DSP - 30 Date: 3/3/2026**

→ Frequency analysis of discrete - time signals (Nyquist)  

- Periodic DT Signals  
  \(x[n + N]=x[n]\)  
  where \(N\in\mathbb{Z}\)  
  (Fundamental periodic length is the least value of \(N\))  

- Not all Sinusoids are Periodic DT Signals  
  \(L\sin\omega n\)  
  \(L\cos\omega n\)  
  \(L e^{j\omega n}=\cos\omega n + j\sin\omega n\)  
  → to be Periodic, we have to find \(k,N\in\mathbb{Z}\) satisfying:  
  \(N=\frac{2\pi k}{\omega}\)  

- Aliasing of DT Frequencies  
  Note: \(\sin\omega n=\sin(\omega n + 2\pi kn),\ \forall\ k,n\in\mathbb{Z}\)  
  \(\therefore\ \sin\omega n=\sin((\omega + 2\pi k)n)\)  
  hence \(\omega\equiv\omega + 2\pi k\)  
  [Diagram: A number line with points at \(-2\pi\), \(-\pi\), \(0\), \(\pi\), \(2\pi\); three semicircular shapes (peaks) are drawn above the line, centered at \(-2\pi\), \(0\), and \(2\pi\)]  

* DTFT of a discrete time signal \(x[n]\) is given by:  
  \(X(e^{j\omega})=\sum_{n = -\infty}^{\infty}x[n]e^{-j\omega n}\)  
  where \(X(e^{j\omega})=X_S(j\frac{\omega}{T})\)  

Nawar

---

## Page 28

**Page: Dsp (dec) Date: 3 / 3 / 2026**

[Diagram: Two frequency-domain plots labeled "Continuous" and "Discrete". The "Continuous" plot shows \( X_s(j\Omega) \) with lobes centered at \( -\Omega_m, \Omega_m \) and \( 2\pi \) (with \( \Omega = 2\pi f \) notation). The "Discrete" plot shows \( X(e^{j\omega}) \) with lobes centered at \( -2\pi, -\omega_m, \omega_m, 2\pi \), where \( \omega_m = \Omega_m T \). An arrow indicates the transition from continuous to discrete.]  

\( \omega = \Omega T \)  
\( t = nT \)  

\( f \): time (seconds)  
\( n \): time index (dimensionless). "Normalized time"  
\( \Omega \): angular frequency (\( 2\pi f \)) (rad/second). linear frequency  

\( \omega \): radian frequency (normalized radian frequency) (Rad) Rad/sample  

\(*\) Note: \( \omega \) is a continuous quantity (\( \omega \in [-\pi, \pi] \))  
So DTFT can’t be computed on Computers  

[Diagram: A sketch with "Discrete time" and "Continuous frequency" labels, showing a relationship between discrete-time and continuous-frequency domains.]  

So, use Discrete Fourier Transform (DFT) (N points)  

Nawar

---

## Page 29

**Page: Date: 3 / 3 / 2026**

* In DFT : Frequency is Sampled  
if the number of needed samples is \( N \),  
Obtained Frequencies are:  
\( 0, \frac{2\pi}{N}, \frac{2\pi}{2N}, \frac{6\pi}{N}, \dots, \frac{2\pi k}{N}, \frac{2\pi (N-1)}{N} \)  
\( \Rightarrow \omega_k = \frac{2\pi}{N} k \)  

DFT : \( X[k] = X(e^{j\frac{2\pi k}{N}}) = \sum_{n=0}^{N-1} x[n] e^{-j\frac{2\pi}{N}kn} \)  
Note : \( x[n] \) is non - zero over only a finite interval  
\( (n \in \{0,1,2,\dots,N-1\}) \).  

[Diagram: Signal → [DFT] → [DTFT] → [CTFT] → output  
Extra plotting]  

* Direct Computation Complexity is \( O(N^2) \).  
\( \Rightarrow \) To reduce Computation Complexity  

Fast Fourier Transform (FFT) is an algorithm  
to Compute \( [X[k] = 0,1,2,\dots,N-1] \) (DFT)  
in \( O(N\log N) \)  

\( \Rightarrow \) Translation.  

MIT  
Resources for DSP / Discrete time Signals  
& Systems  
by Openheim.  

Nawar

---

## Page 30

**Page: Dsp lec Date: 10/3/2026**
* lecture 5  

→ DTFT:  
\[ X(e^{j\omega}) = \sum_{n=-\infty}^{\infty} x[n] e^{-j\omega n} \]  
\(\omega \in [-\pi, \pi]\)  
→ Continous Variable  

→ DFT : Discrete Fourier Transform  
\[ X[k] = \sum_{n=0}^{N-1} x[n] e^{-j \frac{2\pi k}{N} n} \]  
Finite Samplescale = 9 (partial)  

* DTFT of basic signals  
① Impulse : \(\delta[n] \rightarrow 1\) (n=0)  
\[ \sum_{n=-\infty}^{\infty} X(e^{j\omega}) = \sum_{n=-\infty}^{\infty} \delta[n] e^{-j\omega n} = e^{-j\omega \cdot 0} = 1 \]  
[Diagram: Arrow from \(\delta[n]\) to 1, with \(n\) axis showing a spike at \(n=0\)]  

→ if the signal is Narrow in Time domain, Its Fourier will be wide.  

② Right sided exponential: \(x[n] = a^n u[n]\) ; \(a\) is a Complex quantity  
\[ X(e^{j\omega}) = \sum_{n=-\infty}^{\infty} a^n u[n] e^{-j\omega n} = \sum_{n=0}^{\infty} a^n e^{-j\omega n} = 1 + a e^{-j\omega} + a^2 e^{-j2\omega} + \cdots \]  
→ if geometric Series = ∞ No DTFT.  

The DTFT is defined only when: \(|a e^{j\omega}| < 1\)  
\[ |a| < 1 \]  
[Diagram: Box around \(|a| < 1\)]  

Nawar

---

## Page 31

**Page: DSP Lec Date: 10/3/2026**

in this case:  
\[ X(e^{j\omega}) = \frac{1}{1 - ae^{j\omega}} \]  

\[ a^n e^{-j\omega} \xrightarrow{\text{DTFT}} \frac{1}{1 - ae^{-j\omega}} \quad \text{when } |a| < 1 \]  

③ left sided exponential: \( X[n] = -a^n u[-n-1] \)  

\[ X(e^{j\omega}) = \sum_{n=-\infty}^{\infty} -a^n u[-n-1] e^{j\omega n}, \]  
\[ = \sum_{n=-\infty}^{-1} -a^n e^{-j\omega n} = -\sum_{n=-\infty}^{-1} a e^{-j\omega n} = -\left[ a^{-1} e^{j\omega} + a^{-2} e^{j2\omega} + \dots \right] \]  
\[ = -a^{-1} e^{j\omega} \left[ 1 + a^{-1} e^{j\omega} + a^{-2} e^{j2\omega} + \dots \right] \]  

DTFT exists only if: \( |a^{-1} e^{j\omega}| < 1 \implies |a^{-1}| < 1 \implies |a| > 1 \)  

in this case:  
\[ X(e^{j\omega}) = \frac{-a^{-1} e^{j\omega}}{1 - a^{-1} e^{j\omega}} \xleftarrow{\times \frac{-a e^{-j\omega}}{-a e^{-j\omega}}} \frac{-a e^{-j\omega}}{-a e^{-j\omega}} \]  
\[ = \frac{1}{1 - a e^{j\omega}} \]  

\[ -a^n u[-n-1] \xleftarrow{\text{DTFT}} \frac{1}{1 - a e^{j\omega}} \quad \text{when } |a| > 1 \]  

[Diagram: Arrows indicating DTFT relationships between time-domain sequences and frequency-domain expressions, with conditions on \( |a| \) for convergence.]  

Nawar

---

## Page 32

**Page: DSP (dec) Date: 10/3/2026**

④ DTFT of \( x[n] = 1 \) (Impulse Train):  
\( X(e^{j\omega}) = 2\pi \sum_{k=-\infty}^{\infty} \delta(\omega - 2\pi k) \).  
[Diagram: A horizontal axis labeled with \( -4\pi, -2\pi, 0, 2\pi, 4\pi \), with upward-pointing arrows at each multiple of \( 2\pi \), indicating impulses at these frequencies.]  


⑤ DTFT of \( u[n] \):  
Trial: \( X(e^{j\omega}) = \sum_{n=-\infty}^{\infty} u[n] e^{-j\omega n} = \sum_{n=0}^{\infty} e^{-j\omega n} = \frac{1}{1 - e^{-j\omega}} \) (|e^{-j\omega}| = 1)  
Cannot find it.  

So:  
\( X(e^{j\omega}) = \frac{1}{1 - e^{-j\omega}} + \pi \sum_{k=-\infty}^{\infty} \delta(\omega - 2\pi k) \).  
[Diagram: A vertical axis with a horizontal line at \( \frac{1}{2} \) (labeled \( \frac{1}{2} \text{sgn}(t) \)), a horizontal line at \( -\frac{1}{2} \), and a vertical line at \( 0 \) connecting \( -\frac{1}{2} \) to \( \frac{1}{2} \), representing the sign function.]  


⑥ \( \text{sgn}[n] \xleftrightarrow{\text{DTFT}} \frac{2}{1 - e^{-j\omega}} \).  


Nawar

---

## Page 33

**Page: DSP Lec Date: 10/3/2026**

\(\boldsymbol{\times}\) DTFT Properties  

\(\boldsymbol{[1]}\) DTFT is periodic with Period \(2\pi\).  
Proof: \(X(e^{j\omega}) = \sum_{n=-\infty}^{\infty} x[n] e^{-j\omega n}\)  

\(X\left(e^{j(\omega + 2\pi)}\right) = \sum_{n=-\infty}^{\infty} x[n] e^{-j(\omega + 2\pi)n}\)  

\(= \sum_{n=-\infty}^{\infty} x[n] e^{-j\omega n} e^{-j2\pi n}\)  

\(\boldsymbol{[Diagram:}\) A unit circle in the complex plane with a label \(e^{j\theta}\) (where \(e^{j\theta} = \cos\theta + j\sin\theta\)) and an angle \(\theta\) marked. \(\boldsymbol{]}\)  

\(= \sum_{n=-\infty}^{\infty} x[n] e^{-j\omega n} = X(e^{j\omega})\)  


\(\boldsymbol{[2]}\) DTFT is linear  
\(\text{DTFT}\left\{ \alpha_1 x_1[n] + \alpha_2 x_2[n] \right\} = \alpha_1 \text{DTFT}\left\{ x_1[n] \right\} + \alpha_2 \text{DTFT}\left\{ x_2[n] \right\}\)  

\(= \alpha_1 X_1(e^{j\omega}) + \alpha_2 X_2(e^{j\omega})\).  


\(\boldsymbol{[3]}\) Time Shift.  
\(\text{DTFT}\left\{ x[n - k] \right\} = \sum_{n=-\infty}^{\infty} x[n - k] e^{-j\omega n}\)  

Let \(m = n - k\), so \(n = m + k\).  

As \(n \to -\infty\), \(m \to -\infty\); as \(n \to \infty\), \(m \to \infty\).  

\(= \sum_{m=-\infty}^{\infty} x[m] e^{-j\omega (m + k)} = \sum_{m=-\infty}^{\infty} x[m] e^{-j\omega m} e^{-j\omega k}\)  

\(= e^{-j\omega k} \sum_{m=-\infty}^{\infty} x[m] e^{-j\omega m}\)  

\(= e^{-j\omega k} X(e^{j\omega})\).  


Nawar

---

## Page 34

**Page: DSP (lec) 3 Date: 10/3/2026**

\( x[n-k] \xleftarrow{\text{DTFT}} e^{-j\omega k} X(e^{j\omega}) \)  
→ mag = \( |X(e^{j\omega})| \) (no change)  
→ Phase: \( \angle e^{-j\omega k} X(e^{j\omega}) = \angle e^{-j\omega k} + \angle X(e^{j\omega}) = -\omega k + \angle X(e^{j\omega}) \)  
→ linear phase shift.  
(No phase Distortion to the signal)  


[Diagram: Frequency Shift (Modulation Property)]  
\( e^{j\omega_0 n} x[n] \xleftarrow{\text{DTFT}} X(e^{j(\omega - \omega_0)}) \)  
→ Modulation: \( \omega_0 \) is the carrier frequency.  
[Diagram: Spectrum shift: \( X(e^{j\omega}) \) centered at \( \omega = 0 \) shifts to \( \omega = \pm \omega_0 \) via modulation, with a low-pass filter shown.]  


[Diagram: Convolution in time domain (Filtering Property)]  
\( x[n] * h[n] = \sum_{k=-\infty}^{\infty} x[k] h[n-k] \)  

DTFT \( \left\{ x[n] * h[n] \right\} = \sum_{n=-\infty}^{\infty} \sum_{k=-\infty}^{\infty} x[k] h[n-k] e^{-j\omega n} \)  
\( = \sum_{k=-\infty}^{\infty} x[k] \sum_{n=-\infty}^{\infty} h[n-k] e^{-j\omega n} \)  
\( = \sum_{k=-\infty}^{\infty} x[k] \cdot e^{-j\omega k} H(e^{j\omega}) \)  
\( = H(e^{j\omega}) \sum_{k=-\infty}^{\infty} x[k] e^{-j\omega k} = H(e^{j\omega}) X(e^{j\omega}) \).  


Nawar

---

## Page 35

**Page: DSP Lec Date: 16/3/2026**

$x[n] * h[n] \longleftrightarrow X(e^{j\omega}) H(e^{j\omega})$  

Diagram: Frequency response $H(e^{j\omega})$ with a low-pass filter shape, labeled "Low pass filter" and "Cutoff Frequency" at $\omega_c$, showing $H(e^{j\omega})$ as 1 for $|\omega| < \omega_c$ and 0 otherwise. A high-pass filter is also sketched with a similar shape but inverted.] 

$\rightarrow$ Noise is usually of higher frequency, so we use low-pass filter to remove noise.  

$\rightarrow$ We pass signals on a low-pass filter before modulation so that multiple carrier frequencies won’t overlap.  

$\star$ effect of Convolution $\rightarrow$ magnitude multiplication  
$\downarrow$ phase addition.  

$\star$ So, in LTI system, Convolution is called "Filtering".  

$\star$ Frequency response of LTI system = DTFT of impulse response $g$.  

$x[n] \xrightarrow{\text{LTI system}} y[n] = x[n] * h[n]$.  
$X(e^{j\omega})$  
$y(e^{j\omega}) = X(e^{j\omega}) H(e^{j\omega})$  

$\rightarrow$ If the phase of $H(e^{j\omega})$ is not linear, it will cause phase distortion which is an undesirable property.  

$\rightarrow$ Delay (Linear phase shift).  

$\star$ A Channel is $\rightarrow$ Filtering  
$\downarrow$ Attenuation.  

Nawar

---

## Page 36

**Page: DSP Lec Date: 10/ 3/ 2026.**

[6] Energy Conservation (Parseval's Theorem).  
Signal energy of \( x[n] \) is:  
\[ E = \sum_{n=-\infty}^{\infty} |x[n]|^2 \]  
\[ = \frac{1}{2\pi} \int_{-\pi}^{\pi} |X(e^{j\omega})|^2 d\omega \]  
\( \rightarrow \) density per frequency.  

[7] Derivative in frequency domain.  
(multiplication by \( n \)).  
\[ X(e^{j\omega}) = \sum_{n=-\infty}^{\infty} x[n] e^{-j\omega n} \]  
\[ \frac{d}{d\omega} X(e^{j\omega}) = \sum_{n=-\infty}^{\infty} x[n] (-jn) e^{-j\omega n} = -j \sum_{n=-\infty}^{\infty} n x[n] e^{-j\omega n} \]  
\[ = -j \, \text{DTFT}\{ n \cdot x[n] \} \]  
\[ \boxed{ j \, \text{DTFT}\{ n \cdot x[n] \} = j \frac{d}{d\omega} X(e^{j\omega}) } \]  
\[ n x[n] \xleftarrow{\text{DTFT}} j \frac{d}{d\omega} X(e^{j\omega}) \]  

[8] Symmetry Properties.  
Note: A Signal is even symmetric (Conjugate Symmetric)  
iff: \( x[n] = x^*[-n] \).  

A Signal is odd symmetric (Conjugate Anti Symmetric)  
iff: \( x[n] = -x^*[-n] \).  

The DTFT of real Signal is Conjugate Symmetric (even).  
Proof: \( x[n] \) is real \( \rightarrow x^*[n] = x[n] \).  
\[ X(e^{j\omega}) = \sum x[n] e^{j\omega n} \rightarrow X^*(e^{j\omega}) = \sum x^*[n] e^{j\omega n} \]  
\[ = \sum_{n=-\infty}^{\infty} x[n] e^{j\omega n} = X(e^{-j\omega}) \]  
\[ X(e^{j\omega}) = X(e^{-j\omega}) \); is even Symmetric (Conjugate Symmetric).

---

## Page 37

**Page: DSP (Dec) Date: 10/3/2026**

- The DFT of pure imaginary signal is odd symmetric (Conjugate anti Symmetric)  
- The DFT of even Symmetric signal is pure Real  
- The DFT of odd Symmetric signal is pure imaginary  

Examples:  
\[
\text{DFT}\left\{\cos(\omega_0 n)\right\} = \frac{e^{j\omega_0 n} + e^{-j\omega_0 n}}{2}
\]  
\[
= \frac{1}{2} \text{DFT}\left\{e^{j\omega_0 n}\right\} + \frac{1}{2} \text{DFT}\left\{e^{-j\omega_0 n}\right\}
\]  
\[
= \frac{1}{2} \cdot 2\pi \sum_{k=-\infty}^{\infty} \delta(\omega - 2\pi k - \omega_0) + \frac{1}{2} \cdot 2\pi \sum_{k=-\infty}^{\infty} \delta(\omega - 2\pi k + \omega_0)
\]  
\[
= \pi \sum_{k=-\infty}^{\infty} \delta(\omega - \omega_0 - 2\pi k) + \delta(\omega + \omega_0 - 2\pi k) \quad \text{(pure Real)}
\]  

[Diagram: A frequency axis with impulses at \(\omega_0\) and \(-\omega_0\), labeled with "..." for periodicity, and a central impulse at 0]  

\[
\text{DFT}\left\{\sin(\omega_0 n)\right\} = \frac{\pi}{j} \sum_{k=-\infty}^{\infty} \delta(\omega - \omega_0 - 2\pi k) - \delta(\omega + \omega_0 - 2\pi k) \quad \text{(pure imaginary)}
\]  

Nawar

---

## Page 38

**Page: DSP Sec 3 Date: 12/3/2026**

DTFT  
Discrete Time Fourier Transform  
\( x[n] \xrightarrow{\text{DTFT}} X(e^{j\omega}) = \sum_{n=-\infty}^{\infty} x[n] e^{-j\omega n} \)  
→ Cont.  
→ Periodic \( 2\pi \)  

\( x[n] = \delta[n] \xrightarrow{\text{DTFT}} 1 \)  
\( x[n] = a^n u[n] \xrightarrow{\text{DTFT}} \frac{1}{1 - a e^{-j\omega}} \)  
\( |a| < 1 \)  

* Shift Property  
\( x[n] \xleftarrow{\text{DTFT}} X(e^{j\omega}) \)  
\( x[n - n_0] \xleftarrow{\text{DTFT}} X(e^{j\omega}) e^{\pm j\omega n_0} \)  

* Time Reverse Property  
\( x[-n] \xleftarrow{\text{DTFT}} X(e^{-j\omega}) \)  

* Multiplication Property  
\( n x[n] \xleftarrow{\text{DTFT}} j \frac{d}{d\omega} X(e^{j\omega}) \)  
* Diff. Property  
\( n^2 x[n] \xleftarrow{\text{DTFT}} j^2 \frac{d^2}{d\omega^2} X(e^{j\omega}) \)  

* Convolution Property  
\( x[n] * h[n] \xleftarrow{\text{DTFT}} X(e^{j\omega}) H(e^{j\omega}) \)  
\( y[n] = X(e^{j\omega}) H(e^{j\omega}) \xleftarrow{\text{I. DTFT}} \)  

[Diagram: A flowchart showing the relationship between \( x[n] \) and \( X(e^{j\omega}) \) via DTFT, with arrows indicating properties (shift, time reverse, multiplication, convolution) and intermediate steps labeled with mathematical expressions.]  

Nawar

---

## Page 39

**Page: DSP (Sec) Date: 12/ 3/ 2026**

x Continue on Sheet Questions:  
[4] \( x[n] = u[n-2] - u[n-6] \)  

\( x[n] = \delta[n-2] + \delta[n-3] + \delta[n-4] + \delta[n-5] \)  

[Diagram: Hand-drawn sequence plot with impulses at \( n=2,3,4,5 \) (labeled \( u[n-2] \) and \( u[n-6] \) with vertical lines at \( n=2,3,4,5 \) and a dashed line at \( n=6 \))]  

\( \text{DTFT} \)  

\( X(e^{j\omega}) = 1 \cdot e^{-2j\omega} + 1 \cdot e^{-3j\omega} + 1 \cdot e^{-4j\omega} + 1 \cdot e^{-5j\omega} \)  

[Diagram: Frequency-domain plot with impulses at \( \omega \) corresponding to \( n=2,3,4,5 \)]  


[5] \( X[n] = \left( \frac{1}{3} \right)^{|n|} u[n-2] \)  
→ Must use The Rule.  

\( X(e^{j\omega}) = \sum_{n=-\infty}^{\infty} \left( \frac{1}{3} \right)^{|n|} u[n-2] e^{-j\omega n} \)  

\( = \sum_{n=-\infty}^{-2} \left( \frac{1}{3} \right)^{|n|} e^{-j\omega n} \)  

\( = \sum_{n=-\infty}^{-2} \left( \frac{1}{3} \right)^{-n} e^{-j\omega n} = \left( \frac{1}{3} e^{j\omega} \right)^n \)  

\( = \sum_{n=-\infty}^{-2} \left( \frac{1}{3} e^{j\omega} \right)^n = \frac{ \left( \frac{1}{3} e^{j\omega} \right)^{-\infty} - \left( \frac{1}{3} e^{j\omega} \right)^{-1} }{ 1 - \frac{1}{3} e^{j\omega} } \)  

× Geometric Series Rule:  

\( \sum_{n=N_1}^{N_2} a^n = \frac{ a^{N_1} - a^{N_2+1} }{ 1 - a } \)  

\( \sum_{n=0}^{\infty} a^n = \frac{1}{1 - a} \)

---

## Page 40

**Page: DSP (Sec) Date: 12/3/2026.**

6 \( X(e^{j\omega}) = \frac{e^{j\omega} - \frac{1}{5}}{1 - \frac{1}{5}e^{-j\omega}} \), find \( x[n] \)??  

\( X(e^{j\omega}) = \frac{e^{j\omega}}{1 - \frac{1}{5}e^{-j\omega}} - \frac{\frac{1}{5}}{1 - \frac{1}{5}e^{-j\omega}} \)  

\( x[n] = \left( \frac{1}{5} \right)^{n-1} u[n-1] - \frac{1}{5} \cdot \left( \frac{1}{5} \right)^n u[n] \)  
\( = - \left( \frac{1}{5} \right)^{n+1} u[n] \)  


[Diagram: A piecewise function for \( X(e^{j\omega}) \):  
- \( 1 \) for \( \frac{\pi}{4} \leq \omega < \frac{3\pi}{4} \)  
- \( 0 \) for \( \frac{3\pi}{4} \leq \omega \leq \pi \)  
- \( 0 \) for \( -\pi \leq \omega \leq \frac{\pi}{4} \)]  

* Find \( x[n] \)  


* Inverse DTFT  

\( x[n] = \frac{1}{2\pi} \int_{<2\pi>} X(e^{j\omega}) e^{j\omega n} d\omega \)  

\( x[n] = \frac{1}{2\pi} \int_{\frac{\pi}{4}}^{\frac{3\pi}{4}} 1 \cdot e^{j\omega n} d\omega = \frac{1}{2\pi} \cdot \frac{e^{j\omega n}}{jn} \bigg|_{\frac{\pi}{4}}^{\frac{3\pi}{4}} \)  

\( = \frac{1}{2\pi} \cdot \frac{1}{jn} \left[ e^{j\frac{3\pi}{4}n} - e^{j\frac{\pi}{4}n} \right] \)  


Nawar

---

## Page 41

**Page: DSP &c Date: 12/3/2026**

[Diagram: A discrete-time signal plot labeled \( x[n] \) with vertical bars at integer \( n \)-values (e.g., \( n = -2, -1, 0, 1, 2, 3, 4, 5 \)) showing sample amplitudes.]  

1. \( X(e^{j0}) \)  
\( x(e^{j\omega}) = \sum_{n=-\infty}^{\infty} x[n] e^{-j\omega n} \)  
\( X(e^{j0}) = \sum_{n=-\infty}^{\infty} x[n] e^{-j0 \cdot n} = -1 + 1 + 2 + 1 + 1 + 2 + 1 + 1 = 6 \)  
\( X\text{DFT at frequency} = 0 \text{ is the summation of the signal itself} \).  

2. \( X(e^{j\pi}) \)  
\( X(e^{j\pi}) = \sum_{n=-\infty}^{\infty} x[n] e^{-j\pi n} \)  
\( = (-1)e^{-j\pi(-3)} + e^{-j\pi(-1)} + 2e^{-j\pi(0)} + 1e^{-j\pi(1)} + 1e^{-j\pi(2)} + 2e^{-j\pi(3)} + 1e^{-j\pi(4)} + e^{-j\pi(5)} - e^{-j\pi(7)} \)  

3. \( \int_{-\pi}^{\pi} X(e^{j\omega}) d\omega \) - Evaluate  
\( x[n] = \frac{1}{2\pi} \int_{-\pi}^{\pi} X(e^{j\omega}) e^{j\omega n} d\omega \)  
\( \int_{-\pi}^{\pi} X(e^{j\omega}) e^{j\omega n} d\omega = 2\pi x[n] \)  
at \( n = 0 \)  
\( \int_{-\pi}^{\pi} X(e^{j\omega}) d\omega = 2\pi x[0] = 2\pi \cdot 2 = 4\pi \).  

Nawar

---

## Page 42

**Page: Dsp (Sec) Date: 12/ 3 / 2026.**

[Diagram: A discrete-time signal plot labeled \( x[n] \) with vertical lines at integer time indices \( n = -3, -2, -1, 0, 1, 2, 3, 4, 5, 6 \) (some indices have vertical bars, others do not).]  

\( X(e^{j\omega}) = A(\omega) + jB(\omega) \).  
Sketch the function of time corresponding to \( Y(e^{j\omega}) = B(\omega) + A(\omega)e^{j\omega} \).  

Solution:  
\( x[n] = x_e[n] + x_o[n] \).  
[Arrows: \( x_e[n] \to A(\omega) \), \( x_o[n] \to jB(\omega) \)]  

\( Y(e^{j\omega}) = \frac{X_o(e^{j\omega})}{j} + X_e(e^{j\omega})e^{j\omega} \)  

\( y(n) = \frac{1}{j}X_o[n] + X_e[n+1] \).  

*Remember*  
\( x_o[n] = \frac{x[n] - x[-n]}{2} \), \( x_e[n] = \frac{x[n] + x[-n]}{2} \)  

Draw yourself.  

Nawar

---

## Page 43

**Page: Dsp (lec) Date: 12/ 3/2026.**

[Diagram: None]  

An LTI System, with impulse response \( h[n] = \left( \frac{1}{2} \right)^n u[n] \). Use Fourier Transform to determine the response of the following input:  
\( x[n] = \left( \frac{3}{4} \right)^n u[n] \).  

\( X(e^{j\omega}) = \frac{1}{1 - \frac{3}{4} e^{-j\omega}} \)  

\( H(e^{j\omega}) = \frac{1}{1 - \frac{1}{2} e^{-j\omega}} \)  

\( Y(e^{j\omega}) = \frac{1}{1 - \frac{3}{4} e^{-j\omega}} \cdot \frac{1}{1 - \frac{1}{2} e^{-j\omega}} = \frac{A}{1 - \frac{3}{4} e^{-j\omega}} + \frac{B}{1 - \frac{1}{2} e^{-j\omega}} \)  

\( y[n] = A \left( \frac{3}{4} \right)^n u[n] + B \left( \frac{1}{2} \right)^n u[n] \).  

\( \frac{1}{1 - \frac{1}{2} e^{-j\omega}} = A + \frac{B(1 - \frac{3}{4} e^{-j\omega})}{(1 - \frac{1}{2} e^{-j\omega})} \quad e^{-j\omega} = \frac{2}{3} \)  

\( A = 3 \)  

\( \frac{1}{1 - \frac{3}{4} \cdot \frac{2}{3}} \quad B = -2 \quad e^{-j\omega} = 2 \)  

\( y[n] = 3 \left( \frac{3}{4} \right)^n u[n] - 2 \left( \frac{1}{2} \right)^n u[n] \).

---

## Page 44

Page: DSP [Missed]  
Date: 24/3/2026  

DTFT is  
→ Analysis eg: "From time domain to Frequency"  
$$
X(e^{j\omega}) = \sum_{n=-\infty}^{\infty} x[n] e^{-j\omega n}
$$
→ Spectral Analysis  

→ Synthesis eg: "Inverse DTFT"  
$$
x[n] = \frac{1}{2\pi} \int_{-\pi}^{\pi} X(e^{j\omega}) e^{j\omega n} d\omega
$$

*DTFT of Basic Signals*  

| ($x[n]$)                            | ($X(e^{j\omega})$)                                                                                                                 |     |        |     |
| ----------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | --- | ------ | --- |
| ($\delta[n]$)                       | ($1)                                                                                                                               |     |        |     |
| \(1\)                               | \(2\pi \sum_{k=-\infty}^{\infty} \delta(\omega - 2\pi k)\)                                                                         |     |        |     |
| \(u[n]\)                            | \(\frac{1}{1 + e^{-j\omega}} + \pi \sum_{k=-\infty}^{\infty} \delta(\omega - 2\pi k)\)                                             |     |        |     |
| \(\text{sgn}[n]\)                   | \(\frac{2}{1 + e^{-j\omega}}\)                                                                                                     |     |        |     |
| *Right sided expo.* \(a^n u[n]\)    | \(\frac{1}{1 - ae^{-j\omega}}\) (Conditions for existence: \(                                                                      | a   | < 1\)) |     |
| *Left sided expo.* \(-a^n u[-n-1]\) | \(\frac{1}{1 - ae^{-j\omega}}\) (Conditions for existence: \(                                                                      | a   | > 1\)) |     |
| \(\sin(\omega_0 n)\)                | \(\frac{\pi}{j} \sum_{k=-\infty}^{\infty} \left[ \delta(\omega - \omega_0 - 2\pi k) - \delta(\omega + \omega_0 - 2\pi k) \right]\) |     |        |     |
| \(\cos(\omega_0 n)\)                | \(\pi \sum_{k=-\infty}^{\infty} \left[ \delta(\omega - \omega_0 - 2\pi k) + \delta(\omega + \omega_0 - 2\pi k) \right]\)           |     |        |     |

Nawar

---

## Page 45

**Page: Date: / /**

**DTFT Properties**  

| Property       | \( x[n] \)                     | \( X(e^{j\omega}) \)                     |  
|----------------|--------------------------------|-----------------------------------------|  
| Periodic        | any \( x[n] \)                 | \( X(e^{j(\omega + 2\pi)}) = X(e^{j\omega}) \) |  
| Linear          | \( a_1 x_1[n] + a_2 x_2[n] \)    | \( a_1 X_1(e^{j\omega}) + a_2 X_2(e^{j\omega}) \) |  
| Time Shift      | \( x[n - k] \)                 | \( e^{-j\omega k} X(e^{j\omega}) \)       |  
| Convolution     | \( x[n] * h[n] \)              | \( X(e^{j\omega}) H(e^{j\omega}) \)       |  
| Frequency Shift (Modulation) | \( x[n] e^{j\omega_0 n} \) (carrier frequency) | \( X(e^{j(\omega - \omega_0)}) \) |  
| Parseval        | \( \sum_{n=-\infty}^{\infty} |x[n]|^2 \) | \( \frac{1}{2\pi} \int_{-\pi}^{\pi} |X(e^{j\omega})|^2 d\omega \) |  


**Inverse DTFT**  
"Synthesis equation"  
\[ x[n] = \frac{1}{2\pi} \int_{-\pi}^{\pi} X(e^{j\omega}) e^{j\omega n} d\omega \]  

→ Usually, we don’t use this rule. Instead, we use the DTFT properties & basic signals to get the Inverse.  

In Many Cases, we use Partial Fractions.  

[Diagram: None]  

*Nawar*

---

## Page 46

Page:  
Date: / /  

Examples: Find the inverse DFT of the following:  

① \( X(e^{j\omega}) = \frac{3}{1 - 0.2e^{-j\omega}} + \frac{5}{1 - 0.4e^{-j\omega}} \)  
\( x[n] = 3(0.2)^n u[n] - 5(0.4)^n u[n] \)  

② \( X(e^{j\omega}) = \frac{3e^{-j2\omega} + 5e^{-j3\omega}}{1 + 0.3e^{-j\omega}} \)  
\( X(e^{j\omega}) = \frac{3e^{-j2\omega}}{1 + 0.3e^{-j\omega}} + \frac{5e^{-j3\omega}}{1 + 0.3e^{-j\omega}} \)  
\( x[n] = 3(0.3)^{n-2} u[n-2] + 5(0.3)^{n-3} u[n-3] \)  

③ \( X(e^{j\omega}) = \frac{3 + e^{-j\omega}}{1 - 0.75e^{-j\omega} + 0.125e^{-j2\omega}} \)  
\( X(e^{j\omega}) = \frac{3 + e^{-j\omega}}{(1 - 0.5e^{-j\omega})(1 - 0.25e^{-j\omega})} \)  
\( \frac{1}{(1 - 0.5e^{-j\omega})(1 - 0.25e^{-j\omega})} = \frac{A}{1 - 0.5e^{-j\omega}} + \frac{B}{1 - 0.25e^{-j\omega}} \)  
\( A = \left[ \frac{1}{1 - 0.25e^{-j\omega}} \right]_{e^{-j\omega} = 2} = \frac{1}{1 - \frac{0.25}{0.5}} = 2 \)  
\( B = \left[ \frac{1}{1 - 0.5e^{-j\omega}} \right]_{e^{-j\omega} = 4} = \frac{1}{1 - 2} = -1 \)  

Nawar

---

## Page 47

**Page:  Date: / /**

DTF\(^{-1}\) \(\left\{ \frac{3 + e^{-j\omega}}{(1 - 0.5e^{-j\omega})(1 - 0.25e^{-j\omega})} \right\}\)  

\(= \left\{ \frac{3}{( \ ) ( \ )} + \frac{e^{-j\omega}}{( \ ) ( \ )} \right\}\)  

\(= \left\{ \frac{3(2)}{1 - 0.5e^{-j\omega}} + \frac{3(-1)}{1 - 0.25e^{-j\omega}} + \frac{2e^{-j\omega}}{1 - 0.5e^{-j\omega}} + \frac{-2e^{-j\omega}}{1 - 0.25e^{-j\omega}} \right\}\)  

\(\stackrel{\text{IDTFT}}{\longleftrightarrow} 6(0.5)^n u[n] - 3(0.25)^n u[n] + 2(0.5)^{n-1} u[n-1] - (0.25)^{n-1} u[n-1]\)  

\(\frac{3 + e^{-j\omega}}{(1 - 0.5e^{-j\omega})(1 - 0.25e^{-j\omega})} = \frac{A}{1 - 0.5e^{-j\omega}} + \frac{B}{1 - 0.25e^{-j\omega}}\)  

\(A = \left. \frac{3 + e^{-j\omega}}{1 - 0.25e^{-j\omega}} \right|_{e^{-j\omega} = 2} = \frac{3 + 2}{1 - \frac{1}{2}} = 10\)  

\(B = \left. \frac{3 + e^{-j\omega}}{1 - 0.5e^{-j\omega}} \right|_{e^{-j\omega} = 4} = \frac{3 + 4}{1 - 2} = -7\)  

\(\frac{10}{1 - 0.5e^{-j\omega}} + \frac{-7}{1 - 0.25e^{-j\omega}}\)  

[Diagram: A curved arrow labeled "DTF\(^{-1}\)" points from the fraction to the time-domain expression below.]  

\(10(0.5)^n u[n] - 7(0.25)^n u[n]\)  

Nawar

---

## Page 48

**Page:  Date: / /**

Filters :-  

a Filter is a system that passes some frequency components & stops (suppresses) others.  

\* Ideal Filters :-  
It is a filter that multiplies the pass - band components by 1 & stop - band components by 0.  

Example: Ideal low - pass filter.  

in frequency domain,  
Frequency Response \( H(e^{j\omega}) = \begin{cases} 1 & |\omega| < \omega_c \\ 0 & \text{otherwise} \end{cases} \)  
[Diagram: A rectangular frequency response plot with \( H(e^{j\omega}) = 1 \) for \( |\omega| < \omega_c \) (labeled "Cutoff frequency") and \( H(e^{j\omega}) = 0 \) elsewhere, with \( \omega \) on the x - axis and \( H(e^{j\omega}) \) on the y - axis]  

in time domain (impulse response):  
\( h[n] = \text{DTFT}^{-1}\left\{ H(e^{j\omega}) \right\} = \frac{1}{2\pi} \int_{-\pi}^{\pi} H(e^{j\omega}) e^{j\omega n} d\omega \)  
\( = \frac{1}{2\pi} \int_{-\omega_c}^{\omega_c} e^{j\omega n} d\omega = \frac{1}{2\pi} \left[ \frac{e^{j\omega n}}{jn} \right]_{-\omega_c}^{\omega_c} = \frac{e^{j\omega_c n} - e^{-j\omega_c n}}{2\pi jn} \)  
\( = \frac{2j\sin\omega_c n}{2\pi jn} = \frac{\sin\omega_c n}{\pi n} \)  
[Note: \( \sin\omega_c n = 0 \) when \( \omega_c n = k\pi \implies n = \frac{k\pi}{\omega_c} \)]  

[Diagram: A sinc - like impulse response plot labeled "sine function" with \( h[n] = \frac{\sin\omega_c n}{\pi n} \), showing the characteristic oscillatory decay of the sinc function, with \( n \) on the x - axis and \( h[n] \) on the y - axis]  

\( \text{sinc } x = \frac{\sin \pi x}{\pi x} \) (Normalized)  

Nawar

---

## Page 49

**Page: \quad Date: \quad / \quad / \quad \quad \text{low} \quad \text{filter} \quad \text{pass}**

\( h_{\text{ds}} = \frac{\sin \omega_c n}{\pi n} \frac{\omega_c}{\pi} \frac{\sin \pi \left( \frac{\omega_c}{\pi} n \right)}{\pi \left( \frac{\omega_c}{\pi} n \right)} \quad \text{Ideal Pass} \)  

\( \boxed{h_{\text{LP}} = \frac{\omega_c}{\pi} \operatorname{sinc}\left( \frac{\omega_c}{\pi} n \right)} \)  


\# This filter is ideal because it is anti - causal with infinite support  

\# This filter has Zero Phase (instantaneous) \quad \text{No time delay}  


\* approximate low Pass filters:  

\(\underline{\text{Idea: Truncation of } h_{\text{LP}}}\)  

e.g. \( \hat{h}[n] = h_{\text{LP}}[n] \quad -N \leq n \leq N \)  

\(\rightarrow = h_{\text{LP}}[n] \, w[n]\)  

\(\downarrow\) window function  

[Diagram: A sketch of a frequency response \(\hat{H}(e^{j\omega})\) with ripples near the cutoff frequency, labeled "window function"]  

where \( w[n] \rightarrow \begin{cases} 1 & -N \leq n \leq N \\ 0 & \text{otherwise} \end{cases} \)  


So, \( \hat{H}(e^{j\omega}) = H(e^{j\omega}) * w(e^{j\omega}) \)  

\( = \frac{1}{2\pi} \int_{-\pi}^{\pi} H(e^{j\delta}) \, w\left( e^{j(\omega - \delta)} \right) d\delta \)  


Nawar

---

## Page 50

**Page: \quad Date: \quad / \quad /**

\( w[n] = \dots \rightarrow \frac{1}{2\pi} \sum_{N=-\infty}^{\infty} \dots \)  

\( W(e^{j\omega}) = \sum_{n=-\infty}^{\infty} w[n] e^{-j\omega n} = \sum_{n=-N}^{N} w[n] e^{-j\omega n} \)  

\( = e^{j\omega N} + e^{j\omega (N-1)} + \dots + e^{-j\omega N} \)  

\( = e^{j\omega N} \left[ 1 + e^{-j\omega} + \dots + e^{-j2\omega N} \right] \)  

\( \rightarrow \) Geometric Series.  

\( \text{Remember } 1 + r + \dots + r^n = \frac{1 - r^{n+1}}{1 - r} \)  

\( = e^{j\omega N} \frac{1 - e^{-j\omega (2N+1)}}{1 - e^{-j\omega}} \)  

\( \text{if draw by Matlab or Python } \rightarrow \text{it will look like Sinc.} \)  

\( = e^{j\omega N} e^{-j\omega (N + \frac{1}{2})} \left[ e^{j\omega (N + \frac{1}{2})} - e^{-j\omega (N + \frac{1}{2})} \right] \rightarrow \sin \)  

\( e^{-j\omega \frac{1}{2}} \left[ e^{j\omega \frac{1}{2}} - e^{-j\omega \frac{1}{2}} \right] \rightarrow \sin. \)  

\( -\pi < \omega < \pi \)  

\( = \frac{e^{-j\omega \frac{1}{2}} 2j \sin \omega (N + \frac{1}{2})}{e^{-j\omega \frac{1}{2}} 2j \sin \frac{\omega}{2}} = \frac{\sin \omega (N + \frac{1}{2})}{\sin \frac{\omega}{2}} \rightarrow w = \frac{k\pi}{N + \frac{1}{2}} \)  

\( \text{when } \omega = 0 \)  

\( \text{when } \omega = 0 \rightarrow W(e^{j\omega}) = \frac{N + \frac{1}{2}}{\frac{1}{2}} = 2N + 1 \)  

[Diagram: A hand-drawn plot of \( W(e^{j\omega}) \) (labeled "Nawar") showing a central peak at \( \omega = 0 \) with height \( 2N+1 \), symmetric side lobes, and x-axis marked with \( -\pi \), \( 0 \), \( \pi \). Annotations include "2N+1" (peak height), "N+1" (side lobe label), and "dirac" (delta function reference).]  

\( \text{will create } \) [handwritten notes] \( \text{Ripples.} \)

---

## Page 51

**Page: DSP (lec) Date: 24/3/2026**

*lecture 4  
Ideal low Pass filter:  
$H(e^{j\omega})$  
[Diagram: Frequency response of ideal low-pass filter with passband (labeled "Pass band") and stopband (labeled "Stop band"), transition region between passband and stopband]  

$h[n] = \frac{1}{2\pi} \int_{-\pi}^{\pi} H(e^{j\omega}) e^{j\omega n} d\omega$  [labeled "Transition band"]  

$= \frac{1}{2\pi} \int_{-\omega_c}^{\omega_c} e^{j\omega n} d\omega$  

$= \frac{1}{2\pi} \left[ \frac{e^{j\omega n}}{jn} \right]_{-\omega_c}^{\omega_c} = \frac{2\sin \omega_c n}{2\pi n} = \frac{\sin \omega_c n}{\pi n}$  

Sinc function.  

Transition: Sinc Ripples. If $\omega_c$ is...  

Sinc like $\leftrightarrow$ Ideal Rectangular (Convolution)  
Function window  

Decibel $\rightarrow 20\log \text{mag} \equiv 10\log \text{Power}$  

High Pass Filter  

in frequency domain $= 1 - H(e^{j\omega})$  

in time $= \delta[n] - h[n]$  

$\rightarrow$ Since we will stop in digital domain at $f_s/2$ as our digital domain we stop here.  

$\rightarrow$ Could be Considered as a Band Pass filter instead.

---

## Page 52

**Page: Date: 24/3/2026**

Finite Impulse Response (FIR) Filter  
Infinite Impulse Response (IIR) Filter  
→ Recursive Filter in Since it is Recursive it can goon until ∞.  
\[ y[n] = y[n-1] + f(x) \]  
→ appears in frequency domain as a Rational function  

→ We can make an IIR Filter with a lesser order than an FIR But with the Same Performance  
→ But it gives as a Non linear Change in Phase.  
→ Linear in limited frequencies.  

* Digital Filters  
  → Finite Impulse Response (FIR)  
  → Infinite Impulse Response (IIR)  

* Examples on FIR: (truncated ideal Filter)  
  → \( \hat{h}[n] = h[n] \cdot w[n] \).  
  output Non-ideal Response ↓ ideal Response ↓ window function (Sinc)  
  \[ y[n] = x[n] * \hat{h}[n] \rightarrow \text{Filteration is Computed through Convolution} \]  
  eg.  
  I/O Relationship:  
  \[ y[n] = a_0 x[n] + a_1 x[n-1] + a_2 x[n-2] \]  
  \[ y[n] = \dots + a_m x[n-m] \dots \]  
  \[ Y(e^{j\omega}) = (a_0 + a_1 e^{-j\omega} + \dots + a_m e^{-j m \omega}) X(e^{j\omega}) \]

---

## Page 53

**Page: Date: 24/3/2026**

\* IIR Filter (Recursive)  
Example:  
\( y[n] = 0.9 y[n-1] + x[n] \).  

In the frequency domain:  
→ Initial Condition.  
Assuming the system is initially at rest.  
(Use \( y[n] = 0 \) for \( n < 0 \))  

\( Y(e^{j\omega}) = 0.9 \cdot e^{-j\omega} Y(e^{j\omega}) + X(e^{j\omega}) \)  

∴ \( Y(e^{j\omega}) (1 - 0.9 e^{-j\omega}) = X(e^{j\omega}) \)  

∴ \( H(e^{j\omega}) = \frac{Y(e^{j\omega})}{X(e^{j\omega})} = \frac{1}{1 - 0.9 e^{-j\omega}} \)  

∴ \( h[n] = (0.9)^n u[n] \).  

[Diagram: Left plot shows a decaying exponential curve labeled \( h[n] \) with a peak at \( n=0 \) and a dip at \( n=1 \). Right plot shows a stem plot of \( h[n] \) with values \( 1, 0.9, 0.81, \dots \) decreasing exponentially.]  

→ Rectangular → sinc function.  
→ Hanning → raised cosine function.  
→ Hamming → "11" (partial text)  
→ Blackman  
→ Kaiser  
→ Triangular → etc.  

Nawar

---

## Page 54

**Page: Date: 24/3/2026**

FFT of Signal N samples is splitted → we will Pad the Signal with Zero  

[Diagram: A sketch of a frequency spectrum with labels: "Main lobe", "Transition", "Side lobe"]  

* Translation can be also used in Feature Extraction of Speech in Speech Recognition  

* Since, Speech is a Random Signal → we can't calculate its Fourier (wide sense Stationary must make it → Non-Stationary)  

⇒ First Step: Segmentation through Windowing, "Frames"  

→ 20ms Window gives Stationary well  

→ If we use a Rectangular Window, we will calculate the fft of both window + og. Signal  

→ So instead we will a hanning window  

→ Filter Banks → Feature Extraction Methods  

[Diagram: A sketch with labels: "Mel Scale", "log scale w", "log scale Mag.", "Filter Banks", "Spectrogram → 2D Voice", "Mel Cepstrum Coefficients" (circled) → "Mel Scale" (arrow)]

---

## Page 55

**Page: Date: 24/3/2026**

in FIR:  
\( H(e^{j\omega}) = a_0 + a_1 e^{-j\omega} + \dots \)  

Example:  
\( y[n] = \frac{1}{2} (x[n] + x[n-1]) \)  
\( \to \) moving average filter, "order=2"  

Find \( h[n] \):  
\( h[n] = \frac{1}{2} \delta[n] + \frac{1}{2} \delta[n-1] \)  

[Diagram: Impulse response plot with \( h[n] \) values: \( \frac{1}{2} \) at \( n=0 \), \( \frac{1}{2} \) at \( n=1 \), 0 elsewhere (x-axis: \( n \), y-axis: \( h[n] \))]

Find \( H(e^{j\omega}) \):  
Soli- method (1):  
\( H(e^{j\omega}) = \text{DTFT}(h[n]) \)  
\( = \frac{1}{2} (1 + e^{-j\omega}) = e^{-j\omega/2} \left( \frac{e^{j\omega/2} + e^{-j\omega/2}}{2} \right) \)  
\( = \frac{e^{-j\omega/2} \cos \frac{\omega}{2}}{2} \)  

Magnitude:  
\( |H(e^{j\omega})| = e^{-j\omega/2} \cos \frac{\omega}{2} \)  

[Diagram: Magnitude response plot of \( |H(e^{j\omega})| \) vs. \( \omega \): triangular shape peaking at \( \omega=0 \) (value 1), zero at \( \omega=\pm\pi \); labeled "seems like a low pass filter" and "non-ideal LPF" (x-axis: \( \omega \), y-axis: \( |H(e^{j\omega})| \))]

---

## Page 56

**Page: Date: 24/ 3/2026.**

$\angle H(e^{j\omega}) = \frac{\omega}{2} + \alpha$  

[Diagram: A graph with a horizontal axis labeled "Linear Phase" and a vertical axis. The graph shows a line with a negative slope, passing through points at $-\pi$ (vertical axis value $\pi/2$), $0$ (origin), and $\pi$ (vertical axis value $-\pi/2$). Arrows indicate the horizontal axis direction, and labels include $-\pi$, $0$, $\pi$, $-\pi/2$, and $\pi/2$.]  

in Real functions  
its Value +ve $\longrightarrow$ $0$  
its Value -ve $\longrightarrow$ $\frac{\pi}{6}$.  

No Phase  
Distortion.  

Since the slope of the line  
is -ve $\longrightarrow$ So it causes a Delay  
$\#$  

Nawar

---

## Page 57

**Page: DSP dec₃ Date: 31/3/2026.**
× lecture 2  
→ DFT &  
\[ X[k] = \sum_{n=0}^{N-1} x[n] e^{-j\left(\frac{2\pi}{N}k\right)n} \]  
frequency index ↖  
\[ \omega_k = \frac{2\pi}{N}k \]  
→ Analysis eq.  
\[ x[n] = \frac{1}{N} \sum_{k=0}^{N-1} X[k] e^{j\left(\frac{2\pi}{N}k\right)n} \]  
→ Synthesis eq.  
× DFT is also known as (N-Point Fourier transform or Short Time FT)  

× DFT vs DTFT  
① DFT is a sampled version of DTFT  
(i.e. Computes \( X(e^{j\omega}) \) at some specific samples of \( \omega \)).  
i.e. \( X[k] = X\left(e^{j\frac{2\pi}{N}k}\right) \) # finite samples  
② DFT computes spectrum from \( \omega=0 \) to \( 2\pi \)  
while, DTFT’s standard range is from \( -\pi \) to \( \pi \)  
③ In DFT :-  
Circular Convolution in time domain  
≡ Multiplication in frequency domain  
While in DTFT :-  
linear Convolution in time domain  
≡ Multiplication in frequency domain  

Padding for is linear Convolution ⇒ basis equals with Zeros.  

[Diagram: None]  
Nawar

---

## Page 58

**Page: Date: 31/3/2026**

→ Direct Computation Complexity of DFT has \( O(N^2) \).  

→ There exists Several algorithms having Complexity of \( O(N \log N) \).  
  → These algorithms are called "Fast Fourier Transform" (FFT)  

* FFT algorithm when \( N \) is a power of 2 (i.e \( N = 2, 4, 8, 16, 32, 64, \dots \))  

Noting: \( e^{-j \frac{2\pi}{N} k n} \)  
→ there exists symmetry.  

Note: \( e^{-j \frac{2\pi}{N} (5)} = -e^{-j \frac{2\pi}{N} (1)} \).  
\( e^{-j \frac{2\pi}{N} (6)} = -e^{-j \frac{2\pi}{N} (2)} \).  

So: \( e^{-j \frac{2\pi}{N} \left( \frac{N}{2} + k \right)} = -e^{-j \frac{2\pi}{N} k} \).  

\( X[k] = \sum_{n=0}^{N-1} x[n] \, e^{-j \frac{2\pi}{N} k n} \)  

→ For \( M = \frac{N}{2} \)  

\( X[k] = \sum_{m=0}^{M-1} x[2m] \, e^{-j \frac{2\pi}{N} k (2m)} \rightarrow \text{Even Port} \)  

\( + \sum_{m=0}^{M-1} x[2m+1] \, e^{-j \frac{2\pi}{N} k (2m+1)} \rightarrow \text{odd Port} \)  


[Diagram: A hand-drawn unit circle with points labeled (0), (1), (2), (3), (5), (6), showing complex exponentials \( e^{j \frac{2\pi}{N} k} \) and their symmetric relationships (e.g., \( e^{j \frac{2\pi}{N} (0)} \), \( 2e^{j \frac{2\pi}{N} (1)} \), \( e^{j \frac{2\pi}{N} (2)} \), \( e^{j \frac{2\pi}{N} (3)} \), \( e^{j \frac{2\pi}{N} (5)} \), \( e^{j \frac{2\pi}{N} (6)} \)) with annotations like \( N/2 \) and symmetry notes.]  

Nawar

---

## Page 59

**Page: \quad Date: \quad / \quad /**

\[ X[k] = \sum_{m=0}^{M-1} x[2m] e^{-j\frac{2\pi}{M} km} + e^{-j\frac{2\pi}{M} kM} \sum_{m=0}^{M-1} x[2m+1] e^{-j\frac{2\pi}{M} km} \]  

DFT of the even ordered samples \quad add \quad DFT of the ordered samples  

e.g. we have a signal:  

\[ x[0], x[1], x[2], x[3], x[4], x[5], x[6], x[7] \]  

\[ e^{-j\frac{\pi k}{4}}, k=0,1,\cdots,7 \]  

\[ x[0], x[2], x[4], x[6] \quad x[1], x[3], x[5], x[7] \]  

\[ e^{-j\frac{\pi k}{2}}, k=0,1,2,3 \quad e^{-j\frac{\pi k}{2}} \]  

\[ x[0], x[4] \quad x[2], x[6] \quad x[1], x[5] \quad x[3], x[7] \]  

\[ e^{-j\pi k}, k=0 \quad e^{-j\pi k} \quad e^{-j\pi k} \quad e^{-j\pi k} \]  

\[ x[0] \quad x[4] \quad x[2] \quad x[6] \quad x[1] \quad x[5] \quad x[3] \quad x[7] \]  

\[ \text{spf } \frac{N}{3} \text{ Coefficients we can find at level } f \text{ is } \leftarrow \text{ (text unclear, likely related to symmetry or coefficients)} \]  

Symmetry. (text unclear, likely related to symmetry properties)  

\[ \begin{array}{|c|c|} \hline \text{Binary} & \text{Bit Reversed} \\ \hline 000 & 000 \\ 100 & 001 \\ 010 & 010 \\ 110 & 011 \\ 001 & 100 \\ 101 & 101 \\ 011 & 110 \\ 111 & 111 \\ \hline \end{array} \quad \rightarrow \text{ bit Reversal of Binary representation} \]  

Nawar

---

## Page 60

Page:  
Date: 3/3/2026  

\* Butterfly diagram.  
Given: \( x[n] = [3, 2, 1, 5] \)  

[Diagram: Hand-drawn butterfly diagram with labeled nodes (e.g., "3", "1", "2", "5", "4", "11", "-3", "2+j3", "2-j3") and connecting lines (blue and red) showing signal flow. Annotations include \( e^{-j\pi k / 2} \) and \( k=0,1 \).]  

\( X[k] = [11, 2+j3, -3, 2-j3] \)  

\( e^{-j\pi k / 2} \) for \( k=0,1 \)  

\( \Rightarrow e^{-j\pi/2} = -j \)  

\(\rightarrow\) we can use Butterfly Diagrams to calculate both inverse and forward FFT.  

\#  

\* Sampling Theory: (Ideal Sampling)  
Given: \( x_c(t) \)  

\( x_s(t) = x_c(t) P_T(t) = x_c(t) \sum_{n=-\infty}^{\infty} \delta(t - nT) \)  

Previously:  

Continuous F.T of sampled signal:  

\( X_s(j\Omega) = \sum_{n=-\infty}^{\infty} x[n] e^{-j\Omega T n} \)  

\( = X(e^{j\Omega T}) \)  

\( \Rightarrow \) DTFT at \( \omega = \Omega T \)  


Nawar

---

## Page 61

**Page: \quad Date: 3/3/2026**

\* Fourier Series Representation of the impulse train  

\( P_T(t) = \sum_{n=-\infty}^{\infty} \delta(t - nT) \), is Periodic  

with Periodic Time = T  

[Diagram: Impulse train with impulses at \( -2T, -T, 0, T, 2T \)]  

according to Fourier Series, we can write it as:  

\( P_T(t) = \sum_{k=0}^{\infty} d_k e^{\frac{j2\pi k}{T}t} \)  

\( d_k = \frac{1}{T} \int_{-T/2}^{T/2} P_T(t) e^{-\frac{j2\pi k}{T}t} dt \) (Sifting will happen)  

\( = \frac{1}{T} (1) = \frac{1}{T} \)  

\[
\boxed{ P_T(t) = \frac{1}{T} \sum_{k=-\infty}^{\infty} e^{\frac{j2\pi k}{T}t} }
\]  

So,  

\( x_s(t) = x_c(t) \cdot \frac{1}{T} \sum_{k=-\infty}^{\infty} e^{\frac{j2\pi k}{T}t} \)  

\( x_s(t) = \frac{1}{T} \sum_{k=-\infty}^{\infty} x_c(t) e^{\frac{j2\pi k}{T}t} \)  

\( X_s(j\Omega) = \frac{1}{T} \sum_{k=-\infty}^{\infty} X_c\left(j\left(\Omega - \frac{2\pi}{T}k\right)\right) \)  

\[
\begin{array}{c}
\downarrow \\
\text{Sampled Signal}
\end{array}
\quad
\begin{array}{c}
\updownarrow \\
\text{Continuous Signal} \\
\text{"original"}
\end{array}
\]  

Nawar

---

## Page 62

**Page: Date: 31/3/2026**

\( X_c(j\Omega) \)  
\( F \)  
\( -B \quad 0 \quad B \quad \Omega \)  
\( X_s(j\Omega) \)  
\( F \)  
\( \text{alias} \)  
\( -\frac{2\pi}{T} \quad -B \quad 0 \quad B \quad \frac{2\pi}{T} \)  
\( \text{alias} \)  
\( \text{Main alias} \)  

where \( \frac{2\pi}{T} \) is the sampling frequency \( \Omega_s \)  

→ For aliases not to overlap:  
\( \Omega_s = \frac{2\pi}{T} \geq 2B \)  

Where \( 2B \) is the Critical sampling freq. (Nyquist freq).  

→ if aliases interfere, the signal will be distorted.  

→ How to Recover the Continuous from the Sampled  
Signal → we use a "Recovery Filter"  
* Ideal Recovery Filter (Discrete to Continuous D/C).  

[Diagram: Block diagram showing \( X_s(t) \) → [\( h_r(t) \)] → \( X_c(t) \), with labels "gain & low pass filter" and frequency-domain equivalents \( X_s(j\Omega) \) → \( H_r(j\Omega) \) → \( X_c(j\Omega) \)]  

\( H_r(j\Omega) \)  
\( T \)  
\( |\Omega| < \frac{\pi}{T} \) ~ built using \( H_{\text{I/D}} \)  
\( 0 \)  
\( 0 \) otherwise  
Not slow.  

Nawar

---

## Page 63

**Page: \quad Date: \quad / \quad /**

\[ h_r(t) = \frac{1}{2\pi} \int_{-\infty}^{\infty} H_r(j\Omega) e^{j\Omega t} d\Omega \]  

\[ = \frac{1}{2\pi} \int_{-\frac{\pi}{T}}^{\frac{\pi}{T}} T e^{j\Omega t} d\Omega \]  

\[ = \frac{T}{2\pi} \left[ \frac{e^{j\Omega t}}{jt} \right]_{-\frac{\pi}{T}}^{\frac{\pi}{T}} = \frac{T}{2\pi} \cdot \frac{2\sin\left( \frac{\pi t}{T} \right)}{t} \]  

\[ \frac{\sin\left( \frac{\pi t}{T} \right)}{\frac{\pi t}{T}} \equiv \text{sinc}\left( \frac{t}{T} \right) \]  

\[ h_r(t) \]  

[Diagram: A graph of \( h_r(t) \) showing a central peak at \( t=0 \) with decaying oscillations (sinc function) labeled with time points \( -2T, -T, T, 2T \).]  

- Ideal bec → anti Causal  
- infinite response.  

Practically:  
- (ZoH) Zero order hold filter  
- or (FoH) First order hold filter  
[Diagram: A graph with discrete samples (vertical lines) and a dashed line connecting them, labeled "These are all interpolators."]  

Can be used if Sampling ← (ZoH) rate is very small  
[Diagram: A step-like waveform labeled "ZoH" with text "Can be implemented used a Capacitor" and an arrow "waits till the next sample".]  
[Diagram: A triangular waveform labeled "(FoH)".]  

Nawar

---

## Page 64

**Page: Date: 31/3/2026**
* ZOH in frequency domain.  

\( h_{\text{ZOH}}(t) \rightarrow 1 \quad 0 \leq t \leq T \)  
[Diagram: A sketch of \( h_{\text{ZOH}}(t) \) showing a rectangular pulse of height 1 over the interval \( 0 \leq t \leq T \), with a label "ZOH" near the pulse.]  

\( H_{\text{ZOH}}(j\Omega) = \int_{-\infty}^{\infty} h_{\text{ZOH}}(t) e^{-j\Omega t} dt \)  
\( = \int_{0}^{T} 1 \cdot e^{-j\Omega t} dt = \frac{e^{-j\Omega t}}{-j\Omega} \bigg|_{0}^{T} = \frac{e^{-j\Omega T} - 1}{-j\Omega} \)  
\( = \frac{e^{-j\Omega T/2}}{-j\Omega} \left[ e^{-j\Omega T/2} - e^{j\Omega T/2} \right] \)  
\( = \frac{e^{-j\Omega T/2}}{-j\Omega} \cdot (-2j) \sin\left( \frac{\Omega T}{2} \right) = T e^{-j\Omega T/2} \frac{\sin\left( \frac{\Omega T}{2} \right)}{\frac{\Omega T}{2}} \)  
\( = T e^{-j\Omega T/2} \cdot \text{sinc}\left( \frac{\Omega T}{2\pi} \right) \)  

[Diagram: A plot of the ideal ZOH frequency response \( H_{\text{ZOH}}(j\Omega) \). The plot shows a sinc function centered at \( \Omega = 0 \), with main lobe width \( \frac{2\pi}{T} \) (from \( -\frac{\pi}{T} \) to \( \frac{\pi}{T} \)) and side lobes decaying. The x-axis is labeled \( \Omega \), with ticks at \( -\frac{\pi}{T} \), \( \frac{\pi}{T} \), \( \frac{2\pi}{T} \), and \( \frac{2\pi}{T} \). The y-axis is labeled \( T \) (amplitude).]  

Nawar

---

## Page 65

Date: / / impulse  

[Diagram: A horizontal axis labeled with \(-T\) and \(T\), with an upward arrow centered between them, representing an impulse.]  

impulse  
Response  
[Diagram: A triangular waveform symmetric about the origin, with vertices at \(-T\), \(0\), and \(T\), labeled \(h_{\text{Fou}}(t)\). The waveform is centered on the horizontal axis marked with \(-T\) and \(T\).]  

(b)

---
