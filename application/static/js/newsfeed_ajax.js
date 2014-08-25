var last = false;
var running =false;

$(document).ready(function(){
	var offset = 0;
	$.ajax({
		url : '/get_5_post_newsfeed',
		type : 'post',
		data : {"offset" : offset},

		success : function(datas){
			$('#newsfeed_div').append(datas);
		},

		error : function(){
			console.log("error");
		},
		
		complete : function(){
			console.log("complete")
			offset = offset + 5;
		}
	});


	$(window).scroll(function() {
		if($(window).scrollTop() == $(document).height() - $(window).height()){
			if (running == false && last == false){
				running = true;

				// ajax call get data from server and append to the div
				$.ajax({
					url : '/get_5_post_newsfeed',
					type : 'post',
					data : {"offset" : offset},

					success : function(datas){
						if (datas.trim() == ""){
							last = true;
						}
						else{
							$('#newsfeed_div').append(datas);
						}
					},
					error : function(){
						console.log("error");
					},
					complete : function(){
						console.log("complete")
						offset = offset + 5;
						console.log(offset)
						running = false;
					}
				});
			}
		}
	});
});


