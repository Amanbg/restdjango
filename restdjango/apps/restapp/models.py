from __future__ import unicode_literals

from django.db import models
from django.core import validators
from django.utils.translation import ugettext_lazy as _


# Create your models here.
class Recruiter(models.Model):
    username = models.CharField(
        max_length=20,
        unique=True,
        help_text=_('Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[
            validators.RegexValidator(
                r'^[\w.@+-]+$',
                _('Enter a valid username. This value may contain only '
                  'letters, numbers ' 'and @/./+/-/_ characters.')
            ),
        ],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    MALE = 'Male'
    FEMALE = 'Female'
    GENDER = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    )
    gender = models.CharField(max_length=6, choices=GENDER, default='Male')
    contact = models.CharField(
        max_length=10,
        help_text=_('Must contain10 digits only'))
    email_id = models.EmailField(max_length=40)
    company_name = models.CharField(max_length=60)
    date_joined = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.company_name


class Jobs(models.Model):
    # recruiter = models.ForeignKey(Recruiter, related_name='job_post')
    company = models.ForeignKey(Recruiter, related_name='company')
    jobtitle = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    exp_required = models.IntegerField(default=0)
    salary = models.IntegerField(default=500000, error_messages={
        'salary': _("Only Digits allowed")
        })
    created_on = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.jobtitle + " " + self.company


class Candidate(models.Model):
    username = models.CharField(
        max_length=20,
        unique=True,
        help_text=_('Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[
            validators.RegexValidator(
                r'^[\w.@+-]+$',
                _('Enter a valid username. This value may contain only '
                  'letters, numbers ' 'and @/./+/-/_ characters.')
            ),
        ],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    contact = models.CharField(
        max_length=10,
        help_text=_('Must contain10 digits only'))
    email_id = models.EmailField(max_length=40)
    apply_on = models.DateTimeField(auto_now_add=True)
    apply_for = models.ForeignKey(Jobs, related_name='apply_for')
    recruiter = models.ForeignKey(Recruiter, related_name='recruiting')

    def __unicode__(self):
        return self.first_name + " " + self.last_name
