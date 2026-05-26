"""
signal_generator.py
-------------------
Responsible for generating all types of discrete-time signals.
Each function returns a tuple of (time array, signal array).

A "discrete-time signal" is just a list of sample values taken at
equally-spaced time points: n = 0, 1/Fs, 2/Fs, ..., (N-1)/Fs
where Fs is the sampling frequency and N is the number of samples.
"""

import numpy as np


class SignalGenerator:
    """
    Generates common DSP test signals.

    Parameters (set by the GUI and stored here):
        frequency  (Hz)  - oscillation rate of the signal
        amplitude         - peak value of the signal
        fs         (Hz)  - sampling frequency (samples per second)
        n_samples         - total number of samples to generate
        phase      (rad) - phase offset for sinusoidal signals
        duty_cycle (0-1) - for square wave, fraction of period that is HIGH
    """

    def __init__(self, frequency=5.0, amplitude=1.0, fs=100.0,
                 n_samples=256, phase=0.0, duty_cycle=0.5):
        self.frequency = frequency
        self.amplitude = amplitude
        self.fs = fs
        self.n_samples = n_samples
        self.phase = phase
        self.duty_cycle = duty_cycle

    # ------------------------------------------------------------------ helpers
    def _time_axis(self):
        """Return the time axis array t[n] = n / Fs for n in 0..N-1."""
        return np.arange(self.n_samples) / self.fs

    # ------------------------------------------------------------------ signals
    def sine_wave(self):
        """x[n] = A * sin(2π f n/Fs + φ)"""
        t = self._time_axis()
        x = self.amplitude * np.sin(2 * np.pi * self.frequency * t + self.phase)
        return t, x

    def cosine_wave(self):
        """x[n] = A * cos(2π f n/Fs + φ)"""
        t = self._time_axis()
        x = self.amplitude * np.cos(2 * np.pi * self.frequency * t + self.phase)
        return t, x

    def square_wave(self):
        """
        x[n] = +A when sin(2π f n/Fs) >= 0  (if duty_cycle = 0.5)
        More precisely: use modulo arithmetic to create a duty-cycle-aware square.
        """
        t = self._time_axis()
        # Normalised phase within one period: 0 → 1
        period = 1.0 / self.frequency if self.frequency > 0 else 1.0
        phase_in_period = (t % period) / period
        x = self.amplitude * np.where(phase_in_period < self.duty_cycle, 1.0, -1.0)
        return t, x

    def impulse(self):
        """
        Unit impulse (Kronecker delta) scaled by amplitude.
        δ[n] = A if n == 0, else 0.
        """
        t = self._time_axis()
        x = np.zeros(self.n_samples)
        x[0] = self.amplitude          # spike at n = 0
        return t, x

    def random_signal(self):
        """White Gaussian noise with zero mean and amplitude as std-dev."""
        t = self._time_axis()
        rng = np.random.default_rng(seed=42)   # fixed seed for reproducibility
        x = self.amplitude * rng.standard_normal(self.n_samples)
        return t, x

    def custom_signal(self, values_str: str):
        """
        Parse a comma-separated string of floats entered by the user.
        Example: "1, 0.5, -1, 0.5, 1"
        Returns (t, x) where t is integer sample indices.
        """
        values = [float(v.strip()) for v in values_str.split(",") if v.strip()]
        x = np.array(values)
        t = np.arange(len(x)) / self.fs
        return t, x
