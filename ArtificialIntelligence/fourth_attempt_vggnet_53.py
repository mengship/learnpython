from functools import partial

from tensorflow.examples.tutorials.mnist import input_data
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from keras import layers
from keras import models

mnist = input_data.read_data_sets('../MNIST_data/', one_hot=True)
regularizer_ratio = 0.0

simple_conv2d = partial(layers.Conv2D,
                        kernel_size=3,
                        strides=1,
                        padding='same',
                        activation='relu')
simple_maxpool = layers.MaxPooling2D()

def block(in_tensor, filters, n_conv):
    conv_block = in_tensor
    for _ in range(n_conv):
        conv_block = simple_conv2d(filters=filters)(conv_block)
    return simple_maxpool(conv_block)

def vggnet(image_batch):
    block1 = block(image_batch, 64, 2)
    block2 = block(block1, 128, 2)
    block3 = block(block2, 256, 3)
    block4 = block(block3, 512, 3)
    block5 = block(block4, 512, 3)
    flat = layers.Flatten()(block5)
    h_fc1 = layers.Dense(4096, activation='relu')(flat)
    h_fc2 = layers.Dense(4096, activation='relu')(h_fc1)
    _y = layers.Dense(1000, activation='softmax')(h_fc2)
    return _y

# x = tf.placeholder(tf.float32, [None, 784])# 必须是layer生成的，不是tf
x = layers.Input(shape=(224, 224, 3))
# y_ = tf.placeholder(tf.float32, [None, 10])
y_ = layers.Input(shape=(1000,))
y = vggnet(x)
model = models.Model(x, y)# 必须是layer生成的，不是tf
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
