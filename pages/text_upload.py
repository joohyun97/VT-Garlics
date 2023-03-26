import streamlit as st
import audio_converter as voice

def text_uploader():
    
    with st.container():
        story_title = st.text_input('Upload your tale!!', 'Title')
        story_prompt = st.text_area('Text Value','Enter the text to read' , height=500, label_visibility='collapsed')
        upload_bt = st.button('Upload Text')


    if upload_bt and check_textprompt(story_prompt):
        st.write("Text Uploaded!!")
        voice.audio_output(story_title, story_prompt)
    elif upload_bt:
        st.write("Upload Text")
        
    # st.write('Sentiment:', sentiment_score)
        
def check_textprompt(prompt):
    return prompt != '' or prompt != 'Enter the text to read'
