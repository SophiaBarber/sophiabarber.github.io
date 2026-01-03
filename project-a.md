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

<figure>
  <img src="/assets/images/AMATH482_HW1_f2_(1).png" alt="Diagram showing system architecture">
  <figcaption>System architecture overview</figcaption>
</figure>

To view the full paper, code, and data, click [here](https://github.com/SophiaBarber/Submarine-tracking).
