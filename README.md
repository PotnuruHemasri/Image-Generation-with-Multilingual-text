# Image Generation with Multilingual text

This project is a Streamlit-based web application that generates images based on user-provided prompts. The application supports multilingual prompts by translating them into English before sending them to an image generation API.

## Features

- **Multilingual Support**: Prompts can be entered in any language, and they will be translated to English using the `translate_text` function from the `translation_tasks.py` module.
- **Image Generation**: Uses an external API to generate images based on the translated prompt.
- **Streamlit Interface**: Provides a user-friendly interface for entering prompts and viewing generated images.

## Project Structure

- `image_generator_app.py`: Main Streamlit application for the image generator.
- `translation_tasks.py`: Contains the `translate_text` function for translating prompts.
- `flux_dev.ipynb` and `Multilingual_ASR.ipynb`: Not directly related to the image generator but may contain relevant experiments and notes.

## Prerequisites

- Python 3.8 or higher
- Required Python libraries:
  - `streamlit`
  - `requests`
  - `Pillow`
  - `ollama`

pip install -r requirements.txt

>Steps to run
`streamlit run image_generator_app.py`
