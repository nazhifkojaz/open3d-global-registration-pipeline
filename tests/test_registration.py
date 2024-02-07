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
    
    # assert that the output is not None and an instance of RegistrationResult
    assert result is not None
    assert isinstance(result, o3d.pipelines.registration.RegistrationResult)

def test_rough_registration_invalid_input(source_pointcloud, target_pointcloud):
    # Extract source and target point clouds and their features from fixtures
    source, source_features = source_pointcloud
    target, target_features = target_pointcloud

    # Test failure case when invalid input is provided
    with pytest.raises(TypeError):
        rough_registration(None, target, source_features, target_features)

    with pytest.raises(TypeError):
        rough_registration(source, None, source_features, target_features)

    with pytest.raises(TypeError):
        rough_registration(source, target, None, target_features)

    with pytest.raises(TypeError):
        rough_registration(source, target, source_features, None)

    with pytest.raises(TypeError):
        rough_registration(source, target, source_features, target_features, voxel_size=None)

def test_fine_registration(source_pointcloud, target_pointcloud):
    # Extract source and target point clouds and their features from fixtures
    source, source_features = source_pointcloud
    target, target_features = target_pointcloud

    result_ransac = rough_registration(source, target, source_features, target_features)
    result = fine_registration(source, target, result_ransac)

    # assert that the output is an instance of RegistrationResult
    assert result is not None
    assert isinstance(result, o3d.pipelines.registration.RegistrationResult)

def test_fine_registration_invalid_input(source_pointcloud, target_pointcloud):
    # Extract source and target point clouds and their features from fixtures
    source, source_features = source_pointcloud
    target, target_features = target_pointcloud

    result_ransac = rough_registration(source, target, source_features, target_features)

    # Test failure case when invalid input is provided
    with pytest.raises(TypeError):
        fine_registration(None, target, result_ransac)

    with pytest.raises(TypeError):
        fine_registration(source, None, result_ransac)

    with pytest.raises(AttributeError):
        fine_registration(source, target, None)

    with pytest.raises(TypeError):
        fine_registration(source, target, result_ransac, voxel_size=None)
