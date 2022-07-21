// codigo JS para eventos

var parrafo= document.querySelector("#id1"); //cuando creo y selecciono una etiqueta propia debo usar #
var titulo= document.querySelector("#id2");

//AGREGAR EVENTOS A ELEMENTOS
parrafo.addEventListener('mouseover',function()){
  parrafo.style.color='green';
  parrafo.style.border='solid 2px pink';
}
