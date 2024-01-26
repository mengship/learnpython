from tensorflow.examples.tutorials.mnist import input_data
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from keras import layers
# pip install keras
# pip install keras==2.2.5 --upgrade

def imshow(img, shape=[28, 28]):
    plt.imshow(np.reshape(img, shape))
    plt.show()

# def weight_variable(shape):
#     initial = tf.truncated_normal(shape, stddev=0.1) # 后面这个代表正态分布
#     return tf.Variable(initial)
#
# def bias_variable(shape):
#     initial = tf.constant(0.1, shape=shape)
#     return tf.Variable(initial)

mnist = input_data.read_data_sets('../MNIST_data/', one_hot=True)
one_image = mnist.train.images[0]
# imshow(one_image) # 不知道是3还是7
# 灰阶图像 channel = 1, 维度为 28*28

# W_conv = weight_variable([3, 3, 1, 32 ])# 输入的channel数目，输出的channel数目，就是卷积核的数目
# b_conv = bias_variable([32])

input_image = tf.convert_to_tensor(one_image)
image = tf.reshape(input_image, [-1, 28, 28, 1]) # -1 不对 batch size 进行约束,最后是channel是1
features = layers.Conv2D(filters=32, kernel_size=3, padding='same')(image) # 实际是有bias的
# features = tf.nn.conv2d(image, W_conv, strides=[1, 1, 1, 1], padding='SAME' ) + b_conv # 第一个是图像，第二个是 convolution 第三个是strides 第四个是padding
print(input_image)
print(features)

with tf.Session() as sess:
    sess.run(tf.initialize_all_variables())
    output_features = sess.run(features)[0]
    print(output_features.shape)

for _ in range(output_features.shape[2]):
    imshow(output_features[:, :, _])