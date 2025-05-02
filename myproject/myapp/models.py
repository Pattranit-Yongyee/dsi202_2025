from django.db import models

class Student(models.Model):
    username = models.CharField(max_length=150)
    email = models.EmailField()
    major = models.CharField(max_length=100)
    grade = models.CharField(max_length=10)
    hobby = models.TextField(blank=True, null=True)
    interest = models.TextField(blank=True, null=True)
    save = models.BooleanField(default=False)

    def __str__(self):
        return self.username

class Camp(models.Model):
    name = models.CharField(max_length=150)  # ชื่อผู้จัด
    email = models.EmailField()
    phone_num = models.CharField(max_length=20)
    camp_name = models.CharField(max_length=200)
    detail_camp = models.TextField()
    upload_file = models.FileField(upload_to='camp_uploads/', blank=True, null=True)
    typeof_camp = models.CharField(max_length=100)
    start_date = models.DateField()
    final_date = models.DateField()
    add_detail = models.TextField(blank=True, null=True)
    due_date = models.DateField()
    num_candi = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    candi_proper = models.TextField(blank=True, null=True)
    place = models.CharField(max_length=200)
    ig = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    line = models.CharField(max_length=100, blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    linkcamp = models.URLField(blank=True, null=True)
    organize_camp = models.CharField(max_length=200)
    detail_activity = models.TextField()
    poster = models.ImageField(upload_to='camp_posters/', blank=True, null=True)
    submit = models.BooleanField(default=False)

    def __str__(self):
        return self.camp_name
