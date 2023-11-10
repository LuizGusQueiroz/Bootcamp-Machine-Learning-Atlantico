import cv2
import matplotlib.pyplot as plt

# Abrindo imagem

image_path = 'frutas.jpg'
image = cv2.imread(image_path)

image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
plt.imshow(image_rgb)
plt.axis('off')
plt.show()

# Converte a imagem para escala de cinza

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
normalized_image = gray_image / 255.0

# Dados da imagem

propriedades = [
    ('Altura ', image.shape[0]),
    ('Largura', image.shape[1]),
    ('Canais de cor', image.shape[2]),
    ('Tipo de dado ', image.dtype),
    ('Tom de cinza máximo', round(normalized_image.max(), 2)),
    ('Tom de cinza médio ', round(normalized_image.mean(), 2)),
    ('Tom de cinza mínimo', round(normalized_image.min(), 2))
]

for propriedade, valor in propriedades:
    print(f'{propriedade}: {valor}')


