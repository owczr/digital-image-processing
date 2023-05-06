# Digital Image Processing
## About
This repository contains projects made for Digital Image Processing and Analysis course <br>
during summer semester of 3rd year of Data Engineering and Analysis on AGH UST.
## Setup
Create new conda environment from `environment.yml`
```bash
conda env create digital-image --file=environment.yml
```
Or from `requirements.txt`
```bash
conda create -n digital-image -f requirements.txt
```
## Fractals
This program generates a fractal using affine transformations from image or draws points. <br>
- `drawing.py` - It uses `turtle` package for drawing of each point.
- `generator.py` - generates a fractal from specified image. 
- `plots.py` - plot for generated fractal.
- `transformations.py` is the Affine Transformation class which has 4 transformation matrices and a method to get each matrix randomly.
- `utils.py` - function to load image and `MAX_ITERATIONS` constant.
<br>

To generate fractal from an image:
```bash
python fractals/main.py --path <path to image>
```
To draw each point in a loop:
```bash
python fractals/main.py
```
## Kirsch
This program filtrates an image using kirsch operators and plots the results using `matplotlib`.` <br>
- `filtration.py` - here is the main filtration functions
- `operators.py` - here is a class with kirsch operators
- `plots.py` - here is a function for plotting the results
- `utils.py` - loading the image and other utilities

Tu run the program use
```bash
python kirsch/main.py --path <path to image>
```
## Closing
This program performs binary on greyscale closing on input image.
- `closing` - inside this package there are `binary` and `mono` morphology functions
- `element.py` - here is class with structural element
- `plots.py` - here is a function for plotting results
- `utils.py` - functions to load an image and check it's type

To run this program you must specify `path`. You can specify `radius` for the structural element otherwise 
pragram will use default value of 5.
```bash
python closing/main.py --path <path to image> --radius <radius>
```

