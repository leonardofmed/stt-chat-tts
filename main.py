import time
from src.capture_audio import capture_audio
from src.speech_to_text import speech_to_text

# Define the DeepSpeech model path
MODEL_PATH = "models/deepspeech-0.9.3-models.pbmm"

def main():
    # Initialize the DeepSpeech engine
    ds = speech_to_text(model_path=MODEL_PATH)

    # Continuously capture audio from the microphone and transcribe it
    while True:
        audio_data = capture_audio()
        text = ds.stt(audio_data)
        print(text)
        time.sleep(1)

# Ensure that the main() function is only called if the main.py file is being run as the main module, 
# rather than being imported by another module.
if __name__ == "__main__":
    main()