jQuery('#master').on('click', function(e) {
	if($(this).is(':checked',true))  
	{
		$(".sub_chk").prop('checked', true);  
	}  
	else  
	{  
		$(".sub_chk").prop('checked',false);  
	}  
});