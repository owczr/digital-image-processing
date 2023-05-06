import click

from src.closing import binary
from src.closing import mono
from src.plots import plot_input_and_closed
from src.utils import load_image, is_binary


@click.command()
@click.option("--path", "-p", type=click.STRING, help="Path to image")
@click.option("--radius", "-r", type=click.INT, default=5, help="Radius of structural element")
def run(path, radius):
    image = load_image(path)

    if is_binary(image):
        image_closed = binary.closing(image, radius)
    else:
        image_closed = mono.closing(image, radius)

    plot_input_and_closed(image, image_closed)


if __name__ == "__main__":
    run()
