from PIL import Image
import numpy as np

image_path = 'cat.jpg'
image = Image.open(image_path).convert('1') 
image_resized = image.resize((100, 100))
image_bin = np.array(image_resized)
image_bin = 1 - image_bin

print("Matriz binaria 100x100:")
for row in image_bin:
    print(' '.join(map(str, row)))