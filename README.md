
# Speech-to-Text with DeepSpeech

This is a Python script that uses Mozilla's DeepSpeech library to perform speech-to-text transcription. It captures audio from the microphone and converts it to text using the DeepSpeech model.

## Dependencies

To run this script, you need to install the following dependencies:

`deepspeech==0.9.3
numpy==1.21.4
pyaudio==0.2.11` 

Make sure you have Python 3 installed on your system as well.

### Installing DeepSpeech

The `deepspeech` library requires installation of the pre-trained models in addition to the Python package. Follow the steps below to install the `deepspeech` library:

1.  Download the pre-trained models from the [DeepSpeech releases page](https://github.com/mozilla/DeepSpeech/releases/tag/v0.9.3).
2.  Extract the contents of the archive to a directory of your choice.
3.  Install the `deepspeech` Python package using pip:

`pip install deepspeech==0.9.3` 

4.  Modify the `model` variable in the `speech_to_text.py` script to point to the directory containing the pre-trained models:

```python
model = deepspeech.Model('/path/to/deepspeech-0.9.3-models.pbmm')
```

## Usage

To run the script, simply execute the `main.py` file:

`python main.py` 

The script will capture audio from your microphone and convert it to text using the DeepSpeech model. The resulting text will be printed to the console.

## Troubleshooting

If you encounter any issues while installing or running the script, make sure to check the following:

-   Make sure you have installed all the required dependencies, including the specific versions mentioned above.
-   Make sure you have Python 3 installed on your system.
-   Make sure your microphone is connected and working properly.
-   If you encounter any issues with PyAudio, try running the script with administrator privileges or installing PyAudio using a different method (e.g., conda or homebrew).
-   If you encounter any issues with DeepSpeech, try downloading the latest version of the pre-trained model files from the DeepSpeech releases page on GitHub and modifying the script to use the new files.
