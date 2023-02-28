# Speech-to-Text - GPT3 - Text-to-Speech

This is a Python script that uses Mozilla's DeepSpeech library to perform speech-to-text transcription. It captures audio from the microphone and converts it to text using the DeepSpeech model.

The text obtained from the speech-to-text transcription is then used as input to an OpenAI GPT-3 chatbot. The chatbot generates a response based on the input text, which is then transformed into audio using the Google Text-to-Speech API.

## Dependencies
Make sure you have Python 3 installed on your system (Requires maximum Python version 3.9).

To run this project, you need to install the following dependencies:

`pip install deepspeech==0.9.3 numpy pyaudio openai python-dotenv gtts pygame`

### Installing DeepSpeech

The `deepspeech` library requires installation of the pre-trained models in addition to the Python package. Follow the steps below to install the `deepspeech` library:

1. Download the pre-trained models and scorer from the [DeepSpeech releases page](https://github.com/mozilla/DeepSpeech/releases/tag/v0.9.3).

2. Place the contents in a folder named `models` in the project root.

3. Modify the `self.model` variable in the `speech_to_text.py` script to point to the directory containing the pre-trained models and scorer: 

```python
self.model = deepspeech.Model("models/deepspeech-0.9.3-models.pbmm")
self.model.enableExternalScorer("models/deepspeech-0.9.3-models.scorer")
```

## Chatbot

This project uses OpenAI's GPT-3 API to power the chatbot functionality. To use this feature, you'll need to sign up for an API key and set it as an environment variable. Follow these steps:
1.  Sign up for an API key at [https://beta.openai.com/signup/](https://beta.openai.com/signup/).    
2.  Create a new file in the project root called `.env`.    
3.  In the `.env` file, add the following line with your API key:    

`API_KEY=your_api_key_here` 

4.  Save the `.env` file.

## Usage
To run the script, simply execute the `main.py` file:

`python main.py`

The script will capture audio from your microphone and convert it to text using the DeepSpeech model. The resulting text will be printed to the console.

## TODO
- [ ] Allow the user to stop the TTS audio playing manually without exiting the application
- [ ] Add other types of STT and allow user to change between them

## Troubleshooting

If you encounter any issues while installing or running the script, make sure to check the following:
- Make sure you have installed all the required dependencies, including the specific versions mentioned above.
- Make sure you have Python 3 installed on your system.
- Make sure your microphone is connected and working properly.
- If you encounter any issues with PyAudio, try running the script with administrator privileges or installing PyAudio using a different method (e.g., conda or homebrew).
- If you encounter any issues with DeepSpeech, try downloading the latest version of the pre-trained model files from the DeepSpeech releases page on GitHub and modifying the script to use the new files.
- If the audio from the microphone takes a long time to convert to text or is cutting off some of the speech, check if you don't have any other USB devices, such as a webcam, that could be causing interference.