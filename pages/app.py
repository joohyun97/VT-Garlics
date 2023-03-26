import streamlit as st
from streamlit_option_menu import option_menu
import text_upload as tu
import video_upload as vu

st.title('GuardianTales')
st.text('Hoohacks 2023 - VT_Garlics')

st.sidebar.title('Navigation')
with st.sidebar:
    selected = option_menu(
        menu_title=None,
        options=['Home', 'Text Upload', 'Video Upload']
    )
    
if selected == 'Text Upload':
    tu.text_uploader()
elif selected == 'Video Upload':
    vu.video_uploader()
else:
    st.markdown(
        'Welcome to GuardianTails, the one-stop platform where guardians can create their own voices and read any sentences with the voice!. Our website '
        'allows you to upload your voice and imitate it for reading storybooks to '
        'your kids, helping you stay connected with them even when you are not around. With GuardianStoryTime, '
        'you can share the joy of storytelling and create lasting memories for your children. Follow these simple '
        'steps to get started:')

    st.text('Follow these simple steps to get started:')
  
# st.sidebar.radio('Pages', options=['Data Statistics', 'Data Header', 'Plot'])

