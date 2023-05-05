import click

from src.filtration import filtrate_image
from src.utils import load_image
from src.plots import plot_before_and_after


@click.command()
@click.option("--path", "-p", type=click.STRING, help="Path to image")
def run(path):
    # Load image to array
    image_array = load_image(path)

    # Filtrate the image
    filtration = filtrate_image(image_array)

    # Plot results
    plot_before_and_after(image_array, filtration)


if __name__ == "__main__":
    run()
