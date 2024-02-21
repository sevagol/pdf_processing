from PIL import Image
import io
import base64

def split_and_zoom_image(image, cols=5, rows=4, zoom_factor=4):
    # image здесь ожидается как объект PIL.Image
    
    # Calculate the size of each piece
    img_width, img_height = image.size
    piece_width = img_width // cols
    piece_height = img_height // rows
    
    # List to store images in base64
    enlarged_images_base64 = []
    
    for row in range(rows):
        for col in range(cols):
            # Define the coordinates of the piece
            left = col * piece_width
            top = row * piece_height
            right = left + piece_width
            bottom = top + piece_height
            
            # Crop the piece from the image
            piece = image.crop((left, top, right, bottom))
            
            # Enlarge the piece by the zoom factor
            enlarged_piece = piece.resize((int(piece_width * zoom_factor), int(piece_height * zoom_factor)))
            
            # Convert the enlarged piece to base64
            img_byte_arr = io.BytesIO()
            enlarged_piece.save(img_byte_arr, format='PNG')
            img_byte_arr.seek(0)
            base64_str = base64.b64encode(img_byte_arr.read()).decode('utf-8')
            enlarged_images_base64.append(base64_str)
    
    return enlarged_images_base64

