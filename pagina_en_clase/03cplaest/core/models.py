from django.db import models

from django.contrib.auth.models import User

from datetime import timedelta
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

#### GRANT GOAL ####
STATE_CHOICES = (
    ('Done', 'DN'),
    ('Doing', 'DG'),
    ('Not Stared', 'NS'),
)
class GrantGoal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    gg_title = models.CharField(max_length=128, default="Generic Grant Goal Title")
    description = models.CharField(max_length=256, default="Generic Grant Goal Description")
    timestamp = models.DateField(auto_now_add=True)
    days_duration = models.IntegerField(default=7)
    final_date = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)
    status = models.BooleanField(default=True)
    state = models.CharField(max_length=16, choices=STATE_CHOICES)
    sprint = models.IntegerField(default=1)
    slug = models.SlugField(max_length=16)

    def __str__(self):
        return self.gg_title



# ## SIGNALS 
# ### post_save
@receiver(post_save, sender=GrantGoal)
def end_time_grantgoal(sender, instance, **kwargs):
    if instance.final_date is None or instance.final_date=='':
        instance.final_date = instance.timestamp + timedelta(days=instance.days_duration)
        instance.save()


# @receiver(post_save, sender=GrantGoal)
# def end_time_grantgoal(sender, instance, **kwargs):
#     if instance.final_date is None or instance.final_date=='':
#         instance.final_date = instance.timestamp + timedelta(days=instance.days_duration)
#         instance.save()




#### GOALS ####


#### SUBGOALS ####


#### ISSUES ####
