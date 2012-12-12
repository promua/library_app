$(function() {
    $("#delete_book_dialog").dialog({
	    autoOpen: false,
	    modal: true,
	    buttons: {
	        Ok: function() {
	        	var form = $("#delete_book_form");
	        	
	        	var book = $(this).data('book');
	        	//escapes data
	        	book = $('<div/>').text(book).html();
	        	
	        	form.find("input[name='name']").attr('value', book);
	        	
	        	form.submit();
	            $(this).dialog("close");
	        },
	        Cancel: function() {
	            $(this).dialog("close");
	        }
	    },
	    close: function() {
	    }
	});
    
    $(".delete_book")
    .button()
    .click(function() {
    	//gets the author name from the current row
    	var book = $(this).closest('.book')
    					 .find(".data .name .value").text();
    	
    	//escapes data (just for the case)
    	book = $('<div/>').text(book).html();
    	
    	var dialog = $("#delete_book_dialog");
    	dialog.data('book', book);
    	
    	//fills corresponding placeholder with book name
    	dialog.find(".controls .book_name").text(book);
        dialog.dialog("open");
    });
    
});