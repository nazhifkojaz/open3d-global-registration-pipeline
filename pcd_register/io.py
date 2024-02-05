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
    try:
        pointcloud = o3d.io.read_point_cloud(filepath)
        print(f"Loaded point cloud from {filepath}")
        return pointcloud
    except Exception as e:
        print(f"Error: {e}")
        return None

def draw_pointcloud(pointclouds):
    """
    Visualize point cloud.
    
    Args:
    - pointclouds (list of open3d.geometry.PointCloud): list of point cloud objects.
    
    Returns:
    - None
    """
    o3d.visualization.draw_geometries(pointclouds)

def draw_registration_result(source, target, transformation):
    """
    Visualize the registration result.
    
    Args:
    - source (open3d.geometry.PointCloud): source point cloud object.
    - target (open3d.geometry.PointCloud): target point cloud object.
    - transformation (numpy.ndarray): transformation matrix.
    
    Returns:
    - None
    """
    source_temp = copy.deepcopy(source)
    target_temp = copy.deepcopy(target)

    source_temp.paint_uniform_color([1, 0.706, 0])
    target_temp.paint_uniform_color([0, 0.651, 0.929])

    source_temp.transform(transformation)

    o3d.visualization.draw_geometries([source_temp, target_temp])