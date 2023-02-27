import deepspeech

class speech_to_text:
    def __init__(self):
        """
        Initializes the DeepSpeech speech-to-text engine with the specified model file.
        It uses the deepspeech library to load the DeepSpeech model from the specified file path, 
        and also loads an external scorer to improve the accuracy of the transcription.
        """
        self.model = deepspeech.Model("models/deepspeech-0.9.3-models.pbmm")
        self.model.enableExternalScorer("models/deepspeech-0.9.3-models.scorer")

    def stt(self, audio_data):
        """Performs speech-to-text transcription on the specified audio data."""
        text = self.model.stt(audio_data)
        return text