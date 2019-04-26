from django.db import models

from django.db.models.signals import post_save
from django.dispatch import receiver

from authentication.models import User
from phonenumber_field.modelfields import PhoneNumberField


class Profile(models.Model):
    SEXUAL_ORIENTATION = (
        ('Heterosexual', 'Heterosexual'),
        ('Homosexual', 'Homosexual'),
        ('Lesbian', 'Lesbian'),
        ('Bisexual', 'Bisexual'),
        ('Pansexual', 'Pansexual'),
        ('Other', 'Other')

    )
    GENDER = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('T', 'Transgender'),
        ('Other', 'Other'),
        ('Non-Binary', 'Non-Binary')
    )

    ETHNICITY = (
        ('Latin', 'Latin'),
        ('Caucasian', 'Caucasian'),
        ('Black', 'Black'),
        ('White', 'White'),
        ('Middle East', 'Middle East'),
        ('Asian', 'Asian'),
        ('Indian', 'Indian'),
        ('Arabian', 'Arabian'),
        ('Aborgine', 'Aborgine'),
        ('Native American', 'Native American'),
        ('Other', 'Other')
    )
    HAIR_COLOR = (
        ('Black', 'Black'),
        ('Blonde', 'Blonde'),
        ('Brown', 'Brown'),
        ('Brunette', 'Brunette'),
        ('Chestnut', 'Chestnut'),
        ('Auburn', 'Auburn'),
        ('Dark-blonde', 'Dark-blonde'),
        ('Golden', 'Golden'),
        ('Red', 'Red'),
        ('Grey', 'Grey'),
        ('Silver', 'Silver'),
        ('White', 'White'),
        ('Other', 'Other')
    )

    HAIR_LENGTH = (
        ('Bald', 'Bald'),
        ('Short', 'Short'),
        ('Shoulder', 'Shoulder'),
        ('Long', 'Long'),
        ('Very Long', 'Very Long')
    )

    BUST_SIZE = (
        ('VS', 'Very Small'),
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('VL', 'Very Large'),
        ('E+','Enormous')
    )

    LOOKS = (
        ('Nothing Special', 'Nothing Special'),
        ('Average', 'Average'),
        ('Sexy', 'Sexy'),
        ('Ultra Sexy', 'Ultra Sexy')
    )

    BUILD = (
        ('Skinny', 'Skinny'),
        ('Slim', 'Slim'),
        ('Regular', 'Regular'),
        ('Curvy', 'Curvy'),
        ('Fat', 'Fat')
    )

    FLUENCY = (
        ('Minimal', 'Minimal'),
        ('Conversational', 'Conversational'),
        ('Fluent', 'Fluent')
    )

   
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=100)
    dob = models.DateField(default=None, blank=True, null=True)
    phone = PhoneNumberField()
    website = models.URLField(max_length=250, null=True)
    image = models.URLField(max_length=250, null=True)
    country = models.CharField(max_length=100, null=False)
    County = models.CharField(max_length=100)
    City = models.CharField(max_length=100, null=True)
    Estate = models.CharField(max_length=100, null=True)
    bio = models.TextField(max_length=500, default='Update your bio')
    extra_service = models.TextField(max_length=200, blank=True, null=True)
    gender = models.CharField(max_length=20, choices=GENDER)
    sexual_orientation = models.CharField(max_length=20, choices=SEXUAL_ORIENTATION)
    ethnicity = models.CharField(max_length = 20, choices=ETHNICITY)
    hair_color = models.CharField(max_length=20, choices=HAIR_COLOR)
    hair_length = models.CharField(max_length=20, choices=HAIR_LENGTH)
    bust_size = models.CharField(max_length=2, choices=BUST_SIZE)
    build = models.CharField(max_length=20, choices=BUILD)
    looks = models.CharField(max_length=20, choices=LOOKS)
    incall = models.BooleanField(default=False)
    outcall = models.BooleanField(default=False)
    smoker = models.BooleanField(default=False)
    education_level = models.CharField(max_length=100)
    hobbies = models.CharField(max_length=200)
    services = models.TextField()
    language_1 = models.CharField(max_length=100)
    language_2 = models.CharField(max_length=100)
    language_3 = models.CharField(max_length=100)
    language_1_fluency = models.CharField(max_length=20, choices=FLUENCY)
    language_2_fluency = models.CharField(max_length=20, choices=FLUENCY)
    language_3_fluency = models.CharField(max_length=20, choices=FLUENCY)


@receiver(post_save, sender=User)
def create_save_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        instance.profile.save()


class Image(models.Model):
    user = models.ForeignKey(User, related_name="images", on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, related_name="profile_images", on_delete=models.CASCADE, default=1)
    image_url = models.URLField(max_length=250, null=True)

class Video(models.Model):
    user = models.ForeignKey(User, related_name="videos", on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, related_name="profile_videos", on_delete=models.CASCADE, default=1)
    video_url = models.URLField(max_length=250, null=True)

class Review(models.Model):
    user = models.ForeignKey(User, related_name="reviewer", on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, related_name="reviews", on_delete=models.CASCADE)
    review = models.TextField()
    rating = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)