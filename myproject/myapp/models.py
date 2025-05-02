from django.db import models

class Content(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=150)   # เปลี่ยนจาก TextField เป็น CharField จำกัด 150 ตัวอักษร
    detail = models.TextField(blank=True)            # เพิ่มฟิลด์ใหม่ เก็บข้อความได้ไม่จำกัด (allow empty)
    image = models.ImageField(upload_to='images/',blank=True,null=True)
    type = models.CharField(max_length=50)

    def __str__(self):
        return self.title


