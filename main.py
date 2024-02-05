import open3d as o3d
import numpy as np
from pcd_register.io import load_pointcloud, draw_pointcloud, draw_registration_result

def main():
    source = load_pointcloud("data/cloud_bin_0.pcd")
    target = load_pointcloud("data/cloud_bin_1.pcd")
    # draw_pointcloud([target, source])
    draw_registration_result(source, target, np.identity(4))

if __name__ == "__main__":
    main()