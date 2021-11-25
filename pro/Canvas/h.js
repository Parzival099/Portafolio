var teclas = {
  UP: 38,
  DOWN: 40,
  LEFT: 37,
  RIGTH: 39
};
document.addEventListener("keydown",dibujarTeclado);
document.addEventListener("mousedown",dibujarMouse);
document.addEventListener("keydown",dibujarMouse);
var cuadrito = document.getElementById("area_de_dibujo");
var papel = cuadrito.getContext("2d");
var x = 150;
var y = 150;
var puntx = 150;
var punty = 150;
dibujarlinea("red", 149, 149, 151, 151, papel);
function dibujarMouse(eventomouse)
{
  switch (eventomouse.button = true) {
    case puntx = 150:
    dibujarlinea("red", puntx, punty, puntx, punty, papel);
    puntx = eventomouse.pageX;
    punty = eventomouse.pageY;
    console.log(puntx);
      break;
    default:

  }
}

function dibujarlinea(color, xinicial, yinicial, xfinal, yfinal, lienzo)
{
  lienzo.beginPath();
  lienzo.lineWidth = 3;
  lienzo.strokeStyle = color;
  lienzo.moveTo(xinicial, yinicial);
  lienzo.lineTo(xfinal, yfinal);
  lienzo.stroke();
  lienzo.closePath();
}
function dibujarTeclado(evento)
{
  var colorsito = "green";
  var movimiento = 3;
  switch (evento.keyCode) {
    case teclas.UP:

      dibujarlinea(colorsito, x, y, x, y - movimiento, papel );
      y = y - movimiento;
    break;
    case teclas.DOWN:

      dibujarlinea(colorsito, x, y, x, y + movimiento, papel );
      y = y + movimiento;
      break;
      case teclas.LEFT:

        dibujarlinea(colorsito, x, y, x - movimiento, y, papel);
        x = x - movimiento;
        break;
        case teclas.RIGTH:

          dibujarlinea(colorsito, x, y, x + movimiento, y, papel);
          x = x + movimiento;
          break;
    default:

    }
}
