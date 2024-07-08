import streamlit as st
import time

#graph display libraries
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np



st.title ("Streamlit test app")
st.header("Streamlit 101")
st.markdown("Below are the examples for Streamlit tutorial")
st.subheader("This is a subheader")
st.code("x=2021")
st.latex(r''' a+a r^1+a r^2+a r^3 ''')

img, aud, vid = st.columns(3)
img.markdown('Image')
img.image("image.jpg")
img.caption("image sample")

aud.markdown('Audio')
aud.audio("audio.wav")
aud.caption("Audio sample")

vid.markdown('Video')
vid.video("video.mp4")
vid.caption("video sample")


cb, but, rad = st.columns(3)
cb.subheader('Checkbox')
cb.write('Select "Yes" if you are a human')
cb.checkbox("Yes")

but.subheader("Button")
but.write('Click to check the button')
but.button("Click me!")

rad.subheader("Radio button")
rad.radio("Gender?", ['Male', 'Female'])

sb, ms, ss = st.columns(3)
sb.subheader('Selectbox')
sb.selectbox("Choose your city", ['Karachi', 'Islamabad', 'Lahore'])

ms.subheader('Multi-select')
ms.multiselect("Choose your courses", ['DLD', "OOP", 'DSA', "CSM"])

ss.subheader('select-slider')
ss.select_slider("Your experience at NED", ['Bad', 'Good', 'Excellent'])

c = st.container()
c.subheader('Slider')
c.slider('Rate CIS out of 10', 0, 10)

c.subheader('Numeric input')
c.number_input('Rate batch 2020 out of 10', 0, 10)

c.subheader('Text input')
c.text_input("Write your email" )

c.subheader('Date input')
c.date_input('Enter your Birthday')

c.subheader('Time input')
c.time_input('Enter your class time')

c.subheader('Text area input')
c.text_area("Describe yourself")

col1, col2 = st.columns(2)
col1.subheader("File uploader")
col1.file_uploader("upload your resume")

col2.subheader("Color Picker")
col2.color_picker('Choose your favorite color')

# st.balloons(): This function is used to display 
# balloons for celebration. 
# st.progress(): This function is used to display a 
# progress bar. 
# st.spinner(): This function is used to display a 
# temporary waiting message during execution.

c2 = st.container()

c2.subheader("Click to see balloons")
if c2.button('Balloons') == True:
    c2.balloons()

c2.subheader("Click to see progress bar with loading")
if c2.button('Progress bar with loading'):    
    c2.progress(50)
    with st.spinner('Wait for it...'):
        time.sleep(10)



st.sidebar.title('Pages')
st.sidebar.button("Home")
st.sidebar.button("Login")

rand=np.random.normal(1, 2, size=20)
fig, ax = plt.subplots()
ax.hist(rand, bins=15)
st.pyplot(fig)
