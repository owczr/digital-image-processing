import os

import click

from closing.src.closing import binary
from closing.src.closing import mono
from closing.src.plots import plot_input_and_closed
from closing.src.utils import load_image, save_image, is_binary


@click.command()
@click.option("--path", "-p", type=click.STRING, help="Path to image")
@click.option("--radius", "-r", type=click.INT, default=5, help="Radius of structural element")
@click.option("--output", "-o", type=click.STRING, default=None,
              help="Output path, if none image will be saved in the same directory as input image")
@click.option("--name", "-n", type=click.STRING, default="closed",
              help="Name of the output image, default is \"closed\"")
@click.option("--plot", type=click.BOOL, default=False, help="Plot results, default: False")
def main(path, radius, output, name, plot):
    run(path, radius, output, name, plot)


def run(path, radius, output, name, plot):
    # Load the image to array
    image = load_image(path)

    # Perform closing according to image type
    if is_binary(image):
        image_closed = binary.closing(image, radius)
    else:
        image_closed = mono.closing(image, radius)

    # Plot results
    if plot:
        plot_input_and_closed(image, image_closed)

    # Save the image
    if output is None:
        output = os.path.dirname(path)

    save_image(image_closed, output, name)


if __name__ == "__main__":
    main()
