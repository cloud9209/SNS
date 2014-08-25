var xhr;

function find_user()
{	
	$('#found_user_list').empty();

	console.log('here');
	var to_find_user = $("#to_find_user");
	var character = to_find_user.val();
	console.log(character);
	
	if (xhr)
	{
		xhr.abort();
	}
	if (character == ""){
		$('#found_user_list').empty();		
	}
	else{
		xhr = $.ajax({
			url : '/find_user_list',
			type : 'post',
			data : {"character" : character},

			success : function(datas){
				$('#found_user_list').append(datas);
			},
			error : function(){
				console.log("error");
			},
			complete : function(){
				console.log("complete")
			}
		});
	}
}

function add_follow_user(user_id)
{
	$('#following_user_list').empty();
	
	$.ajax({
		url : '/add_follow_user_controllers',
		type : 'post',
		data : {"user_id" : user_id},

		success : function(datas){
			$('#following_user_list').append(datas);
		},
		error : function(){
			console.log("error");
		},
		complete : function(){
			console.log("complete")
		}
	});

}