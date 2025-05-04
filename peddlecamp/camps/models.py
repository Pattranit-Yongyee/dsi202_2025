from django.db import models
from django.utils import timezone

# Create your models here.

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
        ('Digital IT', 'ดิจิตอล ไอที')
    ]
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    participants = models.CharField(max_length=50)
    location = models.CharField(max_length=200)
    fee = models.CharField(max_length=50)
    image = models.ImageField(upload_to='camp_images/', blank=True, null=True)
    
    # ใช้ DateField หรือ DateTimeField
    application_deadline = models.DateField(null=True, blank=True)  # หรือ DateTimeField
    camp_start_date = models.DateField(null=True, blank=True)  # หรือ DateTimeField
    camp_end_date = models.DateField(null=True, blank=True)  # หรือ DateTimeField
    organizer = models.CharField(max_length=200, null=True, blank=True)
    contact_info = models.TextField(null=True, blank=True)
    mode = models.CharField(max_length=10, choices=MODE_CHOICES)

    def __str__(self):
        return self.title