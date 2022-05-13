function updateTime(){ 
 
  function addZero(i) {
      if (i < 10) {i = "0" + i}
      return i;
    }


  const d = new Date();

  let DayWeek = d.getDay();
  const daysWeek = ["Domingo","Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado"];
  let dayWkName = daysWeek[d.getDay()];

  let DayDay = d.getDate();

  let Month = d.getMonth();
  const months = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiember", "Octubre", "Noviember", "Diciember"];
  let MonthName = months[d.getMonth()];

  let Year = d.getFullYear();
  let Hour = addZero(d.getHours());
  let Min = addZero(d.getMinutes());
  let Seg = addZero(d.getSeconds());


  document.getElementById('dia').innerHTML=(dayWkName +', ' + DayDay +' de ' + MonthName +' '+Year);
  document.getElementById('hora').innerHTML=( Hour + ': ' + Min +': '+Seg );

  }

  setInterval(updateTime, 5000);  











