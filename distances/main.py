import click

from src.utils import load_binary_image
from src.geodetic import create_geodetic_map
from src.plots import image_and_heatmap


@click.command()
@click.option("--path", "-p", type=click.STRING, help="Path to image")
@click.option("--x", "-x", type=click.INT, default=20, help="X coordinate, default 20")
@click.option("--y", "-y", type=click.INT, default=231, help="Y coordinate, default: 231")
@click.option("--radius", "-r", type=click.INT, default=3, help="Radius of the structural element, default: 3")
def main(path, x, y, radius):
    binary_image = load_binary_image(path)

    geodetic_map = create_geodetic_map(binary_image, (x, y), radius)

    image_and_heatmap(binary_image, geodetic_map, (x, y))


if __name__ == "__main__":
    main()
