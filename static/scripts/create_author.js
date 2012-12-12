$(function() {
    $("#create_author_dialog").dialog({
	    autoOpen: false,
	    modal: true,
	    buttons: {
	        Ok: function() {
	        		var author = $(this).find("input").val();
	        		
	        	    $.ajax({
	        	        url: "/authors/validate",
	        	        type: "post",
	        	        data: {name: author},
	        	        success: function(response, textStatus, jqXHR){
	        	            var result = $.parseJSON(response);
	        	            console.log(result);
	        	            
	        	            var dialog = $("#create_author_dialog");
	        	            if (result.name != undefined) {
	        	            	dialog.find(".errors")
	        	            		.text(result.name.join(", "));
	        	            	dialog.find(".errors")
	        	            		.css("display", "block");
	        	            	return;
	        	            }
	        	            
        	            	//encodes user input
        	        		author = $('<div/>').text(author).html();
        	        		
        	        		var form = $("#create_author_form");
        	        		form.find("input[name='name']").attr("value", author);

        	        		form.submit();
        	        		dialog.dialog.close();
        	        		dialog.find(".errors").css("display", "none");
	        	        }
	        	    });
	        },
	        Cancel: function() {
	        	dialog = $("#create_author_dialog")
	        	dialog.find(".errors").css("display", "none");
	            dialog.dialog("close");
	        }
	    },
	    close: function() {
        	dialog = $("#create_author_dialog")
        	dialog.find(".errors").css("display", "none");
            dialog.dialog("close");
	    }
	});
 
    $("#create_author")
	    .button()
	    .click(function() {
	        $("#create_author_dialog").dialog("open");
	    });
});