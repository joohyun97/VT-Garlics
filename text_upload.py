import streamlit as st
import text_analysis as ta
import audio_converter as voice

#Header Section
with st.container():
    st.title("GuardianTales")
    st.subheader("HooHacks 2023 Team VT-Garlics :garlic:")
    st.write("---")

with st.container():
    story_title = st.text_input('Upload your tale!!', 'Title')
    story_prompt = st.text_area('Text Value','Enter the text to read' , height=500, label_visibility='collapsed')
    upload_bt = st.button('Upload Text')


if upload_bt and ta.check_textprompt(story_prompt):
    st.write("Text Uploaded!!")
    # voice.audio_output(story_title)
    voice.audio_output(story_prompt)
elif upload_bt:
    st.write("Upload Text")
    
# st.write('Sentiment:', sentiment_score)
    