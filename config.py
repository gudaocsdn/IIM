import os
from easydict import EasyDict as edict
import time
import torch

# init
__C = edict()
cfg = __C

#------------------------------TRAIN------------------------
__C.SEED = 3035  # random seed,  for reproduction
__C.DATASET = 'NWPU'  # dataset selection: GCC, SHHA, SHHB, UCF50, QNRF, WE, Mall, UCSD
__C.SIZE_MAP = True


__C.NET = 'HR_Net' #  optional ['HR_Net', 'VGG16_FPN']

if __C.NET == 'HR_Net':
    __C.PRE_HR_WEIGHTS = '../PretrainedModels/hrnetv2_w48_imagenet_pretrained.pth'

__C.RESUME = False  # contine training
__C.RESUME_PATH = './exp/10-31_11-51_NWPU_HR_Net_1e-05/latest_state.pth'

__C.GPU_ID = '2,3'  # sigle gpu: [0], [1] ...; multi gpus: [0,1]

__C.OPT = 'Adam'  #'Adam'
# learning rate settings
if __C.OPT == 'Adam':
    __C.LR_BASE_NET = 1e-5  # learning rate
    __C.LR_BM_NET = 1e-6  # learning rate

__C.MAX_EPOCH = 600
__C.PRINT_FREQ = 20

now = time.strftime("%m-%d_%H-%M", time.localtime())

__C.EXP_NAME = now \
    + '_' + __C.DATASET \
    + '_' + __C.NET 


__C.EXP_PATH = './exp'  # the path of logs, checkpoints, and current codes

#------------------------------VAL------------------------
__C.VAL_DENSE_START = 0
__C.VAL_FREQ = 1  # Before __C.VAL_DENSE_START epoches, the freq is set as __C.VAL_FREQ

#------------------------------VIS------------------------
__C.VISIBLE_NUM_IMGS = 1  # must be 1 for training images with the different sizes


#================================================================================
#================================================================================
#================================================================================