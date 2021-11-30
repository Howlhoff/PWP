var ip="api5.jdiaz.live";
var direccion="/";


function buscarJuego(){
	var mostrar = document.getElementById("id_resultado");
	mostrar.style.display="block";
	aux = $("#id_buscador").val()   	
	message ='?nombre='+aux;	  	
	console.log(message);
	$.ajax
	({

		url: 'http://'+ip+direccion+message,
		crossDomain: true,		   		   
		success: function(response)
		{
			//console.log(response);			  
		    $.each(response,function(key, registro){		    			    				    			    			    
				console.log(registro);

			}); 						
		},
		error: function(data) {
			console.log(data);
		}
	});   
};