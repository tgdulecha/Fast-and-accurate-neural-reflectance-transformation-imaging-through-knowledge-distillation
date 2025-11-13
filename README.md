# Fast and accurate neural reflectance transformation imaging through knowledge distillation 
**PDF:**  <a href="https://doi.org/10.1016/j.cag.2025.104475" text-decoration="none" target="_blank">https://doi.org/10.1016/j.cag.2025.104475 </a>

This is a PyTorch implementation of Fast-and-accurate-neural-reflectance-transformation-imaging-through-knowledge-distillation.

---
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

Ensure your virtual environment is active, then run:

```bash
pip install -r requirements.txt
pip install torch==2.4.1 torchvision==0.19.1 torchaudio==2.4.1 --index-url https://download.pytorch.org/whl/cu124
```

## Training

To Train train the model, run:


```bash
python train.py --data_path <path_to_dataset> --src_img_type <jpg|png> --mask <True|False>
```

**Arguments:**

| Argument | Description |
|-----------|--------------|
| `--data_path` | Path to your training dataset |
| `--src_img_type` | Image format (default: `jpg`; supports `png`) |
| `--mask` | Enable or disable masking (`True` or `False`) |

**outputs**  
Training results will be saved in an outputs/ directory containing:  
- decoder.pth: Trained model
- coefficient.npy: Compressed coefficients
- Image planes and a JSON file for OpenLIME visualization  

## Testing/Relighting

Download example model files and test light directions from [this link](https://univr-my.sharepoint.com/:f:/g/personal/tinsaegebrechristos_dulecha_univr_it/IgCgd69EOn9jS5eopO9BvviaARIdxmdPiriFBEWF3Hwdoqg?e=0lYgGU).
 

### Run:

```bash
python test.py --model_path <path_to_model_files> --light_path <path_to_light_file> --mask_path <path_to_mask_file>

```

**Arguments:**

| Argument | Description |
|-----------|-------------|
| `--model_path` | Path to folder containing `decoder.pth`, `encoded.npy`, and plane images |
| `--light_path` | Path to test light direction file |
| `--mask_path` | Optional path to mask file (if masking was used) |

**Examples:**

```bash
# Generate Figure 6 from the paper
python test.py --model_path test_files/model_files --light_path test_files/test_dir.lp
```

```bash
# Generate relighted images from 20 light directions
python test.py --model_path test_files/model_files --light_path test_files/test_dirs.lp
```
**Arguments:**

| Argument | Description |
|-----------|-------------|
| `--model_path` | Path to folder containing `decoder.pth`, `encoded.npy`, and plane images |
| `--light_path` | Path to test light direction file |
| `--mask_path` | Optional path to mask file (if masking was used) |
The generated relighted images will be saved in a `relighted/` folder.

👉 This output is also: [Available here](https://univr-my.sharepoint.com/:f:/g/personal/tinsaegebrechristos_dulecha_univr_it/IgBQ2HC32WNZRYNcDlFqcJo9Aaj7m9vzgRE1fayoK48t3DE?e=6Mu0Ei)

---

## Datasets:

All the images(training, test, and relighted using different algorithms) can be found at
<a href="https://univr-my.sharepoint.com/:f:/g/personal/tinsaegebrechristos_dulecha_univr_it/Er4M2DWps1FDjLce2Ssd3pYByROXPOKOeeYATFjhl261cQ?e=0ClcJ9" text-decoration="none" target="_blank"> DiskNeuralRTI Datasets </a>.

## Evaluation / Metrics

For example, To reproduce Table 6 from the paper (Average LPIPS / ΔE for RealRTI relighting):
Download RealRTI dataset from
<a href="https://univr-my.sharepoint.com/:f:/g/personal/tinsaegebrechristos_dulecha_univr_it/EjRfAl2DeppAsDLDo5rkr0gBg1-54GrN3WYzLIKQRu2yPg?e=fbv2tp" target="_blank"> here </a>.

### Run

```bash
python calculate_metrics.py --parent_folder <path_to_RealRTI>
```

**Argument:**

| Argument | Description |
|-----------|-------------|
| `--parent_folder` | Path to folder RealRTI items, shown below |


```bash
RealRTI/  #parent-folder
├── item01
├── item02
├── item03
├── .
├── .
├── item12

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
@article{dulecha2025fast,
  title={Fast and accurate neural reflectance transformation imaging through knowledge distillation},
  author={Dulecha, Tinsae G and Righetto, Leonardo and Pintus, Ruggero and Gobbetti, Enrico and Giachetti, Andrea},
  journal={Computers \& Graphics},
  pages={104475},
  year={2025},
  publisher={Elsevier}
}

```

## License

This project is licensed under the MIT License with the Commons Clause.

You are free to use, modify, and distribute this code for non-commercial purposes. Commercial use is prohibited without obtaining a commercial license. For commercial use inquiries, please contact the authors.
