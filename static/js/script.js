gsap.registerPlugin(Flip);

const links = document.querySelectorAll(".nav-item a");
const activeNav = document.querySelector(".active-nav");


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