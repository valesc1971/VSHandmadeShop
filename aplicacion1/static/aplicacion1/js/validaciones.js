function checkRut(rut) {

    if (rut.value.length <= 1) {
      alerta.classList.remove('alert-success', 'alert-danger');
      alerta.classList.add('alert-info');
      mensaje.innerHTML = 'Ingrese un RUT en el siguiente campo de texto para validar si es correcto o no';
    }
  
    // Obtiene el valor ingresado quitando puntos y guión.
    var valor = clean(rut.value);
  
    // Divide el valor ingresado en dígito verificador y resto del RUT.
    cuerpo = valor.slice(0, -1);
    dv = valor.slice(-1).toUpperCase();
  
    // Separa con un Guión el cuerpo del dígito verificador.
    rut.value = format(rut.value);
  
    // Si no cumple con el mínimo ej. (n.nnn.nnn)
    if (cuerpo.length < 7) {
      rut.setCustomValidity("RUT Incompleto");
      alerta.classList.remove('alert-success', 'alert-danger');
      alerta.classList.add('alert-info');
      mensaje.innerHTML = 'Ingresó un RUT muy corto, el RUT debe ser mayor a 7 Dígitos. Ej: x.xxx.xxx-x';
      return false;
    }
  
    // Calcular Dígito Verificador "Método del Módulo 11"
    suma = 0;
    multiplo = 2;
  
    // Para cada dígito del Cuerpo
    for (i = 1; i <= cuerpo.length; i++) {
      // Obtener su Producto con el Múltiplo Correspondiente
      index = multiplo * valor.charAt(cuerpo.length - i);
  
      // Sumar al Contador General
      suma = suma + index;
  
      // Consolidar Múltiplo dentro del rango [2,7]
      if (multiplo < 7) {
        multiplo = multiplo + 1;
      } else {
        multiplo = 2;
      }
    }
  
    // Calcular Dígito Verificador en base al Módulo 11
    dvEsperado = 11 - (suma % 11);
  
    // Casos Especiales (0 y K)
    dv = dv == "K" ? 10 : dv;
    dv = dv == 0 ? 11 : dv;
  
    // Validar que el Cuerpo coincide con su Dígito Verificador
    if (dvEsperado != dv) {
      rut.setCustomValidity("RUT Inválido");
  
      alerta.classList.remove('alert-info', 'alert-success');
      alerta.classList.add('alert-danger');
      mensaje.innerHTML = 'El RUT ingresado: ' + rut.value + ' Es <strong>INCORRECTO</strong>.';
  
      return false;
    } else {
      rut.setCustomValidity("RUT Válido");
  
      alerta.classList.remove('d-none', 'alert-danger');
      alerta.classList.add('alert-success');
      mensaje.innerHTML = 'El RUT ingresado: ' + rut.value + ' Es <strong>CORRECTO</strong>.';
      return true;
    }
  }
  