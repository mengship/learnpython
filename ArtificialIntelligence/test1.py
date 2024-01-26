# # import tensorflow as tf
#
# tensorflow tutorials.mnist
# # tf.__version__
#
# pip install "chardet_version<5.0.0"
#
# ERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts.
# tensorboard 2.11.2 requires requests<3,>=2.21.0, but you have requests 2.20.1 which is incompatible.
# aiohttp 3.8.1 requires charset-normalizer<3.0,>=2.0, but you have charset-normalizer 3.0.0 which is incompatible.

import tensorflow as tf
# import tensorflow.compat.v1 as tf
from absl import app
# from tensorflow.lite.tutorials.mnist_tflite import dataset
# from tensorflow.examples.tutorials.mnist import input_data

import numpy as np
import matplotlib.pyplot as plt
import tensorflow_datasets as tfds

# Construct a tf.data.Dataset
ds = tfds.load('mnist', split='train', shuffle_files=True )

# def imshow(img):
#     plt.imshow(np.reshape(img, [28, 28]))
#     plt.show()

# Build your input pipeline
# ds = ds.shuffle(1024).repeat().batch(1) # 一批一个
# for example in ds.take(10): # 取出10个图片
#     image, label = example['image'], example['label'] # 将图象与结果值取出来
#     print(image.shape) # 打印出图片的尺寸
#     print(label) # label中已经写了这张图片的值，也就是结果值
    # print(np.nonzero(label))
    # imshow(image) # 打印出图片
# for i in image:
#     plt.imshow(tf.squeeze(i))
#     plt.show()
def weight_variable(shape):
    initial = tf.truncated_normal(shape, stddev=0.1) # 后面这个代表正态分布
    return tf.Variable(initial)

def bias_variable(shape):
    initial = tf.constant(0.1, shape=shape)
    return tf.Variable(initial)

def fcnn(image_batch):
    W_fc1 = weight_variable([784, 200])
    b_fc1 = bias_variable([200])
    W_fc2 = weight_variable([200, 200])
    b_fc2 = bias_variable([200])
    W_out = weight_variable([200, 10])
    b_out = bias_variable([10])
    hidden_1 = tf.nn.sigmoid(tf.matmul(image_batch, W_fc1) * b_fc1) # image_batch 是 B*784 hidden_1 是B*200
    hidden_2 = tf.nn.sigmoid(tf.matmul(hidden_1, W_fc2) * b_fc2) # hidden_2 B*200
    _y = tf.nn.softmax(tf.matmul(hidden_2, W_out) * b_out) # 这是不是激活函数，是一个概率
    return _y

# x = tf.placeholder(tf.float32, [None, 784])
# x = tf.enable_eager_execution(tf.float32, [None, 784])
x = tf.placeholder(shape=[None, 784], dtype=tf.float32)
# y_ = tf.placeholder(tf.float32, [None, 10])
y_ = tf.enable_eager_execution(tf.float32, [None, 10])
y = fcnn(x)
correct_prediction = tf.equal(tf.argmax(y_, 1), tf.argmax(y, 1))  # 取出最大的值
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32)) # 不希望出现整数

cross_entropy = tf.reduce_mean(tf.reduce_sum(-y_ * tf.log(y+0.0000001), reduction_indices=[1] )) # 此处加一个非零小数的原因是，如果y=0，则结果为无穷小，则溢出，返回None
train_step = tf.train.GrandientDescentOptimizer(0.01).minimize(cross_entropy)

training_iteration = 50000
batch_size = 64
display_step = 50
with tf.Session() as sess:
    sess.run(tf.initilize_all_variables())
    for iteration in range(training_iteration):
        batch_xs, batch_ys = ds.shuffle().repeat().next_batch(batch_size)# batch(batch_size)
        _, current_accuracy = sess.run([train_step, accuracy] , feed_dict = {x: batch_xs, y_: batch_ys})
        if iteration % display_step == 0:
            print('Iteration: %5d | Accuracy: %.6f' % (iteration + 1, current_accuracy))
    print('Test Accuracy: %.6f' % sess.run(accuracy, feed_dict={x: ds.test['image'], y_: ds.test['label']}))