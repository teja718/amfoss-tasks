import pytesseract
from PIL import Image
import re

# Load the image
image_path = "/home/teja/Documents/2_plus_2.png"
img = Image.open(image_path)

# Use OCR to extract text
extracted_text = pytesseract.image_to_string(img).strip()

# Print the extracted text for debugging
print(f"Extracted Text: '{extracted_text}'")

# Use a more flexible regex to match the arithmetic expression
try:
    # Allow more flexible matching for basic arithmetic expressions
    match = re.search(r'\d+\s*[\+\-\*/]\s*\d+', extracted_text)

    if match:
        expression = match.group()
        # Evaluate the expression
        result = eval(expression)
        print(f"The expression is: {expression}")
        print(f"The result is: {result}")
    else:
        print("No valid arithmetic expression found.")
except Exception as e:
    print(f"Error: {e}")

