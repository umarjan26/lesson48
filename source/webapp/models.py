from django.db import models

# Create your models here.

CATEGORY_CHOICES = [('other', 'other'), ('fruits', 'fruits'), ('milk', 'milk'), ('chocolate', 'chocolate'),
                    ('coffee', 'coffee')]


class Good(models.Model):
    description = models.CharField(max_length=100, null=False, blank=False, verbose_name='description')
    detailed_description = models.TextField(max_length=2000, null=True, blank=True, verbose_name='detailed_description')
    category = models.CharField(max_length=15, default='other', choices=CATEGORY_CHOICES, null=False)
    remainder = models.IntegerField()
    price = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return f"{self.pk}. {self.description}: {self.category}"

    class Meta:
        db_table = 'Goods'
        verbose_name = 'товар'
        verbose_name_plural = 'товары'

