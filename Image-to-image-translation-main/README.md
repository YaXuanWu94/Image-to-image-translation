# Generative-AI Navigation Information Competition for UAV Reconnaissance in Natural Environments I : Image Data Generation
## Environment
* Operating system: CentOS 7.8
* Programmimg language: Python 3.8.19
* Hardware: NVIDIA Tesla V100-PCIE-32GB
## create folder
```bash
./
├── river
├── road
```
## Intallation(conda environment)
An environment can be created with all the Python dependencies.
```bash
conda env create -f environment.yml
```
## Data preparation
After the data preprocessing, place the training dataset `img` and `label_img` in `train_B` and `train_A`.
```bash
./river/AICUP2024-spring/dataset/cityscapes
├── train_A
│   ├── TRA_RI_1000000.png
│              .
|              .
|              .
│   └── TRA_RI_1002159.png
├── train_B
│   ├── TRA_RI_1000000.jpg
|              .
|              .
|              .
│   └── TRA_RI_1002159.jpg
├── test_A
|   ├── PRI_RI_1000000.png
|              . 
|              .
|              .
|   └── PRI_RI_1000359.png
└── test_B
```
```bash
./road/AICUP2024-spring/dataset/cityscapes
├── train_A
│   ├── TRA_RO_1002160.png
│              .
|              .
|              .
│   └── TRA_RO_1004319.png
├── train_B
│   ├── TRA_RO_1002160.jpg
|              .
|              .
|              .
│   └── TRA_RO_1004319.jpg
├── test_A
|   ├── PRI_RO_100360.png
|              . 
|              .
|              .
|   └── PRI_RO_1000719.png
└── test_B
```
## Training
* **river**
```bash
python train.py --name RIVER --label_nc 0 --no_instance
```
* **road**
```bash
python train.py --name ROAD --label_nc 0 --no_instance
```
The model parameters will be saved in `checkpoints` folder.
> latest_net_G.pth

> latest_net_D.pth

## Testing
* **river**
```bash
python test.py --name RIVER --label_nc 0 --no_instance --how_many 360
```
* **road**
```bash
python test.py --name ROAD --label_nc 0 --no_instance --how_many 360
```
The generated results will be saved in `results` folder. And it also can be downloaded from [here](https://drive.google.com/drive/folders/14ndZe1obuvLoUSfteyIQHEnuyUXBjnve?usp=drive_link)

