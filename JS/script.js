function revealOnScroll() {
  const reveals = document.querySelectorAll(".reveal");
  reveals.forEach(el => {
    const top = el.getBoundingClientRect().top;
    if (top < window.innerHeight - 50) {
      el.classList.add("active");
    }
 });
)

window.addEventListener("scroll", revealOnScroll);
window.addEventListener("load", revealOnScroll);

setTimeout(() => {
  bootScreen.style.display = "none";
  mainContent.style.display = "block";
  localStorage.setItem("booted", "true");
  revealOnScroll();
}, 800);

bootScreen.style.opacity = "0";
setTimeOut(() => {
  bootScreen.style.display = "none";
  mainContent.style.display = "block";
}, 500);