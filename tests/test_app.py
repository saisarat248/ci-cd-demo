from app.db import init_db, add_user, get_users

def test_add_user():
    init_db()
    add_user("TestUser")
    users = get_users()
    assert ("TestUser",) in users
