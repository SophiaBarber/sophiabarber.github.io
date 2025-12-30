---
layout: page
title: Resume
permalink: /resume/
nav_order: 3
---

# Responsive PDF Viewer Example

Here is the PDF embedded on this page:

<!-- PDF.js Viewer Container -->
<div id="pdf-viewer" style="width:100%; height:80vh; border:1px solid #ccc; overflow:auto;"></div>

<!-- Fallback download link -->
<p>If the PDF does not display, <a href="https://sophiabarber.github.io/assets/files/resume.pdf">download it here</a>.</p>

<!-- PDF.js scripts -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/pdf.js/3.14.305/pdf.min.js"></script>
<script>
  const url = "https://sophiabarber.github.io/assets/files/resume.pdf"; // Replace with your PDF URL

  pdfjsLib.GlobalWorkerOptions.workerSrc = 'https://cdnjs.cloudflare.com/ajax/libs/pdf.js/3.14.305/pdf.worker.min.js';

  let pdfDoc = null;

  const container = document.getElementById('pdf-viewer');

  // Function to render PDF pages
  function renderPDF() {
    if (!pdfDoc) return;
    container.innerHTML = '';
    const containerWidth = container.clientWidth;

    for (let pageNum = 1; pageNum <= pdfDoc.numPages; pageNum++) {
      pdfDoc.getPage(pageNum).then(page => {
        const viewport = page.getViewport({ scale: 1 });
        const scale = containerWidth / viewport.width;
        const scaledViewport = page.getViewport({ scale });

        const canvas = document.createElement('canvas');
        canvas.width = scaledViewport.width;
        canvas.height = scaledViewport.height;
        const context = canvas.getContext('2d');

        container.appendChild(canvas);
        page.render({ canvasContext: context, viewport: scaledViewport });
      });
    }
  }

  // Load the PDF
  pdfjsLib.getDocument(url).promise.then(pdf => {
    pdfDoc = pdf;
    renderPDF();
  }).catch(err => {
    console.error('PDF loading error:', err);
    container.innerHTML = 'Failed to load PDF. Please use the download link above.';
  });

  // Re-render on window resize
  window.addEventListener('resize', () => {
    renderPDF();
  });
</script>
