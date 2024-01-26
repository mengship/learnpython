from tensorflow.examples.tutorials.mnist import input_data
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from keras import layers

mnist = input_data.read_data_sets('../MNIST_data/', one_hot=True)
regularizer_ratio = 0.0


# CNN structure: 28*28*1 -> relu(conv(5,5,16)) -> max_pool(2,2) ->
#   relu(conv(5,5,32)) -> max_pool(2,2) -> flatten -> relu(fc(256)) -> softmax(fc(10))


# def fcnn(image_batch):
#     W_fc1 = weight_variable([784, 200])
#     b_fc1 = bias_variable([200])
#     W_fc2 = weight_variable([200, 200])
#     b_fc2 = bias_variable([200])
#     W_out = weight_variable([200, 10])
#     b_out = bias_variable([10])
#     hidden_1 = tf.nn.sigmoid(tf.matmul(image_batch, W_fc1) + b_fc1) # image_batch 是 B*784 hidden_1 是B*200
#     hidden_2 = tf.nn.sigmoid(tf.matmul(hidden_1, W_fc2) + b_fc2) # hidden_2 B*200
#     _y = tf.nn.softmax(tf.matmul(hidden_2, W_out) + b_out) # 这是不是激活函数，是一个概率
#     return _y

def cnn(image_batch):
    x_image = tf.reshape(image_batch, [-1, 28, 28, 1])
    # h_conv1 = tf.nn.relu(simple_conv2d(x_image, W_conv1) + b_conv1)
    h_conv1 = layers.Conv2D(filters=16, kernel_size=5, padding='same', activation='relu', use_bias=True)(x_image)
    h_pool1 = layers.MaxPooling2D(pool_size=(2, 2),padding='same')(h_conv1)
    h_conv2 = layers.Conv2D(filters=32, kernel_size=5, padding='same', activation='relu', use_bias=True)(h_pool1)
    h_pool2 = layers.MaxPooling2D(pool_size=(2, 2), padding='same')(h_conv2)

    # h_pool2 = simple_pooling(h_conv2)
    # h_pool2_flat = tf.reshape(h_pool2, [-1, 7 * 7 * 32])
    h_pool2_flat = layers.Flatten()(h_pool2)
    h_fc1 = layers.Dense(256, activation='relu')(h_pool2_flat)
    _y = layers.Dense(10, activation='softmax')(h_fc1)
    # _y = tf.nn.softmax(tf.matmul(h_fc1, W_fc2) + b_fc2)  # 这个位置不能加激活函数，会使负数消失
    return _y


x = tf.placeholder(tf.float32, [None, 784])
y_ = tf.placeholder(tf.float32, [None, 10])
y = cnn(x)

correct_prediction = tf.equal(tf.argmax(y_, 1), tf.argmax(y, 1))  # 取出最大的值
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))  # 不希望出现整数
weight_loss = tf.add_n(tf.losses.get_regularization_losses()) if regularizer_ratio != 0.0 else 0.0
cross_entropy = weight_loss + tf.reduce_mean(
    tf.reduce_sum(-y_ * tf.log(y + 0.0000001), reduction_indices=[1]))  # 此处加一个非零小数的原因是，如果y=0，则结果为无穷小，则溢出，返回None
# train_step = tf.train.GradientDescentOptimizer(0.01).minimize(cross_entropy)
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
