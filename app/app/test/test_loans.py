def test_index_loans(client):
    response = client.get('/Loan/')
    assert response.status_code == 200
    assert b'Lista de Pr\xc3\xa9stamos' in response.data


def test_add_loan(client, book, user):
    response = client.post('/Loan/add', data={
        'bookId': book.idBook,
        'userId': user.idUser,
        'returnDate': '2026-10-10'
    }, follow_redirects=True)
    assert response.status_code == 200
    assert b'Lista de Pr\xc3\xa9stamos' in response.data


def test_edit_loan(client, loan):
    response = client.post(f'/Loan/edit/{loan.idLoan}', data={
        'returnDate': '2026-10-10',
        'fine': '5.0',
        'status': 'Returned'
    }, follow_redirects=True)
    assert response.status_code == 200
    assert b'Lista de Pr\xc3\xa9stamos' in response.data


def test_delete_loan(client, loan):
    response = client.get(f'/Loan/delete/{loan.idLoan}', follow_redirects=True)
    assert response.status_code == 200
    assert b'Lista de Pr\xc3\xa9stamos' in response.data


def test_return_loan(client, loan):
    response = client.get(f'/Loan/return/{loan.idLoan}', follow_redirects=True)
    assert response.status_code == 200
    assert b'Lista de Pr\xc3\xa9stamos' in response.data
