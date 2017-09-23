from __future__ import unicode_literals

from django.db import models
class CourseManager(models.Manager):
    def validate(self, post_data):
        errors = []
        if len(post_data['name']) < 5:
            errors.append("Name field must be 5 characters or more")
        if len(post_data['desc']) < 15:
            errors.append("Description field must be 15 characters or more")
        return errors
class Course(models.Model):
    name=models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    desc=models.TextField(max_length=1000)
    objects = CourseManager()

# Create your models here.
