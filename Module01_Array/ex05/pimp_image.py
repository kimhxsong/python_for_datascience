import matplotlib.pyplot as plt
import numpy as np

from load_image import ft_load


def ft_invert(array):
    return 255 - array.copy()


def ft_red(array):
    return [1, 0, 0] * array.copy()


def ft_green(array):
    return array.copy() - [255, 0, 255]


def ft_blue(array):
    copied = array.copy()
    copied[:, :, 0] = 0
    copied[:, :, 1] = 0
    return copied


def ft_grey(array):
    """Transforms the image received in a grey scale."""
    copied = array.copy()
    copied = np.sum(copied / 3, axis=2).astype(np.uint8)
    return copied


def main():
    image = ft_load("../../01_landscape.jpg")

    plt.imshow(image)
    plt.title("Figure VIII.1: Original")
    plt.axis('off')
    plt.show()

    inverted_image = ft_invert(image)
    plt.imshow(inverted_image)
    plt.title("Figure VIII.2: Inverted Image")
    plt.axis('off')
    plt.show()

    red_filtered_image = ft_red(image)
    plt.imshow(red_filtered_image)
    plt.title("Figure VIII.3: Red Filter")
    plt.show()

    blue_filtered_image = ft_blue(image)
    plt.imshow(blue_filtered_image)
    plt.title("Figure VIII.4: Blue Filter")
    plt.axis('off')
    plt.show()

    green_filtered_image = ft_green(image)
    plt.imshow(green_filtered_image)
    plt.title("Figure VIII.5: Green Filter")
    plt.axis('off')ㅂ
    plt.show()

    grey_filtered_image = ft_grey(image)
    plt.imshow(grey_filtered_image, cmap='gray')
    plt.title("Figure VIII.6: Grayscale Filter")
    plt.axis('off')
    plt.show()


if __name__ == "__main__":
    main()
