from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import Table, Column, ForeignKey, ColumnDefault
from sqlalchemy.types  import BINARY, String
from sqlalchemy.orm    import relationship

import uuid

Base = declarative_base()

author_book_rel = Table("author_book_rel", Base.metadata,
    #Column("author_id", String(36), ForeignKey("author.id", ondelete="cascade"), primary_key = True),
    #Column("book_id",   String(36), ForeignKey("book.id", ondelete="cascade"),  primary_key = True)
    
    Column("author_id", String(36), ForeignKey("author.id"), primary_key = True),
    Column("book_id",   String(36), ForeignKey("book.id"),  primary_key = True)
)

class Author(Base):
    __tablename__ = "author"

    id   = Column(String(36), primary_key = True, default = lambda: str(uuid.uuid4()))
    name = Column(String(64), unique = True) 

    #books = relationship("Book", secondary = author_book_rel, cascade = "delete")
    books = relationship("Book", secondary = author_book_rel, cascade = "delete")
    
    def __repr__(self):
        template   = "<book name='%s' id='%s'/>"
        books_data = map(lambda b: template % (b.name, b.id), self.books)
        books_data = "".join(books_data)
        
        template    = "<author name='%s' id='%s'><books>%s</books></author>"
        author_data = template % (self.name, self.id, books_data)
        
        return author_data

class Book(Base):
    __tablename__ = "book"
    id   = Column(String(36), primary_key = True, default = lambda: str(uuid.uuid4()))
    name = Column(String(64), unique = True)

    authors = relationship("Author", secondary = author_book_rel)

    def __repr__(self):
        template   = "<author name='%s' id='%s'/>"
        authors_data = map(lambda a: template % (a.name, a.id), self.authors)
        authors_data = "".join(authors_data)
        
        template  = "<book name='%s' id='%s'><authors>%s</authors></book>"
        book_data = template % (self.name, self.id, authors_data)
        
        return book_data
    
