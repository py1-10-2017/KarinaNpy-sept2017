from __future__ import unicode_literals
import re
import bcrypt
from django.db import models

email_reg = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
name_reg = re.compile(r'^[a-zA-Z]\w+$')

# Create your models here.

class UserManager(models.Manager):
    def validate_login(self, post_data):
        errors = []
        if len(self.filter(email=post_data['email'])) > 0:
            user = self.filter(email = post_data['email'])[0]
            if not bcrypt.checkpw(post_data['password'].encode(), user.password.encode()):
                errors.append("incorrect email or password")
        else:
            errors.append("incorrect email or password")

        if errors:
            return errors
        return user

    def validate_registration(self, post_data):
        errors = []

        if len(post_data['first_name']) < 2 or len(post_data['last_name']) < 2:
            errors.append("name fields must have at least 3 characters")

        if not re.match(name_reg, post_data['first_name']) or not re.match(name_reg, post_data['last_name']):
            errors.append("name fields must be letter characters only")

        if len(User.objects.filter(email = post_data['email'])) > 0:
            errors.append("email belongs to a registered user")

        if not re.match(email_reg, post_data['email']):
            errors.append("invalid email format")

        if len(post_data['password']) < 8:
            errors.append("password must be at least 8 characters")

        if post_data['password'] != post_data['confirm_pw']:
            errors.append("passwords must match")

        if not errors:
            hashed = bcrypt.hashpw((post_data['password'].encode()), bcrypt.gensalt(5))

            new_user = self.create(
                first_name = post_data['first_name'],
                last_name = post_data['last_name'],
                email = post_data['email'],
                password = hashed
            )
            return new_user
        return errors


class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique = True)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    objects = UserManager()