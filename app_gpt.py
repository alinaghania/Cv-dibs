import streamlit as st
from rembg import remove
from PIL import Image
import io

# Function to remove background from image
def remove_bg(image):
    return remove(image)

# Function to save image with metadata
def save_image_with_metadata(image, item, color, category):
    # Save image
    img_byte_arr = io.BytesIO()
    image.save(img_byte_arr, format='PNG')
    img_byte_arr = img_byte_arr.getvalue()
    
    # Save metadata
    metadata = {
        'item': item,
        'color': color,
        'category': category
    }
    
    # Here you can save image and metadata to your preferred storage solution
    # For example, saving to local storage:
    with open(f"{item}_{color}_{category}.png", "wb") as f:
        f.write(img_byte_arr)
    with open(f"{item}_{color}_{category}.txt", "w") as f:
        f.write(str(metadata))

# Streamlit app interface
def main():
    st.title("Clothing Background Removal and Categorization")

    st.sidebar.header("Upload and Categorize")

    uploaded_file = st.sidebar.file_uploader("Choose an image...", type=["jpg", "jpeg", "png", "webp"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image', use_column_width=True)

        # Remove background
        if st.sidebar.button('Remove Background'):
            with st.spinner('Removing background...'):
                image_no_bg = remove_bg(image)
                st.image(image_no_bg, caption='Image without Background', use_column_width=True)

                # Collect metadata
                item = st.sidebar.selectbox("Select Item Type", ["Pants", "Skirt", "T-Shirt", "Dress", "Shoes"])
                color = st.sidebar.text_input("Enter Color")
                category = st.sidebar.selectbox("Select Category", ["Casual", "Chic", "Work"])

                if st.sidebar.button('Save'):
                    save_image_with_metadata(image_no_bg, item, color, category)
                    st.success(f"Image and metadata saved as {item}_{color}_{category}")

if __name__ == "__main__":
    main()
