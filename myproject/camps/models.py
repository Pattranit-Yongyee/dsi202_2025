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

class StudentProfile(models.Model):
    EDUCATION_LEVELS = [
        ('M1', 'มัธยมศึกษาปีที่ 1'),
        ('M2', 'มัธยมศึกษาปีที่ 2'),
        ('M3', 'มัธยมศึกษาปีที่ 3'),
        ('M4', 'มัธยมศึกษาปีที่ 4'),
        ('M5', 'มัธยมศึกษาปีที่ 5'),
        ('M6', 'มัธยมศึกษาปีที่ 6'),
        ('VOCATIONAL', 'อาชีวศึกษา'),
        ('UNIVERSITY', 'มหาวิทยาลัย'),
        ('OTHER', 'อื่น ๆ'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student_profile')
    education_level = models.CharField(max_length=20, choices=EDUCATION_LEVELS, blank=True)
    hobbies = models.TextField(blank=True)
    interests = models.TextField(blank=True)

    def __str__(self):
        return f"{self.user.email}'s Profile"