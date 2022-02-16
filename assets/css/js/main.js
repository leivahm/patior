const app = document.getElementById('typewriter');

const typewriter = new Typewriter(app, {
    loop: true,
    delay: 150
});

typewriter
//.typeString('Cartuchos Compatibles con...')
.typeString('Patior... ')
.pauseFor(3000)
.typeString('  Somos Compatibles')
.pauseFor(7000)
.start();