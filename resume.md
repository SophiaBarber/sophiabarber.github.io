---
layout: page
title: Resume
permalink: /resume/
nav_order: 3
---

# My Resume

Here is the PDF document embedded on this page:

<!-- PDF.js Viewer Container -->
<div id="pdf-viewer" style="width:100%; height:80vh; border:1px solid #ccc; overflow:auto;"></div>

<!-- Fallback download link -->
<p>If the PDF does not display, <a href="https://sophiabarber.github.io.github.io/assets/files/resume.pdf">download it here</a>.</p>

<!-- PDF.js scripts -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/pdf.js/3.14.305/pdf.min.js"></script>
<script>
  const url = "https://sophiabarber.github.io.github.io/assets/files/resume.pdf"; // Replace with your PDF URL

  // PDF.js worker
  pdfjsLib.GlobalWorkerOptions.workerSrc = 'https://cdnjs.cloudflare.com/ajax/libs/pdf.js/3.14.305/pdf.worker.min.js';

  // Load PDF
  pdfjsLib.getDocument(url).promise.then(pdf => {
    const container = document.getElementById('pdf-viewer');
    container.innerHTML = '';

    for (let pageNum = 1; pageNum <= pdf.numPages; pageNum++) {
      pdf.getPage(pageNum).then(page => {
        const viewport = page.getViewport({ scale: 1 }); // initial scale
        const canvas = document.createElement('canvas');
        const context = canvas.getContext('2d');

        // Set canvas width to container width
        const containerWidth = container.clientWidth;
        const scale = containerWidth / viewport.width; // scale to fit width
        const scaledViewport = page.getViewport({ scale });

        canvas.width = scaledViewport.width;
        canvas.height = scaledViewport.height;

        container.appendChild(canvas);
        page.render({ canvasContext: context, viewport: scaledViewport });
      });
    }
  }).catch(err => {
    console.error('PDF loading error:', err);
    document.getElementById('pdf-viewer').innerHTML = 'Failed to load PDF. Please use the download link above.';
  });
</script>
