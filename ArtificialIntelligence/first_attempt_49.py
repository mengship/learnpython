from tensorflow.examples.tutorials.mnist import input_data
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

mnist = input_data.read_data_sets('../MNIST_data/', one_hot=True)

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
    hidden_1 = tf.nn.sigmoid(tf.matmul(image_batch, W_fc1) + b_fc1) # image_batch 是 B*784 hidden_1 是B*200
    hidden_2 = tf.nn.sigmoid(tf.matmul(hidden_1, W_fc2) + b_fc2) # hidden_2 B*200
    _y = tf.nn.softmax(tf.matmul(hidden_2, W_out) + b_out) # 这是不是激活函数，是一个概率
    return _y

x = tf.placeholder(tf.float32, [None, 784])
y_ = tf.placeholder(tf.float32, [None, 10])
y = fcnn(x)

correct_prediction = tf.equal(tf.argmax(y_, 1), tf.argmax(y, 1))  # 取出最大的值
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32)) # 不希望出现整数

cross_entropy = tf.reduce_mean(tf.reduce_sum(-y_ * tf.log(y+0.0000001), reduction_indices=[1] )) # 此处加一个非零小数的原因是，如果y=0，则结果为无穷小，则溢出，返回None
train_step = tf.train.GradientDescentOptimizer(0.01).minimize(cross_entropy)

training_iteration = 50000
batch_size = 64
display_step = 50
with tf.Session() as sess:
    sess.run(tf.initialize_all_variables())
    for iteration in range(training_iteration):
        batch_xs, batch_ys = mnist.train.next_batch(batch_size)# batch(batch_size)
        _, current_accuracy = sess.run([train_step, accuracy] , feed_dict = {x: batch_xs, y_: batch_ys})
        if iteration % display_step == 0:
            print('Iteration: %5d | Accuracy: %.6f' % (iteration + 1, current_accuracy))
    print('Test Accuracy: %.6f' % sess.run(accuracy, feed_dict={x: mnist.test.images, y_: mnist.test.labels}))
