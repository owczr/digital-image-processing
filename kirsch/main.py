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
@click.option("--plot", type=click.BOOL, default=False, help="Plot results, default: False")
def run(path, output, name, plot):
    # Load image to array
    image_array = load_image(path)

    # Filtrate the image
    filtration = filtrate_image(image_array)

    # Plot results
    if plot:
        plot_before_and_after(image_array, filtration)

    # Save results to file
    if output is None:
        output = os.path.dirname(path)

    save_image(filtration, output, name)


if __name__ == "__main__":
    run()
