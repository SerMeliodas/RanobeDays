import factory


class TeamFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'teams.Team'

    name = factory.Sequence(lambda n: f'team {n}')
    team_type = 'autor'

    @factory.post_generation
    def users(self, create, extracted, **kwargs):
        if not create or not extracted:
            return

        self.users.add(*extracted)

    @factory.post_generation
    def novels(self, create, extracted, **kwargs):
        if not create or not extracted:
            return

        self.novels.add(*extracted)
