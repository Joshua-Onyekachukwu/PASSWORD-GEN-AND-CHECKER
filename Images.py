from PIL import Image, ImageFilter



img = Image.open(r'..\Python Scraping\212 - astro.jpg')

new_img = img.resize((400, 400))
new_img.save('thumbnail.png', 'png')

# img = Image.open('../Python Scraping/pikachu.jpg')
# img = Image.open('..\\Python Scraping\\pikachu.jpg')
# img = Image.open(r'..\Python Scraping\pikachu.jpg')
#
# filtered_img = img.filter(ImageFilter.BLUR)
# filtered_img.save('blur.png', 'png')
# filtered_img.show()

# print(img.format)
# print(img.size)
# print(img.width, img.height)

