import open3d as o3d
import copy
import pytest
import numpy as np
from pcd_register.preprocessing import preprocess_pointcloud, downsample, compute_features


@pytest.fixture
def load_pointcloud():
    return o3d.io.read_point_cloud(o3d.data.DemoICPPointClouds().paths[0])

def test_preprocess_pointcloud(load_pointcloud):
    # Load a sample pointcloud from demo data
    pointcloud = load_pointcloud
    pointcloud_temp = copy.deepcopy(pointcloud)
    pointcloud_downsampled, pointcloud_features = preprocess_pointcloud(pointcloud_temp, voxel_size=0.05)

    # Assert that the pointcloud_downsampled
    assert pointcloud_downsampled is not None
    assert isinstance(pointcloud_downsampled, o3d.geometry.PointCloud)
    assert len(pointcloud_downsampled.points) != len(pointcloud.points)
    assert pointcloud_temp is not pointcloud 

    # Assert that the pointcloud_features
    assert pointcloud_features is not None
    assert isinstance(pointcloud_features, o3d.pipelines.registration.Feature)
    assert pointcloud_temp is not pointcloud

def test_downsample_invalid_input(load_pointcloud):
    # Test failure case when invalid input is provided
    with pytest.raises(AttributeError):
        downsample(None, 0.05)

    with pytest.raises(TypeError):
        downsample(load_pointcloud, None)

    with pytest.raises(ValueError):
        downsample(load_pointcloud, -0.05)

def test_downsample_consistency(load_pointcloud):
    pointcloud_downsampled_1 = downsample(load_pointcloud)
    pointcloud_downsampled_2 = downsample(load_pointcloud)

    # Assert that the downsampled point clouds are consistent
    assert np.allclose(pointcloud_downsampled_1.points, pointcloud_downsampled_2.points)

def test_compute_features_dimension(load_pointcloud):
    pointcloud_features = compute_features(load_pointcloud)

    # Assert that the dimension of the features is as expected (33)
    assert pointcloud_features.data.shape[0] == 33

def test_compute_features_consistency(load_pointcloud):
    pointcloud_fpfh_1 = compute_features(load_pointcloud)
    pointcloud_fpfh_2 = compute_features(load_pointcloud)

    # Assert that the computed features are consistent
    assert np.allclose(pointcloud_fpfh_1.data, pointcloud_fpfh_2.data)

def test_compute_features_invalid_input(load_pointcloud):
    # Test failure case when invalid input is provided
    with pytest.raises(AttributeError):
        compute_features(None)

    with pytest.raises(TypeError):
        compute_features(load_pointcloud, None)

    with pytest.raises(ValueError):
        compute_features(load_pointcloud, -0.05)