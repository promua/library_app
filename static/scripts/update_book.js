$(function() {
    $("#update_book_dialog").dialog({
	    autoOpen: false,
	    modal: true,
	    buttons: {
	        Ok: function() {
	        	var book = $(this).find("input").val();
	        	
        	    $.ajax({
        	        url: "/books/validate",
        	        type: "post",
        	        data: {name: book},
        	        success: function(response, textStatus, jqXHR){
        	            var result = $.parseJSON(response);
        	            console.log(result);
        	            
        	            var dialog = $("#update_book_dialog");
        	            if (result.name != undefined) {
        	            	dialog.find(".errors")
        	            		.text(result.name.join(", "));
        	            	dialog.find(".errors")
        	            		.css("display", "block");
        	            	return;
        	            }
        	            
        	            var form = $("#update_book_form");
    	        		
    	        		//TODO: to replace with id
    	        		var name = dialog.data('old_name');
    	        		
    	        		//escapes data before insert to html
    	        		name = $('<div/>').text(name).html();
            			form.find("input[name='old_name']").attr('value', name);
            		
            			//escapes data before insert to html
            			book = $('<div/>').text(book).html();
    	        		//sets form value to input data
    	        		form.find("input[name='name']").attr("value", book);
    	        	
    	        		form.find("select option").remove();
    	        		
    	        		var authors = dialog.find("select").val();
    	        		var author = "";
    	        		for (i = 0; i < authors.length; ++i) {
    	        			author = authors[i];
    	        			//escapes data
    	        			author = $('<div/>').text(author).html();
    	        			form.find("select").append(
    	        				"<option selected='selected'>" + author + "</option>");
    	        		}
    	        		
    	        		form.submit();
        	    		dialog.find(".errors").css("display", "none");
        	            dialog.dialog("close");
        	        }
        	    });
	        },  
	        Cancel: function() {
	        	dialog = $("#update_book_dialog")
	        	dialog.find(".errors").css("display", "none");
	            dialog.dialog("close");
	        }
	    },
	    close: function() {
        	dialog = $("#update_book_dialog")
        	dialog.find(".errors").css("display", "none");
            dialog.dialog("close");
	    }
	});
 
    $(".update_book")
    .button()
    .click(function() {
    	//gets the book name from the current row
    	var book = $(this).closest('.book')
    					 .find(".data .name .value").text();
    	
    	var selected = $(this).closest('.book')
    		.find(".data .authors .value").text().split(", ");
    	
    	var dialog = $("#update_book_dialog");
    	dialog.data('old_name', book);
    	
    	//fills corresponding placeholder with book name
    	dialog.find(".controls input").val(book);
    	
        var create_authors_list = function(data) {
        	var authors = $.parseJSON(data);
        	dialog.find("select[name='authors'] option").remove();
        	var author = "";
        	for (i = 0; i < authors.length; ++i) {
        		//escapes data
        		author = $('<div/>').text(authors[i].name).html();
        		if ($.inArray(author, selected) > -1) {
        			dialog.find("select[name='authors']").append(
		        			"<option selected='selected'>" + author + "</option>");
        		} else {
        			dialog.find("select[name='authors']")
        				.append("<option>" + author + "</option>");
        		}
        	}
        }
        //TODO: to replace with post?
        $.get("/authors/search", {}, create_authors_list);
        dialog.dialog("open");
    });
    
});