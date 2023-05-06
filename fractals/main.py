import click

from src.drawing import draw
from src.generator import generate
from src.plots import plot_fractal


@click.command()
@click.option("--path", "-p", default=None, help="Path to generate the fractal from, if not specified program will "
                                                 "draw points")
def run(path):
    if path is None:
        draw()
        return

    fractal = generate(path)
    plot_fractal(fractal)


if __name__ == "__main__":
    run()
