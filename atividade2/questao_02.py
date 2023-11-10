import cv2
import matplotlib.pyplot as plt

# Abrindo imagem

image_path = 'imagem3.jpg'
image = cv2.imread(image_path)

image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
plt.imshow(image_rgb)
plt.axis('off')


# Filtro da média
blurred_image_mean = cv2.blur(image_rgb, (5,5))

# Filtro da mediana
blurred_image_medi = cv2.medianBlur(image_rgb, 5)

# Filtro Gaussiano
blurred_image_gaus = cv2.GaussianBlur(image_rgb, (5,5), 0)




# Plotando as imagens

plt.subplot(2, 2, 1)
plt.imshow(image_rgb)
plt.title('Imagem Original')

plt.subplot(2, 2, 2)
plt.imshow(blurred_image_mean)
plt.title('Filtro da média')

plt.subplot(2, 2, 3)
plt.imshow(blurred_image_medi)
plt.title('Filtro da mediana')

plt.subplot(2, 2, 4)
plt.imshow(blurred_image_gaus)
plt.title('Filtro Gaussiano')

plt.tight_layout()
plt.show()