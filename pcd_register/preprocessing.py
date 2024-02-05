import open3d as o3d

def preprocess_pointcloud(pointcloud, voxel_size=0.05):
    downsampled_pc = downsample(pointcloud, voxel_size)
    features = compute_features(downsampled_pc)
    return downsampled_pc, features

def downsample(pointcloud, voxel_size=0.05):
    return pointcloud.voxel_down_sample(voxel_size)

def compute_features(pointcloud, voxel_size=0.05):
    radius_normal = voxel_size * 2
    pointcloud.estimate_normals(
        o3d.geometry.KDTreeSearchParamHybrid(radius=radius_normal, max_nn=30))
    
    radius_feature = voxel_size * 5
    pointcloud_fpfh = o3d.pipelines.registration.compute_fpfh_feature(
        pointcloud,
        o3d.geometry.KDTreeSearchParamHybrid(radius=radius_feature, max_nn=100)
    )
    return pointcloud_fpfh