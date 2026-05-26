"""
fourier_transforms.py
---------------------
Implements DTFT, DFT (manual), and FFT (NumPy) for a discrete-time signal x[n].

Mathematical background
-----------------------
Let x[n] be a length-N discrete-time signal.

DTFT  — Discrete-Time Fourier Transform
  X(e^jω) = Σ_{n=0}^{N-1}  x[n] · e^{-jωn}     ω ∈ [0, 2π)
  • Continuous in frequency ω.
  • We approximate it by evaluating at many equally-spaced ω points (e.g. 1024).
  • Result: a complex array; |X| = magnitude, ∠X = phase.

DFT   — Discrete Fourier Transform
  X[k]  = Σ_{n=0}^{N-1}  x[n] · e^{-j2πkn/N}    k = 0, 1, ..., N-1
  • Discrete in both time and frequency.
  • Implemented here naively: O(N²) double loop — educational but slow.
  • Equivalent to sampling the DTFT at ω_k = 2πk/N.

FFT   — Fast Fourier Transform (Cooley-Tukey algorithm)
  Mathematically identical to the DFT; produces the same X[k].
  Implemented in O(N log N) via numpy.fft.fft.
  For large N the speed difference is dramatic.
"""

import numpy as np
import time


class FourierTransforms:
    """Encapsulates DTFT, manual DFT, and NumPy FFT computations."""

    # ------------------------------------------------------------------ DTFT
    @staticmethod
    def dtft(x: np.ndarray, num_freq_points: int = 1024):
        """
        Approximate the DTFT of x[n] evaluated at `num_freq_points` ω values
        uniformly spaced in [0, 2π).

        Returns
        -------
        omega : np.ndarray  shape (num_freq_points,)
            Angular frequency axis in radians/sample.
        X     : np.ndarray  shape (num_freq_points,), complex
            Complex DTFT values.
        """
        N = len(x)
        omega = np.linspace(0, 2 * np.pi, num_freq_points, endpoint=False)
        # n = [0, 1, 2, ..., N-1]  →  shape (N,)
        n = np.arange(N)

        # Vectorised outer product:
        # phase_matrix[k, n] = omega[k] * n   →  shape (num_freq_points, N)
        phase_matrix = np.outer(omega, n)

        # X[k] = Σ_n x[n] * exp(-j * omega[k] * n)
        # = (exp(-j * phase_matrix)) @ x       →  shape (num_freq_points,)
        X = np.exp(-1j * phase_matrix) @ x
        return omega, X

    # ------------------------------------------------------------------ DFT
    @staticmethod
    def dft_manual(x: np.ndarray):
        """
        Manual (naive) DFT implementation using the definition formula.
        Time complexity: O(N²) — intentionally slow to contrast with FFT.

        X[k] = Σ_{n=0}^{N-1}  x[n] · e^{-j2πkn/N}

        Returns
        -------
        freqs     : np.ndarray  integer bin indices 0..N-1
        X         : np.ndarray  complex DFT coefficients
        elapsed   : float  computation time in seconds
        """
        N = len(x)
        X = np.zeros(N, dtype=complex)

        start = time.perf_counter()
        n = np.arange(N)                         # sample indices
        for k in range(N):
            # Twiddle factor for bin k: W_N^k = e^{-j2πkn/N}
            twiddle = np.exp(-1j * 2 * np.pi * k * n / N)
            X[k] = np.dot(x, twiddle)            # inner product = Σ x[n]·W
        elapsed = time.perf_counter() - start

        freqs = np.arange(N)
        return freqs, X, elapsed

    # ------------------------------------------------------------------ FFT
    @staticmethod
    def fft_numpy(x: np.ndarray):
        """
        FFT via numpy.fft.fft.
        Mathematically the same as DFT but O(N log N) — much faster.

        Returns
        -------
        freqs   : np.ndarray  integer bin indices 0..N-1
        X       : np.ndarray  complex FFT coefficients
        elapsed : float  computation time in seconds
        """
        start = time.perf_counter()
        X = np.fft.fft(x)
        elapsed = time.perf_counter() - start

        freqs = np.arange(len(x))
        return freqs, X, elapsed

    # ------------------------------------------------------------------ helpers
    @staticmethod
    def magnitude(X: np.ndarray):
        """Return |X| normalised to the number of points."""
        return np.abs(X) / len(X)

    @staticmethod
    def phase(X: np.ndarray):
        """Return ∠X in degrees, zeroing out values where |X| is negligible."""
        mag = np.abs(X)
        threshold = 1e-6 * np.max(mag) if np.max(mag) > 0 else 1e-10
        ph = np.angle(X, deg=True)
        ph[mag < threshold] = 0.0     # suppress numerical noise
        return ph

    @staticmethod
    def freq_axis_hz(N: int, fs: float):
        """
        Convert DFT/FFT bin indices to Hz using the sampling frequency.
        We only show the one-sided spectrum (0 to Fs/2) because the
        negative-frequency half is a mirror image for real signals.

        Returns
        -------
        freqs_hz : np.ndarray  shape (N//2,)
        half     : int  number of bins in one-sided spectrum
        """
        half = N // 2
        freqs_hz = np.fft.fftfreq(N, d=1.0 / fs)[:half]
        return freqs_hz, half
