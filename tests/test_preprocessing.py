import open3d as o3d
import copy
import pytest
from pcd_register.preprocessing import preprocess_pointcloud, downsample, compute_features


@pytest.fixture
def source_pointcloud():
    return o3d.io.read_point_cloud(o3d.data.DemoICPPointClouds().paths[0])

@pytest.fixture
def target_pointcloud():
    return o3d.io.read_point_cloud(o3d.data.DemoICPPointClouds().paths[1])

def test_preprocess_pointcloud(source_pointcloud, target_pointcloud):
     # Create a sample point cloud for testing
    pointcloud = o3d.io.read_point_cloud(o3d.data.DemoICPPointClouds().paths[0])
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