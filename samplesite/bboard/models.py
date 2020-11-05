from django.db import models

class Bb(models.Model):
    title = models.CharField(max_length=50, verbose_name='goods')
    content = models.TextField(null=True, blank=True, verbose_name='description')
    price = models.FloatField(null=True, blank=True, verbose_name='price')
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='published')
    rubric = models.ForeignKey('Rubric', null=True, on_delete=models.PROTECT, verbose_name='Rubrica')

    class Meta:
        verbose_name_plural = 'annoncement'
        verbose_name = 'annoncement'
        ordering = ['-published']

class Rubric(models.Model):
    name = models.CharField(max_length=20, db_index=True, verbose_name='Naming')

    class Meta:
        verbose_name_plural = 'rubrics'
        verbose_name = 'rubric'
        ordering = ['name']

    def __str__(self):
        return self.name
