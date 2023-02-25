from django.db import models
from django.contrib.auth import get_user_model
from tinymce import models as tinymce_models


User = get_user_model()


class Priority(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=200)
    deadline_date = models.DateField(null=True, blank=True,
                                    db_index=True)
    deadline_time = models.TimeField(null=True, blank=True)
    content = tinymce_models.HTMLField(max_length=7000)
    status = models.BooleanField(default=False)
    priority = models.ForeignKey(Priority, on_delete=models.CASCADE,
                                 default=None)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE,
                                default=None)
    class Meta:
        verbose_name = 'Задачу'
        verbose_name_plural = 'Задачи'

    def __str__(self):
        return self.title



