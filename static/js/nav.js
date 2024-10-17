
    document.addEventListener('DOMContentLoaded', function() {
        const dropdowns = document.querySelectorAll('.dropdown');
        
        dropdowns.forEach(dropdown => {
            dropdown.querySelector('.dropbtn').addEventListener('click', function() {
                dropdown.classList.toggle('show');
            });
        });
    
        // Cerrar el menú desplegable si el usuario hace clic fuera de él
        window.onclick = function(event) {
            if (!event.target.matches('.dropbtn')) {
                dropdowns.forEach(dropdown => {
                    if (dropdown.classList.contains('show')) {
                        dropdown.classList.remove('show');
                    }
                });
            }
        };
    });

    function toggleMenu() {
        var nav = document.querySelector('.nav');
        nav.classList.toggle('show');
    }