$(document).on("ready", function(){
	$('.datepicker').datetimepicker({
		format:'Y-m-d H:i:s'
	});
	$(".delete").on("click",function(event){
		event.preventDefault();
		a = confirm("Seguro que quiere borrarlo?");
		if(a){
			window.location = $(this).attr("href");
		}
	});
	$("#agregarPagina").on("click", function(event){
		event.preventDefault();
		htmlPagina = $("#paginas li:last-child").html();
		console.log(htmlPagina);
	});
});
Shadowbox.init();

