from PIL import Image, ImageFilter
import numpy as np
import matplotlib.pyplot as plt

image_path = 'icecream.jpg' 
image = Image.open(image_path)
image_resized = image.resize((400, 400))
image_rgb = np.array(image_resized)

def rgb_to_hex(rgb):
    return '#{:02x}{:02x}{:02x}'.format(rgb[0], rgb[1], rgb[2])

hex_matrix = np.apply_along_axis(rgb_to_hex, 2, image_rgb)

def apply_grayscale(image):
    return image.convert('L')

def apply_blur(image):
    return image.filter(ImageFilter.GaussianBlur(radius=2))

def apply_threshold(image, threshold=128):
    return image.convert('L').point(lambda p: p > threshold and 255)

def apply_edges(image):
    return image.filter(ImageFilter.FIND_EDGES) 

image_grayscale = apply_grayscale(image_resized)
image_blurred = apply_blur(image_resized)
image_threshold = apply_threshold(image_resized)
image_edges = apply_edges(image_resized)  
plt.figure(figsize=(15, 12))

plt.subplot(2, 3, 1)
plt.imshow(image_resized)
plt.title('Imagen Original')
plt.axis('off')

plt.subplot(2, 3, 2)
plt.imshow(image_grayscale, cmap='gray')
plt.title('Escala de Grises')
plt.axis('off')

plt.subplot(2, 3, 3)
plt.imshow(image_blurred)
plt.title('Desenfoque Gaussiano')
plt.axis('off')

plt.subplot(2, 3, 4)
plt.imshow(image_threshold, cmap='gray')
plt.title('Umbral (Blanco y Negro)')
plt.axis('off')

plt.subplot(2, 3, 5)
hex_image = np.array([[[int(h[1:3], 16), int(h[3:5], 16), int(h[5:7], 16)] for h in row] for row in hex_matrix])
plt.imshow(hex_image)
plt.title('Matriz Hexadecimal Original')
plt.axis('off')

plt.subplot(2, 3, 6)
plt.imshow(image_edges, cmap='gray')
plt.title('Contornos')
plt.axis('off')

plt.show()

