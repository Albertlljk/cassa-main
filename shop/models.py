from django.db import models
from django.urls import reverse

class Product(models.Model):
    category = models.ForeignKey(
        'Category', 
        related_name='products', 
        on_delete=models.CASCADE,  
        verbose_name="Категория"
    )
    name = models.CharField(
        max_length=200, 
        db_index=True, 
        verbose_name="Название продукта"
    )
    slug = models.SlugField(
        max_length=200, 
        db_index=True,  
        unique=True, 
        verbose_name="Slug"
    )
    description = models.TextField(
        blank=True,  
        verbose_name="Описание продукта"
    )
    price = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        verbose_name="Цена"
    )
    available = models.BooleanField(
        default=True,  
        verbose_name="В наличии"
    )
    is_popular = models.BooleanField(
        default=False,  
        verbose_name="Популярный"
    )
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    stock = models.PositiveIntegerField(db_default=0)

    created_at = models.DateTimeField(
        auto_now_add=True, 
        verbose_name="Дата создания"
    )
    updated_at = models.DateTimeField(
        auto_now=True,  
        verbose_name="Дата обновления"
    )

    class Meta:
        ordering = ['name']  
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
       
        indexes = [
            models.Index(fields=['id']),   
            models.Index(fields=['slug']) 
        ]

    def __str__(self):
        return self.name
    
    def get_adsolute_url(self):
        return reversed(viewname='shop:product_detail',
                        args=[self.id,self.slug])
    

class Category(models.Model):
    name = models.CharField(
        max_length=200,  
        db_index=True,    
        verbose_name="Название категории"
    )
    slug = models.SlugField(
        max_length=200,  
        db_index=True,    
        unique=True,    
        verbose_name="Slug категории"
    )

    class Meta:
        ordering = ['name']  
        verbose_name = "Категория"
        verbose_name_plural = "Категории" 
                     

    def __str__(self):
        return self.name
    
    def get_adsolute_url(self):
        return reverse(viewname="shop:product_detail",
                       args=[self.id, self.slug])