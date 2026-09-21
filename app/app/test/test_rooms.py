def test_index_rooms(client):
    response = client.get('/room/')
    assert response.status_code == 200
    assert b'Lista de Salas' in response.data


def test_add_room(client):
    response = client.post('/room/add', data={
        'name': 'Sala 101',
        'description': 'Sala de lectura'
    }, follow_redirects=True)
    assert response.status_code == 200
    assert b'Sala 101' in response.data


def test_edit_room(client, room):
    response = client.post(f'/room/edit/{room.id}', data={
        'name': 'Sala Actualizada',
        'description': 'Nueva descripción'
    }, follow_redirects=True)
    assert response.status_code == 200
    assert b'Sala Actualizada' in response.data


def test_delete_room(client, room):
    response = client.get(f'/room/delete/{room.id}', follow_redirects=True)
    assert response.status_code == 200
    assert b'Lista de Salas' in response.data
