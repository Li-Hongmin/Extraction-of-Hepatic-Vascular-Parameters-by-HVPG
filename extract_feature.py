# -*- coding: UTF-8 -*-
from Code.VesselParameter.compute_centerlines import compute_centerlines
from Code.VesselParameter.compute_params import compute_params
import os
import tqdm

def compute_feature(nifti_file):
    # this funciton is used to compute the feature of the nifti file
    # nifti_file: the path of the nifti file
    # it will save the feature file in the XXX_ProcessedData folder
    processed_data_path = "ProcessedData"
    result_path = "Features"
    feature_file_path = result_path + "/" + "feature.xls"
    os.makedirs(processed_data_path, exist_ok=True)
    # set the prefix as the file name of the nifti file
    # os file name
    filename = os.path.basename(nifti_file)
    prefix = filename.split(".")[0]
    compute_centerlines(nifti_file, processed_data_path, prefix)
    mesh_file = processed_data_path + "/" + prefix + ".vtk"
    centerlines_file = processed_data_path + "/" + prefix + "_centerlines.vtk"
    feature_file_path = processed_data_path + "/" + "feature.xls"
    compute_params(nifti_file, mesh_file, centerlines_file, feature_file_path)


# list all the nifti file with suffix .nii.gz
nifti_file_folder = "DemoData"
nifti_file_list = [nifti_file_folder + "/" + file for file in os.listdir(nifti_file_folder) if file.endswith(".nii.gz")]

# # use for loop to compute the feature
# for i in tqdm.tqdm(range(len(nifti_file_list)), desc="Compute the feature of the nifti file"):
#     nifti_file = nifti_file_list[i]
#     if nifti_file is not None:
#         compute_feature(nifti_file)

# use multiprocessing to compute the feature
print("Use multiprocessing to compute the feature of the nifti file")
print("this may take a long time")
from multiprocessing import Pool
pool = Pool()
pool.map(compute_feature, nifti_file_list)
pool.close()
pool.join()