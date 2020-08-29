var canvas = document.querySelector('canvas');

canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

var contact = canvas.getContext('2d');

contact.fillRect(100,100,100,100);
console.log(canvas);