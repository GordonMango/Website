// Function to resize images to exact 1920x1080 dimensions
function resizeImages() {
    const images = document.querySelectorAll('.blogs-image img');
    
    images.forEach(img => {
        // Force exact dimensions
        img.style.width = '1920px';
        img.style.height = '1080px';
        img.style.objectFit = 'cover';
        img.style.objectPosition = 'center';
        img.style.borderRadius = '24px';
    });
}

// Run on page load
document.addEventListener('DOMContentLoaded', resizeImages);

// Run on window resize
window.addEventListener('resize', resizeImages); 