from PIL import Image, ImageDraw, ImageFont

# Create a new image with white background
img = Image.new('RGB', (200, 50), color=(255, 255, 255))

# Initialize the drawing context
d = ImageDraw.Draw(img)

# Use a large basic font
try:
    font = ImageFont.truetype("arial", 40)
except IOError:
    font = ImageFont.load_default()

# Draw the text "2 + 2" on the image
d.text((50, 5), "2 + 2", fill=(0, 0, 0), font=font)

# Save the image
img.save("/home/teja/Documents/2+2.png")

