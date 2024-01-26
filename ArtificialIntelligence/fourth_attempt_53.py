from tensorflow.examples.tutorials.mnist import input_data
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from keras import layers
from keras import models

mnist = input_data.read_data_sets('../MNIST_data/', one_hot=True)
regularizer_ratio = 0.0



def lenet(image_batch):
    # x_image = tf.reshape(image_batch, [-1, 28, 28, 1])
    x_image = layers.Reshape(([28, 28, 1]))(image_batch)
    h_conv1 = layers.Conv2D(filters=6, kernel_size=5, padding='same', activation='relu', use_bias=True)(x_image)
    h_pool1 = layers.AveragePooling2D(pool_size=(2, 2),padding='same')(h_conv1)
    h_conv2 = layers.Conv2D(filters=16, kernel_size=5, padding='valid', activation='relu', use_bias=True)(h_pool1)
    h_pool2 = layers.AveragePooling2D(pool_size=(2, 2), padding='same')(h_conv2)

    h_pool2_flat = layers.Flatten()(h_pool2)
    h_fc1 = layers.Dense(120, activation='relu')(h_pool2_flat)
    h_fc2 = layers.Dense(84, activation='relu')(h_fc1)
    _y = layers.Dense(10, activation='softmax')(h_fc2)
    return _y


# x = tf.placeholder(tf.float32, [None, 784])# 必须是layer生成的，不是tf
x = layers.Input(shape=(784,))
# y_ = tf.placeholder(tf.float32, [None, 10])
y_ = layers.Input(shape=(10,))
y = lenet(x)
model = models.Model(x, y)# 必须是layer生成的，不是tf
print(model.summary())

correct_prediction = tf.equal(tf.argmax(y_, 1), tf.argmax(y, 1))  # 取出最大的值
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))  # 不希望出现整数
weight_loss = tf.add_n(tf.losses.get_regularization_losses()) if regularizer_ratio != 0.0 else 0.0
cross_entropy = weight_loss + tf.reduce_mean(
    tf.reduce_sum(-y_ * tf.log(y + 0.0000001), reduction_indices=[1]))  # 此处加一个非零小数的原因是，如果y=0，则结果为无穷小，则溢出，返回None
train_step = tf.train.AdamOptimizer(0.01).minimize(cross_entropy)

tf.summary.scalar('loss', cross_entropy)
tf.summary.scalar('accuracy', accuracy)
merged = tf.summary.merge_all()

training_iteration = 50000
batch_size = 64
display_step = 50
with tf.Session() as sess:
    writer = tf.summary.FileWriter('./cnn/', sess.graph)
    sess.run(tf.initialize_all_variables())
    for iteration in range(training_iteration):
        batch_xs, batch_ys = mnist.train.next_batch(batch_size)  # batch(batch_size)
        summary, _, current_accuracy = sess.run([merged, train_step, accuracy], feed_dict={x: batch_xs, y_: batch_ys})
        writer.add_summary(summary, iteration)
        if iteration % display_step == 0:
            print('Iteration: %5d | Accuracy: %.6f' % (iteration + 1, current_accuracy))
            print('Test Accuracy: %.6f' % sess.run(accuracy, feed_dict={x: mnist.train.images, y_: mnist.train.labels}))
    print('Test Accuracy: %.6f' % sess.run(accuracy, feed_dict={x: mnist.test.images, y_: mnist.test.labels}))
    writer.close()
