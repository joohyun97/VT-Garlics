import streamlit as st
import text_analysis as ta


#Header Section
with st.container():
    st.title("GuardianTales")
    st.subheader("HooHacks 2023 Team VT-Garlics :garlic:")

with st.container():
    inital_title = 'Title'
    inital_prompt = 'Enter the text to read'
    
    story_prompt = st.text_area('Upload your tale!!',inital_prompt , height=500)
    upload_bt = st.button('Upload Text')




if upload_bt and story_prompt != inital_prompt and story_prompt != '':
    st.write("Text Uploaded!!")
elif upload_bt:
    st.write("Upload Text")
    
# st.write('Sentiment:', sentiment_score)
    
