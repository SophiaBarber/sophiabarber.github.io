---
layout: page
title: PCA Digit Classifiers
nav_exclude: true
permalink: /projects/project-c/
---

**Abstract:**

In this paper we will classify images of digits. We perform PCA on both the train and test data
with k such that the low-dimensional reconstruction of the data from k-PC modes will retain 85% of the
energy. Then we project the data into k-modes PCA space and use Ridge, KNN, and SVM classifiers to
classify each image by digit, using cross-validation to tune hyper-parameters. We also restrict our data to
only images of certain digits and apply the same process. We then evaluate the accuracy of each classifier
on both the train and test data.

**Results:**

<figure>
  <img src="/assets/files/AMATH482_HW3_m3.png" alt="test">
  <figcaption>Test caption</figcaption>
</figure>


**To view the full paper, code, and data, click [here](https://github.com/SophiaBarber/PCA-Digit-Classifiers).**
