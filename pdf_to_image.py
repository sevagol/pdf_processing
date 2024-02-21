import fitz  # PyMuPDF
import io
from PIL import Image
def convert_pdf_to_images(pdf_bytes, image_format="jpeg", dpi=400):
    # Open the PDF from bytes
    doc = fitz.open("pdf", pdf_bytes)
    images = []
    for page_number in range(len(doc)):
        # Get the page
        page = doc.load_page(page_number)

        # Specify zoom factor based on DPI. Default PDF DPI is 72.
        zoom = dpi / 72
        matrix = fitz.Matrix(zoom, zoom)

        # Get the pixmap of the page with specified DPI (rasterized image)
        pix = page.get_pixmap(matrix=matrix)

        # Convert the pixmap to an image format suitable for streamlit
        img_data = pix.tobytes(image_format)
        img = Image.open(io.BytesIO(img_data))
        images.append(img)
    
    # Close the PDF after processing
    doc.close()
    return images
