from wtforms import Form, TextField, validators

class AuthorForm(Form):
    name = TextField("Author name", [validators.Length(min=3, max=32)])

class BookForm(Form):
    name = TextField("Book name", [validators.Length(min=3, max=64)])
