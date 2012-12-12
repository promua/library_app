from library_app.src.code.model import Author, Book
from library_app.src.code.converter import AuthorConverter, BookConverter
from sqlalchemy import or_

class LibraryManager(object):
    def __init__(self, session):
        self.session = session
        
    def create_author(self, author_dto):
        author = AuthorConverter.from_dto(author_dto).to_mo()
        
        self.session.add(author)
        self.session.commit()
        
        return
    
    def create_book(self, book_dto):
        book = BookConverter.from_dto(book_dto).to_mo()
        
        authors = self.session.query(Author).filter(
            Author.name.in_(map(lambda a: a.name, book_dto.authors))).all()
        
        book.authors = authors
            
        self.session.add(book)
        self.session.commit()
        
        return
    
    def delete_author(self, author_dto):
        author = self.session.query(Author)\
            .filter(Author.name == author_dto.name).one()
        
        #HOOK:just to be in time - got issue with
        #cascade deleting for many to many relation -
        #have not found solution yet
        #self.session.begin()
        books = author.books
        try:
            self.session.expunge(author)
            for book in books:
                self.session.expunge(book)
                self.session.execute("delete from book where id = :id", {"id": book.id})
                self.session.execute("delete from author_book_rel where book_id = :book_id", {"book_id": book.id})
            self.session.execute("delete from author where id = :id", {"id" : author.id})
            self.session.commit()
        except Exception, e:
            self.session.rollback()
            raise e
        return
    
    def delete_book(self, book_dto):
        book = self.session.query(Book).filter(Book.name == book_dto.name).one()
        #self.session.begin()
        try:
            self.session.expunge(book)
            self.session.execute("delete from book where name = :name", {"name" : book.name})
            self.session.execute("delete from author_book_rel where book_id = :book_id", {"book_id": book.id})
            self.session.commit()
        except Exception, e:
            self.session.rollback()
            raise e
        return
    
    def update_author(self, author_dto):
        author = self.session.query(Author)\
            .filter(Author.id == author_dto.id).one()
            
        author.name = author_dto.name
        self.session.commit()
        return
    
    def update_book(self, book_dto):
        book = self.session.query(Book)\
            .filter(Book.id == book_dto.id).one()
        
        authors = self.session.query(Author).filter(
            Author.name.in_(map(lambda a: a.name, book_dto.authors))).all()
        
        book.name = book_dto.name
        book.authors = authors
        
        self.session.commit()
        return
    
    def search_authors(self):
        query = self.session.query(Author).order_by(Author.name)
        authors = query.all()
        return map(lambda author: AuthorConverter.from_mo(author).to_dto(), authors)
    
    def search_books(self, expression):
        query = self.session.query(Book).order_by(Book.name)
        
        if expression:
            query = query.filter(or_(
                Book.name.like("%" + expression + "%"),
                Book.authors.any(Author.name.like("%" + expression + "%"))))
            
        return map(lambda book: BookConverter.from_mo(book).to_dto(), query.all())
    
    def get_author(self, author_dto):
        query = self.session.query(Author)
        
        if author_dto.id:
            query = query.filter(Author.id == author_dto.id)
            
        if author_dto.name:
            query = query.filter(Author.name == author_dto.name)
        
        author = query.one()
            
        return AuthorConverter.from_mo(author).to_dto()
    
    def get_book(self, book_dto):
        query = self.session.query(Book)
        
        if book_dto.id:
            query = query.filter(Book.id == book_dto.id)
            
        if book_dto.name:
            query = query.filter(Book.name == book_dto.name)
        
        book = query.one()
            
        return BookConverter.from_mo(book).to_dto()
    
