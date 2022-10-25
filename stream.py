import streamlit as st
from pytube import Playlist, YouTube


st.write('Hi, this web will help you download audio file in youtube (mp4 extention)')
url = st.text_input('Enter youtube url:')

# Tạo hàm chuyển đổi các ký tự đăt biệt tránh bị lỗi khi tạo folder có ký tự đặt biệt
def trans_name(name):
    table = name.maketrans('\/|?"<>*:', '---------')
    return name.translate(table)


# yt = YouTube(url)
# def download_single(url):
#     yt.streams.get_by_itag(140).download()

# if st.button('Check link'):
#     st.write('Link hợp lệ, nhấp vào nút download')
#     if st.button('Donwload'):
#         yt.streams.get_by_itag(140).download()
#     #st.download_button('Video',yt.streams.get_by_itag(140).download())
# else:
#     st.write('Link không hợp lệ')

try:
    yt = YouTube(url)
    if st.button('Download'):
        placeholder = st.empty()
        placeholder.text('Downloading')
        yt.streams.get_by_itag(140).download()
        placeholder.text('Done!')
except:
    st.write('Invalid link')

