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
