import open3d as o3d
import numpy as np
from pcd_register.io import load_pointcloud, draw_pointcloud, draw_registration_result
from pcd_register.preprocessing import preprocess_pointcloud

def main():
    source = load_pointcloud("data/cloud_bin_0.pcd")
    target = load_pointcloud("data/cloud_bin_1.pcd")

    source_downsampled, source_features = preprocess_pointcloud(source)
    target_downsampled, target_features = preprocess_pointcloud(target)
    
    # draw_pointcloud([target, source])
    # draw_registration_result(source, target, np.identity(4))
    draw_registration_result(source_downsampled, target_downsampled, np.identity(4))

if __name__ == "__main__":
    main()