import streamlit as st

st.set_page_config(page_title = "HooHacks Virginia Garlics", page_icon=":boom:", layout = "wide")

#Header Section
with st.container():
    st.subheader("HooHacks 2023 Team VT-Garlics :garlic:")
    st.title("GuardianTales")

    st.write("Project description:")
    
with st.container():
    st.write("---") #divider
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Upload your voice")
        st.write("##")
    with right_column:
        uploaded_file = st.file_uploader('Upload your file here')
        
        