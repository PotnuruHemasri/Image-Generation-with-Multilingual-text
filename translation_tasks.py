import ollama

client = ollama.Client()


model = "llama3.2"


def translate_text(text: str, target_language: str, model=model) -> str:
    """
    Translate the given text into the target language using the specified model.

    Args:
        text (str): The text to be translated.
        target_language (str): The target language for translation.

    Returns:
        str: The translated text.
    """
    prompt = f"Translate the following text to {target_language}: {text} and just give me the translated text! in a single line of just the translation"
    # response = client.chat(model=model, messages=[{"role": "user", "content": prompt}])
    response = client.generate(model=model, prompt=prompt)
    return response.response
