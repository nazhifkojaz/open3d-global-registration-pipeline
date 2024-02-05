import open3d as o3d
import numpy as np
import argparse

from pcd_register.io import load_pointcloud, draw_pointcloud, draw_registration_result
from pcd_register.preprocessing import preprocess_pointcloud
from pcd_register.registration import rough_registration, fine_registration

def main(method, voxel_size):
    source = load_pointcloud('data/cloud_bin_0.pcd')
    target = load_pointcloud('data/cloud_bin_1.pcd')

    if method == 0:
        draw_pointcloud([source, target])
        return
    
    source_downsampled, source_features = preprocess_pointcloud(source, voxel_size=voxel_size)
    target_downsampled, target_features = preprocess_pointcloud(target, voxel_size=voxel_size)

    if method == 1:
        draw_pointcloud([source_downsampled, target_downsampled])
        return
    result_ransac = rough_registration(source_downsampled, target_downsampled, source_features, target_features, voxel_size=voxel_size)

    if method == 2:
        draw_registration_result(source_downsampled, target_downsampled, result_ransac.transformation)
        return
    
    result_icp = fine_registration(source, target, result_ransac, voxel_size=voxel_size)
    if method == 3:
        draw_registration_result(source, target, result_icp.transformation)
        return
    
if __name__ == "__main__":
    class ArgumentParserWithDefaults(argparse.ArgumentParser):
        def add_argument(self, *args, help=None, default=None, **kwargs):
            if help is not None:
                kwargs["help"] = help
            if default is not None and args[0] != "-h":
                kwargs["default"] = default
                if help is not None:
                    kwargs["help"] += " (default: {})".format(default)
            super().add_argument(*args, **kwargs)
        
    parser = ArgumentParserWithDefaults(description="open3d global registration",
                                        formatter_class=argparse.RawTextHelpFormatter)
    
    method = "Visualization type\n"
    method += "0: Non-processed model\n"
    method += "1: Downsampled model.\n"
    method += "2: Rough Registration.\n"
    method += "3: Fine Registration.\n"
    parser.add_argument("--method", type=int, choices=[0, 1, 2, 3], default=3, help=method)
    parser.add_argument("--voxel_size", type=float, default=0.05, help="Voxel size for downsampling.")

    args = parser.parse_args()
    
    main(args.method, args.voxel_size)