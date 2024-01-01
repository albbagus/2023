# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 00:43:53 2024

@author: Albertus Bagus

how to run it?

1. Open Anaconda Powershell Prompt
2. Ketikkan 2 baris di bawah ini
conda activate main-ds
streamlit run 2023_Recap.py
"""

import streamlit as st
import requests
from io import BytesIO

# Title
st.title('2023 Recap with Eva')

# Video
st.video('https://github.com/albbagus/2023/raw/main/2023.mp4')

# Text
with st.expander("2023 Recap with Eva"):
    st.write("""
             Eva.
             Salah satu atau bahkan satu-satunya orang yang melihat bagaimana proses pendewasaan Bagus di 2023. Mulai dari Bagus yang malas-malasan, Bagus yang sagapung, Bagus yang tempramen, Bagus yang boros, Bagus yang picky eater, dan banyak lainnya. Hingga di akhir 2023, Bagus perlahan berubah menjadi lebih baik. Setidaknya itu dari sudut pandang Bagus.
             Bagus merasa bahwa banyak pengaruh baik yang diberikan Eva kepada Bagus. Baik itu berupa nasihat, teguran, ataupun teladan. Banyak hal baik yang Bagus dapatkan dari Eva. Setidaknya berkaca pada beberapa hal buruk yang Bagus sebutkan sebelumnya, kini perlahan sudah diperbaiki.
             Terimakasih Eva sudah menjadi (banyak) bagian dari hidup Bagus. Mungkin hampir 24/7, Eva mendampingi Bagus. Menurut Bagus tahun 2023 ini menjadi salah satu tahun terbaiknya. Terlepas dari masih banyak kegagalan dan kekecewaan yang Bagus rasakan tahun ini, banyak hal baik yang bisa Bagus syukuri karena hadirnya Eva disisi Bagus. Bagus senang bisa bersama-sama Eva menjalani 2023 yang penuh kesan dan makna.
             Bagus berharap 2024 bisa menjadi tahun yang baik juga untuk kita berdua. Meskipun Bagus ini kelihatannya memiliki iman yang goyah, percayalah Eva, bahwa dalam setiap doa Bagus ada namamu di sana. Bagus selalu mendoakan Eva mendapatkan hal-hal terbaik. Percayalah juga bahwa Bagus punya cinta yang besar juga untuk Eva. Walaupun kelihatannya Bagus cuek, tidak peka, atau pun tidak pengertian.
             
             Selamat tahu baru, Eva. Bagus berdoa semoga 2024 bisa menjadi tahun yang lebih baik dari tahun-tahun sebelumnya. Terutama Bagus berdoa semoga di 2024 ini Bagus dan Eva bisa mendapatkan pekerjaan yang sesuai dan kita ditempatkan di daerah yang sama. Sungguh Bagus berharap doa itu dapat terjadi.
             
             Salam sayang
             
             Bagus 2023
             """)
