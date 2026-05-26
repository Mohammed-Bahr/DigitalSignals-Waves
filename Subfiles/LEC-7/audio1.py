import pyaudio
import wave
import numpy as np

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100


def ReadFromMic(RECORD_SECONDS):
    p = pyaudio.PyAudio()
    stream = p.open(
        format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK
    )
    print("* recording")
    frames = []
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)
    print("* done recording")
    stream.stop_stream()
    stream.close()
    p.terminate()
    frames1 = bytes([item for sublist in frames for item in sublist])
    x = np.frombuffer(frames1, dtype="<i2").copy()
    return x


def WriteToSpeakers(x):
    data = np.array(x, "<i2").tobytes()
    p = pyaudio.PyAudio()
    stream = p.open(
        format=FORMAT,
        channels=CHANNELS,
        rate=RATE,
        output=True,
        frames_per_buffer=CHUNK,
    )
    for i in range(0, len(data), CHUNK):
        chunk = data[i : i + CHUNK]
        stream.write(chunk)
    stream.stop_stream()
    stream.close()
    p.terminate()


x = ReadFromMic(5)
N = 25
fc = 2000
wc = fc / (0.5 * RATE) * np.pi
n = np.arange(-N, N + 1)
h = wc / np.pi * np.sinc(wc / np.pi * n)
delta = np.zeros(2 * N + 1)
delta[N] = 1
h1 = delta - h * np.hamming(2 * N + 1)  # High pass filter with cutoff frequency fc
y = np.convolve(x, h1)
WriteToSpeakers(y)
print(np.sum(np.abs(y[: len(x)] - x)) / len(x))
