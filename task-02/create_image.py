from PIL import Image, ImageDraw, ImageFont
img = Image.new('RGB', (200, 50), color=(255, 255, 255))
# above line is to generate white background and these numbers are pixels
d = ImageDraw.Draw(img)
# this line is to intilize drawing
font = ImageFont.truetype("DejaVuSans-Bold.ttf", 40) 
# this line is to give the font 
d.text((50, 5), "2 + 2", fill=(0, 0, 0), font=font)
# this line is to draw 2+2 text on the image 
img.save("/home/teja/Documents/2_plus_2.png")
# this line is to save the image 
