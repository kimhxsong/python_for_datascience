import imageio.v3 as iio
from numpy import ndarray


def ft_load(path: str) -> ndarray:
    im = iio.imread(path)

    print(f"The shape of image is: {im.shape}")
    return im
