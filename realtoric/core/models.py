import itertools

from django.conf import settings
from django.db import models
from django.template.defaultfilters import slugify


class TimeStampedModel(models.Model):
    """
    An abstract base class model that provides self-updating ``created`` and ``modified`` fields.
    """

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Property(TimeStampedModel):
    """
    Inherited model for listing properties.
    """

    class PropertyType(models.TextChoices):
        """
        Property type choices.
        """

        HOUSE = "House"
        APARTMENT = "Apartment"
        VILLA = "Villa"
        COMMERCIAL = "Commercial"
        LAND = "Land"

    class SaleStatus(models.TextChoices):
        """
        Sale status choices.
        """

        FOR_SALE = "For Sale"
        SOLD = "Sold"
        # FOR_RENT = 'For Rent'
        # RENTED = 'Rented'

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="posted_by"
    )
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=512)
    image = models.ImageField(
        upload_to="uploads/properties/%Y/%m/", null=True, verbose_name="Image"
    )
    type = models.CharField(
        max_length=50, choices=PropertyType.choices, default=PropertyType.HOUSE
    )
    address = models.TextField(max_length=512)
    city = models.CharField(max_length=255)
    google_maps = models.URLField(
        max_length=512, blank=True, verbose_name="Google maps link (optional)"
    )
    contact_info = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="Contact number or email (optional)",
        help_text="Your default phone number or email will be used if this field is not filled.",
    )
    sale_status = models.CharField(
        max_length=50, choices=SaleStatus.choices, default=SaleStatus.FOR_SALE
    )
    slug = models.SlugField(unique=True)

    class Meta:
        ordering = ["-created"]
        verbose_name = "Property"
        verbose_name_plural = "Properties"

    def __str__(self):
        """
        String representation of the model objects.
        """

        return self.name

    def _generate_slug(self):
        """
        Generate a unique slug for each property.
        """

        # max_length = self._meta.get_field("slug").max_length
        value = self.name
        slug_candidate = slug_original = slugify(value)
        for i in itertools.count(1):
            if not Property.objects.filter(slug=slug_candidate).exists():
                break
            slug_candidate = f"{slug_original}-{i}"
        self.slug = slug_candidate

    def save(self, *args, **kwargs):
        """
        Prevent generating the slug each time you save an existing model,
        detect if it is an update of the model on each call of model's save() method.
        """

        if not self.pk:
            self._generate_slug()
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        """
        Return the absolute url of the property.
        """

        # return reverse('properties:detail', kwargs={'slug': self.slug})
        return f"/property/{self.slug}/"
