import streamlit as st
from utils import cosmic_card
from PIL import Image
import io

cosmic_card("🛸 3D Cosmic File Converter", "Convert any file—text, image, audio, video—to any format. Fast, secure, cosmic!")
uploaded_file = st.file_uploader("Upload your file", type=["txt", "pdf", "jpg", "png", "bmp", "mp3", "mp4", "docx", "csv", "xlsx", "zip"])
output_format = st.selectbox("Choose Output Format", ["JPG", "PNG", "BMP", "PDF", "TXT", "MP3", "MP4", "CSV", "XLSX", "ZIP"])

if st.button("🚀 Convert Now"):
    if uploaded_file:
        st.info(f"File '{uploaded_file.name}' received. Starting conversion to {output_format}...")
        try:
            if uploaded_file.type.startswith("image/"):
                image = Image.open(uploaded_file)
                output_buffer = io.BytesIO()

                # Convert image
                if output_format in ["JPG", "PNG", "BMP"]:
                    image.save(output_buffer, format=output_format)
                    st.success(f"Successfully converted to {output_format}!")

                    file_extension = output_format.lower()
                    st.download_button(
                        label=f"Download Converted {output_format}",
                        data=output_buffer.getvalue(),
                        file_name=f"converted.{file_extension}",
                        mime=f"image/{file_extension}"
                    )
                else:
                    st.warning(f"Conversion from image to {output_format} is not yet supported.")
            else:
                st.warning(f"Conversion for file type '{uploaded_file.type}' is not yet supported.")

        except Exception as e:
            st.error(f"An error occurred during conversion: {e}")
    else:
        st.warning("Please upload a file first.")
