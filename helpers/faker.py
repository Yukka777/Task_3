from faker import Faker


def fake_user():
    fake = Faker('ru_RU')
    
    user_map = {
        'name': fake.name(),
        'password': fake.password(),
        'email': fake.email()
    }
    
    return user_map
