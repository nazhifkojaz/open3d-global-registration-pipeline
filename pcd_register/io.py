import open3d as o3d
import copy

def load_pointcloud(filepath):
    """
    Load point cloud from file.

    Args:
    - filepath (str): path to the point cloud file.

    Returns:
    - pointcloud (open3d.geometry.PointCloud): the point cloud object.
    """
    pointcloud = o3d.io.read_point_cloud(filepath)
    return pointcloud
    
def draw_pointcloud(source, target, transformation, colorized=1):
    """
    Visualize the registration result.
    
    Args:
    - source (open3d.geometry.PointCloud): source point cloud object.
    - target (open3d.geometry.PointCloud): target point cloud object.
    - transformation (numpy.ndarray): transformation matrix.
    - colorized (int): flag to colorize the point clouds (default: 1).
    
    Returns:
    - None
    """
    source_temp = copy.deepcopy(source)
    target_temp = copy.deepcopy(target)

    if colorized:
        source_temp.paint_uniform_color([1, 0.706, 0])
        target_temp.paint_uniform_color([0, 0.651, 0.929])

    source_temp.transform(transformation)

    o3d.visualization.draw_geometries([source_temp, target_temp])