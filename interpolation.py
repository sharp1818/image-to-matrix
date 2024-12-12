import matplotlib.pyplot as plt
from skimage.transform import resize
import imageio

input_image = imageio.imread("low-resolution.jpg")

output_shape = (input_image.shape[0] * 2, input_image.shape[1] * 2)

output_nearest = resize(input_image, output_shape, order=0, anti_aliasing=True)  
output_bilinear = resize(input_image, output_shape, order=1, anti_aliasing=True)  
output_quadratic = resize(input_image, output_shape, order=2, anti_aliasing=True) 
output_cubic = resize(input_image, output_shape, order=3, anti_aliasing=True) 
output_polynomial = resize(input_image, output_shape, order=5, anti_aliasing=True)  

fig, axes = plt.subplots(3, 2, figsize=(12, 18))

axes[0, 0].imshow(input_image)
axes[0, 0].set_title("Imagen Original (Baja Resolución)", fontsize=14)
axes[0, 0].axis('off')

axes[0, 1].imshow(output_nearest)
axes[0, 1].set_title("Interpolación (order=0)", fontsize=14)
axes[0, 1].axis('off')

axes[1, 0].imshow(output_bilinear)
axes[1, 0].set_title("Interpolación (order=1)", fontsize=14)
axes[1, 0].axis('off')

axes[1, 1].imshow(output_quadratic)
axes[1, 1].set_title("Interpolación (order=2)", fontsize=14)
axes[1, 1].axis('off')

axes[2, 0].imshow(output_cubic)
axes[2, 0].set_title("Interpolación (order=3)", fontsize=14)
axes[2, 0].axis('off')

axes[2, 1].imshow(output_polynomial)
axes[2, 1].set_title("Interpolación (order=5)", fontsize=14)
axes[2, 1].axis('off')

plt.subplots_adjust(hspace=0.4, wspace=0.3) 
plt.show()
