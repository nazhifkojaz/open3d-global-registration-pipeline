import open3d as o3d

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