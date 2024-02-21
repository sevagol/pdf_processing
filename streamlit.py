import streamlit as st
from openai import OpenAI
import openai
from pdf_to_image import *
from split_img_into_pieces import *
from openai_processing import *

import streamlit as st
from PIL import Image
import io
import base64

st.header("Convert diploma to JSON")

file = st.file_uploader("Choose a file")

def image_to_base64(_image):
    img_byte_arr = io.BytesIO()
    _image.save(img_byte_arr, format=_image.format)  # Используем _image вместо image
    img_byte_arr = img_byte_arr.getvalue()
    return base64.b64encode(img_byte_arr).decode('utf-8')

if file and st.button('Convert PDF to Images'):
    # Запускаем процесс конвертации и сохраняем результаты в session_state
    images = convert_pdf_to_images(file.read())
    st.session_state['summaries'] = []

    for i, img in enumerate(images):
        progress_value = (i + 1) / len(images)
        st.progress(progress_value)
        img_base64 = image_to_base64(img)
        summary = image_captioning(img_base64)
        st.session_state['summaries'].append(summary)

# Если в session_state уже есть список summaries, используем его для отображения
if 'summaries' in st.session_state and st.session_state['summaries']:
    index_list = list(range(1, len(st.session_state['summaries']) + 1))
    selected_index = st.select_slider("Select page", options=index_list, value=1)
    st.json(st.session_state['summaries'][selected_index - 1])
