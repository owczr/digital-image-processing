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
This program generates a fractal using affine transformations. <br>
It uses `turtle` package for drawing of each point. <br>
- `generator.py` is the main loop which calculates and draws coordinates. <br>
- `transformations.py` is the Affine Transformation class which has 4 transformation matrices and a method to get each matrix randomly.
<br>

To run this program use
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


