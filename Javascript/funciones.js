var mensaje1= " cómo estás" // VARIABLE GLOBAL


function wellcome(nombre){
  var frase= "Hola " + nombre + " buen día";
  console.log(frase);
}

function globales(nombre){
  var frase= "Hola " + nombre + " buen día" + mensaje1;
  return frase;
}

wellcome("Sofia"); //puedo pasar más parámetros, igual que java
var frase1= globales("Sofia");
console.log(frase1);
