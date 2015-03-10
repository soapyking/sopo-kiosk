$(document).ready(function() {
	var current_fs, next_fs, previous_fs; //fieldsets

	$(".next").click(function(){
		
		console.log("It's happening")
		current_fs = $(this).parent();
		next_fs = $(this).parent().next();
		
		//activate next step on progressbar using the index of next_fs
		$("#progressbar li").eq($("fieldset").index(next_fs)).addClass("active");
		
		next_fs.show(); 
		current_fs.hide();
	});

	$(".previous").click(function(){
		
		current_fs = $(this).parent();
		previous_fs = $(this).parent().prev();
		
		//de-activate current step on progressbar
		$("#progressbar li").eq($("fieldset").index(current_fs)).removeClass("active");
		
		//show the previous fieldset
		previous_fs.show(); 
		current_fs.hide();
	});

	$(".submit").click(function(){
		return false;
	})
})
