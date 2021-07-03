





$(document).ready(function(){
//$('.datepicker').datepicker();
$('select').formSelect();
var x=[0,0,0,0],y=[0,0,0,0];
plotea(x,y);


$("#opcion").change(function(){





});


$("#grafica").click(function(e){
	e.preventDefault();

	var opc=$("#opcion").val();
	var pos	=Number($("#pos").val())-1;


	switch(Number(opc)) {
    case 1:
    	var a=$("#vector1").val();
    	//VALORES Y DEL VECTOR
		var y=a.split(',');
		//VALORES X DEL VECTOR
		var x=[];
		for(var i=-(pos);i<y.length;i++){
        	x.push(i);        	
   	   }

   	   //generamos arreglo de apoyo
   	   var inter=3;
   	   var auxX=[];
   	   var auxY=[];

   	   contador=x[0];

   	   for (var i = 0; i <y.length; i++) {
   	   	auxX.push(contador);
   	   	auxY.push(Number(y[i]));
   	   	var dis=((y[i+1]-y[i])/inter);
   	   	alert(y[i+1]);
   	   	alert(y[i]);
		var sum=0
   	   	for (var j = 1; j < inter; j++) {
   	   		contador++;
   	   		auxX.push(contador);
   	   		
   	   		if(j==1)
   	   		{
   	   			sum=dis+Number(y[i]);
   	   		}
   	   		else{
   	   			sum=sum+dis;	  
   	   		}
   	   		auxY.push(sum);
   	   		 	   		
   	   	}
   	   	contador++;   	   	
   	   }

   	   x=auxX;
   	   y=auxY;










   	   //empezamos interpolacion
   	   


        break;
    case 2:
        
        break;

    }

    Plotly.purge('tester');
    plotea(x,y);

});


});


function plotea(a_x,a_y)
{

 TESTER = document.getElementById('tester');

var x = a_x,
	 y = a_y,
	 // create a zero-filled array
	 zeros = new Array(x.length).fill(0);

Plotly.plot( TESTER, [
	{
		x: x,
		y: y,
		type: 'scatter',
		marker: {
			symbol: 'circle',
			size: 15
		},
		line: {width: 0},
		hoverinfo: 'x+text', // The default configuration would print "16 +0/-16"...
		hovertext: y.map(Plotly.d3.format('.4 ')), // ... so we redefine the text
    error_y: {
			type: 'data',
			symmetric: false,
			array: zeros, // use zero-filled array
			arrayminus: y, // re-use y values
			width: 0 // hide cross-bars at end of error bars
		}
}], { 
    margin: { t: 0 } } );

/* Current Plotly.js version */
console.log( Plotly.BUILD );
}