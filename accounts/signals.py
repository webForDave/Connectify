# core django 
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model

# third party
from username_generator import get_uname

CustomUser = get_user_model()

@receiver(post_save, sender=CustomUser)
def generate_username(sender, instance, created, **kwargs):
    # Generates a random username immediately a user in saved in the database.
    if created:
        generated_username = get_uname(min_size=10, max_size=25, underscores=True)
        user = CustomUser.objects.filter(username=instance.username).first()

        # Checks whether the username field of the user insatnce is empty.
        # If empty assigns a username to the user.
        if user.username == None:
            user.username = generated_username
            user.save()
        elif user.username != None:
            # By defult, django allauth assigns the email as the username. 
            # The username becomes 'user<id>' if the email is too long.
            # This changes the username if it contains the word 'user'.
            if 'user' in user.username:
                user.username = generated_username
                user.save()
        else:
            user.username = generated_username
            user.save()