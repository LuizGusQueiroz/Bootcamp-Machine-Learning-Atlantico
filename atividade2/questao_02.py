import cv2
import matplotlib.pyplot as plt

# Abrindo imagem

image_path = 'frutas.jpg'
image = cv2.imread(image_path)

image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
plt.imshow(image_rgb)
plt.axis('off')


# Filtro da média
blurred_image_mean = cv2.blur(image, (5,5))

# Filtro da mediana
...

# Filtro Gaussiano
blurred_image_gaus = cv2.GaussianBlur(image, (5,5), 0)




# Plotando as imagens

plt.subplot(2, 2, 1)
plt.imshow(image_rgb)
plt.title('Imagem Original')

plt.subplot(2, 2, 2)
plt.imshow(blurred_image_mean)
plt.title('Filtro da média')

plt.subplot(2, 2, 3)
#plt.imshow()
plt.title('Filtro da mediana')

plt.subplot(2, 2, 4)
plt.imshow(blurred_image_gaus)
plt.title('Filtro Gaussiano')

plt.tight_layout()
plt.show()