import os

import click

from src.utils import load_binary_image, save_image
from src.geodetic import create_geodetic_map
from src.plots import image_and_heatmap


@click.command()
@click.option("--path", "-p", type=click.STRING, help="Path to image")
@click.option("--x", "-x", type=click.INT, default=20, help="X coordinate, default 20")
@click.option("--y", "-y", type=click.INT, default=231, help="Y coordinate, default: 231")
@click.option("--radius", "-r", type=click.INT, default=3, help="Radius of the structural element, default: 3")
@click.option("--output", "-o", type=click.STRING, default=None,
              help="Output path, if none image will be saved in the same directory as input image")
@click.option("--name", "-n", type=click.STRING, default="map",
              help="Name of the output image, default is \"map\"")
@click.option("--plot", type=click.BOOL, default=False, help="Plot results, default: False")
def main(path, x, y, radius, output, name, plot):
    binary_image = load_binary_image(path)

    geodetic_map = create_geodetic_map(binary_image, (x, y), radius)

    if plot:
        image_and_heatmap(binary_image, geodetic_map, (x, y))

    if output is None:
        output = os.path.dirname(path)

    save_image(geodetic_map, output, name)


if __name__ == "__main__":
    main()
