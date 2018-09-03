#!@Author : menglinpan
#!datetime : 2018/8/24 8:24

import os
import tensorflow as tf
import numpy as np
from sklearn.preprocessing import LabelBinarizer
import pandas as pd

os.chdir(r"F:\zhangjianwei")

data_x = pd.read_table("images.txt", delimiter=",", header=None)
data_y = pd.read_table("labels.txt", delimiter=",", header=None)

arr_x = np.asarray(data_x, np.float32)
arr_y = np.asarray(LabelBinarizer().fit_transform(data_y), np.float32)

state = np.random.get_state()
np.random.shuffle(arr_x)
np.random.set_state(state)
np.random.shuffle(arr_y)

training_x = arr_x[0:9000, :]
training_y = arr_y[0:9000, :]
testing_x = arr_x[9000:, :]
testing_y = arr_y[9000:, :]

x = tf.placeholder(tf.float32, [None, 784])
y = tf.placeholder(tf.float32, [None, 10])

def weight_int(_in, _out, _w=None, _h=None):
    if _w is not None:
        return tf.Variable(tf.random_normal([_w, _h, _in, _out], stddev=0.1))
    else:
        return tf.Variable(tf.random_normal([_in, _out], stddev=0.1))

def bais_init(_n):
    return tf.Variable(tf.random_normal([_n], stddev=0.1))

def conv2d_init(_input, _filter, _strides, _padding="SAME"):
    return tf.nn.conv2d(_input, _filter, _strides, _padding)

def pool2d_init(_value, _ksize, _strides, _padding="SAME"):
    return tf.nn.max_pool(_value, _ksize, _strides, _padding)

def train(x):
    input = tf.reshape(x, shape=[-1, 28, 28, 1])
    con = conv2d_init(input, weight_int(1, 32, 5, 5), _strides=[1, 1, 1, 1])
    relu = tf.nn.relu(tf.nn.bias_add(con, bais_init(32)))

    pool = pool2d_init(relu, _ksize=[1, 2, 2, 1], _strides=[1, 2, 2, 1])
    dp = tf.nn.dropout(pool, 0.8)
    dp_fc = tf.reshape(dp, shape=[-1, 14*14*32])
    out= tf.nn.xw_plus_b(dp_fc, weight_int(14*14*32, 10), bais_init(10))
    return out

y_ = train(x)
cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=y_, labels=y))
train = tf.train.GradientDescentOptimizer(learning_rate=0.001).minimize(cost)
predict = tf.equal(tf.argmax(y_, 1), tf.argmax(y, 1))
acc = tf.reduce_mean(tf.cast(predict, tf.float32))

batch_size = 128

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for i in range(3001):
        permution = np.random.permutation(9000)
        print(type(permution))
        print(permution.shape)
        batch_xs = training_x[permution[:batch_size], :]
        batch_ys = training_y[permution[:batch_size], :]
        sess.run(train, feed_dict={x: batch_xs, y: batch_ys})
        if i % 100 == 0:
            cur_cost = sess.run(cost, feed_dict={x: batch_xs, y: batch_ys})
            cur_acc = sess.run(acc, feed_dict={x: testing_x, y: testing_y})
            print(i, cur_cost, cur_acc)






