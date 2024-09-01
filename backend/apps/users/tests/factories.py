import factory


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'users.User'

    username = factory.Faker('user_name')
    email = factory.Faker('email')
    password = factory.Faker('password')
