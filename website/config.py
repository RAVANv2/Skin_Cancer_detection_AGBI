from easydict import EasyDict as edict
from pathlib import Path

def get_config():
    conf = edict()
    conf.data_path = Path('test_images')
    return conf
