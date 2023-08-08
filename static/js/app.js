import translations from "./translations.js";

gsap.registerPlugin(ScrollTrigger);

if (ScrollTrigger.isTouch !== 2) {
  // ScrollSmoother.create({
  //   wrapper: ".wrapper",
  //   content: ".content",
  //   smooth: 1.5,
  //   effects: true,
  // });

  gsap.fromTo(
    ".hero-section",
    { opacity: 1 },
    {
      opacity: 0,
      scrollTrigger: {
        trigger: ".hero-section",
        start: "center",
        end: "820",
        scrub: true,
      },
    }
  );

  let itemsL = gsap.utils.toArray(".gallery__left .gallery__item");

  itemsL.forEach((item) => {
    gsap.fromTo(
      item,
      { opacity: 0, x: -50 },
      {
        opacity: 1,
        x: 0,
        scrollTrigger: {
          trigger: item,
          start: "-900",
          end: "-200",
          scrub: true,
        },
      }
    );
  });

  gsap.fromTo(
    ".gallery__item.height",
    { opacity: 0, y: -50 },
    {
      opacity: 1,
      y: 0,
      scrollTrigger: {
        trigger: ".gallery__item.height",
        start: "-850",
        end: "-100",
        scrub: true,
      },
    }
  );

  let itemsR = gsap.utils.toArray(".gallery__right .gallery__item");

  itemsR.forEach((item) => {
    gsap.fromTo(
      item,
      { opacity: 0, x: 50 },
      {
        opacity: 1,
        x: 0,
        scrollTrigger: {
          trigger: item,
          start: "-750",
          end: "top",
          scrub: true,
        },
      }
    );
  });
}
// Scroll NavBar
const navBar = document.querySelector(".navbar");
window.addEventListener("scroll", () => {
  if (window.scrollY > 200) {
    navBar.classList.add("blur");
  } else {
    navBar.classList.remove("blur");
  }
});

let bars = document.querySelector(".bars");
let linksMenu = document.querySelector(".links");
bars.addEventListener("click", () => {
  linksMenu.classList.toggle("active");
});
// Dark Light Toggler
const modeToggler = document.querySelector(".mode");
const bodyEl = document.body;
modeToggler.addEventListener("click", () => {
  toggleClasses(bodyEl);
});
window.addEventListener("load", () => {
  const mode = localStorage.getItem("mode") || "dark";
  if (mode === "light") {
    bodyEl.classList.remove("dark");
    bodyEl.classList.add("light");
    modeToggler.innerHTML = ` <i class="fa-regular fa-moon"></i>`;
  } else {
    bodyEl.classList.remove("light");
    bodyEl.classList.add("dark");
    modeToggler.innerHTML = `<i class="fa-regular fa-lightbulb"></i>`;
  }
});
const toggleClasses = (bodyEl) => {
  if (bodyEl.classList.contains("dark")) {
    bodyEl.classList.remove("dark");
    bodyEl.classList.add("light");
    modeToggler.innerHTML = ` <i class="fa-regular fa-moon"></i>`;
    localStorage.setItem("mode", "light");
  } else {
    bodyEl.classList.remove("light");
    bodyEl.classList.add("dark");
    modeToggler.innerHTML = ` <i class="fa-regular fa-lightbulb"></i>`;
    localStorage.setItem("mode", "dark");
  }
};
//Language
const setLanguage = (language) => {
  const elements = document.querySelectorAll("[data-i18n]");
  elements.forEach((element) => {
    const translationKey = element.getAttribute("data-i18n");
    element.textContent = translations[language][translationKey];
  });
  document.dir = language === "ar" ? "rtl" : "ltr";
};
const langBtns = document.querySelectorAll(".language");
langBtns.forEach((btn) => {
  btn.addEventListener("click", toggleLang);
});
function toggleLang() {
  const lang = document.documentElement.getAttribute("lang");
  if (lang === "en") {
    document.documentElement.setAttribute("lang", "ar");
    localStorage.setItem("lang", "ar");
    setLanguage("ar");
  } else {
    document.documentElement.setAttribute("lang", "en");
    localStorage.setItem("lang", "en");
    setLanguage("en");
  }
}
window.addEventListener("load", () => {
  const lang = localStorage.getItem("lang") || "en";
  if (lang === "en") {
    document.documentElement.setAttribute("lang", "en");
    localStorage.setItem("lang", "en");
    setLanguage("en");
  } else {
    document.documentElement.setAttribute("lang", "ar");
    localStorage.setItem("lang", "ar");
    setLanguage("ar");
  }
});
let links = document.querySelectorAll(".links li a");
links.forEach((link) => {
  link.classList.remove("active");
  if (window.location.pathname === "/") {
    if (link.dataset.i18n === "home") {
      console.log("object");
      link.classList.add("active");
    }
  } else if (window.location.pathname === "/architecture/") {
    if (link.dataset.i18n === "arch") {
      console.log("arch");
      link.classList.add("active");
    }
  } else if (window.location.pathname === "/advertising/") {
    if (link.dataset.i18n === "adver") {
      console.log("adver");
      link.classList.add("active");
    }
  } else if (window.location.pathname === "/blog") {
    if (link.dataset.i18n === "blog") {
      console.log("blog");
      link.classList.add("active");
    }
  }
});
