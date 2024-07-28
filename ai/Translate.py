from transformers import pipeline

class Translator:
    def __init__(self, model_name="Helsinki-NLP/opus-mt-en-ar"):
        self.pipe = pipeline("translation", model=model_name)

    def translate(self, text):
        result = self.pipe(text)
        return result[0]['translation_text']
