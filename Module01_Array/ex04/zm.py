import matplotlib.pyplot as plt
import numpy as np

from load_image import ft_load


def zoom(image):
    sliced_image = image[100:500, 450:850, 0:1]

    print(f"New shape after slicing: {sliced_image.shape} or {sliced_image.shape[:2]}")
    return sliced_image


def display(image):
    fig, ax = plt.subplots()
    ax.imshow(image, cmap='gray')

    height, width = image.shape[:2]

    x_ticks = np.arange(0, width, 50)
    ax.set_xticks(x_ticks)
    ax.set_xticklabels(x_ticks)

    y_ticks = np.arange(0, height, 50)
    ax.set_yticks(y_ticks)
    ax.set_yticklabels(y_ticks)

    plt.show()


def main():
    image = ft_load("../../01_animal.jpeg")
    print(image)

    sliced_image = zoom(image)

    print(sliced_image)

    display(sliced_image)


if __name__ == "__main__":
    main()
