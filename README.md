# SimREC

[![Python](https://img.shields.io/badge/python-blue.svg)](https://www.python.org/)
![PyTorch](https://img.shields.io/badge/pytorch-%237732a8) 

SimREC is a simple and lightweight codebase for   our paper  "A Survivor in the Era of Large-Scale Pretraining: An Empirical Study of One-Stage Referring Expression Comprehension" .  More models will be updated. 

 

## Installation
- Clone this repo
```bash
git clone https://github.com/aaai23anonymous/SimREC.git
cd SimREC
```
- Create a conda virtual environment and activate it
```bash
conda create -n simrec python=3.7 -y
conda activate simrec
```
- Install Pytorch following the [official installation instructions](https://pytorch.org/get-started/locally/)
- Install mmcv following the [installation guide](https://github.com/open-mmlab/mmcv#installation)
- Install [Spacy](https://spacy.io/) and initialize the [GloVe](https://github-releases.githubusercontent.com/84940268/9f4d5680-4fed-11e9-9dd2-988cce16be55?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAIWNJYAX4CSVEH53A%2F20210815%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20210815T072922Z&X-Amz-Expires=300&X-Amz-Signature=1bd1bd4fc52057d8ac9eec7720e3dd333e63c234abead471c2df720fb8f04597&X-Amz-SignedHeaders=host&actor_id=48727989&key_id=0&repo_id=84940268&response-content-disposition=attachment%3B%20filename%3Den_vectors_web_lg-2.1.0.tar.gz&response-content-type=application%2Foctet-stream) and install other requirements as follows:
```
pip install -r requirements.txt
wget https://github.com/explosion/spacy-models/releases/download/en_vectors_web_lg-2.1.0/en_vectors_web_lg-2.1.0.tar.gz -O en_vectors_web_lg-2.1.0.tar.gz
pip install en_vectors_web_lg-2.1.0.tar.gz
```

## Data preparation

-  Follow the instructions of  [DATA_PRE_README.md](./DATA_PRE_README.md) to generate training data and testing data.
-  Download the pretrained weights of backbone (vgg, darknet, cspdarknet, DResNet, etc.).  Expect for DResNet, all pretrained backbones are trained on COCO 2014 *train+val*  set while removing the images appeared in the *val+test* sets of RefCOCO, RefCOCO+ and RefCOCOg (nearly 6500 images).  Please follow the instructions of  [DATA_PRE_README.md](./DATA_PRE_README.md) to download them.

## Training and Evaluation 

<!-- 1. Prepare your settings. To train a model, you should  modify ``./config/config.yaml``  to adjust the settings  you want. 
2. Train the model. run ` train.py`  under the main folder to start training:
```
python train.py --config ./config/config.yaml
```
3. Test the model.   Then, you can run ` test.py`  by
```
python test.py --eval-weights ./logs/simrec/1/weights/det_best.pth
```
4. Training log.  Logs are stored in ``./logs`` directory, which records the detailed training curve and accuracy per epoch. If you want to log the visualizations, please  set  ``LOG_IMAGE`` to ``True`` in ``config.yaml``.    -->

1. **Config preparation**. Prepare your own configs in [configs](./configs), you don't need to rewrite all the contents in config every time.You can import the config as a python file to use the default configs in [configs/common](./configs/common) as follows:

```python
# your own config.py
from simrec.config import LazyCall
from .common.dataset import dataset
from .common.train import train
from .common.optim import optim
from .common.models.simrec import model

# modify the config depend your own need
dataset.ann_path["refcoco"] = "path/to/refcoco_data"
train.output_dir = "./path/to/output_dir"
...
```

2. **Train the model**. Run `bash/train.sh` under the [tools](./tools) to start training, for example, training `simrec` model on 4 GPUs:
```shell
bash tools/train.sh config/simrec_refcoco_scratch.py 4
```
The `training logs`, `tensorboard logs`, `config.yaml` and `model checkpoints` will be automatically saved under `cfg.train.output_dir`.

3. **Resume training**. We support two resume training mode. You can resume from a specific checkpoint or resume from the latest checkpoint:

- Auto resume from `last_checkpoint.pth`:
```python
# config.py
from .common.train import train
train.auto_resume.enabled = True
```
Setting `train.auto_resume.enabled=True`, which will automatically resume from `last_checkpoint.pth` saved in `cfg.train.output_dir`.

- Resume from a specific checkpoint

```python
# config.py
from .common.train import train

# disable auto resume first
train.auto_resume.enabled = False

# modify the resume path
train.resume_path = "path/to/specific/checkpoint.pth"
```
Setting `train.resume_path` to the specific `checkpoint.pth` you want to resume from.

4. **Test the model.** Run `bash/eval.sh` under [tools](./tools) to evaluate the saved weight.

```shell
bash tools/eval.sh config/simrec_refcoco_scratch.py 4 /path/to/checkpoint
```

## Model Zoo
More results  are available  in [Model Zoo](https://github.com/aaai23anonymous/SimREC/blob/main/MODEL_ZOO.md).

 

## License

This project is released under the [Apache 2.0 license](LICENSE).


## Acknowledgement

Thanks a lot for the nicely organized code from the following repos
- [OpenVQA](https://github.com/MILVLG/openvqa).
- [Swin-Transformer](https://github.com/microsoft/Swin-Transformer)
- [Detectron2](https://github.com/facebookresearch/detectron2)

