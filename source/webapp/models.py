from django.db import models

# Create your models here.
STATUS_CHOICES = [('new', 'Новая'), ('in_progress', 'В процессе'), ('done', 'Сделано')]


class Task(models.Model):
    task_name = models.CharField(max_length=50, null=False, verbose_name="Названия задачи")
    description = models.TextField(max_length=3000, null=False, verbose_name="Описание")
    status = models.CharField(max_length=60, null=False, verbose_name="Статус", default=STATUS_CHOICES,
                              choices=STATUS_CHOICES)
    created_at = models.DateField(null=True, blank=True, verbose_name="Дата создания")


    def __str__(self):
        return f"{self.id}. {self.description}: {self.status}"

    class Meta:
        db_table = "tasks"
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"
