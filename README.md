18-645 GPU Seamcarving
===

Git repository for CMU 18-645.

You can find the final report here: [final-report.pdf](http://abhandaru.github.io/gpu-seamcarving/final-report.pdf)


Updates on this branch
======================
After pulling this onto a machine running Ubuntu 16.04 wtih a CUDA enabled graphics card and CUDA drivers installed and working in a Deep Learning environment I found that:
a. the CPU version worked fine for the images provided but not for other images.
b. the GPU version did not work.

a. 
    i.For some reason the images in the original repo returned a negative height dimension but images saved with opencv or ffmpeg returned a positive dimension. Fixed for both cases.
    ii. The code was written with support for .bmp saved as bgra format. I included scripts to convert images to bgra. To run these scripts you need ffmpeg installed. A proper fix for this would be to link opencv and read images with it. But as with the original authors of this github, this goes beyond the scope of my current tests. 

b. To get CUDA version to work I had to install cppunit ( can be installed through pip or conda ).
the Make file  CFLAGS and LDFLAGS have to reflect that change. This version has my paths, which come from conda install commented out as well as the original paths. Adjust as necessary after cloning. CUDA version is worth the trouble if you are going to use this, it is a couple orders of magnitude faster.


Installation
============
1. Ensure NVIDIA graphics card has CUDA drivers installed. 
2. Install cppunit.
3. Change the CUDA makefile to reflect the note above.
make clean
make

Use
===
Change your images to bgra .bmp 
cd cuda or cd sequential
#bash 
run ./driver.out -n <int number of carved seams> -i <input bitmap> -o <output bitmap>

Caveat: CUDA version works only with images smaller than 1024 pixels wide.


Examples
========
The jupyter notebook included shows examples where seam carving works and where it does not. I added some that fail miserably to illustrate future work that could be done on this topic. 
Xk.



