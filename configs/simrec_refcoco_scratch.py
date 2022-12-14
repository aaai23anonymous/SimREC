from simrec.config import LazyCall
from .common.dataset import dataset
from .common.train import train
from .common.optim import optim
from .common.models.simrec import model


# Refine data path depend your own need
dataset.ann_path["refcoco"] = "/home/dataset/rec/anns/refcoco.json"
dataset.image_path["refcoco"] = "/home/dataset/rec/images/train2014"
dataset.mask_path["refcoco"] = "/home/dataset/rec/masks/refcoco"

# Refine training cfg
train.output_dir = "./output/test_no_syncbn_one_gpu"
train.batch_size = 32
train.save_period = 1
train.log_period = 10
train.evaluation.eval_batch_size = 32
train.sync_bn.enabled = False

# Refine optim
optim.lr = train.base_lr

# Refine model cfg
model.visual_backbone.pretrained = True
model.visual_backbone.pretrained_weight_path="./data/weights/cspdarknet_coco.pth"
