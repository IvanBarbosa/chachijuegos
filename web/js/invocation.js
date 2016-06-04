function getJuegos(){
	var plataforma=$('input:radio[name=plataforma]:checked').val();
	var genero=$('input:radio[name=genero]:checked').val();
	var orden=$('input:radio[name=orden]:checked').val();
	$.ajax({
		type:"GET",
		dataType:"json",
		url: "http://127.0.0.1:5000/devolverjuegos/"+plataforma+"/"+genero+"/"+orden,
		success:function(data){
			var html="";
            var labels = [];
            var values = [];
			$.each(data,function(i,item){
				html+='<div class="mid-grids">';
				html+='<div class="container panelIzquierdo">';
				html+='<div class="top-grid-left col-md-3">';
				html+='<img src="'+data[i].imagen+'" class="img-responsive tamImg" title="doc" /></div>';
				html+='<div class="top-grid-center col-md-7">';
				html+='<h2>'+data[i].titulo+'</h2>';
				html+='<p>'+data[i].descripcion+'</p></div>';
				html+='<div class="top-grid-right col-md-2">';
				html+='<div class="wrapper">';
				html+='<h2 class="panelPuntuacion">'+data[i].puntuacion+'</h2></div></div></div></div>';
                labels.push(data[i].titulo);
                values.push(parseFloat(data[i].puntuacion.replace(',', '.')));
			});
            html+='<canvas id="myChart" width="300" height="200"></canvas>';
			$('#resultado').html(html);
            var ctx = document.getElementById("myChart");
            var myChart = new Chart(ctx, {
                type: 'bar',
                data: {
                    labels: labels,
                    datasets: [{
                        label: 'Puntuación',
                        data: values,
                        backgroundColor: 'rgba(255, 99, 132, 0.2)',
                        borderColor: 'rgba(255,99,132,1)',
                        borderWidth: 1
                    }]
                },
                options: {
                    scales: {
                        yAxes: [{
                            ticks: {
                                beginAtZero:true
                            }
                        }]
                    }
                }
            });
		},
		error:function(res){
			console.log(res),
			alert("Error: "+res.statusText);
		}
	});
}


function getNoticias(){
	$.ajax({
		type:"GET",
		dataType:"json",
		url:"http://127.0.0.1:5000/devolvernoticias",
		success:function(data){
			var html="";
			var referencia;
			for(i=0;i<3;i++){
				
				if(i==0){
					html+='<div class="item active">';
				}else{
					html+='<div class="item">';
				}
				referencia=data[i].referencia;
				referencia=referencia.replace(/[/]/g,';');
				html+='<h2 class="text-center">'+data[i].titulo+'</h2>';
				html+='<img class="center-block" src="'+data[i].imagen+'" alt="Noticia'+i+'"><button type="button" class="btn btn-default center-block" onClick="getContenidoNoticia(\''+referencia+'\')">Extender</button>';
				html+='</div>';
			}
			$('#noticias').html(html);
		},
		error:function(res){
			alert("Error: "+res.statusText);
		}
	});
}


function getContenidoNoticia(input){
	$.ajax({
		type:"GET",
		dataType:"json",
		url:"http://127.0.0.1:5000/devolvercontenido/"+input,
		success:function(data){
			var html="";
			html+='<h4>'+data.texto+'</h4>';
			if(data.video!=null){
				html+='<div class="center-block">';
				html+='<video width="520" height="340" controls><source src="'+data.video+'" type="video/mp4"></video></div>';
			}
			$('#resultado2').html(html);
		},
		error:function(res){
			console.log(res),
			alert("Error: "+res.statusText);
		}
	});
}



