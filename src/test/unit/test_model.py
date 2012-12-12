import unittest

from library_app.src.code.model import Author, Book
from library_app.src.code.sahelper import SaHelper
from library_app.etc import config

import uuid

#TODO: to add CRUD tests
class Test(unittest.TestCase):
    def setUp(self):
        print "Inside setUp ..."
        self.sa_helper = SaHelper(config.testing.db.url)
        self.sa_helper.create_all()
        
    def tearDown(self):
        print "Inside tearDown ..."
        
        self.sa_helper.drop_all()
        self.sa_helper.session.remove()
        
    def testDbSchemaExists(self):
        #TODO: to check if query was executed without errors
        result = self.sa_helper.session.execute("select * from book")
        self.assertEqual(result.fetchone(), None)
        
    def testOrmWorks(self):
        author_name = "Martin Fowler"
        author_id   = str(uuid.uuid4())
        
        #TODO: to check if result is ok
        result = self.sa_helper.session.execute(
            "insert into author (id, name) values (:id, :name)",
            {"id": author_id, "name": author_name}
        )
                
        author = self.sa_helper.session.query(Author).all()[0]
        self.assertEqual(author.name, author_name)
        
        print author.id
        
    def testIfManyToManyRelationWorks(self):
        #dictionary of {book: [authors]}
        data = {
            "Refactoring" : ["Martin Fowler", "Kent Beck"],
            "Planning XP" : ["Martin Fowler", "Kent Beck"]
        }
        
        #TODO: to make code below more readable
        #{book_name: book_id}
        processed_books   = {}
        
        #{author_name: author_id}
        processed_authors = {}
        
        for book, authors in data.iteritems():  
            if book in processed_books.keys():
                book_id = processed_books[book]
            else:
                #generates unique id for current book
                book_id = str(uuid.uuid4())
                
                #inserts data into book table
                self.sa_helper.session.execute(
                    "insert into book (id, name) values (:id, :name)",
                    {"id" : book_id, "name": book}
                )
                processed_books[book] = book_id
            
            for author in authors:
                if author in processed_authors.keys():
                    author_id = processed_authors[author]
                else:
                    #generates unique id for current author
                    author_id = str(uuid.uuid4())
                    
                    #inserts data into author table
                    self.sa_helper.session.execute(
                        "insert into author (id, name) values (:id, :name)",
                        {"id" : author_id, "name" : author}
                    )
                    
                    processed_authors[author] = author_id
                
                #inserts corresponding relation into author_book_rel
                self.sa_helper.session.execute(
                    "insert into author_book_rel (author_id, book_id) "
                    "values (:author_id, :book_id)",
                    {"author_id" : author_id, "book_id": book_id}
                )

        books = self.sa_helper.session.query(Book).all()
        for book in books:
            print book
            self.assertTrue(len(book.authors) > 1)
            
            
        authors = self.sa_helper.session.query(Author).all()
        for author in authors:
            print author
            self.assertTrue(len(author.books) > 1)
            
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
