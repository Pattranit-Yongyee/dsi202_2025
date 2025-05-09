from django.db import models
from django.contrib.auth.models import User

MODE_CHOICES = [
    ('online', 'ออนไลน์'),
    ('onsite', 'ออนไซต์'),
]

class Camp(models.Model):
    CATEGORY_CHOICES = [
        ('health', 'สายสุขภาพ'),
        ('engineering', 'สายวิศวกรรม'),
        ('architecture', 'สายสถาปัตยกรรม'),
        ('language', 'สายภาษา'),
        ('volunteer', 'ค่ายจิตอาสา'),
        ('digital-it', 'ดิจิตอล ไอที')
    ]
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    participants = models.CharField(max_length=50)
    location = models.CharField(max_length=200)
    fee = models.CharField(max_length=50)
    image = models.ImageField(upload_to='camp_images/', blank=True, null=True)
    application_deadline = models.DateField(null=True, blank=True)
    camp_start_date = models.DateField(null=True, blank=True)
    camp_end_date = models.DateField(null=True, blank=True)
    organizer = models.CharField(max_length=200, null=True, blank=True)
    contact_info = models.TextField(null=True, blank=True)
    mode = models.CharField(max_length=10, choices=MODE_CHOICES)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.title

# ✅ ย้ายออกมานอก Camp
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    grade_level = models.CharField(
        max_length=20,
        choices=[
            ('m1', 'ม.1'), ('m2', 'ม.2'), ('m3', 'ม.3'),
            ('m4', 'ม.4'), ('m5', 'ม.5'), ('m6', 'ม.6'),
            ('other', 'อื่นๆ'),
        ],
        default='other'
    )
    other_grade = models.CharField(max_length=100, blank=True, null=True)
    hobbies = models.TextField(blank=True)
    interests = models.TextField(blank=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"
