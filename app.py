import io
import requests
from PIL import Image
import matplotlib.pyplot as plt
import streamlit as st
from llm import LLM
import sys

image = Image.open("Image/url_image.png")
st.set_page_config(page_title="Know Image",page_icon=image)

hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.image("Image/title.jpg")
st.sidebar.title("Paste Image Link")
input_url = st.sidebar.text_input(label="Input", label_visibility="hidden")
st.sidebar.button("Submit", use_container_width=True)
tab = st.sidebar.radio("tab", 
                       ("Image Description",
                        "Hotel Finder",
                        "Custom Query"),
                        label_visibility="hidden"
                        )

def plot_image(image_url):
    response = requests.get(image_url)
    image = Image.open(
        io.BytesIO(response.content)
        ).resize((1280, 720))
    return image

if input_url:
    st.image(plot_image(input_url))
else:
    sys.exit(0)


gemini = LLM([input_url])

if tab=="Image Description":
    response = gemini.describe_image()
    st.write(f"<span style='color:white'>{response}</span>", unsafe_allow_html=True)

if tab=="Hotel Finder":
    response = gemini.hotel_finder()
    st.write(f"<span style='color:white'>{response}</span>", unsafe_allow_html=True)
    
if tab == "Custom Query":
    prompt: str = st.chat_input("Enter Your Question here")

    USER = "user"
    ASSISTANT = "assistant"

    if prompt:
        st.chat_message(USER).write(f"USER: {prompt}")
        response = gemini.custom_query(prompt)
        st.chat_message(ASSISTANT).write(f"GEMINI: {response}")









