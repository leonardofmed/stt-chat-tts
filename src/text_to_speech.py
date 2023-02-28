from gtts import gTTS
from io import BytesIO
from pygame import mixer

def text_to_speech(text):
    tts = gTTS(text=text, lang='en')

    # Save the audio as a byte object
    fp = BytesIO()
    tts.write_to_fp(fp)
    fp.seek(0)

    # Initialize pygame mixer
    mixer.init()

    # Load the audio byte object into mixer
    mixer.music.load(fp)

    # Play the audio
    mixer.music.play()

    # Wait for the audio to finish playing before continuing
    while mixer.music.get_busy():
        continue