from PIL import Image

# Image.open() can also open other image types
name='Rui.jpeg'
img = Image.open("images/teampic/{}".format(name))
WIDTH, HEIGHT = 600, 600
# WIDTH and HEIGHT are integers
resized_img = img.resize((WIDTH, HEIGHT))
resized_img.save("images/teampic/{}".format('Rui.jpg'))