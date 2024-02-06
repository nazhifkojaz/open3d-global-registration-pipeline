# open3d-global-registration-pipeline
Welcome to open3d-global-registration-pipeline, a reusable python module for pointcloud registration.

## Installation
The simplest way to install the package is to clone the repository to a local directory:
```commandline
git clone https://github.com/nazhifkojaz/open3d-global-registration-pipeline
```
Use Pythons package manager `pip` to install it into your current Python environment:
```commandline
pip install -e /path/to/open3d-global-registration-pipeline/repository/clone
```
Or to install it directly from git into your current Python environment:
```commandline
pip install git+https://github.com/nazhifkojaz/open3d-global-registration-pipeline
```
To use the module, [these packages](https://github.com/nazhifkojaz/open3d-global-registration-pipeline/blob/main/requirements.txt) are required. To install them
manually and directly import the code from your local clone of the repository:
```commandline
pip install /path/to/requirements.txt
```
The required packages are:



1. `open3d>=0.17.0`
2. `numpy==1.19.5`
3. `pytest>=8.0.0`

## Usage
To use this project, simply run [`main.y`](https://github.com/nazhifkojaz/open3d-global-registration-pipeline/blob/main/main.py) script with this command:
```
python main.py
```
it will use [`Living Room model`](https://github.com/nazhifkojaz/open3d-global-registration-pipeline/blob/main/data/living_source.pcd) and [`Local Refinement Registration`](https://www.open3d.org/docs/release/tutorial/pipelines/global_registration.html#Local-refinement) by default.

For all available options
```
$ python3 run.py -h
```

### Useful options
You can adjust the visualization type, model, voxel size and whether you want to color the target and source pointcloud (to distinguish them):
- --method : to adjust the visualization type
- --model : to adjust the model used
- --voxel_size : to adjust the voxel size
- --colorize : to adjust whether the model is using the original color or solid colors
