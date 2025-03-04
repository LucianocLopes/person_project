from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

USER = get_user_model()


# Choices
class GenderChoices(models.TextChoices):
    M = 'M', _("Male")
    F = 'F', _("Female")


# Abstracts models
class TimeStamp(models.Model):
    created_at = models.DateTimeField(_("created at"), auto_now=False, auto_now_add=True)
    created_by = models.ForeignKey(
        USER, 
        verbose_name=_("user created by"), 
        related_name="usercreated_by",
        related_query_name="usercreate_by",
        on_delete=models.DO_NOTHING,
        )
    modified_at = models.DateTimeField(_("modified at"), auto_now=True, auto_now_add=False)
    modified_by = models.ForeignKey(
        USER, 
        verbose_name=_("user modified by"), 
        related_name="usermodified_by",
        related_query_name="usermodified_by",
        on_delete=models.DO_NOTHING,
        )
    
    class Meta:
        abstract = True


# Mixin models



# Models
class Person(TimeStamp):
    """Model definition for Person."""

    # TODO: Define fields here
    first_name = models.CharField(_("first name"), max_length=30)
    last_name = models.CharField(_("last name"), max_length=50)
    cpf_number = models.CharField(_("CPF"), max_length=11)
    email = models.EmailField(_("e-mail"), max_length=254)
    date_of_birth = models.DateField(_("date of birth"))
    gender = models.CharField(_("gender"), max_length=1, choices=GenderChoices.choices)
    
    class Meta:
        """Meta definition for Person."""

        verbose_name = 'Person'
        verbose_name_plural = 'Persons'
    
    @property
    def full_name(self) -> str:
        return f'{self.first_name.title()} {self.last_name.title()}'
    
    def __str__(self):
        """Unicode representation of Person."""
        return self.full_name.upper()


    def get_absolute_url(self):
        """Return absolute url for Person."""
        return reverse('persons:person', kwargs={"pk": self.pk})

    # TODO: Define custom methods here
    