import streamlit as st
import streamlit as st
from PIL import Image
import numpy as np
import cv2
import io
import numpy as np

from config import config
from yolo_detect import model

if __name__ == "__main__":
    
    st.title("Кадастровый участок")
    st.session_state[f"are_images_labeled"] = False
    
    cadastral_numbers = st.text_input(
        "Кадастровый номер или несколько, через запятые", 
        value="71:11:010201:78, 71:11:010301:3327"
    )
    
    st.session_state[f"cadastral_numbers"] = cadastral_numbers.split(',')
    
    st.selectbox(
        "Файлы на выходе", 
        options=['Табличка', 'Фото с боксами'], 
        index=0, 
        key=f"animation_selectbox"
    )
    
    t = st.slider(label='Threshold for Yolo, %', min_value=0, max_value=100, value=20)


    if st.button(label="Получить всю аналитику", key=f"button"):

        f = f'{np.random.randint(1,100)}.png'
        image = model.get_boxs(thr=t /100)
        st.session_state[f"are_images_labeled"] = True

        st.write('Пример работы')
        st.image(np.array(image))

