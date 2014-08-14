$(document).ready(function(){

	$.ajax({
		url : '/get_5_post',
		type : 'post',

		success : function(datas){
			$('#table_div').append(datas);
		},
		error : function(){
			console.log("error");
		},
		complete : function(){
			console.log("complete")
		}
	});

});