import matplotlib.pyplot as plt

from src.filtration import filtrate_image
from src.utils import load_image

IMAGE_PATH = "static/cameraman.tif"
# IMAGE_PATH = "static/peppers.png"


def run():
    image_array = load_image(IMAGE_PATH)

    filtration = filtrate_image(image_array)

    plt.imshow(filtration, cmap="gray")
    plt.show()


if __name__ == "__main__":
    run()
