import open3d as o3d
import copy
from pcd_register.preprocessing import preprocess_pointcloud, downsample, compute_features

def test_downsample():
    # Create a sample point cloud for testing
    pointcloud = o3d.io.read_point_cloud(o3d.data.DemoICPPointClouds().paths[0])
    pointcloud_temp = copy.deepcopy(pointcloud)
    downsampled_pc = downsample(pointcloud_temp, voxel_size=0.05)

    # Assert that the output
    assert downsampled_pc is not None
    assert isinstance(downsampled_pc, o3d.geometry.PointCloud)
    assert len(downsampled_pc.points) != len(pointcloud.points)
    assert downsampled_pc is not pointcloud 

def test_compute_features():
    # Create a sample point cloud for testing
    pointcloud = o3d.io.read_point_cloud(o3d.data.DemoICPPointClouds().paths[0])
    pointcloud_temp = copy.deepcopy(pointcloud)
    features = compute_features(pointcloud_temp, voxel_size=0.05)

    # Assert that the output
    assert features is not None
    assert isinstance(features, o3d.pipelines.registration.Feature)
    assert pointcloud is not pointcloud_temp
    

def test_preprocess_pointcloud():
    # Create a sample point cloud for testing
    pointcloud = o3d.io.read_point_cloud(o3d.data.DemoICPPointClouds().paths[0])
    downsampled_pc, features = preprocess_pointcloud(pointcloud, voxel_size=0.05)

    # Assert that the outputs are instances of PointCloud and Feature respectively
    assert isinstance(downsampled_pc, o3d.geometry.PointCloud)
    assert isinstance(features, o3d.pipelines.registration.Feature)
