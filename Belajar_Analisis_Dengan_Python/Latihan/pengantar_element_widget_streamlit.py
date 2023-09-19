import streamlit as st 
 
st.write(
    """
    # My first app
    Hello, para calon praktisi data masa depan!
    """
)

# Write
import streamlit as st
import pandas as pd
 
st.write(pd.DataFrame({
    'c1': [1, 2, 3, 4],
    'c2': [10, 20, 30, 40],
}))

# Text
# 1. Markdown()
import streamlit as st 
 
st.markdown(
    """
    # My first app
    Hello, para calon praktisi data masa depan!
    """
)

# 2. Title()
import streamlit as st
 
st.title('Belajar Analisis Data')

# 3. Header()
import streamlit as st
 
st.header('Pengembangan Dashboard')

# 4. Subheader()
import streamlit as st
 
st.subheader('Pengembangan Dashboard')

# 5. Caption()
import streamlit as st
 
st.caption('Copyright (c) 2023')

# 6. Code()
import streamlit as st
 
code = """def hello():
    print("Hello, Streamlit!")"""
st.code(code, language='python')

# 7. Text()
import streamlit as st
 
st.text('Halo, calon praktisi data masa depan.')

# 8. Latex()
import streamlit as st
 
st.latex(r"""
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
""")

# Data Display
# 1. Data Frame()
import pandas as pd
import streamlit as st 
 
df = pd.DataFrame({
    'c1': [1, 2, 3, 4],
    'c2': [10, 20, 30, 40],
})
 
st.dataframe(data=df, width=500, height=150)

# 2. Table()
import pandas as pd
import streamlit as st 
 
df = pd.DataFrame({
    'c1': [1, 2, 3, 4],
    'c2': [10, 20, 30, 40],
})
st.table(data=df)

# 3. Metric()
import streamlit as st
 
st.metric(label="Temperature", value="28 °C", delta="1.2 °C")

# 4. Json()
import streamlit as st
 
st.json({
    'c1': [1, 2, 3, 4],
    'c2': [10, 20, 30, 40],
})

# 5. Chart()
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st
 
x = np.random.normal(15, 5, 250)
 
fig, ax = plt.subplots()
ax.hist(x=x, bins=15)
st.pyplot(fig)

# Text input
import streamlit as st
 
name = st.text_input(label='Nama lengkap', value='')
st.write('Nama: ', name)

# Text Area
import streamlit as st
 
text = st.text_area('Feedback')
st.write('Feedback: ', text)

# Number Input
import streamlit as st
 
number = st.number_input(label='Umur')
st.write('Umur: ', int(number), ' tahun')

# Data Input
import datetime
import streamlit as st
 
date = st.date_input(label='Tanggal lahir', min_value=datetime.date(1900, 1, 1))
st.write('Tanggal lahir:', date)

# File Uploader
import streamlit as st
import pandas as pd
 
uploaded_file = st.file_uploader('Choose a CSV file')
 
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.dataframe(df)

# Camera Input
import streamlit as st
picture = st.camera_input('Take a picture')
if picture:
    st.image(picture)

# Button
import streamlit as st
 
if st.button('Say hello'):
    st.write('Hello there')

# Checkbox
import streamlit as st
 
agree = st.checkbox('I agree')
 
if agree:
    st.write('Welcome to MyApp')

# Radio Button
import streamlit as st
 
genre = st.radio(
    label="What's your favorite movie genre",
    options=('Comedy', 'Drama', 'Documentary'),
    horizontal=False
)

# Select Box
import streamlit as st
 
genre = st.selectbox(
    label="What's your favorite movie genre",
    options=('Comedy', 'Drama', 'Documentary')
)

# Multi-select
import streamlit as st
 
genre = st.multiselect(
    label="What's your favorite movie genre",
    options=('Comedy', 'Drama', 'Documentary')
)

# Slider
values = st.slider(
    label='Select a range of values',
    min_value=0, max_value=100, value=(0, 100))
st.write('Values:', values)

# Sidebar
