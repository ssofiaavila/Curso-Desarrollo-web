var num1;
var num2;
var operacion;
var resultado=null;;
var texto= null;

function lectura(){
  var dato1= prompt("Primer número: ");
  var dato2= prompt("Segundo número: ");
  operacion= prompt("Operación a realizar: ");
  num1= parseInt(dato1);
  num2= parseInt(dato2);
}
function calculo(){
  if (operacion =="+"){
    resultado= num1+num2;
    texto= "La suma es "+ resultado;
  }
  if (operacion == "-"){
    resultado= num1-num2;
    texto= "La resta es "+ resultado;
  }
  if (operacion == "/"){
    resultado= num1/num2;
    texto= "La división es "+ resultado;
  }
  if (operacion == "*"){
    resultado= num1*num2;
    texto= "La multiplicación es "+ resultado;
  }
}

lectura();
calculo();
alert(texto);
console.log(texto);
