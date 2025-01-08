# from django.db import models
# from django.contrib.auth.models import AbstractUser, Group, Permission
# # Create your models here.

# class User(AbstractUser):
#     email = models.EmailField(unique=True)
#     groups = models.ManyToManyField(
#         Group,
#         related_name="custom_user_groups",
#         blank=True,
#         help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
#         verbose_name="groups",
#     )
#     user_permissions = models.ManyToManyField(
#         Permission,
#         related_name="custom_user_permissions",
#         blank=True,
#         help_text="Specific permissions for this user.",
#         verbose_name="user permissions",
#     )

#     REQUIRED_FIELDS = ['email']
#     USERNAME_FIELD = 'username'

#     def __str__(self):
#         return self.username



