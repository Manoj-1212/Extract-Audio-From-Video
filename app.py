import moviepy.editor
import streamlit as st 



def audiofile(vid):
    video = moviepy.editor.VideoFileClip(vid)
    duration = video.duration
    st.write(f'Video Duration is: {duration}')
    audio = video.audio
    audio.write_audiofile('OutputAudio.mp3')

vid = 'videoplayback3.mp4'
audiofile(vid)
