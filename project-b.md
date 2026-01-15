---
layout: page
title: Robot Movement Classifier PCA
nav_exclude: true
permalink: /projects/project-b/
---

**Abstract:**

Here, we study a robot which records the movements of 38 of its joints. It performs 3 movements:
running, jumping, and walking. Our goal is to construct a classifier that takes a sample of movement and
identifies which movement was performed. We do this by using Principal Component Analysis (PCA) to
project our data onto a lower dimension, and classify each sample by assigning it to the class of movement
whose centroid is closest to its position, in low-dimensional space. We will adjust the dimensionality of the
problem and explore how many dimensions are necessary in our low-dimensional approximation.

**Results:**

<figure>
  <img src="/assets/files/AMATH482_HW2_fig2.png" alt="test">
  <figcaption>Cumulative Energy plot, showing the percent of energy that is retained when we approximate the training data with k PCA spatial modes. This is shown for k up to 10, and the minimum number of modes we need to retain various energy thresholds is indicated.</figcaption>
</figure>

<figure style="margin-bottom: 2em;">
  <div style="display: flex; gap: 16px; align-items: center;">
    <img src="/assets/files/AMATH482_HW2_fig3.png" alt="test 1" style="width: 48%;">
    <img src="/assets/files/AMATH482_HW2_fig4_new.png" alt="test 2" style="width: 48%;">
  </div>
  <figcaption>
    Plots of training data projected into truncated PCA space with 2 PCA modes (left) and with 3 PCA modes (right), both including the centroids (means). This allows us to see that our data is well separated by movement type.
  </figcaption>
</figure>

<figure>
  <img src="/assets/files/AMATH482_HW2_fig8.png" alt="test">
  <figcaption>Plots of accuracy in classification vs k. (A) shows accuracy in classification of train data, (B) shows accuracy in classification of test data, and (C) again shows accuracy in classification of test data, but where we did not scale our data before classifying.</figcaption>
</figure>

<figure>
  <img src="/assets/files/AMATH482_HW2_fig9.png" alt="test">
  <figcaption>Plots of accuracy in classification via logistic regression method vs k. (A) shows accuracy in classification of train data; (B) shows accuracy in classification of test data.</figcaption>
</figure>

**To view the full paper, code, and data, click [here](https://github.com/SophiaBarber/Robot-Movement-Classifier-PCA).**


Note: Data and project setup provided by Dr. Natalie Frank at the University of Washington as a part of the AMATH 482 Course.
