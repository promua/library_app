class AuthorRef(object):
    def __init__(self, id = None, name = None):
        self.id   = id
        self.name = name
        
class AuthorDto(AuthorRef):
    def __init__(self, id = None, name = None, books = []):
        super(AuthorDto, self).__init__(id, name)
        self.books = map(None, books)

class BookRef(object):
    def __init__(self, id = None, name = None):
        self.id   = id
        self.name = name
                
class BookDto(BookRef):
    def __init__(self, id = None, name = None, authors = []):
        super(BookDto, self).__init__(id, name)
        self.authors = map(None, authors)
    