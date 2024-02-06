import pytest
import open3d as o3d
from pcd_register.registration import rough_registration, fine_registration
from pcd_register.preprocessing import preprocess_pointcloud, compute_features

@pytest.fixture
def source_pointcloud():
    # Load a sample pointcloud from demo data
    source = o3d.io.read_point_cloud(o3d.data.DemoICPPointClouds().paths[0])
    source_downsampled, source_features = preprocess_pointcloud(source)
    return source_downsampled, source_features

@pytest.fixture
def target_pointcloud():
    # Load a sample pointcloud from demo data
    target = o3d.io.read_point_cloud(o3d.data.DemoICPPointClouds().paths[1])
    target_downsampled, target_features = preprocess_pointcloud(target)
    return target_downsampled, target_features

def test_rough_registration(source_pointcloud, target_pointcloud):
    # Extract source and target point clouds and their features from fixtures
    source, source_features = source_pointcloud
    target, target_features = target_pointcloud

    result = rough_registration(source, target, source_features, target_features)
    
    # assert that the output is an instance of RegistrationResult
    assert isinstance(result, o3d.pipelines.registration.RegistrationResult)

def test_fine_registration(source_pointcloud, target_pointcloud):
    # Extract source and target point clouds and their features from fixtures
    source, source_features = source_pointcloud
    target, target_features = target_pointcloud

    result_ransac = rough_registration(source, target, source_features, target_features)
    result = fine_registration(source, target, result_ransac)

    # assert that the output is an instance of RegistrationResult
    assert isinstance(result, o3d.pipelines.registration.RegistrationResult)
