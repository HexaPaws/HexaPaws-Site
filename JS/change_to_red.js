const themeStylesheet = document.getElementById('theme-stylesheet');
const themeToggle = document.getElementById('theme-toggle');

const savedTheme = localStorage.getItem('theme');
if (savedTheme) {
    themeStylesheet.setAttribute('href', savedTheme);
    updateButtonText(savedTheme);
}

themeToggle.addEventListener('click', () => {
    const currentTheme = themeStylesheet.getAttribute('href');
    let newTheme = 'css.red_cybercat.css';

    if (currentTheme === 'css/cybercat.css') {
        newTheme = 'css/red_cybercat.css';
    }

    themeStylesheet.setAttribute('href', newTheme);

    localStorage.setItem('theme', newTheme);
    updateButtonTest(newTheme);
});

function updateButtonText(themeFile) {
    if (themeFile === 'css/cybercat_css') {
        themeToggle.textContent = 'Switch to Red Mode';
  } else {
        themeToggle.textContent = 'Switch to Cyan Mode';
  }
}