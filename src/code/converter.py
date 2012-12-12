from library_app.src.code.model import Author, Book
from library_app.src.code.dto import AuthorDto, BookDto, AuthorRef, BookRef

class GenericConverter(object):
    mo  = None
    dto = None
    
    @classmethod
    def from_dto(cls, dto):
        converter = cls()
        converter.dto = dto
        
        return converter
    
    @classmethod
    def from_mo(cls, mo):
        converter = cls()
        converter.mo = mo
        
        return converter
    
    def to_dto(self):
        raise NotImplementedException(
            "You must implement this method in subclass of %s ..."
            % self.__class__.name)
    
    def to_mo(self):
        raise NotImplementedException(
            "You must implement this method in subclass of %s ..."
            % self.__class__.name)

class AuthorConverter(GenericConverter):
    def to_dto(self):
        if self.dto:
            return self.dto
        
        #prepares references to books
        books = map(lambda b: BookRef(id = b.id, name = b.name), self.mo.books)
           
        self.dto = AuthorDto(
            id = self.mo.id, name = self.mo.name, books = books)
        
        return self.dto
    
    def to_mo(self):
        if self.mo:
            return mo
        
        #prepares books objects from references
        books = map(lambda b: Book(id = b.id, name = b.name), self.dto.books)
        
        self.mo = Author()
        self.mo.id    = self.dto.id
        self.mo.name  = self.dto.name
        self.mo.books = books
        
        return self.mo
    
class BookConverter(GenericConverter):
    def to_dto(self):
        if self.dto:
            return self.dto
        
        #prepares references to authors
        authors = map(lambda a: AuthorRef(id = a.id, name = a.name), self.mo.authors)
           
        self.dto = BookDto(
            id = self.mo.id, name = self.mo.name, authors = authors)
        
        return self.dto
    
    def to_mo(self):
        if self.mo:
            return self.mo
        
        #prepares authors objects from references
        authors = map(lambda b: Author(id = b.id, name = b.name), self.dto.authors)
        
        self.mo = Book()
        self.mo.id      = self.dto.id
        self.mo.name    = self.dto.name
        self.mo.authors = authors
        
        return self.mo
    