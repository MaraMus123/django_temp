from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Images(models.Model):
    """
    Model to store images.
    """
    image = models.ImageField(upload_to='images/')
    description = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        verbose_name = _("Image")
        verbose_name_plural = _("Images")

    def __str__(self):
        return self.description if self.description else str(self.image)
