// Load navbar from navbar.html
// Place this script near the end of your HTML, right before </body>

document.addEventListener('DOMContentLoaded', function() {
  // Find the navbar container
  const navbarContainer = document.getElementById('navbar-container');
  
  if (!navbarContainer) {
    console.warn('No #navbar-container found');
    return;
  }
  
  // Load banner CSS
  const bannerCSS = document.createElement('link');
  bannerCSS.rel = 'stylesheet';
  bannerCSS.href = 'css/banner.css';
  bannerCSS.type = 'text/css';
  document.head.appendChild(bannerCSS);
  
  // Fetch navbar.html
  fetch('navbar.html')
    .then(response => {
      if (!response.ok) throw new Error(`Failed to load navbar: ${response.status}`);
      return response.text();
    })
    .then(html => {
      navbarContainer.innerHTML = html;
      
      // Reinitialize Webflow scripts if needed
      if (window.Webflow) {
        window.Webflow.ready();
      }
    })
    .catch(error => {
      console.error('Error loading navbar:', error);
      navbarContainer.innerHTML = '<p style="color:red;">Failed to load navbar</p>';
    });
});
