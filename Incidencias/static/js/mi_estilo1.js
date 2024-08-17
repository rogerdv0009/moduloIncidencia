window.addEventListener('load', function(){
    let titulo = document.getElementById('idtitulop');
    let carrusel = document.getElementsByClassName('pintado');
    let completoListar = document.getElementsByClassName('completo-listar');
    let antesl = document.getElementsByClassName('antesl');
    let formulario = document.getElementsByClassName('formulario');
    let fotop = document.getElementsByClassName('foto-principal');
    
    for (let i = 0; i < fotop.length; i++) {
        fotop[i].classList.add('foto-principal2');        
    }
    for (let i = 0; i < formulario.length; i++) {
        formulario[i].classList.add('formulario2');        
    }
    for (let i = 0; i < antesl.length; i++) {
        antesl[i].classList.add('antesl2');        
    }
    for (let i = 0; i < completoListar.length; i++) {
        completoListar[i].classList.add('completo-listar2');        
    }    
    for (let i = 0; i < carrusel.length; i++) {
        carrusel[i].classList.add('pintado-visto');      
    }
    titulo.classList.add('acomodar');
});
$(function(){
    $("procesarR").on("click", function(){
        $("modalR").modal('show');
    });
});



