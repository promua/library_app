$(function() {
    $("#create_book_dialog").dialog({
	    autoOpen: false,
	    modal: true,
	    buttons: {
	        Ok: function() {
	        	var dialog = $("#create_book_dialog");
        		var book = dialog.find("input").val();
        		
        	    $.ajax({
        	        url: "/books/validate",
        	        type: "post",
        	        data: {name: book},
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
        	            
        	            //escapes user input
        	        	book = $("<div/>").text(book).html();
        	        	
        	        	var form = $("#create_book_form");
        	        	form.find("input[name='name']").attr("value", book);
            	
        	        	//prepares select control for submit 
        	    		form.find("select option").remove();
        	    		
        	    		var authors = dialog.find("select").val();
        	    		for (i = 0; i < authors.length; ++i) {
        	    			form.find("select").append(
        	    				"<option selected='selected'>" + authors[i] + "</option>");
        	    		}
        	    		
        	    		form.submit();
        	    		dialog.find(".errors").css("display", "none");
        	            dialog.dialog("close");
        	        }
        	    });
	        },
	        Cancel: function() {
	        	dialog = $("#create_book_dialog")
	        	dialog.find(".errors").css("display", "none");
	            dialog.dialog("close");
	        }
	    },
	    close: function() {
        	dialog = $("#create_book_dialog")
        	dialog.find(".errors").css("display", "none");
            dialog.dialog("close");
	    }
	});
    
    $("#create_book")
	    .button()
	    .click(function() {
        	var dialog = $("#create_book_dialog");
        	
	        var create_authors_list = function(data) {
	        	var authors = $.parseJSON(data);
        	
	        	dialog.find("select[name='authors'] option").remove();
	        	
	        	var name = "";
	        	for (i = 0; i < authors.length; ++i) {
	        		//escapes json data before insert
	        		//TODO: to check if it is needed
	        		name = $('<div/>').text(authors[i].name).html();
	        		
	        		dialog.find("select[name='authors']")
	        			.append("<option>" + name + "</option>");
	        	}
	        }
	        
	    	$.get('/authors/search', {}, create_authors_list);
	        dialog.dialog("open");
	    });
});