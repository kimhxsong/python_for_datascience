import numpy as np

from load_image import ft_load
from zm import display, zoom


def main():
    image = ft_load("../../01_animal.jpeg")
    print(image)

    sliced_image = zoom(image)
    rotated_image = np.empty((len(sliced_image[0]), len(sliced_image)))
    for i in range(0, 400):
        for j in range(0, 400):
            rotated_image[j, i] = sliced_image[i, j].item()

    display(rotated_image)


if __name__ == "__main__":
    main()
