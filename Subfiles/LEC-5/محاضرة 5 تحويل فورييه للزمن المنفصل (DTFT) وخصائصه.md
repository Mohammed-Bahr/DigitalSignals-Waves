---
Created: " 2026-04-27 20:33"
modified: 2026-04-27 20:33
tags:
  - FACL
  - DigitalSignals
Source:
---

> [!quote] If you lose today, win tomorrow. In this never-ending spirit of challenge is the heart of a victor.
> — Daisaku Ikeda

**"اللهم إني أسألك فهم النبيين، وحفظ المرسلين، والملائكة المقربين، اللهم اجعل ألسنتنا عامرة بذكرك، وقلوبنا بخشيتك، إنك على كل شيء قدير"**

---

- DTFT : 
$$
X(e^{j\omega}) = \sum_{n=-\infty}^{\infty} x[n]e^{-j\omega n}
$$
- DFT :
$$
X[k] = X(e^{j\frac{2\pi k}{N}}) = \sum_{n=0}^{N-1} x[n]e^{-j\frac{2\pi}{N}kn}
$$
---
## DTFT of basic signals:
1. **Impulse**: $\delta[n] = \begin{cases} 1 & n=0 \\ 0 & \text{o.w.} \end{cases}$

$$ X(e^{j\omega}) = \sum_{n=-\infty}^{\infty} \delta[n]e^{-j\omega n} = e^{-j\omega(0)} = 1 $$

$$ \delta[n] \xleftrightarrow{\text{DTFT}} 1 $$
2. **Right sided exponential:**

$$ x[n] = a^n u[n] $$

$a$ is a complex quantity (constant)

$$ X(e^{j\omega}) = \sum_{n=-\infty}^{\infty} a^n u[n] e^{-j\omega n} $$


> [!example] **Geometric Series Reference:**
> $$ 1 + r + \dots + r^n = \frac{1 - r^{n+1}}{1 - r} $$
> if $|r| < 1$ and $n \to \infty$
> $$ 1 + r + \dots = \frac{1}{1 - r} $$

$$ = \sum_{n=0}^{\infty} a^n e^{-j\omega n} = 1 + a e^{-j\omega} + a^2 e^{-j2\omega} + \dots $$

The DTFT is defined only when: $|a e^{-j\omega}| < 1$

$$ |a| \cdot |e^{-j\omega}| < 1 $$
$$ (|a| < 1) $$

In this case:
$$ X(e^{j\omega}) = \frac{1}{1 - a e^{-j\omega}} $$

$$
a^n e^{-j\omega} \xleftrightarrow{\text{DTFT}} \frac{1}{1 - a e^{-j\omega}}, \quad \text{when } |a| < 1
$$



3. **Left sided exponential** :


$$
x[n] = -a^n u[-n-1]
$$



$$
X(e^{j\omega}) = \sum_{n=-\infty}^{\infty} -a^n u[-n-1] e^{-j\omega n}

$$

Since:

$$
-n - 1 \geq 0
$$

$$
-n \geq 1
$$
$$
n \leq -1
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
Then:$$
|a^{-1}| < 1
$$$$
\Rightarrow |a| > 1
$$
In this case:

$$ X(e^{j\omega}) = \frac{-a^{-1}e^{j\omega}}{1 - a^{-1}e^{j\omega}} = \frac{1}{-a e^{-j\omega} + 1} = \frac{1}{1 - a e^{-j\omega}} $$

$$ -a^n u[-n-1] \xleftrightarrow{\text{DTFT}} \frac{1}{1 - a e^{-j\omega}} \quad \text{when } |a| > 1 $$

4. **DTFT of**  $X[n] = 1$:
![[../Attachments/image.png]]
	$$
x(e^{jw}) = 2\pi \sum_{k=-\infty}^{\infty}\delta(w-2\pi k)
$$
5. **DTFT** of $u[n]$ :
Trial : $$
x(e^{jw}) = \sum_{n=-\infty}^{\infty} u[n]e^{-jwn}= \sum_{n=0}^{\infty}e^{-jwn}= 1+e^{-jw}+e^{-2jw}+.... \quad , r = e^{-jw} , |r| = 1
$$ 
prof :
$$
 x(e^{jw}) = \frac{1}{1-e^{-jw}} + \pi \sum^{\infty}_{k=-\infty} \delta(w-2\pi k)
$$


---
---

## DTFT Properties

## 1. DTFT is periodic with period = 2π

**Proof:**

$$X(e^{j\omega}) = \sum_{n=-\infty}^{\infty} x[n] e^{-j\omega n}$$

$$X(e^{j(\omega + 2\pi)}) = \sum_{n=-\infty}^{\infty} x[n] e^{-j(\omega + 2\pi)n}$$

$$= \sum_{n=-\infty}^{\infty} x[n] e^{-j\omega n} \cdot e^{-j2\pi n}$$
$$
= \sum_{n=-\infty}^{\infty} x[n] e^{-j\omega n} = x(e^{jw})
$$
Since $e^{-j2\pi n} = 1$ for all integer $n$, we get $X(e^{j(\omega+2\pi)}) = X(e^{j\omega})$ ∎

---

### Signum Function

$$\frac{1}{2}\text{sgn}(t) \xrightarrow{\text{DTFT}} \frac{2}{1 - e^{j\omega}}$$

$$\text{sgn}[n] \xrightarrow{\text{DTFT}} \frac{2}{1 - e^{j\omega}}$$


## 2. DTFT is Linear

$$\text{DTFT}{\alpha_1 x_1[n] + \alpha_2 x_2[n]} = \alpha_1 \text{ DTFT}{x_1[n]} + \alpha_2 \text{ DTFT}{x_2[n]}$$

$$= \alpha_1 X_1(e^{j\omega}) + \alpha_2 X_2(e^{j\omega})$$

---

## 3. Time Shift

$$\text{DTFT}({x[n-k]}) = \sum_{n=-\infty}^{\infty} x[n-k], e^{-j\omega n}$$

Let $m = n - k \quad \therefore n = m + k$

- As $n \to -\infty,\quad m \to -\infty$
- As $n \to +\infty,\quad m \to +\infty$

$$\text{DTFT}({x[n-k]}) = \sum_{m=-\infty}^{\infty} x[m], e^{-j\omega(m+k)}$$

$$= e^{-j\omega k} \sum_{m=-\infty}^{\infty} x[m], e^{-j\omega m} = e^{-j\omega k}, X(e^{j\omega})$$
#### Time Shift Property — Implications

$$x[n-k] \xleftrightarrow{\text{DTFT}} e^{-j\omega k}, X(e^{j\omega})$$

↑ _delay in time domain_


##### Magnitude

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



---
## 4. Frequency Shift (Modulation)

$$e^{j\omega_0 n}. x[n] \xleftrightarrow{\text{DTFT}} X(e^{j(\omega - \omega_0)})$$

> Multiplying by a complex exponential $e^{j\omega_0 n}$ in the **time domain** shifts the spectrum by $\omega_0$ in the **frequency domain**.

---

### Visualization
![[../Attachments/image-1.png]]
**Original spectrum $X(e^{j\omega})$** — centered at $\omega = 0$:

$$\underbrace{\frown}_{-2\omega_0 \quad 0 \quad 2\omega_0}$$

After modulation, the spectrum shifts — one copy moves to $+\omega_0$, one to $-\omega_0$:

$$\underbrace{\frown}_{-\omega_0} \qquad \underbrace{\frown}_{+\omega_0}$$

---

### Why it works

Starting from the definition:

$$\text{DTFT}{e^{j\omega_0 n} x[n]} = \sum_{n=-\infty}^{\infty} x[n], e^{j\omega_0 n} e^{-j\omega n}$$

$$= \sum_{n=-\infty}^{\infty} x[n], e^{-j(\omega - \omega_0)n} = X(e^{j(\omega-\omega_0)})$$

The $e^{j\omega_0 n}$ term simply replaces $\omega$ with $\omega - \omega_0$ inside the DTFT sum — shifting the entire spectrum to the right by $\omega_0$.

---

### Key takeaway

|Domain|Operation|
|---|---|
|Time|Multiply by $e^{j\omega_0 n}$|
|Frequency|Shift spectrum by $+\omega_0$|

This is the mathematical basis of **modulation** in communications — shifting a baseband signal up to a carrier frequency.


---

## Convolution Theorem (DTFT) — Proof

### Statement

$$x[n] * h[n] \xleftrightarrow{\text{DTFT}} X(e^{j\omega}) \cdot H(e^{j\omega})$$

Convolution in time domain **=** Multiplication in frequency domain.

---

### Step-by-Step Proof

**Start:** Take the DTFT of the convolution sum.

$$\text{DTFT}{x[n] * h[n]} = \sum_{n=-\infty}^{\infty} \left[\sum_{k=-\infty}^{\infty} x[k], h[n-k]\right] e^{-j\omega n}$$

---

**Step 1 — Swap the order of summation** (both are absolutely convergent):

$$= \sum_{k=-\infty}^{\infty} x[k] \sum_{n=-\infty}^{\infty} h[n-k], e^{-j\omega n}$$

The outer sum over $k$ pulls $x[k]$ out since it doesn't depend on $n$.

---

**Step 2 — Substitute** $m = n - k$ in the inner sum, so $n = m + k$:

$$\sum_{n=-\infty}^{\infty} h[n-k], e^{-j\omega n} = \sum_{m=-\infty}^{\infty} h[m], e^{-j\omega(m+k)} = e^{-j\omega k} \sum_{m=-\infty}^{\infty} h[m], e^{-j\omega m}$$

The inner sum is exactly $H(e^{j\omega})$ by definition of the DTFT.

$$= e^{-j\omega k} \cdot H(e^{j\omega})$$

---

**Step 3 — Substitute back:**

$$= \sum_{k=-\infty}^{\infty} x[k], e^{-j\omega k} \cdot H(e^{j\omega})$$

Factor out $H(e^{j\omega})$ since it doesn't depend on $k$:

$$= H(e^{j\omega}) \underbrace{\sum_{k=-\infty}^{\infty} x[k], e^{-j\omega k}}_{X(e^{j\omega})}$$

---

**Result:**
$$
\text{DTFT}({x[n] * h[n]}) \longleftrightarrow X(e^{j\omega}) \cdot H(e^{j\omega})
$$
---

### Why This Matters

|Domain|Operation|
|---|---|
|Time|Convolution $x[n] * h[n]$ (hard, infinite sum)|
|Frequency|Multiplication $X \cdot H$ (easy, pointwise)|

This is the foundation of **LTI system analysis** — instead of convolving a signal with an impulse response, you multiply their spectra in the frequency domain, then IDTFT back if needed.

### Convolution Property

$$
x[n] * h[n] \xleftrightarrow{\text{DTFT}} X(e^{j\omega})H(e^{j\omega})  
$$
This means:

- **Convolution in time domain** becomes **multiplication in frequency domain**.
    

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

- (h[n]) = impulse response of the system
    
- (H(e^{j\omega})) = frequency response
    

---

### System Block Diagram
![[../Attachments/image-2.png]]
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

### Explanation (Simple)

Imagine you send a signal into a system.

- In **time domain**, the system processes it using **convolution**.
    
- In **frequency domain**, it simply multiplies frequencies.
    

That’s why frequency domain is easier to analyze.

Example:

- If ($H(e^{j\omega})$) removes high frequencies → **Low-pass filter**
    
- If it removes low frequencies → **High-pass filter**
    

So convolution = filtering because the system selects frequencies.

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
## 
- Then this channal its model what it does ?
	- at transmitter :
		- filtration
		- delay the signal
		- attenuation 
	- at receiver :
		- de-modulation
		- amplify   
		- de-attenuation
		- and do nothing for delay 

---

## Property 6 — Energy conservation (Parseval's theorem)

The total energy of a discrete-time signal $x[n]$ is defined as:

$$E = \sum_{n=-\infty}^{\infty} |x[n]|^2$$

Parseval's theorem states that this energy can equivalently be computed in the **frequency domain**:

$$E = \frac{1}{2\pi} \int_{-\pi}^{\pi} |X(e^{j\omega})|^2 , d\omega$$

where $X(e^{j\omega})$ is the DTFT of $x[n]$. The $\frac{1}{2\pi}$ factor accounts for the normalization of the DTFT integral over one period $[-\pi, \pi]$.

**Intuition:** Energy is preserved whether you "look" at the signal in time or in frequency. The squared DTFT magnitude $|X(e^{j\omega})|^2$ is called the **energy spectral density** — it tells you how energy is distributed across frequencies.

---

## Property 7 — Frequency domain derivative (multiplication by n)

Starting from the DTFT definition:

$$X(e^{j\omega}) = \sum_{n=-\infty}^{\infty} x[n] , e^{-j\omega n}$$

Differentiate both sides with respect to $\omega$:

$$\frac{d}{d\omega} X(e^{j\omega}) = \sum_{n=-\infty}^{\infty} x[n] \cdot (-jn) , e^{-j\omega n}$$

Factor out $-j$:

$$\frac{d}{d\omega} X(e^{j\omega}) = -j \sum_{n=-\infty}^{\infty} n \cdot x[n] , e^{-j\omega n} = -j \cdot \text{DTFT}{n \cdot x[n]}$$

Rearranging to isolate the DTFT of $n \cdot x[n]$:

$$\boxed{\text{DTFT}{n \cdot x[n]} = j \frac{d}{d\omega} X(e^{j\omega})}$$

**Intuition:** Multiplying a signal by $n$ in the time domain corresponds to differentiating its spectrum with respect to $\omega$ and multiplying by $j$. This is the **dual** of the time-shifting property (shift in time → multiply by complex exponential in frequency).The key takeaways:
![[../Attachments/image-3.png]]
**Parseval:** You never have to sum $|x[n]|^2$ over all $n$ — you can integrate the energy spectral density $|X(e^{j\omega})|^2$ over $[-\pi, \pi]$ instead. Both give the same total energy.

**Derivative property:** The $j$ factor appears because differentiating $e^{-j\omega n}$ with respect to $\omega$ pulls out $-jn$, and when you move the $-j$ to the other side it becomes $+j$. This property is useful for finding the DTFT of signals like $n \cdot u[n]$ or $n \cdot a^n u[n]$ — instead of computing the transform from scratch, you differentiate a known DTFT and multiply by $j$.


---


## Recap + Property 8 — Symmetry Properties

First, the top line is the DTFT pair from Property 7 (recap):

$$n \cdot x[n] \xleftrightarrow{\text{DTFT}} j\frac{d}{d\omega}X(e^{j\omega})$$

And the two complex conjugate identities shown (used in the proof below):

$$(ab)^* = a^* b^* \qquad (a+b)^* = a^* + b^*$$

---

## Property 8 — Symmetry Properties

### Definitions
![[../Attachments/image-5.png]]
**Conjugate symmetric (even symmetric)** — a signal satisfies:

$$x[n] = x^*[-n]$$

This means if you flip the signal in time AND take its complex conjugate, you get back the same signal. For real signals this reduces to ordinary even symmetry: $x[n] = x[-n]$.

**Conjugate anti-symmetric (odd symmetric)** — a signal satisfies:

$$x[n] = -x^*[-n]$$

Same idea but with a sign flip. For real signals this reduces to odd symmetry: $x[n] = -x[-n]$.

---

### Key theorem: The DTFT of a real signal is conjugate symmetric (even)

This is the most important result on this slide. If $x[n]$ is real, then:

$$X^*(e^{j\omega}) = X(e^{-j\omega})$$

meaning the spectrum at $+\omega$ is the complex conjugate of the spectrum at $-\omega$. This is why for real signals you only need to look at $\omega \in [0, \pi]$ — the negative-frequency half carries no new information.

---

### Proof

Start with the DTFT definition:

$$X(e^{j\omega}) = \sum_{n=-\infty}^{\infty} x[n], e^{-j\omega n}$$

Since $x[n]$ is real, $x^*[n] = x[n]$. Now take the complex conjugate of the entire DTFT:

$$X(e^{j\omega}) = \sum_{n=-\infty}^{\infty} x[n] \, e^{-j\omega n}$$

Apply $(ab)^* = a^* b^*$ and $(a+b)^* = a^* + b^*$ to distribute the conjugate inside the sum:

$$X(e^{j\omega}) = \sum_{n=-\infty}^{\infty} x[n] \, e^{-j \omega n}$$

Since $x[n]$ is real, replace $x^*[n]$ with $x[n]$:

$$X^*(e^{j\omega}) = \sum_{n=-\infty}^{\infty} x[n], e^{+j\omega n} = \sum_{n=-\infty}^{\infty} x[n], e^{-j(-\omega)n} = X(e^{-j\omega})$$

$$\boxed{X^*(e^{j\omega}) = X(e^{-j\omega})}$$

This completes the proof. 
![[../Attachments/image-4.png]]
The practical punchline: whenever you see a spectrum plot of a real-world signal (audio, images, sensor data — all real-valued), the left half is always a mirror of the right half. That's this theorem at work. Engineers exploit it constantly — if you're running an FFT on a real signal with $N$ points, you only need to compute $N/2 + 1$ unique frequency bins.

---
the DTFT of pure imaginary signal :
	is odd symmetric (conjugate anti-symmetric)
the DTFT of even symmetric signal :
	is pure real
the DTFT of old symmetric signal :
	is pure imaginary .



> [!quote] It's so simple to be wise. Just think of something stupid to say and then don't say it.
> — Sam Levenson

**"اللهم إني أسألك فهم النبيين، وحفظ المرسلين، والملائكة المقربين، اللهم اجعل ألسنتنا عامرة بذكرك، وقلوبنا بخشيتك، إنك على كل شيء قدير"**


---
 

## 1. المقدمة: الفرق بين DTFT و DFT

**تحويل فورييه للزمن المنفصل (DTFT):**
$$X(e^{j\omega}) = \sum_{n=-\infty}^{\infty} x[n]e^{-j\omega n}$$

- يحول الإشارة من **الزمن المنفصل** $n$ إلى **التردد المستمر** $\omega$
- التردد $\omega$ هنا متغير مستمر (continuous)، أي له قيم لا نهائية
- لهذا السبب، **لا يمكن** حسابه مباشرة على الكمبيوتر

**تحويل فورييه المنفصل (DFT):**
$$X[k] = \sum_{n=0}^{N-1} x[n]e^{-j\frac{2\pi}{N}kn}$$

- لجعل الحساب ممكنًا على الكمبيوتر، قمنا بأمرين:
  1. **أخذ عينات (Sampling)** من التردد: $\omega = \frac{2\pi k}{N}$
  2. **تقليص المجموع** لعدد محدود من العينات $N$
- إذن: DFT = نسخة مخففة (Sampled) من الـ DTFT يمكن حسابها رقميًا

> **ملاحظة مهمة:** عند استخدام DFT، يجب أن تكون الإشارة محدودة (Finite). إذا كانت الإشارة تمتد للما لا نهاية، نقوم بـ **Truncation** (قصها) بضربها في نافذة مستطيلة (Rectangular Window)، وهذا يسبب تشويهًا طفيفًا في التردد.

---

## 2. DTFT للإشارات الأساسية

###  (Impulse) $\delta[n]$
$$\delta[n] \xleftrightarrow{\text{DTFT}} 1$$

**التفسير:** الدالة $\delta[n]$ موجودة فقط عند $n=0$. عند التحويل، يبقى لدينا فقط حد واحد = 1. 
- في الزمن: نبضة قصيرة جدًا عند الصفر
- في التردد: محتوى ترددي ثابت (كل الترددات موجودة بنفس القدر)

---

### ب) الأسي الجانبي الأيمن (Right-Sided Exponential)
$$x[n] = a^n u[n]$$

$$X(e^{j\omega}) = \frac{1}{1 - ae^{-j\omega}}, \quad \text{عندما } |a| < 1$$

**التفسير:**
- $u[n]$ تجعل المجموع يبدأ من $n=0$ إلى $\infty$
- الناتج هو **متسلسلة هندسية** لانهائية: $1 + ae^{-j\omega} + a^2e^{-j2\omega} + \dots$
- شرط التقارب: يجب أن يكون $|ae^{-j\omega}| < 1$
- لأن $|e^{-j\omega}| = 1$ دائمًا، فالشرط يبسط إلى: **$|a| < 1$**
- إذا كان $|a| \geq 1$: المجموع ينفجر للما لا نهاية → الـ DTFT **غير موجود**

---

### ج) الأسي الجانبي الأيسر (Left-Sided Exponential)
$$x[n] = -a^n u[-n-1]$$

$$X(e^{j\omega}) = \frac{1}{1 - ae^{-j\omega}}, \quad \text{عندما } |a| > 1$$

**التفسير:**
- $u[-n-1]$ تجعل الإشارة موجودة فقط عند $n \leq -1$
- بعد التعويض والتبسيط، نصل لنفس الصيغة السابقة!
- لكن الشرط هنا معكوس: **$|a| > 1$**
- هذا يعني: نفس الصيغة الرياضية، لكن لمناطق مختلفة من قيمة $a$

---

### د) الإشارة الثابتة $x[n] = 1$
$$X(e^{j\omega}) = 2\pi \sum_{k=-\infty}^{\infty} \delta(\omega - 2\pi k)$$

**التفسير:**
- إشارة ثابتة في الزمن = تردد صفر فقط
- لكن بما أن الـ DTFT دوري بـ $2\pi$، فنحصل على **قطارات نبضات** (Impulse Train) عند كل $2\pi k$
- كل نبضة ارتفاعها $2\pi$

---

### هـ) دالة الدرجة الواحدة (Unit Step) $u[n]$
$$X(e^{j\omega}) = \frac{1}{1-e^{-j\omega}} + \pi \sum_{k=-\infty}^{\infty} \delta(\omega - 2\pi k)$$

**التفسير:**
- لا يمكن حسابها مباشرة بالمتسلسلة الهندسية لأن $|e^{-j\omega}| = 1$ (الحد الأدنى للتقارب)
- يتم اشتقاقها باعتبارها: $u[n] = \frac{1}{2}\text{sgn}[n] + \frac{1}{2}$
- الجزء الأول: $\frac{1}{1-e^{-j\omega}}$ (الجزء المستمر)
- الجزء الثاني: $\pi \sum \delta(\omega - 2\pi k)$ (نبضات عند مضاعفات $2\pi$)

---

## 3. خصائص الـ DTFT

### الخاصية 1: الدورية (Periodicity)
$$X(e^{j(\omega + 2\pi)}) = X(e^{j\omega})$$

**البرهان:** $e^{-j(\omega+2\pi)n} = e^{-j\omega n} \cdot e^{-j2\pi n} = e^{-j\omega n} \cdot 1 = e^{-j\omega n}$

> الـ DTFT دائمًا دوري بفترة $2\pi$. لهذا السبب نكتب الإشارة الثابتة كمجموع نبضات متكررة وليس نبضة واحدة.

---

### الخاصية 2: الخطية (Linearity)
$$\text{DTFT}\{\alpha_1 x_1[n] + \alpha_2 x_2[n]\} = \alpha_1 X_1(e^{j\omega}) + \alpha_2 X_2(e^{j\omega})$$

**التفسير:** يمكن فك الإشارة المركبة وتحويل كل جزء على حدة ثم جمع النتائج.

---

### الخاصية 3: الإزاحة في الزمن (Time Shift)
$$x[n-k] \xleftrightarrow{\text{DTFT}} e^{-j\omega k} X(e^{j\omega})$$

**التفسير العميق:**
- **التأخير في الزمن** $\rightarrow$ **ضرب في أسي مركب** في التردد
- **المركب (Magnitude):** $|e^{-j\omega k}| = 1$ → لا يتغير!
- **الطور (Phase):** $\angle e^{-j\omega k} = -\omega k$ → إزاحة خطية

> **لماذا الإزاحة الخطية مهمة؟**
> - إزاحة خطية في الطور تعني أن كل الترددات تتأخر بنفس مقدار الوقت $k$
> - هذا يحافظ على شكل الإشارة (No Phase Distortion)
> - لو كانت الإزاحة غير خطية، لاختلف شكل الإشارة بعد المرور بالنظام

---

### الخاصية 4: الإزاحة في التردد (Frequency Shift) / التضمين (Modulation)
$$e^{j\omega_0 n} x[n] \xleftrightarrow{\text{DTFT}} X(e^{j(\omega - \omega_0)})$$

**التفسير:**
- **الضرب في أسي مركب في الزمن** $\rightarrow$ **إزاحة في التردد**
- هذا أساس **التضمين (Modulation)** في الاتصالات:
  - عند المرسل: نضرب الإشارة الأساسية (Baseband) في $e^{j\omega_0 n}$ لننقلها لتردد أعلى
  - عند المستقبل: نضرب مرة أخرى في نفس الأس لإرجاعها للتردد الأصلي
  - ثم نستخدم **فلتر تمرير منخفض (Low-pass Filter)** لاستعادة الإشارة الأصلية

**التطبيق العملي:**
- نقل صوت المذيع (تردد منخفض) لتردد محطة الراديو (تردد عالٍ)
- عند الاستقبال: نزلها للتردد الأساسي مرة أخرى

---

### الخاصية 5: نظرية الالتفاف (Convolution Theorem)
$$x[n] * h[n] \xleftrightarrow{\text{DTFT}} X(e^{j\omega}) \cdot H(e^{j\omega})$$

**التفسير:**
- **الالتفاف في الزمن** (صعب، مجموع لانهائي) $\rightarrow$ **ضرب في التردد** (سهل، نقطة بنقطة)
- في أنظمة LTI: $y[n] = x[n] * h[n]$
- في التردد: $Y(e^{j\omega}) = X(e^{j\omega}) \cdot H(e^{j\omega})$

**التأثير على المركب والطور:**
- $|Y| = |X| \cdot |H|$ (ضرب المراكب)
- $\angle Y = \angle X + \angle H$ (جمع الطورات)

**التطبيق: الفلاتر (Filtering)**
- $|H(e^{j\omega})|$ يحدد أي الترددات تمر وأيها تُمنع:
  - **Low-pass Filter:** $|H| \approx 1$ عند الترددات المنخفضة، $|H| \approx 0$ عند العالية
  - **High-pass Filter:** العكس
  - **Band-pass Filter:** يمر نطاق معين فقط

**نموذج القناة (Channel Model):**
القناة في الاتصالات تؤثر في الإشارة بثلاث طرق:
1. **Filtration:** تقييد النطاق الترددي
2. **Delay:** تأخير في الوصول
3. **Attenuation:** تضاؤل في السعة

المستقبل يقوم بـ:
- **Demodulation** (إزالة التضمين)
- **Amplification** (تعويض التضاؤل)
- **Filtering** (استعادة النطاق الترددي)

> **ملاحظة:** التأخير (Delay) لا يمكن تعويضه في المستقبل لأن الإشارة وصلت متأخرة بالفعل!

---

### الخاصية 6: نظرية بارسيفال (Parseval's Theorem) - حفظ الطاقة
$$\sum_{n=-\infty}^{\infty} |x[n]|^2 = \frac{1}{2\pi} \int_{-\pi}^{\pi} |X(e^{j\omega})|^2 d\omega$$

**التفسير:**
- الطاقة الكلية للإشارة هي نفسها سواء حسبتها في الزمن أو في التردد
- $|X(e^{j\omega})|^2$ تُسمى **كثافة الطاقة الطيفية (Energy Spectral Density)**
- العامل $\frac{1}{2\pi}$ يعوض عن التغيير في متغير التكامل

---

### الخاصية 7: الاشتقاق في التردد (ضرب في n في الزمن)
$$n \cdot x[n] \xleftrightarrow{\text{DTFT}} j\frac{d}{d\omega}X(e^{j\omega})$$

**التفسير:**
- الضرب في $n$ في الزمن $\rightarrow$ اشتقاق في التردد + ضرب في $j$
- مفيدة لحساب تحويلات إشارات مثل $n \cdot a^n u[n]$ بدلًا من البدء من الصفر

---

### الخاصية 8: خصائص التماثل (Symmetry Properties)

**التعريفات:**
- **متناظرة مرافقة (Conjugate Symmetric):** $x[n] = x^*[-n]$
- **معاكسة مرافقة (Conjugate Anti-symmetric):** $x[n] = -x^*[-n]$

**النتائج المهمة:**

| إشارة الزمن $x[n]$ | طيف التردد $X(e^{j\omega})$ |
|---|---|
| **حقيقية** (Real) | متناظر مرافق: $X^*(e^{j\omega}) = X(e^{-j\omega})$ |
| **حقيقية + زوجية** (Even) | **حقيقي** (Pure Real) |
| **حقيقية + فردية** (Odd) | **تخيلي** (Pure Imaginary) |
| **تخيلية صرفة** | معاكسة مرافقة |

**الفائدة العملية:**
- للإشارات الحقيقية، الطيف عند $+\omega$ هو المرافق للطيف عند $-\omega$
- لذلك لا نحتاج لحساب إلا نصف الطيف! (من $0$ إلى $\pi$)
- هذا هو أساس **rFFT** في برمجة Python/MATLAB التي توفر نصف الحسابات

---

## 4. أمثلة تطبيقية

### مثال 1: DTFT لـ $\cos(\omega_0 n)$

باستخدام متطابقة أويلر:
$$\cos(\omega_0 n) = \frac{1}{2}e^{j\omega_0 n} + \frac{1}{2}e^{-j\omega_0 n}$$

باستخدام خاصية الإزاحة في التردد:
$$X(e^{j\omega}) = \pi \sum_{k=-\infty}^{\infty} \left[ \delta(\omega - \omega_0 - 2\pi k) + \delta(\omega + \omega_0 - 2\pi k) \right]$$

**التفسير:**
- في التردد: نبضتان عند $\pm\omega_0$ (ومتكررتان كل $2\pi$)
- ارتفاع كل نبضة = $\pi$
- الطيف **حقيقي** (لأن الكوساين زوجية)

---

### مثال 2: DTFT لـ $\sin(\omega_0 n)$

$$\sin(\omega_0 n) = \frac{1}{2j}e^{j\omega_0 n} - \frac{1}{2j}e^{-j\omega_0 n}$$

$$X(e^{j\omega}) = \frac{\pi}{j} \sum_{k=-\infty}^{\infty} \left[ \delta(\omega - \omega_0 - 2\pi k) - \delta(\omega + \omega_0 - 2\pi k) \right]$$

**التفسير:**
- نبضتان عند $\pm\omega_0$ بإشارة معاكسة
- الطيف **تخيلي صرف** (لأن الساين فردية)
- هذا يتوافق مع خاصية التماثل: إشارة فردية $\rightarrow$ طيف تخيلي

---

## 5. ملخص العلاقات المزدوجة (Duality)

| في الزمن (Time Domain) | في التردد (Frequency Domain) |
|---|---|
| إزاحة: $x[n-k]$ | ضرب بأسي: $e^{-j\omega k}X(e^{j\omega})$ |
| ضرب بأسي: $e^{j\omega_0 n}x[n]$ | إزاحة: $X(e^{j(\omega-\omega_0)})$ |
| التفاف: $x[n]*h[n]$ | ضرب: $X \cdot H$ |
| ضرب: $n \cdot x[n]$ | اشتقاق: $j\frac{dX}{d\omega}$ |

---

## 6. نصائح للحفظ والفهم

1. **الدلتا في الزمن** $\rightarrow$ **ثابت في التردد** (والعكس)
2. **الأسي الجانبي** $\rightarrow$ **بسط يحتوي على $1/(1-ae^{-j\omega})$**
3. **التأخير في الزمن** $\rightarrow$ **طور سالب خطي** (المعكوس يحافظ على الشكل)
4. **التضمين** $\rightarrow$ **نقل الإشارة لتردد أعلى** للإرسال
5. **الالتفاف** $\rightarrow$ **فلترة** (النظام يختار الترددات)
6. **الإشارة الحقيقية** $\rightarrow$ **طيف متناظر** (احسب نصفه فقط)

---

> **الخلاصة:** DTFT ليس مجرد رياضيات، بل هو أداة لتحليل الإشارات والأنظمة. كل خاصية لها تطبيق مباشر في معالجة الإشارات والاتصالات. الفهم الجيد لهذه الأساسيات يسهل فهم مراحل متقدمة مثل Sampling, Filtering, و Modulation.