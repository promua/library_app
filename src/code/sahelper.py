from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

class GenericSaHelper(object):
    def __init__(self, url, base_class):
        self.url = url
        
        self.base_class = base_class
        
        #sets up in memory database
        #self.engine = create_engine(url, echo=True)
        self.engine = create_engine(url)
        
        self.session = scoped_session(sessionmaker(bind = self.engine))
    
    def create_all(self):
        self.base_class.metadata.create_all(bind = self.engine)
        
    def drop_all(self):
        self.base_class.metadata.drop_all(bind = self.engine)

    def __del__(self):
        self.session.remove()

from library_app.src.code.model import Base

class SaHelper(GenericSaHelper):
    def __init__(self, url):
        super(SaHelper, self).__init__(url, Base)
        
