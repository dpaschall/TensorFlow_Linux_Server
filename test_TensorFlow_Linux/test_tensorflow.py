# This script tests if TensorFlow is setup properly
# Be sure to use python version 3.5.x
# install tensor flow using pip3

# ONLY DISPLAY ERRORS NOT WARNINGS!
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
#

# the beginning of every tensorflow script:
import tensorflow as tf
#

# Hello World:
hello = tf.constant('Hello, TensorFlow!')
sess = tf.Session()
print(sess.run(hello))

#end of file