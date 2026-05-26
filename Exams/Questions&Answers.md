---
Created: " 2026-04-08 09:44"
tags:
  - FACL
Source:
---
> [!quote] Every man takes the limits of his own field of vision for the limits of the world.
> — Arthur Schopenhauer

**"اللهم إني أسألك فهم النبيين، وحفظ المرسلين، والملائكة المقربين، اللهم اجعل ألسنتنا عامرة بذكرك، وقلوبنا بخشيتك، إنك على كل شيء قدير"**

# Question 1:
### Problem Setup

$$x[n] \rightarrow \boxed{h[n]} \rightarrow y[n]$$

$$y[n] = \frac{3}{4}y[n-1] - \frac{1}{8}y[n-2] + x[n]$$

**Find:**

1. System Frequency Response H($e^{jω}$)
2. Impulse Response h[n]

---

## Step 1: Apply DTFT to Both Sides

Using the **time-shift property**: $y[n-k] \xrightarrow{DTFT} e^{-j\omega k} Y(e^{j\omega})$

$$Y(e^{j\omega}) = \frac{3}{4}Y(e^{j\omega})e^{-j\omega} - \frac{1}{8}Y(e^{j\omega})e^{-2j\omega} + X(e^{j\omega})$$

Move all Y terms to the left:

$$Y(e^{j\omega}) - \frac{3}{4}Y(e^{j\omega})e^{-j\omega} + \frac{1}{8}Y(e^{j\omega})e^{-2j\omega} = X(e^{j\omega})$$

Factor out $Y(e^{j\omega})$:

$$Y(e^{j\omega})\left[1 - \frac{3}{4}e^{-j\omega} + \frac{1}{8}e^{-2j\omega}\right] = X(e^{j\omega})$$

---

## Step 2: Frequency Response H($e^{jω}$)

$$\boxed{H(e^{j\omega}) = \frac{Y(e^{j\omega})}{X(e^{j\omega})} = \frac{1}{1 - \frac{3}{4}e^{-j\omega} + \frac{1}{8}e^{-2j\omega}}}$$

---

## Step 3: Factor the Denominator

We need to factor:

$$1 - \frac{3}{4}e^{-j\omega} + \frac{1}{8}e^{-2j\omega}$$

Let $z = e^{j\omega}$, so we solve:

$$1 - \frac{3}{4}z^{-1} + \frac{1}{8}z^{-2} = 0$$

Multiply by $z^2$:

$$z^2 - \frac{3}{4}z + \frac{1}{8} = 0$$

Using quadratic formula:

$$z = \frac{\frac{3}{4} \pm \sqrt{\frac{9}{16} - \frac{4}{8}}}{2} = \frac{\frac{3}{4} \pm \sqrt{\frac{9}{16} - \frac{8}{16}}}{2} = \frac{\frac{3}{4} \pm \frac{1}{4}}{2}$$

$$z_1 = \frac{1}{2}, \quad z_2 = \frac{1}{4}$$

So the denominator factors as:

$$H(e^{j\omega}) = \frac{1}{(1 - \frac{1}{2}e^{-j\omega})(1 - \frac{1}{4}e^{-j\omega})}$$
---

## Step 4: Partial Fraction Decomposition

$$H(e^{j\omega}) = \frac{A}{1 - \frac{1}{2}e^{-j\omega}} + \frac{B}{1 - \frac{1}{4}e^{-j\omega}}$$
### 🎯 Goal

We want to decompose:

$$  
H(e^{j\omega}) = \frac{1}{(1 - \frac{1}{2}e^{-j\omega})(1 - \frac{1}{4}e^{-j\omega})}  
$$

### ⚡ Step 1: Simplify Notation

Let:

$$  
x = e^{-j\omega}  
$$

Now the problem becomes:

$$  
\frac{1}{(1 - \frac{1}{2}x)(1 - \frac{1}{4}x)}  
$$
### ⚡ Step 2: Assume Partial Fractions

$$  
\frac{1}{(1 - \frac{1}{2}x)(1 - \frac{1}{4}x)} =  
\frac{A}{1 - \frac{1}{2}x} + \frac{B}{1 - \frac{1}{4}x}  
$$
### ⚡ Step 3: Multiply Both Sides

Multiply by the denominator:

$$  
1 = A(1 - \frac{1}{4}x) + B(1 - \frac{1}{2}x)  
$$
### ⚡ Step 4: Expand

$$  
1 = A - \frac{A}{4}x + B - \frac{B}{2}x  
$$

Group terms:

$$  
1 = (A + B) + \left(-\frac{A}{4} - \frac{B}{2}\right)x  
$$
### ⚡ Step 5: Compare Coefficients

Match both sides:

##### Constant term:

$$  
A + B = 1  
$$

##### Coefficient of (x):

$$  
-\frac{A}{4} - \frac{B}{2} = 0  
$$
### ⚡ Step 6: Solve the System

From second equation:

$$  
\frac{A}{4} + \frac{B}{2} = 0  
$$

Multiply by 4:

$$  
A + 2B = 0  
$$

Now solve:

$$  
A + B = 1  
$$
$$  
A + 2B = 0  
$$

Subtract:

$$  
(A + 2B) - (A + B) = 0 - 1  
$$

$$  
B = -1  
$$

Then:

$$  
A = 1 - B = 2  
$$

### ✅ Final Result

$$  
H(e^{j\omega}) =  
\frac{2}{1 - \frac{1}{2}e^{-j\omega}} -  
\frac{1}{1 - \frac{1}{4}e^{-j\omega}}  
$$


---

## Step 5: Impulse Response h[n]

Using the **inverse DTFT** pair: $$\frac{1}{1 - ae^{-j\omega}} \xrightarrow{\mathcal{F}^{-1}} a^n u[n]$$
- $a \rightarrow$ is constant .  
$$\boxed{h[n] = 2\left(\frac{1}{2}\right)^n u[n] - \left(\frac{1}{4}\right)^n u[n]}$$

This is a **causal, stable** system since both poles $(\frac{1}{2}, \frac{1}{4})$ are inside the unit circle.