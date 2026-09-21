def test_index_books(client):
    response = client.get('/Book/')
    assert response.status_code == 200
    assert b'Lista de Libros' in response.data


def test_add_book(client, author):
    response = client.post('/Book/add', data={
        'titleBook': 'Cien años de soledad',
        'authorId': author.idAuthor
    }, follow_redirects=True)
    assert response.status_code == 200
    assert b'Lista de Libros' in response.data
    assert b'Cien' in response.data


def test_edit_book(client, book, author):
    response = client.post(f'/Book/edit/{book.idBook}', data={
        'titleBook': 'Book Updated',
        'authorId': author.idAuthor
    }, follow_redirects=True)
    assert response.status_code == 200
    assert b'Book Updated' in response.data


def test_delete_book(client, book):
    response = client.get(f'/Book/delete/{book.idBook}', follow_redirects=True)
    assert response.status_code == 200
    assert b'Lista de Libros' in response.data
