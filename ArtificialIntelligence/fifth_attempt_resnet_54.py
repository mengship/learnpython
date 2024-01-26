from functools import partial

from tensorflow.examples.tutorials.mnist import input_data
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from keras import layers
from keras import models

mnist = input_data.read_data_sets('../MNIST_data/', one_hot=True)
regularizer_ratio = 0.0


def _after_conv(in_tensor):  # 标准归一化 + 激活函数
    norm = layers.BatchNormalization()(in_tensor)
    return layers.Activation('relu')(norm)


def conv3(in_tensor, filters):
    conv = layers.Conv2D(filters, kernel_size=3, strides=1, padding='same')(in_tensor)
    return _after_conv(conv)


def conv3_downsample(in_tensor, filters):
    conv = layers.Conv2D(filters, kernel_size=3, strides=2, padding='same')(in_tensor)
    return _after_conv(conv)


def conv1(in_tensor, filters):
    conv = layers.Conv2D(filters, kernel_size=1, strides=1, padding='same')(in_tensor)
    return _after_conv(conv)


def conv1_downsample(in_tensor, filters):
    conv = layers.Conv2D(filters, kernel_size=1, strides=2, padding='same')(in_tensor)
    return _after_conv(conv)


def resnet_block(in_tensor, filters, downsample=False):
    if downsample:
        conv1_rb = conv3_downsample(in_tensor, filters)
    else:
        conv1_rb = conv3(in_tensor, filters)
    conv2_rb = conv3(conv1_rb, filters)

    if downsample:
        in_tensor = conv1_downsample(in_tensor, filters)
    result = layers.Add()([conv2_rb, in_tensor])

    return layers.Activation('relu')(result)


def block(in_tensor, filters, n_block, downsample=False):
    res = in_tensor
    for i in range(n_block):
        if i == 0:
            res = resnet_block(res, filters, downsample)
        else:
            res = resnet_block(res, filters, False)
    return res


def resnet(image_batch):
    conv = layers.Conv2D(64, 7, strides=2, padding='same')(image_batch)
    conv = _after_conv(conv)
    pool1 = layers.MaxPool2D(3, 2, padding='same')(conv)
    conv1_block = block(pool1, 64, 3, False)
    conv2_block = block(conv1_block, 128, 4, True)
    conv3_block = block(conv2_block, 256, 6, True)
    conv4_block = block(conv3_block, 512, 3, True)
    pool2 = layers.GlobalAvgPool2D()(conv4_block)
    _y = layers.Dense(1000, activation='softmax')(pool2)
    return _y


# x = tf.placeholder(tf.float32, [None, 784])# 必须是layer生成的，不是tf
x = layers.Input(shape=(224, 224, 3))
# y_ = tf.placeholder(tf.float32, [None, 10])
y_ = layers.Input(shape=(1000,))
y = resnet(x)
model = models.Model(x, y)  # 必须是layer生成的，不是tf
print(model.summary())
#
# correct_prediction = tf.equal(tf.argmax(y_, 1), tf.argmax(y, 1))  # 取出最大的值
# accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))  # 不希望出现整数
# weight_loss = tf.add_n(tf.losses.get_regularization_losses()) if regularizer_ratio != 0.0 else 0.0
# cross_entropy = weight_loss + tf.reduce_mean(
#     tf.reduce_sum(-y_ * tf.log(y + 0.0000001), reduction_indices=[1]))  # 此处加一个非零小数的原因是，如果y=0，则结果为无穷小，则溢出，返回None
# train_step = tf.train.AdamOptimizer(0.01).minimize(cross_entropy)
#
# tf.summary.scalar('loss', cross_entropy)
# tf.summary.scalar('accuracy', accuracy)
# merged = tf.summary.merge_all()
#
# training_iteration = 50000
# batch_size = 64
# display_step = 50
# with tf.Session() as sess:
#     writer = tf.summary.FileWriter('./cnn/', sess.graph)
#     sess.run(tf.initialize_all_variables())
#     for iteration in range(training_iteration):
#         batch_xs, batch_ys = mnist.train.next_batch(batch_size)  # batch(batch_size)
#         summary, _, current_accuracy = sess.run([merged, train_step, accuracy], feed_dict={x: batch_xs, y_: batch_ys})
#         writer.add_summary(summary, iteration)
#         if iteration % display_step == 0:
#             print('Iteration: %5d | Accuracy: %.6f' % (iteration + 1, current_accuracy))
#             print('Test Accuracy: %.6f' % sess.run(accuracy, feed_dict={x: mnist.train.images, y_: mnist.train.labels}))
#     print('Test Accuracy: %.6f' % sess.run(accuracy, feed_dict={x: mnist.test.images, y_: mnist.test.labels}))
#     writer.close()
