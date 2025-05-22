import streamlit as st
import requests
from PIL import Image
from io import BytesIO
import translation_tasks

# Streamlit app title
st.title("Image Generator")

# Input prompt for the user
prompt = st.text_input("Enter a prompt for the image generator:")

# Translate the prompt to English before sending it for image generation
translated_prompt = translation_tasks.translate_text(prompt, "English")
print(translated_prompt)

# Button to generate the image
if st.button("Generate Image"):
    # API endpoint and payload
    url = "https://8000-01jqta8xsdqvqysj7q72axe0z5.cloudspaces.litng.ai/predict"
    payload = {"prompt": translated_prompt}
    headers = {"Content-Type": "application/json"}

    # Make the API request
    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        # Display the image
        image = Image.open(BytesIO(response.content))
        st.image(image, caption="Generated Image", use_column_width=True)
    else:
        # Display an error message
        st.error(f"Request failed with status code {response.status_code}.")
