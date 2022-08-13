from django.db import models


class Bb(models.Model):
    title = models.CharField("Товар", max_length=50)
    content = models.TextField("Описание", null=True, blank=True)
    price = models.FloatField("Цена", null=True, blank=True)
    published = models.DateTimeField("Опубликовано", auto_now_add=True, db_index=True)

    class Meta:
        verbose_name_plural = "Объявления"
        verbose_name = "Объявление"
        ordering = ["-published"]
