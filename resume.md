---
layout: page
title: Resume
permalink: /resume/
nav_order: 3
---

Here is my PDF document:

<div id="pdf-viewer" style="width:100%; height:600px; border:1px solid #ccc; overflow:auto;"></div>

<script src="https://cdnjs.cloudflare.com/ajax/libs/pdf.js/3.14.305/pdf.min.js"></script>
<script>
  const url = "https://<username>.github.io/<repo>/assets/files/Sophia Barber Resume v12.pdf"; // use your actual URL

  pdfjsLib.GlobalWorkerOptions.workerSrc = 'https://cdnjs.cloudflare.com/ajax/libs/pdf.js/3.14.305/pdf.worker.min.js';

  pdfjsLib.getDocument(url).promise.then(pdf => {
    const container = document.getElementById('pdf-viewer');
    container.innerHTML = '';
    for (let pageNum = 1; pageNum <= pdf.numPages; pageNum++) {
      pdf.getPage(pageNum).then(page => {
        const viewport = page.getViewport({ scale: 1.2 });
        const canvas = document.createElement('canvas');
        canvas.height = viewport.height;
        canvas.width = viewport.width;
        const context = canvas.getContext('2d');
        container.appendChild(canvas);
        page.render({ canvasContext: context, viewport: viewport });
      });
    }
  }).catch(err => {
    console.error('PDF loading error:', err);
    document.getElementById('pdf-viewer').innerHTML = 'Failed to load PDF. Please use the download link.';
  });
</script>
