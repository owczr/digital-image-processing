import os

import click

from src.drawing import draw
from src.generator import generate
from src.plots import plot_fractal
from src.utils import save_image


@click.command()
@click.option("--path", "-p", default=None,
              help="Path to generate the fractal from, if not specified program will draw points")
@click.option("--output", "-o", type=click.STRING, default=None,
              help="Output path, if none image will be saved in the same directory as input image")
@click.option("--name", "-n", type=click.STRING, default="fractal",
              help="Name of the output image, default is \"fractal\"")
def run(path, output, name):
    if path is None:
        draw()
        return

    fractal = generate(path)
    plot_fractal(fractal)

    if output is None:
        output = os.path.dirname(path)

    save_image(fractal, output, name)


if __name__ == "__main__":
    run()
