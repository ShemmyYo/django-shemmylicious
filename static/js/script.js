gsap.registerPlugin(Flip);

const links = document.querySelectorAll(".nav-item a");
const activeNav = document.querySelector(".active-nav");
const myCarouselElement = document.querySelector('#carouselExampleInterval');
const sectionBlank = document.querySelector('.section-blank');
const indexHero = document.querySelector('.hero');
const indexSlider = document.querySelector('.index-slider');
const indexHeadline = document.querySelector('.headline');
const indexHeadlineBttn = document.querySelectorAll('.headline-bttn');
const navbar = document.querySelector('.navbar');
const footer = document.querySelector('.footer');
const innerText = document.querySelector('.inner-text');

// Index automations
const tl = new TimelineMax();

tl.fromTo(sectionBlank, 0.0001, { height: "100%" }, { height:"0%" })
.fromTo(indexHero, 2.0, { height: "0%" }, { height:"80%", ease: Power2.easeInOut })
.fromTo(indexHeadline, 1.0, { opacity: 0, x: 60 }, { opacity: 1, x: 0 }, "-=1.0")
.fromTo(indexHero,1.5, { width: "100%" }, { width:"80%", ease: Power2.easeInOut })
.fromTo(indexSlider, 1.2, { x: "-100%" }, { x:"100%", ease: Power2.easeInOut }, "-=1.5")
.fromTo(indexSlider, 0.0001, { width: "100%" }, { width:"0%" }, "-=0.5")
.fromTo(indexHeadlineBttn, 1.0, { opacity: 0, x: 120 }, { opacity: 1, x: 0 })
.fromTo(navbar, 3.5, { opacity: 0, y: -60 }, { opacity: 1, y: 0 })
.fromTo(footer, 2.5, { opacity: 0, y: 60 }, { opacity: 1, y: 0 }, "-=2.5")
.fromTo(myCarouselElement, 1.5, { opacity: 0, y: 60 }, { opacity: 1, y: 0 }, "-=2.5")
.fromTo(innerText, 1.5, { opacity: 0, x: -60 }, { opacity: 1, x: 0 }, "-=2.0")

// Underline Manu
import carousel from 'bootstrap/js/dist/carousel'
const carousel = new bootstrap.Carousel(myCarouselElement, {});

links.forEach(link => {
    link.addEventListener('mouseover', () => {
        // move underline
        const state = Flip.getState(activeNav);
        link.appendChild(activeNav);
        Flip.from(state, {
            duration: 1.4,
            absolue: true,
            ease: 'elastic.out(1, 0.5)'
        })
    });
})
// Credits: https://www.youtube.com/watch?v=xB27AuRa5h4
