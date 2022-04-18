from entities.Entity import Session, engine, Base
from entities.User import User

Base.metadata.create_all(engine)
session = Session()

users = session.query(User).all()

print('### USERS:')
for user in users:
    print(f'({user.id}) {user.first_name} {user.last_name} - {user.email}')

if len(users) == 0:
    test_user = User("First","Last","first.last@test.com","9999999999","script")
    session.add(test_user)
    session.commit()
    session.close()

    users = session.query(User).all()

print('### USERS:')
for user in users:
    print(f'({user.id}) {user.first_name} {user.last_name} - {user.email}')