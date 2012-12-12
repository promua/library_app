$(function() {
    $("#delete_author_dialog").dialog({
	    autoOpen: false,
	    //height: 1,
	    //width: 350,
	    modal: true,
	    buttons: {
	        Ok: function() {
	        	var form = $("#delete_author_form");
	        	form.find("input[name='name']")
	        		.attr('value', $(this).data('author'));
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
    
    $(".delete_author")
    .button()
    .click(function(event) {
    	//gets the author name from the current row
    	var author = $(event.target).parent().parent().find(".data .name .value").text();
    	
    	var dialog = $("#delete_author_dialog");
    	dialog.data('author', author);
    	
    	//fills corresponding placeholder with author name
    	dialog.find(".controls .author_name").text(author);
        dialog.dialog("open");
    });
});