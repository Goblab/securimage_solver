# about captcha image
IMAGE_HEIGHT = 40
IMAGE_WIDTH = 230
CHAR_SETS = 'ABCDEFGHKLMNPRSTUVWYZabcdefghklmnprstuvwyz23456789'
CLASSES_NUM = len(CHAR_SETS)
CHARS_NUM = 2
# for train
RECORD_DIR = './data'
TRAIN_FILE = 'train.tfrecords'
VALID_FILE = 'valid.tfrecords'

