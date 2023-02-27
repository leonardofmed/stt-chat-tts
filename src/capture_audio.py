import pyaudio
import numpy as np

# Define some constants for audio capture
RATE = 16000
CHUNK_SIZE = 1024

def capture_audio():
    """Captures audio from the default microphone and returns the audio data as a numpy array."""
    audio = pyaudio.PyAudio()
    stream = audio.open(format=pyaudio.paInt16, channels=1, rate=RATE, input=True, frames_per_buffer=CHUNK_SIZE)
    frames = []

    # Capture 5 seconds of audio data by reading chunks from the audio stream.
    for i in range(int(RATE / CHUNK_SIZE * 5)):
        data = stream.read(CHUNK_SIZE, exception_on_overflow=False)
        frames.append(np.frombuffer(data, dtype=np.int16))
        
    audio_data = np.concatenate(frames)
    stream.stop_stream()
    stream.close()
    audio.terminate()
    return audio_data