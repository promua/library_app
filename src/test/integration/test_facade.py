import unittest

from library_app.src.code.dto import AuthorDto, BookDto
from library_app.src.code.model import Author, Book
from library_app.src.code.sahelper import SaHelper
from library_app.src.code.facade import LibraryManager
from library_app.etc import config

import uuid

class Test(unittest.TestCase):
    def setUp(self):
        print "Inside setUp ..."
        self.sa_helper = SaHelper(config.testing.db.url)
        self.sa_helper.create_all()
        
        self.facade = LibraryManager(self.sa_helper.session)
        
    def tearDown(self):
        print "Inside tearDown ..."
        
        self.sa_helper.drop_all()
        self.sa_helper.session.remove()
        
    def testAuthorCreation(self):
        author_name = "Martin Fowler"
        
        #creates author record in db using LibraryManager api
        author_dto  = AuthorDto(name = author_name)
        self.facade.create_author(author_dto)
        
        #checks if record was created
        res = self.sa_helper.session.query(Author)\
            .filter(Author.name == author_name).count()
        
        self.assertEqual(res, 1)
   
    def testBookCreation(self):
        book_name = "Refactoring"
        
        #creates book record in db using LibraryManager api
        book_dto  = BookDto(name = book_name)
        self.facade.create_book(book_dto)
        
        #checks if record was created
        res = self.sa_helper.session.query(Book)\
            .filter(Book.name == book_name).count()
        
        self.assertEqual(res, 1)
        
    def testAuthorDeletion(self):
        author_name = "Martin Fowler"
        
        #creates author record
        author = Author()
        author.name = author_name
        
        self.sa_helper.session.add(author)
        self.sa_helper.session.flush()
        
        #checks if record was created
        res = self.sa_helper.session.query(Author)\
            .filter(Author.name == author_name).count()
            
        self.assertEqual(res, 1)
        
        #deletes this record using LibraryManager api
        author_dto  = AuthorDto(name = author_name)        
        self.facade.delete_author(author_dto)
        
        #checks if author was deleted
        res = self.sa_helper.session.query(Author)\
            .filter(Author.name == author_name).count()
            
        self.assertEqual(res, 0)
               
    def testBookDeletion(self):
        book_name = "Refactoring"
        
        #creates book record
        book = Book()
        book.name = book_name
        
        self.sa_helper.session.add(book)
        self.sa_helper.session.flush()
        
        #checks if record was created 
        res = self.sa_helper.session.query(Book)\
            .filter(Book.name == book_name).count()
        
        self.assertEqual(res, 1)
        
        #deletes this record using LibraryManager api
        book_dto  = BookDto(name = book_name)        
        self.facade.delete_book(book_dto)
        
        #checks if book was deleted
        res = self.sa_helper.session.query(Book)\
            .filter(Book.name == book_name).count()
            
        self.assertEqual(res, 0)
        
