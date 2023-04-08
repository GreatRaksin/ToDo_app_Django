from django.db import models
from PIL import Image

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    file = models.FileField(blank=True, null=True, upload_to='users_feedback')
    created_date = models.DateTimeField(auto_now_add=True)
    checked = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_date']

    '''def save(self, *args, **kwargs):
        super().save()
        file = Image.open(self.file.path)  # открываем файл по пути
        if file.height > 300 or file.width > 300:
            new_file = (300, 300)
            file.thumbnail(new_file)
            file.save(self.file.path)'''

    def __str__(self):
        return f'{self.name} - {self.subject}'
