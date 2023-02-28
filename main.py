import time
from src.capture_audio import capture_audio
from src.speech_to_text import speech_to_text
from src.chatbot import ChatBot
from src.text_to_speech import text_to_speech
import numpy as np

def main():    
    ds = speech_to_text() # Initialize the DeepSpeech engine   
    chatbot = ChatBot()  # Initialize the chatbot

    # Continuously capture audio from the microphone and transcribe it
    while True:       
        input("Press Enter to start listening: ") # Wait for user input to start listening

        # Initialize variables to store audio data and track silence
        audio_data = np.array([], dtype=np.int16)
        silence_threshold = 1000 # Set a threshold for the volume of "silence"
        silence_duration_limit = 1.0 # Set a limit for how long silence can last (in seconds)
        last_spoken_time = time.time() # Initialize the time of the last spoken word

        # Continuously capture audio until there is a period of silence longer than the limit
        while True:            
            chunk = capture_audio() # Capture a chunk of audio
            audio_data = np.concatenate((audio_data, chunk)) # Add the chunk to the array of audio data

            # If there is no audio in the chunk, break out of the loop
            if len(chunk) == 0:
                break

            volume = np.abs(chunk).mean()  # Calculate the volume of the chunk

            # If the volume is below the silence threshold, check how long it has been silent for
            if volume < silence_threshold:
                duration = time.time() - last_spoken_time # Calculate the duration of the silence
                # If the duration of the silence is longer than the limit, break out of the loop
                if duration > silence_duration_limit:
                    break

            # If the volume is above the silence threshold, update the time of the last spoken word
            else:
                last_spoken_time = time.time()

        text = ds.stt(audio_data) # Use DeepSpeech to transcribe the audio data
        print("You said:", text) # Print the transcribed text

        # Pass the text to the chatbot to get a response
        response = chatbot.get_response(text)
        print("Chatbot says:", response)

        # Generate speech output from the response using gTTS
        text_to_speech(response)

# Ensure that the main() function is only called if the main.py file is being run as the main module, 
# rather than being imported by another module.
if __name__ == "__main__":
    main()