from django.db import models


class NetworkNode(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    house_number = models.CharField(max_length=10)
    supplier = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    debt = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    creation_time = models.DateTimeField(auto_now_add=True)
    level = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        if self.supplier:
            if self.supplier.supplier is None:
                self.level = 1
            else:
                self.level = self.supplier.level + 1
        super(NetworkNode, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} - {self.country}, {self.city}"


class Product(models.Model):
    name = models.CharField(max_length=100)
    model = models.CharField(max_length=50)
    release_date = models.DateField()
    node = models.ForeignKey(NetworkNode, related_name='products', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.model}"
