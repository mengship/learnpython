from tensorflow.examples.tutorials.mnist import input_data
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

mnist = input_data.read_data_sets('../MNIST_data/', one_hot=True)
regularizer_ratio = 0.0


# CNN structure: 28*28*1 -> relu(conv(5,5,16)) -> max_pool(2,2) ->
#   relu(conv(5,5,32)) -> max_pool(2,2) -> flatten -> relu(fc(256)) -> softmax(fc(10))
def weight_variable(shape, name):
    if regularizer_ratio == 0.0:
        initial = tf.truncated_normal(shape, stddev=0.1)  # 后面这个代表正态分布
        weight = tf.get_variable(name, initializer=initial)
    else:
        regularizer = tf.contrib.layers.l2_regularizer(0.0)
        initial = tf.truncated_normal(shape, stddev=0.1)
        weight = tf.get_variable(name, initializer=initial, regularizer=regularizer)
    return weight


def bias_variable(shape, name):
    initial = tf.constant(0.1, shape=shape)
    return tf.Variable(initial, name=name)


def simple_conv2d(x, W):
    return tf.nn.conv2d(x, W, strides=[1, 1, 1, 1], padding='SAME')


def simple_pooling(x):
    return tf.nn.max_pool(x, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1],
                          padding='SAME')  # 第一个是batchsize 第二三个是长宽 第四个是channel数


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
    W_conv1 = weight_variable([5, 5, 1, 16], name='weight_conv1')  # core size, 输入前的channel数，filter个数
    b_conv1 = bias_variable([16], name='bias_conv1')
    W_conv2 = weight_variable([5, 5, 16, 32], name='weight_conv2')  # core size, 输入前的channel数，filter个数 每个core是16层的
    b_conv2 = bias_variable([32], name='bias_conv2')
    W_fc1 = weight_variable([7 * 7 * 32, 256], name='weight_fc1')
    b_fc1 = bias_variable([256], name='bias_fc1')
    W_fc2 = weight_variable([256, 10], name='weight_fc2')
    b_fc2 = bias_variable([10], name='bias_fc2')
    x_image = tf.reshape(image_batch, [-1, 28, 28, 1])
    h_conv1 = tf.nn.relu(simple_conv2d(x_image, W_conv1) + b_conv1)
    h_pool1 = simple_pooling(h_conv1)
    h_conv2 = tf.nn.relu(simple_conv2d(h_pool1, W_conv2) + b_conv2)
    h_pool2 = simple_pooling(h_conv2)
    h_pool2_flat = tf.reshape(h_pool2, [-1, 7 * 7 * 32])
    h_fc1 = tf.nn.relu(tf.matmul(h_pool2_flat, W_fc1) + b_fc1)
    _y = tf.nn.softmax(tf.matmul(h_fc1, W_fc2) + b_fc2)  # 这个位置不能加激活函数，会使负数消失
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
