# Graphics Task
# Problem Statement
Given is a .json that contains data which is enough to construct 7 3D models. Each object's name (eg:biology,engineering,crypto...) gives a hint as to what the model is about. Each object contains path property which is a 2D array. Each inner array is a set of 3d coordinates where every consecutive 3 numbers are one single point in 3d space and so each of this inner array has a multiple of 3 elements. Each inner array therefore contains enough points to map a curve in 3d space. These given curves when constructed together resemble the mentioned 3d model. Write a program in any language and any software of your choice to construct a model when such data.json as above mentioned is provided. You may also use custom shaders to manipulate and beautify your model.
[https://drive.google.com/file/d/15SC6w4IvxZ3wiXSq9J7k2HfSWNwWQZIM/view?usp=sharing/](https://drive.google.com/file/d/15SC6w4IvxZ3wiXSq9J7k2HfSWNwWQZIM/view?usp=sharing/)
# Solution
I have basically written a python script that converts the given **3D** coordinates in `data.json` file into a `.obj` file.
This will allows us to use the model anywhere as `.obj` is the standard file format for 3D objects.

- The code is in `js3d.py`
- The generated models are in `/models`
