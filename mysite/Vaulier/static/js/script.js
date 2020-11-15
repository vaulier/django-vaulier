$(function() {
    $("#formulario").validate({
        rules: {
                rut: { required: true, rut: true},

                nombres: {required: true},

                apellidos: {required: true},
                
                email: {required: true},

                /*telefono:{required: true},*/


                album-pedido: {required: true},

                radio: {required: true},


                /*          ---------------- seccion contacto  ----------------          */
                asunto: {required: true},
                mensaje: {required: true},
            },

        messages: {
                rut: { required: 'Ingresa tu RUT', rut: 'El formato del RUT no es válido', minlength: 'Largo insuficiente' },

                nombres: { required: 'Ingresa nombres', minlength: 'Largo insuficiente' },


                apellidos: { required: 'Ingresa apellidos', minlength: 'Largo insuficiente' },

                email:{ required: 'Ingresa e-mail', minlength: 'Largo insuficiente' },
                
                /*telefono:{ required: 'Ingresa telefono', minlength: 'Largo insuficiente'},*/
                
                album-pedido:{ required: 'Ingresa ARTISTA - ALBUM', minlength: 'Largo insuficiente'},

                radio:{required: 'Elige la version del vinilo', minlength: 'Solo una opcion'},

                asunto:{required: 'Escribe un asunto', minlength: 'Solo un asunto'},

                mensaje:{required: 'Escribe un mensaje', minlength: 'Más especifico'},

            }
        });
    });
    