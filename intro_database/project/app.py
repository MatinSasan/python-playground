from user import User
from database import Database

Database.initialize()

my_user = User(
    'test1@test.com',
    'test1',
    'test2',
    None
)


# inserting data
# my_user.save_to_db()

# retrieving data
user_from_db = User.load_from_db_by_email('test@test.com')
print(user_from_db)
