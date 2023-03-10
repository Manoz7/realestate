from django.db import models


# Contact Model
class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=20)
    subject = models.CharField(max_length=100)
    message = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name} : {self.subject}"

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'
