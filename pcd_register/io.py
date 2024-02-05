import open3d as o3d
import copy

def load_pointcloud(filepath):
    try:
        pointcloud = o3d.io.read_point_cloud(filepath)
        print(f"Loaded point cloud from {filepath}")
        return pointcloud
    except Exception as e:
        print(f"Error: {e}")
        return None

def draw_pointcloud(pointclouds):
    o3d.visualization.draw_geometries(pointclouds)

def draw_registration_result(source, target, transformation):
    source_temp = copy.deepcopy(source)
    target_temp = copy.deepcopy(target)

    source_temp.paint_uniform_color([1, 0.706, 0])
    target_temp.paint_uniform_color([0, 0.651, 0.929])

    source_temp.transform(transformation)

    o3d.visualization.draw_geometries([source_temp, target_temp])