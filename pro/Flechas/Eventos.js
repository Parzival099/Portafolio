var teclas = {
  UP: 38,
  DOWN: 40,
  LEFT: 37,
  RIGHT: 39
};

console.log(teclas);

document.addEventListener("mouseup", dibujarTeclado);
var cuadrito = document.getElementById("area_de_dibujo");
var papel = cuadrito.getContext("2d");


dibujarLinea("red", 100, 100, 200, 200, papel);

function dibujarLinea(color, xinicial, yinicial, xfinal, yfinal, lienzo)
{
  lienzo.beginPath();
  lienzo.strokeStyle = color;
  lienzo.linewidth = 3;
  lienzo.moveTo(xinicial, yinicial);
  lienzo.lineTo(xfinal, yfinal);
  lienzo.stroke();
  lienzo.closePath();
}

function dibujarTeclado(evento)
{
  if (evento.keyCode == teclas.UP)
  {
    console.log("vamo' para arriba")
  }

  if (evento.keyCode == teclas.DOWN)
  {
    console.log("Vamo' pa' bajo")
  }

  switch (evento.keyCode)
  {
    case teclas.RIGHT:
      console.log("Derecha");
      break;
    case teclas.LEFT:
      console.log("Izquierda");
    break;

  }

}
