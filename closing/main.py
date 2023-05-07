import os

import click

from src.closing import binary
from src.closing import mono
from src.plots import plot_input_and_closed
from src.utils import load_image, save_image, is_binary


@click.command()
@click.option("--path", "-p", type=click.STRING, help="Path to image")
@click.option("--radius", "-r", type=click.INT, default=5, help="Radius of structural element")
@click.option("--output", "-o", type=click.STRING, default=None,
              help="Output path, if none image will be saved in the same directory as input image")
@click.option("--name", "-n", type=click.STRING, default="closed",
              help="Name of the output image, default is \"closed\"")
def run(path, radius, output, name):
    image = load_image(path)

    if is_binary(image):
        image_closed = binary.closing(image, radius)
    else:
        image_closed = mono.closing(image, radius)

    plot_input_and_closed(image, image_closed)

    if output is None:
        output = os.path.dirname(path)

    save_image(image_closed, output, name)


if __name__ == "__main__":
    run()
