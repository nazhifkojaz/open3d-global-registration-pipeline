import open3d as o3d

def rough_registration(source, target, source_features=None, target_features=None, voxel_size=0.5):
    """
    Rough registration of two pointclouds
    
    Args:
    - source: open3d.geometry.PointCloud
    - target: open3d.geometry.PointCloud
    - source_features: open3d.pipelines.registration.Feature (default: None)
    - target_features: open3d.pipelines.registration.Feature (default: None)
    - voxel_size: float (default: 0.5)

    Returns:
    - result: open3d.pipelines.registration.RegistrationResult
    """
    distance_threshold = voxel_size * 1.5
    result = o3d.pipelines.registration.registration_ransac_based_on_feature_matching(
        source, target, source_features, target_features, True,
        distance_threshold,
        o3d.pipelines.registration.TransformationEstimationPointToPoint(False),
        3, [
            o3d.pipelines.registration.CorrespondenceCheckerBasedOnEdgeLength(
                0.9),
            o3d.pipelines.registration.CorrespondenceCheckerBasedOnDistance(
                distance_threshold)
        ], o3d.pipelines.registration.RANSACConvergenceCriteria(100000, 0.999))
    return result

def fine_registration(source, target, result_ransac, voxel_size=0.05):
    """
    Fine registration of two pointclouds
    
    Args:
    - source: open3d.geometry.PointCloud
    - target: open3d.geometry.PointCloud
    - result_ransac: open3d.pipelines.registration.RegistrationResult
    - voxel_size: float (default: 0.05)
    
    Returns:
    - result: open3d.pipelines.registration.RegistrationResult
    """
    distance_threshold = voxel_size * 0.4
    result = o3d.pipelines.registration.registration_icp(
        source, target, distance_threshold, result_ransac.transformation,
        o3d.pipelines.registration.TransformationEstimationPointToPlane())
    return result