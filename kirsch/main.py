import os
import click

from src.filtration import filtrate_image
from src.utils import load_image, save_image
from src.plots import plot_before_and_after


@click.command()
@click.option("--path", "-p", type=click.STRING, help="Path to image")
@click.option("--output", "-o", type=click.STRING, default=None,
              help="Output path, if none image will be saved in the same directory as input image")
@click.option("--name", "-n", type=click.STRING, default="filtrated",
              help="Name of the output image, default is \"filtrated\"")
def run(path, output, name):
    # Load image to array
    image_array = load_image(path)

    # Filtrate the image
    filtration = filtrate_image(image_array)

    # Plot results
    plot_before_and_after(image_array, filtration)

    # Save results to file
    if output is None:
        output = os.path.dirname(path)

    save_image(filtration, output, name)


if __name__ == "__main__":
    run()
