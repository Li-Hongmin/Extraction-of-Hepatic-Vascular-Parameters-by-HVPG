# Segmentation Network (2.5D)

The model is based on UNet with modifications of the dimension with shape of h x w x 5.

## Dependencies

Ubuntu 20.04.3, python 3.6, CUDA 11.0, anaconda (4.10.1),nibabel (3.2.1), SimpleITK (2.1.1), numpy (1.19.5), scikit-image (0.17.2), scipy (1.5.2), pytorch (1.7.1), tqdm(4.46.0), opencv-python(4.46.0.66), itk(5.2.0), tensorboard(2.5.0)

## Setup

```bash
conda install pytorch==1.7.1 torchvision==0.8.2 torchaudio==0.7.2 -c pytorch
pip install nibabel==3.2.1
pip install tensorboard==2.5.0
pip install simpleITK==5.2.0
...
```

## Data

##### Prepare data

1. Annotate your data and convert to nifity format files (.nii/.nii.gz).

   example(hepatic vein):

   <img src="./DemoData/img1.png" style="zoom:50%;" />

2. Put the original image and the corresponding labels into two folders to prepare for preprocessing and training.

##### Preprocess data

Preprocess data into numpy files required by the network: modify the corresponding path parameters in the `preprocess.py` and run it by your environment.

You can train better network models by modifying these preprocessing parameters:

 `*spacing*, *shape*, *data_type*(can be modified by yourself)`

## Run

#### Train

  run `train.py`

  *You need check and set the parameters: CUDA_VISIBLE_DEVICES, dir_checkpoint, input_path, label_path, batchsize, lr, model_type, channels, classes...

#### Test

  run `predict.py`

  *You need to check and set the parameters: CUDA_VISIBLE_DEVICES, model_path, threshold, model_type, channels, classes, data_type, ornt, spacing, shape(according to your preprocess parameters), img_nii_dir, pred_dir...

## Results

The following is one of my predicting results.

<img src="./DemoData/img2.png" style="zoom:50%;" />

<img src="./DemoData/img3.png" style="zoom:75%;" />


# Extraction of Hepatic Vascular Parameters
  
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


