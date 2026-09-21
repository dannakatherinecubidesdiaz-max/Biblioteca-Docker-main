def test_index_authors(client):
    response = client.get('/Author/')
    assert response.status_code == 200
    assert b'Lista de Autores' in response.data


def test_add_author(client):
    response = client.post('/Author/add', data={
        'nameAuthor': 'Gabriel García Márquez',
        'nationalityAuthor': 'Colombia'
    }, follow_redirects=True)
    assert response.status_code == 200
    assert b'Gabriel' in response.data


def test_edit_author(client, author):
    response = client.post(f'/Author/edit/{author.idAuthor}', data={
        'nameAuthor': 'Updated Author',
        'nationalityAuthor': 'Uruguay'
    }, follow_redirects=True)
    assert response.status_code == 200
    assert b'Updated Author' in response.data


def test_delete_author(client, author):
    response = client.get(f'/Author/delete/{author.idAuthor}', follow_redirects=True)
    assert response.status_code == 200
    assert b'Lista de Autores' in response.data
