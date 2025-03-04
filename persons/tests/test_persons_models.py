from django.core.exceptions import ValidationError
from parameterized import parameterized

from .test_persons_base import Person, PersonsTestBase


class PersonsModelTest(PersonsTestBase):
    def setUp(self) -> None:
        self.person = self.make_person()
        return super().setUp()

    def make_person_no_defaults(self):
        person = Person(
            created_by=self.make_user,
            modified_by=self.make_user,
            first_name='PersonDefault',
            last_name='Test Record No',
            cpf_number='12345678912',
            email='person_testrecord@test.com.br',
            date_of_birth='01/01/1990',
            gender='M',
        )
        person.full_clean()
        person.save()
        return person

    @parameterized.expand([
        ('first_name', 30),
        ('last_name', 50),
        ('email', 254),
        ('cpf_number', 11),
        ('gender', 1),
    ])
    
    def test_persons_fields_max_length(self, field, max_length):
        setattr(self.person, field, 'A' * (max_length + 1))
        with self.assertRaises(ValidationError):
            self.person.full_clean()
    
    def test_persons_string_representation(self):
        needed = 'Testing Name'
        needed_last = 'Testing'
        self.person.first_name = needed
        self.person.last_name = needed_last
        self.person.full_clean()
        self.person.save()
        self.assertEqual(
            str(self.person), f'{needed.upper()} {needed_last.upper()}',
            msg=f'Person string representation must be '
                f'"{needed} {needed_last}" but "{str(self.person)}" was received.'
        )