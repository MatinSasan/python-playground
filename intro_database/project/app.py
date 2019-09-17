from user import User

my_user = User(
    'test@test.com',
    'test1',
    'test2',
    None
)


# inserting data
# my_user.save_to_db()

# retrieving data
my_user = User.load_from_db_by_email('test@test.com')
print(my_user)
