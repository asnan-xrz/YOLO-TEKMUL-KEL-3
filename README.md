# SETUP YOLOv11

conda create -n yolov11_custom python=3.12 -y

conda activate yolov11_custom

pip install ultralytics

kemudian biar bisa ngeproses pake gpu (bukan cpu), pastikan untuk menginstall:

1. https://developer.nvidia.com/cuda-downloads?target_os=Windows&target_arch=x86_64&target_version=Server2025&target_type=exe_local

2. https://pytorch.org/

Pastikan konfigurasikan path enviroment variables nya dengan benar

```
C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.8
C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.8\bin
C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.8\libnvvp
```

Pastikan juga pilih versi pytorch sesuai dengan versi CUDA kalian. Misalnya ini untuk versi cuda 12.8

pip3 install --upgrade torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu128

Kalau sudah semua, bisa run dengan

python predict.py

pastikan pilih nama source (file) yang benar untuk di predict. File hasil predict akan berada di folder runs-detect-predict.
