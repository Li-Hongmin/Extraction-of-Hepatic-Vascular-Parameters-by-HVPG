# Extraction of Hepatic Vascular Parameters

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/Li-Hongmin/Extraction-of-Hepatic-Vascular-Parameters-by-HVPG)

  
Preprocessing of 3-D medical images and extraction of vascular parameters.

## Setup

Install basic dependencies.
```bash
sudo apt-get update
sudo apt-get install libosmesa6-dev

```

If you don't have conda, I recommand the Mambaforge.
```bash
curl -L -O "https://github.com/conda-forge/miniforge/releases/latest/download/Mambaforge-$(uname)-$(uname -m).sh"
bash Mambaforge-$(uname)-$(uname -m).sh
source /home/gitpod/.bashrc
```


If you use conda, just replace mamba to conda.
```bash
mamba create -n vmtk python==3.6.9
mamba activate vmtk
mamba install -c vmtk vtk itk vmtk
pip install itk scikit-image nibabel xlwt xlrd xlutils vtk tqdm
```

Fix vmtk bug, by run the following command.
```bash
python fixbug_vmtk.py 
```

## Run

#### Use the source code

*Command "mamba activate vmtk", to switch to the vmtk environment and enter the directory of the source code. 
```bash
mamba activate vmtk
```

The input files are only nifti files. This code can be used to extract the parameters of the hepatic vessels. Please place your nifti files in the directory. Our default directory is "DemoData". You can modify the directory in the script.

nifti_file_folder is the directory of the nifti files. The generated 3-D files include model files of vessels and the corresponding centerline files. After running, they will be stored in the directory of "ProcessedData". 
The features of vessels will be stored in excel file in the directory "Features". 

```bash
python extract_feature.py
```


