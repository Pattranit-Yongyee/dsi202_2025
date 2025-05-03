
# Create your models here.
from django.db import models
from django.contrib.auth.models import User
import datetime

class CampCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Camp(models.Model):
    STATUS_CHOICES = [('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')]
    camp_name = models.CharField(max_length=200, verbose_name="ชื่อแคมป์")
    detail_camp = models.TextField(verbose_name="รายละเอียดแคมป์")
    duration_days = models.PositiveIntegerField(verbose_name="จำนวนวัน", blank=True, null=True)
    duration_year = models.PositiveIntegerField(verbose_name="ปี", blank=True, null=True)
    seats = models.PositiveIntegerField(verbose_name="จำนวนที่นั่ง", blank=True, null=True)
    time_range = models.CharField(max_length=50, verbose_name="ช่วงเวลา", blank=True, null=True)
    start_date = models.DateField(verbose_name="วันที่เริ่ม", default=datetime.date.today)
    organizer_name = models.CharField(max_length=100, verbose_name="ชื่อผู้จัด", blank=True, null=True)
    email = models.EmailField(verbose_name="อีเมล", blank=True, null=True)
    phone_num = models.CharField(max_length=20, verbose_name="เบอร์โทร", blank=True, null=True)
    place = models.CharField(max_length=200, verbose_name="สถานที่", blank=True, null=True)
    ig = models.URLField(verbose_name="Instagram", blank=True, null=True)
    facebook = models.URLField(verbose_name="Facebook", blank=True, null=True)
    line = models.CharField(max_length=50, verbose_name="Line ID", blank=True, null=True)
    detail_activity = models.TextField(verbose_name="รายละเอียดกิจกรรม", blank=True, null=True)
    poster = models.ImageField(upload_to='posters/', verbose_name="โปสเตอร์", blank=True, null=True)
    category = models.ForeignKey(CampCategory, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="หมวดหมู่")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending', verbose_name="สถานะ")
    submit = models.DateTimeField(auto_now_add=True, verbose_name="วันที่ส่ง")

    def __str__(self):
        return self.camp_name

    def clean(self):
        from django.core.exceptions import ValidationError
        today = datetime.date.today()
        if self.start_date and self.start_date < today:
            raise ValidationError({'start_date': 'วันที่เริ่มต้องเป็นวันที่ในอนาคต'})
        if self.duration_year and self.duration_year < datetime.date.today().year:
            raise ValidationError({'duration_year': 'ปีต้องเป็นปีในอนาคต'})

    def __str__(self):
        return self.camp_name

class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=100)
    major = models.CharField(max_length=100, blank=True)
    grade = models.CharField(max_length=10, blank=True)
    hobby = models.CharField(max_length=200, blank=True)
    interest = models.CharField(max_length=200, blank=True)
    saved_camps = models.ManyToManyField(Camp, blank=True)

    def __str__(self):
        return self.username