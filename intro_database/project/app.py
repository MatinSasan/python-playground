from user import User

my_user = User(
    'test@test.com',
    'test1',
    'test2',
    None
)


my_user.save_to_db()
