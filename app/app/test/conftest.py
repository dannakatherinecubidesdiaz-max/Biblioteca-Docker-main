from app import create_app, db
import pytest

@pytest.fixture
def app():
    app = create_app()
    with app.app_context():
        db.create_all()  # Create tables within the context
        yield app
        db.session.remove()  # Cleanup session objects
        db.drop_all()
  

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def user(app):
    from app.models.users import User
    user = User(nameUser="test_user", passwordUser="test_password")
    db.session.add(user)
    db.session.commit()  # Commit changes within the context
    yield user
    # Cleanup changes within the context

@pytest.fixture
def author(app):
    from app.models.authors import Author
    author = Author(nameAuthor='Test Author', nationalityAuthor='Argentina')
    db.session.add(author)
    db.session.commit()
    yield author

@pytest.fixture
def book(app, author):
    from app.models.books import Book
    book = Book(titleBook='Test Book', authorId=author.idAuthor)
    db.session.add(book)
    db.session.commit()
    yield book

@pytest.fixture
def room(app):
    from app.models.rooms import Room
    room = Room(name='Test Room', description='Room description')
    db.session.add(room)
    db.session.commit()
    yield room

@pytest.fixture
def computer(app):
    from app.models.computers import Computer
    computer = Computer(brandComputer='Dell', modelComputer='Latitude 5400', statusComputer='Active')
    db.session.add(computer)
    db.session.commit()
    yield computer

@pytest.fixture
def loan(app, book, user):
    from app.models.loans import Loan
    loan = Loan(bookId=book.idBook, userId=user.idUser, status='Active')
    db.session.add(loan)
    db.session.commit()
    yield loan

@pytest.fixture
def computer_loan(app, computer, user):
    from app.models.cloans import ComputerLoan
    loan = ComputerLoan(computerId=computer.idComputer, userId=user.idUser, status='Active')
    db.session.add(loan)
    db.session.commit()
    yield loan