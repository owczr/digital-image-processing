import click

import fractals.main as fractals
import kirsch.main as kirsch
import closing.main as closing
import distances.main as distances


@click.command()
@click.option("--program", type=click.INT, help="\b\nSelect program to run.\n"
                                                "   1. Fractals\n"
                                                "   2. Kirsch\n"
                                                "   3. Closing\n"
                                                "   4. Distances")
@click.option("--path", help="Path to image")
@click.option("--radius", type=click.INT, default=3, help="Radius for structural element, programs 3 and 4, default: 5")
@click.option("--x", "-x", type=click.INT, default=20, help="X coordinate, program 4, default: 20")
@click.option("--y", "-y", type=click.INT, default=231, help="Y coordinate, program 4, default: 231")
@click.option("--output", "-o", type=click.STRING, default=None,
              help="Output path, if none image will be saved in the same directory as input image")
@click.option("--name", "-n", type=click.STRING, default="output",
              help="Name of the output image, default is \"output\"")
@click.option("--plot", type=click.BOOL, default=False, help="Plot results, default: False")
def main(program, path, radius, x, y, output, name, plot):
    if program == 1:
        fractals.run(path, output, name, plot)
    elif program == 2:
        kirsch.run(path, output, name, plot)
    elif program == 3:
        closing.run(path, radius, output, name, plot)
    elif program == 4:
        distances.run(path, x, y, radius, output, name, plot)
    else:
        raise ValueError("Choose program 1, 2, 3 or 4")


if __name__ == "__main__":
    main()
