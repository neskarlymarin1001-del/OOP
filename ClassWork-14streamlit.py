import streamlit as st
from PIL import Image

col1, col2 = st.columns((4,5))

with col1:
    st.title("My Resume")
    st.header("Justus Selwyn")

with col2:
    image = Image.open('566a713d85e21e34e2af13885c041eb5.jpg')
    st.image(image, width=200)

st.divider()

st.markdown("**About Me**")
st.text("I am an Academician, Researcher. and a Musician.")
st.text("I am currently working with JBU")
st.divider()

st.markdown("**Education:**")

st.divider()

st.markdown("**Work Experience:**")

st.divider()

st.markdown("**Projects:**")

st.divider()

st.markdown("**Hobbies:**")

st.divider()

st.markdown("**Contact Me:**")
st.text_input("Your Name: ")
st.text_input("Your EmailID: ")
st.text_input("Your Message for me: ")
st.button("Send Message: ")



