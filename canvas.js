//Atributos del Canvas
var canvas = document.querySelector('canvas');
canvas.width = 800;
canvas.height = 800;

var context = canvas.getContext('2d');

//Pide la distancia del terrreno en Metros
var distanciaX = 25;
var distanciaY = 25;
var area = distanciaX * distanciaY;

//Valor en Metros de la Mesa y Sana Distancia
var mesaX = 1;
var mesaY = 1;
var distanciaMinima = 1.5;
var areaMesa = (mesaX + distanciaMinima / 2) * (mesaY + distanciaMinima / 2);

//Calcula el numero de mesas totales y el numero de mesas por renglon y fila
var numeroMesa = Math.floor(area / areaMesa);
var numeroMesasX = Math.floor(distanciaX * numeroMesa / area);
var numeroMesasY =Math.floor(distanciaY * numeroMesa / area);
var mesasTotales = numeroMesasX *  numeroMesasY;

//Asigna la caoacidad del total de mesas 1 es 100%
var capacidad = 1;
if( capacidad < 1){
    mesasTotales = mesasTotales * capacidad;
    numeroMesasX = Math.sqrt(mesasTotales);
    numeroMesasY = Math.sqrt(mesasTotales);
}

//Se hace una escala de metros a pixeles tomando en cuenta lo que mide el canvas
distanciaMinimaCanvasX = distanciaMinima * canvas.width / distanciaX;
distanciaMinimaCanvasY = distanciaMinima * canvas.height / distanciaY;
mesaCanvasX = mesaX * canvas.width / distanciaX;
mesaCanvasY = mesaY * canvas.height / distanciaY;


//Prints para validar la informacion
/*
console.log(canvas.width, canvas.height);
console.log(distanciaX, distanciaY, area);
console.log(mesaX, mesaY, distanciaMinima,areaMesa)
console.log(numeroMesa, numeroMesasX, numeroMesasY);
console.log(distanciaMinimaCanvasX, distanciaMinimaCanvasY, mesaCanvasX, mesaCanvasY);
*/

//Ciclo para dibujar en el canvas las mesas
var posicionX = 0;
var contadorX = 0
while(contadorX < numeroMesasX){
    var posicionY = 0;
    var contadorY = 0;
    while(contadorY < numeroMesasY){
        context.fillRect(posicionX,posicionY,mesaCanvasX,mesaCanvasY);
        posicionY = posicionY + mesaCanvasY + distanciaMinimaCanvasY;
        contadorY +=1
    }
    posicionX = posicionX +  mesaCanvasX + distanciaMinimaCanvasX
    contadorX +=1
}
console.log(canvas)

/*
context.fillStyle="#FF0000";
//Linea Roja que marca una Mesa
context.fillRect(0,mesaCanvasY,mesaCanvasX, 2);
//Linea Roja que marca sana distancia en X
context.fillRect(mesaCanvasX,mesaCanvasY,distanciaMinimaCanvasX,2);
//Linea Roja que marca sana distancia en Y
context.fillRect(mesaCanvasX,mesaCanvasY,distanciaMinimaCanvasX,distanciaMinimaCanvasY);
*/
