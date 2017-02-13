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
    $(".removeLi").on("click",removeLi);
	/*$("#agregarPagina").on("click", function(event){
		event.preventDefault();
		htmlPagina = $("#paginas li:last-of-type").html();
        $("#paginas").append("<li>"+htmlPagina+"</li>");
        lastLi = $("#paginas li:last-of-type input[type=text]");
        lastLi.attr("value", parseInt(lastLi.val())+1);
        $(".removeLi").off("click").on("click",removeLi);
	});*/
    $("#agregarPaginaEdit, #agregarPagina").on("click", function(event){
		event.preventDefault();
		htmlPagina = $(".copy").html();
        $("#paginas").append("<li>"+htmlPagina+"</li>");
        var i = 1;
        $("#paginas").find("li").each(function(){
            $(this).find("input[type=text]").val(i);
            i++;
        });
         $(".removeLi").off("click").on("click",removeLi);
	});
    $("#paginas").sortable({
        stop: function(){
            var i = 1;
            $(this).find("li").each(function(){
                $(this).find("input[type=text]").val(i);
                i++;
            });
        }
    });
    $("#chaptersBoolean").on("change", function(){
        $("#uploadPage").toggle();
    });
});
Shadowbox.init();

function removeLi(){
    $(this).parent().remove();
}