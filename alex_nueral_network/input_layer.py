import tensorflow as tf
from keras import layers, models

def create_alexnet_model(input_shape = (227,227,1), num_classes=10):
    model = models.Seq