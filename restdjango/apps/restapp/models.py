from __future__ import unicode_literals

from django.db import models
from django.core import validators


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
    gender = models.CharField(max_length=12)
    contact = models.CharField(max_length=10)
    email_id = models.EmailField(max_length=40)
    date_joined = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.first_name + self.last_name


class Jobs(models.Model):
    recruiter = models.ForeignKey(Recruiter, related_name='job-post')
    jobtitle = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    job_posted_on = models.DateTimeField(auto_now_add=True)
    exp_required = models.IntegerField(default=0)
    salary = models.IntegerField(default=500000, error_messages={
        'salary': _("Only Digits allowed")
        })

    def __unicode__(self):
        return self.jobtitle
