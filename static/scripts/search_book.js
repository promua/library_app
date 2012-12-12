$(function() {
		populate_books_container = function(books_data) {
			var books = $.parseJSON(books_data);
			var book_record_template = [
         	    '<div class="book">',
    	            '<div class="data">',            
    	                '<div class="name">',
    	                    '<div class="label">Name:</div>',
    	                    '<div class="value">{{=it.name}}</div>',
    	                    '<div class="clear"></div>',  
    	                '</div>',
	    	            '<div class="authors">',
		                	'<div class="label">Authors:</div>',
		                	'<div class="value">{{=it.authors.join(", ")}}</div>',
		                	'<div class="clear"></div>',
		                '</div>',
    	            '</div>',
    	            '<!--',
    	            '<div class="controls">',
    	                '<input type="button" value="edit" class="update_book"/>',
    	                '<input type="button" value="delete" class="delete_book"/>',
    	            '</div>',
    	            '-->',
    	            '<div class="clear"></div>',
    	        '</div>'
			].join("\n");
			render = doT.template(book_record_template);
			
			//$("#books_container .book").remove();

			container = $("#books_container");
			
			container.find(".book").remove();
			container.find(".summary").remove();
			
			container.append("<div class='summary'>" + books.length + " results found ...</div>");
			
			var author = "";
			var book_name = "";
			for (i = 0; i < books.length; ++i) {
				authors = [];
				
				for (j = 0; j < books[i].authors.length; ++j) {
					author = books[i].authors[j].name;
					//escapes data before render
					author = $("<div/>").text(author).html();
					authors.push(author);
				}
				
				book_name = books[i].name;
				//escapes data before render
				book_name = $("<div/>").text(book_name).html();
				
				book = {
					'name': book_name,
					'authors': authors
				}
				
				container.append(render(book));
			}
		};

		
		$("#wrapper .search_control input[name='search']")
		.button()
		.click(function() {
			//to escape on server side?
			//sqlalchemy has such feature
			var expression = $(this).closest(".search_control")
				.find("input[name='expression']").val();

			$.get(
				"/books/search",
				{
					expression: expression
				},
				populate_books_container
			);
		});
});