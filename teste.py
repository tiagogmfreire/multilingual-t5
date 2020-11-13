# python teste.py --module_import="multilingual_t5.tasks"
from multilingual_t5 import preprocessors
from multilingual_t5 import utils
import t5.data
from t5.data import sentencepiece_vocabulary
from t5.evaluation import metrics
import tensorflow_datasets as tfds

print("aloha!")