
var mailformat = /^([A-Za-z0-9_\-\.])+\@([A-Za-z0-9_\-\.])+\.([A-Za-z]{2,4})$/;

function validacion() {
  if (document.miFormu.nombre.value == "") {
    Swal.fire("Ingresar nombre");
    return false
    document.miFormu.nombre.focus()

  } else if (document.miFormu.apellido.value == "") {
    Swal.fire("Ingresar apellido");
    return false
    document.miFormu.apellido.focus()

    } else if (document.miFormu.email.value == "") {
    Swal.fire("Ingresar correo");
    return false
    document.miFormu.email.focus()

    }else if (!document.miFormu.email.value.match(mailformat))
            {Swal.fire ("Ingrese email valido");
            return false
                document.miFormu.email.focus()
                


    } else if (document.miFormu.mensaje.value == "") 
    {Swal.fire("Ingresar mensaje");
    return false
      document.miFormu.mensaje.focus()
    
      } else if (document.miFormu.mensaje.value =true) 
      {{alert("Gracias por su mensaje. Me contactare a la brevedad");}
      return true
    
      }
    }

    var Fn = {
      // Valida el rut con su cadena completa "XXXXXXXX-X" https://codepen.io/donpandix/pen/jWNNKj
      validaRut : function (rutCompleto) {
        rutCompleto = rutCompleto.replace("‐","-");
        if (!/^[0-9]+[-|‐]{1}[0-9kK]{1}$/.test( rutCompleto ))
          return false;
        var tmp 	= rutCompleto.split('-');
        var digv	= tmp[1]; 
        var rut 	= tmp[0];
        if ( digv == 'K' ) digv = 'k' ;
        
        return (Fn.dv(rut) == digv );
      },
      dv : function(T){
        var M=0,S=1;
        for(;T;T=Math.floor(T/10))
          S=(S+T%10*(9-M++%6))%11;
        return S?S-1:'k';
      }
    }
    
    
    $("#btnvalida").click(function(){
      if (Fn.validaRut( $("#txt_rut").val() )){
        $("#msgerror").html("El rut ingresado es válido :D");
      } else {
        $("#msgerror").html("El Rut no es válido :'( ");
      }
    }); 
    
    
    $(document).ready(function() {
      $('#example').DataTable( {
          "language": {
              "lengthMenu": "Mostrar _MENU_ Registros por pagina",
              "zeroRecords": "No se encontraron registros",
              "info": "Mostrando pagina _PAGE_ de _PAGES_",
              "thousands":      ".",
              "infoFiltered": "(filtrado de _MAX_ registros totales)",
              "infoEmpty":      "Mostrando 0 a 0 de 0 entradas",
              "paginate": {
          "first":      "Primero",
          "last":       "Ultimo",
          "next":       "Siguiente",
          "previous":   "Anterior"
      },
              "search":         "Buscar:",
          }
      } );
      $('#example').show();
    
    } );