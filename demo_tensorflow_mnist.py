# -*- coding:utf-8 -*-
#
# @Author: Miss
# @Time:   18/7/11   19:29
# @Name:   demo_tensorflow_mnist
#
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
import numpy as np
import matplotlib.pyplot as plt

print('下载数据')

mnist = input_data.read_data_sets('MNIST_data/', one_hot=True)
