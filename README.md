# TensorFlow_Linux_Server
# A repo specifically containing all the code to build TensorFlow from source or with a docker.
# will have GPU support.

Documentation folder contains the links to get setup and the requirements.

test_TensorFlow_Linux folder has some good example files to run to confirm tensorFlow works

bin folder will contain the actual setup files needed for the linux pc to run tensorFlow optimally
the setup_all.py script will do the setup/build process automatically, and test using the Mandelbrot set.

############################################################################################################
########################################### TO-DO ##########################################################
############################################################################################################

Danny >           Start a fresh linux machine with remote access to terminal.
				  Specialized for running Python, CUDA drivers, and Bazel. (Almost any linux distro)
				  [Save install and setup commands in a script setup_all.any_ext in bin folder]
				  
Daniel/All >      Get tensorFlow installed using a dock or building from source.
				  Try docker first and confirm performance enchancements are in place.
				  https://www.tensorflow.org/performance/performance_guide

Critter/Daniel >  Add CUDA and GPU support

Daniel >          Get TensorBoard working and both the Mandelbrot & Cifar10 examples.

############################################################################################################
############################################################################################################
############################################################################################################

============================================================================================================
GPU INFORMATION FOR TENSORFLOW:
https://www.tensorflow.org/install/install_linux#nvidia_requirements_to_run_tensorflow_with_gpu_support

NVIDIA requirements to run TensorFlow with GPU support

If you are installing TensorFlow with GPU support using one of the mechanisms described in this guide, then the following NVIDIA software must be installed on your system:

CUDA® Toolkit 8.0. For details, see NVIDIA's documentation. Ensure that you append the relevant Cuda pathnames to the LD_LIBRARY_PATH environment variable as described in the NVIDIA documentation.
The NVIDIA drivers associated with CUDA Toolkit 8.0.
cuDNN v5.1. For details, see NVIDIA's documentation. Ensure that you create the CUDA_HOME environment variable as described in the NVIDIA documentation.
GPU card with CUDA Compute Capability 3.0 or higher. See NVIDIA documentation for a list of supported GPU cards.
The libcupti-dev library, which is the NVIDIA CUDA Profile Tools Interface. This library provides advanced profiling support. To install this library, issue the following command:

$ sudo apt-get install libcupti-dev
If you have an earlier version of the preceding packages, please upgrade to the specified versions. If upgrading is not possible, then you may still run TensorFlow with GPU support, but only if you do the following:

Install TensorFlow from sources as documented in Installing TensorFlow from Sources).
Install or upgrade to at least the following NVIDIA versions:
CUDA toolkit 7.0 or greater
cuDNN v3 or greater
GPU card with CUDA Compute Capability 3.0 or higher.
============================================================================================================

Collaborators: Daniel Paschall, Christopher Stanquist, and John Stinchcomb 