---
layout: page
title: Resume
permalink: /resume/
nav_order: 3
---

Here is my PDF document:

<!-- PDF.js Viewer Container -->
<div id="pdf-viewer" style="width: 100%; height: 600px; border: 1px solid #ccc; overflow: auto;"></div>

<!-- Fallback Download Link -->
<p>If the PDF does not display, you can <a href="{{ '/assets/files/my-document.pdf' | relative_url }}">download it here</a>.</p>

<!-- PDF.js Script -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/pdf.js/3.14.305/pdf.min.js"></script>
<script>
  const url = "{{ '/assets/files/my-document.pdf' | relative_url }}";

  // Configure PDF.js worker
  pdfjsLib.GlobalWorkerOptions.workerSrc = 'https://cdnjs.cloudflare.com/ajax/libs/pdf.js/3.14.305/pdf.worker.min.js';

  const loadingTask = pdfjsLib.getDocument(url);
  loadingTask.promise.then(pdf => {
    const container = document.getElementById('pdf-viewer');
    container.innerHTML = ''; // Clear container

    for (let pageNum = 1; pageNum <= pdf.numPages; pageNum++) {
      pdf.getPage(pageNum).then(page => {
        const viewport = page.getViewport({ scale: 1.2 });
        const canvas = document.createElement('canvas');
        const context = canvas.getContext('2d');
        canvas.height = viewport.height;
        canvas.width = viewport.width;

        container.appendChild(canvas);

        page.render({ canvasContext: context, viewport: viewport });
      });
    }
  }).catch(err => {
    console.error('Error loading PDF: ', err);
    const container = document.getElementById('pdf-viewer');
    container.innerHTML = '<p>Failed to load PDF. Please use the download link above.</p>';
  });
</script>
