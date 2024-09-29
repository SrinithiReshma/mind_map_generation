from PIL import Image
import pytesseract

# Specify the path to the Tesseract OCR executable (adjust based on your installation)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Path to the image file
image_path = 'sample.jpeg'  # Replace with your image file path
# Path to the output text file
output_file_path = 'extracted_text.txt'

def perform_ocr(image_path, output_file_path):
    try:
        # Open the image file
        img = Image.open(image_path)
        
        # Perform OCR on the image
        text = pytesseract.image_to_string(img)
        
        # Save the extracted text to a text file
        with open(output_file_path, 'w', encoding='utf-8') as file:
            file.write(text)
        
        print(f"Extracted text saved to {output_file_path}")
    
    except Exception as e:
        print(f"Error performing OCR: {e}")

if __name__ == "__main__":
    perform_ocr(image_path, output_file_path)

