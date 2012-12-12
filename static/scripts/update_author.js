$(function() {
    $("#update_author_dialog").dialog({
	    autoOpen: false,
	    modal: true,
	    buttons: {
	        Ok: function() {
	        		var dialog = $("#update_author_dialog");
	        		var author = dialog.find("input").val();
	        		
	        	    $.ajax({
	        	        url: "/authors/validate",
	        	        type: "post",
	        	        data: {name: author},
	        	        success: function(response, textStatus, jqXHR){
	        	            var result = $.parseJSON(response);
	        	            console.log(result);
	        	            
	        	            if (result.name != undefined) {
	        	            	dialog.find(".errors")
	        	            		.text(result.name.join(", "));
	        	            	dialog.find(".errors")
	        	            		.css("display", "block");
	        	            	return;
	        	            }
	        	            
	        	            //TODO: to substitute old_name to id
	    	        		var name = dialog.data('old_name');

	    	        		//encodes user input
	    	        		name = $('<div/>').text(name).html();
	    	        		
	    	        		var form = $("#update_author_form");
	    	        		form.find("input[name='old_name']").attr('value', name);
	    	        		
	    	        		//encodes user input
	    	        		author = $('<div/>').text(author).html();

	    	        		//sets form value to input data
	    	        		form.find("input[name='new_name']").attr("value", author);
	    	        	
	    	        		form.submit();
	    	        		dialog.dialog("close");
	    	        		dialog.find(".errors").css("display", "none");
	        	        }
	        	    });
	        },
	        Cancel: function() {
	        	dialog = $("#update_author_dialog")
	        	dialog.find(".errors").css("display", "none");
	            dialog.dialog("close");
	        }
	    },
	    close: function() {
	    	dialog = $("#update_author_dialog")
        	dialog.find(".errors").css("display", "none");
            dialog.dialog("close");
	    }
	});
    
    $(".update_author")
    .button()
    .click(function(event) {
    	//gets the author name from the current row
    	var author = $(event.target).parent().parent()
    					 .find(".data .name .value").text();
    	
    	var dialog = $("#update_author_dialog");
    	dialog.data('old_name', author);
    	
    	//fills corresponding placeholder with author name
    	dialog.find(".controls input").val(author);
    	
        dialog.dialog("open");
    });

});