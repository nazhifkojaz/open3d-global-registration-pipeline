import open3d as o3d
import numpy as np
import argparse

from pcd_register.io import load_pointcloud, draw_pointcloud
from pcd_register.preprocessing import preprocess_pointcloud
from pcd_register.registration import rough_registration, fine_registration

def main(method, model, voxel_size, colorize):
    if model == 1:
        source = load_pointcloud('data/office_source.pcd')
        target = load_pointcloud('data/office_source.pcd')
    else:
        source = load_pointcloud('data/living_source.pcd')
        target = load_pointcloud('data/living_target.pcd')

    if method == 0:
        draw_pointcloud(source, target, np.identity(4), colorize)
        return
    
    source_downsampled, source_features = preprocess_pointcloud(source, voxel_size)
    target_downsampled, target_features = preprocess_pointcloud(target, voxel_size)

    if method == 1:
        draw_pointcloud([source_downsampled, target_downsampled])
        return
    result_ransac = rough_registration(source_downsampled, target_downsampled, source_features, target_features, voxel_size=voxel_size)

    if method == 2:
        draw_pointcloud(source_downsampled, target_downsampled, result_ransac.transformation)
        return
    
    result_icp = fine_registration(source, target, result_ransac, voxel_size=voxel_size)
    if method == 3:
        draw_pointcloud(source, target, result_icp.transformation, colorize)
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

    model = "Model to use\n"
    model += "0: Living room\n"
    model += "1: Office\n"
    parser.add_argument("--model", type=int, choices=[0, 1], default=0, help=model)

    parser.add_argument("--voxel_size", type=float, default=0.05, help="Voxel size for downsampling.")

    parser.add_argument("--colorize", type=int, choices=[0, 1], default=1, help="Colorize the model.")

    args = parser.parse_args()
    
    main(args.method, args.model, args.voxel_size, args.colorize)