from .models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token
from django.db.models.signals import post_save, pre_save, post_delete
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.mail import send_mail


@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    print ("error")
    if created:
        Token.objects.create(user=instance)

@receiver(post_save, sender=User)
def send_welcome_email(sender, instance, created, **kwargs):

    if created:
        # Отправить приветственное письмо новому пользователю
        subject = "Welcome to our website!"
        message = "Hi {},\n\nWelcome to our website! We hope you enjoy your stay.\n\nSincerely,\nThe Website Team".format(instance.username)
        send_mail(subject, message, from_email='your_email@example.com', to=[instance.email])


@receiver(pre_save, sender=User)
def validate_username(sender, instance, **kwargs):

    if not instance.username:
        raise ValidationError("Имя пользователя не может быть пустым")
    

@receiver(post_delete, sender=User)
def delete_user_profile(sender, instance, **kwargs):

    # Удалить профиль пользователя
    pass