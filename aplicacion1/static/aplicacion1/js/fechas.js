
const d = new Date();

let DayWeek = d.getDay();
const daysWeek = ["Domingo","Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado"];
let dayWkName = daysWeek[d.getDay()];

let DayDay = d.getDate();

let Month = d.getMonth();
const months = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiember", "Octubre", "Noviember", "Diciember"];
let MonthName = months[d.getMonth()];

let Year = d.getFullYear();
let Hour = d.getHours();
let Min = d.getMinutes();
let Seg = d.getSeconds();


document.getElementById('dia').innerHTML=('Hoy es ' + dayWkName +' ' + DayDay +' ' + MonthName +' de '+Year);
document.getElementById('hora').innerHTML=('La hora es ' + Hour + ' horas ' + Min +' mins '+Seg +' segs.');












