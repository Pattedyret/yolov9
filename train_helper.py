import torch
from torch.serialization import safe_globals, add_safe_globals
from models.yolo import DetectionModel
from torch.nn import Sequential, Conv2d, BatchNorm2d, ModuleList, Module, SiLU
from models.common import *

# Get all classes from models.common
common_classes = [obj for name, obj in globals().items() if isinstance(obj, type)]

# Add required classes to safe globals
add_safe_globals([
    DetectionModel, 
    Sequential, 
    Conv2d,
    BatchNorm2d,
    ModuleList,
    Module,
    SiLU
] + common_classes)

# Now run the training script
import train

if __name__ == '__main__':
    train.main(train.parse_opt()) 