(function () {

    const btnEliminacion = document.querySelectorAll(".btnEliminacion");

    btnEliminacion.forEach(btn => {
        btn.addEventListener('click', (e) => {
            const confirmacion = confirm('¿Seguro que decea eliminar la informacion de este paciente?');
            if (!confirmacion) {
                e.preventDefault();
            }
        });
    });
    
})();