import streamlit as st
from rembg import remove
from PIL import Image
import sqlite3
import pandas as pd

# Create a connection to the SQLite database
conn = sqlite3.connect('clothing.db')
c = conn.cursor()

# Create a table to store the clothing details
c.execute('''CREATE TABLE IF NOT EXISTS clothing
             (id INTEGER PRIMARY KEY, type TEXT, color TEXT, category TEXT, image BLOB)''')

# Function to remove the background from an image
def remove_background(image):
    return remove(image)

# Function to save the clothing details to the database
def save_clothing(type, color, category, image):
    c.execute("INSERT INTO clothing (type, color, category, image) VALUES (?, ?, ?, ?)",
              (type, color, category, image))
    conn.commit()

# Streamlit app
st.title('Clothing Upload and Dressing Room')

# Image upload
uploaded_file = st.file_uploader("Choose an image...", type=["webp", "jpg", "png"])
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)

    # Remove background
    image = remove_background(image)
    st.image(image, caption='Image with Background Removed.', use_column_width=True)

    # Form for clothing details
    with st.form(key='clothing_form'):
        type = st.selectbox('Type of Clothing', ['Pants', 'Skirt', 'T-Shirt', 'Dress', 'Shoes'])
        color = st.color_picker('Color')
        category = st.selectbox('Category', ['Casual', 'Chic', 'Work'])
        submit_button = st.form_submit_button(label='Save Clothing')

    # Save clothing details
    if submit_button:
        save_clothing(type, color, category, image)
        st.success('Clothing details saved!')

# Dressing room page
st.title('Dressing Room')

# Display all clothing items
df = pd.read_sql_query("SELECT * from clothing", conn)
st.dataframe(df)

# Filtering and grouping
# Add code here to filter and group the clothing items by type, color, and category
