from transformers import pipeline

class Translator:
    def __init__(self, model_name: str = "Helsinki-NLP/opus-mt-en-ar"):
        """
        Initializes the Translator with the specified model.

        :param model_name: The model name for translation.
        """
        try:
            self.pipe = pipeline("translation", model=model_name)
        except Exception as e:
            print(f"Error loading translation model: {e}")

    def translate(self, text: str) -> str:
        """
        Translates text to Arabic.

        :param text: The text to translate.
        :return: The translated text.
        """
        try:
            result = self.pipe(text)
            return result[0]['translation_text']
        except Exception as e:
            print(f"Error during translation: {e}")
            return ""
