# apps/customers/models.py
from django.db import models
from django.urls import reverse
from django.utils.text import slugify

# Class for Customer model.
class Customer(models.Model):
    first_name = models.CharField('First Name', max_length=50)
    last_name = models.CharField('Last Name', max_length=50)
    email = models.EmailField('Email Address', unique=True)
    country = models.CharField('Country', max_length=50, blank=True, null=True)
    city = models.CharField('City', max_length=50, blank=True, null=True)
    phone_number = models.CharField('Phone Number', max_length=15, blank=True, null=True)
    address = models.TextField('Address', blank=True, null=True)
    slug = models.SlugField('Slug', unique=True, blank=True, editable=False)
    
    created_at = models.DateTimeField('Created At', auto_now_add=True)
    updated_at = models.DateTimeField('Updated At', auto_now=True)

    class Meta:
        ordering = ['last_name', 'first_name']
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'

    @property
    def full_name(self) -> str:
        """Returns the full name of the customer. (Python 3.9+ type hint)"""
        return f"{self.first_name} {self.last_name}"
    
    def __str__(self) -> str:
        return self.full_name

    def get_absolute_url(self) -> str:
        """Returns the canonical URL for a customer instance."""
        return reverse('customers:detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs) -> None:
        """
        Overrides the save method to generate a unique slug before saving.
        This method performs only one database hit on creation.
        """
        if not self.slug:
            base_slug = slugify(self.full_name)
            slug = base_slug
            counter = 1
            while Customer.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        
        super().save(*args, **kwargs)