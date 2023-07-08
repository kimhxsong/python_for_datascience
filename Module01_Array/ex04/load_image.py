import imageio.v3 as iio


def ft_load(path: str):
    im = iio.imread(path)

    print(f"The shape of image is: {im.shape}")
    return im
