from db import init_db, add_user, get_users

if __name__ == "__main__":
    init_db()
    add_user("Sarat")
    print(get_users())
