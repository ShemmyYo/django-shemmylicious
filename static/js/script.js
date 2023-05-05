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



// Underline Manu
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
