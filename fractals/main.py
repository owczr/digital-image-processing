import os

import click

from fractals.src.drawing import draw
from fractals.src.generator import generate
from fractals.src.plots import plot_fractal
from fractals.src.utils import save_image


@click.command()
@click.option("--path", "-p", default=None,
              help="Path to generate the fractal from, if not specified program will draw points")
@click.option("--output", "-o", type=click.STRING, default=None,
              help="Output path, if none image will be saved in the same directory as input image")
@click.option("--name", "-n", type=click.STRING, default="fractal",
              help="Name of the output image, default is \"fractal\"")
@click.option("--plot", type=click.BOOL, default=False, help="Plot results, default: False")
def main(path, output, name, plot):
    run(path, output, name, plot)


def run(path, output, name, plot):
    # Draw the fractal if path is not specified
    if path is None:
        draw()
        return

    # Generate the fractal
    fractal = generate(path)

    # Plot results
    if plot:
        plot_fractal(fractal)

    # Save the image
    if output is None:
        output = os.path.dirname(path)

    save_image(fractal, output, name)


if __name__ == "__main__":
    main()
