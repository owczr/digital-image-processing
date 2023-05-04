# Digital Image Processing
## About
This repository contains projects made for Digital Image Processing and Analysis course <br>
during summer semester of 3rd year of Data Engineering and Analysis on AGH UST.
## Setup
Create new conda environement from `requirements.txt`.
```bash
conda create -n digital-image -f requirements.txt
```
## Fractals
This program generates a fractal using affine transformations. <br>
It uses `turtle` package for drawing of each point. <br>
In `generation.py` is the main loop which calculates and draws coordinates. <br>
In `transformations.py` is the Affine Transformation class which has 4 transformation matrices and a method to get each matrix randomly.
<br>

To run this program use
```bash
python fractals/main.py
```
