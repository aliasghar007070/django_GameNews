from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.core.validators import MinValueValidator,MaxValueValidator

# Create your models here.


class category(models.Model):
    title = models.CharField(max_length=300, verbose_name="عنوان دسته بندی")
    url_title = models.CharField(max_length=300)


    def __str__(self):
        return self.title


class content(models.Model):
    title = models.CharField(max_length=100, verbose_name='عنوان')
    category = models.ForeignKey(category, on_delete=models.CASCADE)
    picture = models.ImageField(default=None, upload_to='static/images', verbose_name='تصویر')
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)], default=50, verbose_name='امتیاز')
    short_description = models.TextField(max_length=500)
    long_description = models.TextField(max_length=5000)
    slug = models.SlugField(default="", null=False, db_index=True, blank=True)
    is_active = models.BooleanField(default=False, verbose_name='نمایش')

    def get_absolute_url(self):
        return reverse('detail-news-page', args=[self.slug])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
