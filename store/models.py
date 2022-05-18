from django.db import models
from django.urls import reverse

from shop.settings import AUTH_USER_MODEL

# Create your models here.


"""
ProductApp  
    -Nom
    -Prix
    -La Quantite en stock
    -Description
    -Image
"""
class ProductApp(models.Model):
    name = models.CharField(max_length=128)
    slug = models.SlugField(max_length=128)
    price = models.FloatField(default=0.0)
    stock = models.IntegerField(default=0)
    description = models.TextField(blank=True)
    thumbnail = models.ImageField(upload_to="products", blank= True, null= True)
    
    def __str__(self):
        return f"{self.name} ({self.stock})"
    
    def get_absolute_url(self):
        return reverse("product", kwargs={"slug": self.slug})
    
# Article (Order)
"""
- Utilisateur
- Produit
- Quantite
- Commandé ou non
"""   
class Order(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete= models.CASCADE)
    product = models.ForeignKey(ProductApp, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    ordered = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.product.name}({self.quantity})"
        
# Panier (Cart)
"""
- Utilisateur
- Articles
- Commandé ou non
- Date de la commande
"""
class Cart(models.Model):
    user = models.OneToOneField(AUTH_USER_MODEL, on_delete=models.CASCADE)
    orders = models.ManyToManyField(Order)
    ordered = models.BooleanField(default=False)
    ordered_date = models.DateTimeField(blank=True, null=True)
    
    
    def __str__(self):
        return self.user.username