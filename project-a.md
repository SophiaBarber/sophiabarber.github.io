---
layout: page
title: Submarine Signal Processing
nav_exclude: true
permalink: /projects/project-a/
---

**Abstract:**

In this paper, we consider recorded acoustic pressure data obtained over a 24-hour
period at 30-minute intervals. We aim to locate the path of a moving submarine, which emits
an unknown acoustic frequency, over this time period. We detect the dominant frequency of the
submarine by averaging the Fourier transform over all time steps. We use this to construct a filter
to extract the center frequency in the Fourier domain, thereby cleaning the data. We then use the
location of highest acoustic pressure in the clean data at each time step to determine the location
of the submarine.

**Results:**

<figure style="margin-bottom: 2em;">
  <div style="display: flex; gap: 16px; align-items: center;">
    <img src="/assets/files/AMATH482_HW1_f3_(1).png" alt="test 1" style="width: 48%;">
    <img src="/assets/files/AMATH482_HW1_f2_(1).png" alt="test 2" style="width: 48%;">
  </div>
  <figcaption>
    3D trajectory of the submarine over time, extracted from the original, noisy data (left)
    vs from the filtered, clean data (right). We filtered the data by applying a gaussian filter
    to our data.
  </figcaption>
</figure>

<figure>
  <img src="/assets/files/AMATH482_HW1_f4.png" alt="test" style="width:70%;">
  <figcaption>
    3D trajectory of the submarine, showing the effect on the choice of the parameter &tau;
    in our gaussian filter. (C) was found to be the optimal &tau;.
  </figcaption>
</figure>


<figure>
  <img src="/assets/files/AMATH482_HW1_f5.png" alt="test">
  <figcaption>(x,y) Coordinates of the Submarine's path over time.</figcaption>
</figure>


**To view the full paper, code, and data, click [here](https://github.com/SophiaBarber/Submarine-tracking).**

Note: Data is not provided due to large size, and code is in a zip file. Data and project setup provided by Dr. Natalie Frank at the University of Washington as a part of the AMATH 482 Course.
