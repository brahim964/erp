// scripts.js

document.addEventListener('DOMContentLoaded', function() {
    // Mostrar un mensaje de bienvenida en la consola
    console.log("Bienvenido a la Gestoría de Automóviles!");

    // Resaltar el enlace activo en el menú
    const menuLinks = document.querySelectorAll('.header .menu a');
    const currentPath = window.location.pathname;

    menuLinks.forEach(link => {
        // Obtener la ruta del enlace
        const linkPath = new URL(link.href).pathname;

        // Comparar la ruta del enlace con la ruta actual
        if (linkPath === currentPath) {
            link.classList.add('active'); // Añadir una clase para el enlace activo
        }
    });
});
