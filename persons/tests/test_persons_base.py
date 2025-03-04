from django.test import TestCase
from persons.models import USER, Person
from datetime import date

class PersonsMixin:
    def make_user(
        self,
        first_name='username',
        last_name='last name',
        username='username',
        password='123456',
        email='username@email.com',
    ):
        return USER.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
            password=password,
            email=email
        )

    def make_person(
        self,
        created_by=None,
        modified_by=None,
        first_name='Person',
        last_name='Test Record',
        cpf_number='12345678912',
        email='person_testrecord@test.com.br',
        birth='1990-02-01',
        gender='M',
    ):

        user_created_modified = self.make_user()
            
        person = Person(
            created_by=user_created_modified,
            modified_by=user_created_modified,
            first_name=first_name,
            last_name=last_name,
            cpf_number=cpf_number,
            email=email,
            date_of_birth=birth,
            gender=gender,
        )
        person.full_clean()
        person.save()
        return person

    def make_person_in_batch(self, qtd=10):
        persons = []
        for i in range(qtd):
            kwargs = {
                'last_name': f'Test Record {i}',
                'created_by': {'username': f'u{i}'},
                'modified_by':{'username': f'u{i}'},
            }
            person = self.make_person(**kwargs)
            persons.append(person)
        return persons


class PersonsTestBase(TestCase, PersonsMixin):
    def setUp(self) -> None:
        return super().setUp()