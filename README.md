# Fast-and-accurate-neural-reflectance-transformation-imaging-through-knowledge-distillation Implementation
This is a PyTorch implementation of Fast-and-accurate-neural-reflectance-transformation-imaging-through-knowledge-distillation. 

## Getting Started
Download  
```bash
git clone https://github.com/univr-GRAIL/Fast-and-accurate-neural-reflectance-transformation-imaging-through-knowledge-distillation.git

```
Change working directory
```bash
cd Fast-and-accurate-neural-reflectance-transformation-imaging-through-knowledge-distillation
```
## Create a virtual environment:   
```bash
python -m venv neuralenv  
```
### Activate a virtual environment:  
On Windows: 
```bash
neuralenv\Scripts\activate  
```
On Linux/macOS:  
```bash
source neuralenv/bin/activate  
```
## Install Dependencies:   
Make sure you're in a Python environment, neuralenv
Install the dependencies using the following command:    
```bash    
pip install -r requirements.txt  
pip install torch==2.4.1 torchvision==0.19.1 torchaudio==2.4.1 --index-url https://download.pytorch.org/whl/cu124
```
## Training



To Train train a Fast and accurate neural reflectance transformation imaging through knowledge distillation   
Execute:  
   ```bash
python train.py --data_path data_path --src_img_type src_img_type --output_path output_path
   ```  
   Where:   
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; data_path  # Path to your training dataset  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; output_path  # Directory for saving outputs  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; mask  # True or False, for Enable/disable masking  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; src_img_type  # Image extension type, i.e., jpg [default], png.  
At the end of the training, the outputs will be saved inside the output-path directory, inside the Teacher and Student subdirectories. Each subdirectory contains:
- The trained model (.pth) 
- Compressed coefficients
- Image planes and a JSON file for OpenLIME visualization

## Testing/Relighting  
  **Download, example, trained model files and test light direction file from <a href="https://univr-my.sharepoint.com/:f:/g/personal/tinsaegebrechristos_dulecha_univr_it/IgCgd69EOn9jS5eopO9BvviaARIdxmdPiriFBEWF3Hwdoqg?e=0lYgGU" text-decoration="none" target="_blank">here </a>**  


###  Run:  
```bash
python test.py  --model_path model_path  --light_path light_path
```  

Where:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;model_path # Path to the trained model directory and encoded coefficients  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; light_path   # test light directions  and mask path, if needed  

For example, if you set: 
```bash 
model_path=test_dataset/outputs/Student 
light_path = test_dataset/test_fig6 and
```
This will generate images shown in figure 6 on the paper and saves it in the relighted folder. 

but if you set:
```bash 
light_path = 'test_dataset/test'
``` 
Generates images relighted from 20 light directions Which corresponds to images found 
 <a href="https://univr-my.sharepoint.com/:f:/g/personal/tinsaegebrechristos_dulecha_univr_it/IgBQ2HC32WNZRYNcDlFqcJo9Aaj7m9vzgRE1fayoK48t3DE?e=6Mu0Ei" target="_blank"> here </a>.  




 <!-- <a href="https://univr-my.sharepoint.com/:f:/g/personal/tinsaegebrechristos_dulecha_univr_it/EkVPviXq86VGjixc6Ti18SoBdkKTOeaWqBlQzV09rpdHfg?e=cY54V6" text-decoration="none" target="_blank">**here** </a>  -->


## Datasets:

All the images(training, test, and relighted using different algorithms) can be found at 
<a href="https://univr-my.sharepoint.com/:f:/g/personal/tinsaegebrechristos_dulecha_univr_it/Er4M2DWps1FDjLce2Ssd3pYByROXPOKOeeYATFjhl261cQ?e=0ClcJ9" text-decoration="none" target="_blank"> DiskNeuralRTI Datasets </a>.

##  Evaluation / Metrics
For example, To reproduce Table 6 from the paper (Average LPIPS / ΔE for RealRTI relighting):

### 1. Set a parameter
 Download RealRTI dataset from 
 <a href="https://univr-my.sharepoint.com/:f:/g/personal/tinsaegebrechristos_dulecha_univr_it/EjRfAl2DeppAsDLDo5rkr0gBg1-54GrN3WYzLIKQRu2yPg?e=fbv2tp" target="_blank"> here </a>.  
 
 set parent_folder = ['RealRTI dataset folder'] # path to the parent folder containing subfolders(default: ./datasets/RealRTI) 
 
### 2. Run
``` bash
python python calculate_metrics.py --parent_folder parent_folder
```
## 📁 Project Structure

```bash
DiskNeuralRTI/
│
├── requirements.txt  
├── Calculate_metrics.py 
├── test.py  
├── train.py  
├── README.md             # Project dependencies
├── modules/                 
    ├── dataset/                   
    ├── model/
    ├── relight/                  
    ├── utils/
    │   └── params.py             # Tra         
                   # Project documentation
```

## Citation

If you consider our work useful for your research, please consider citing:

```bash
@article{dulecha2025fastaccurateneuralreflectance,
      title={Fast and accurate neural reflectance transformation imaging through knowledge distillation}, 
      author={Tinsae G. Dulecha and Leonardo Righetto and Ruggero Pintus and Enrico Gobbetti and Andrea Giachetti},
      year={2025},
      eprint={2510.24486},
      archivePrefix={arXiv},
      primaryClass={cs.CV},
      url={https://arxiv.org/abs/2510.24486}, 
}
```
## License

This project is licensed under the MIT License with the Commons Clause.

You are free to use, modify, and distribute this code for non-commercial purposes. Commercial use is prohibited without obtaining a commercial license. For commercial use inquiries, please contact the authors.




