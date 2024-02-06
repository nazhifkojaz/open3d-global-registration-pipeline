import open3d as o3d
from pcd_register.io import load_pointcloud

def test_load_pointcloud_success():
    # Test successful loading of point cloud
    pointcloud = load_pointcloud(o3d.data.DemoICPPointClouds().paths[0])
    
    # Assert that the output is an instance of PointCloud
    assert isinstance(pointcloud, o3d.geometry.PointCloud)

def test_load_pointcloud_failure():
    # Test failure case when invalid file path is provided
    invalid_file_path = "invalid_file.pcd"
    pointcloud = load_pointcloud(invalid_file_path)

    # Assert empty point cloud is returned
    assert len(pointcloud.points) == 0
