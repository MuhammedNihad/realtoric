import itertools

from django.contrib.auth import get_user_model
from django.db import models
from django.template.defaultfilters import slugify

User = get_user_model()


class SaleStatus(models.TextChoices):
    """
    Sale status of the property.
    """

    FOR_SALE = "For Sale"
    SOLD = "Sold"


class CountChoice(models.TextChoices):
    """
    Integer choices for the number of bedrooms and bathrooms.
    """

    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FOUR_PLUS = "4+"


class CountWithZeroChoice(models.TextChoices):
    """
    Integer choices with zero for the number of car parking.
    """

    ZERO = 0
    ONE = 1
    TWO = 2
    THREE = 3
    THREE_PLUS = "3+"


class TimeStampMixin(models.Model):
    """
    Abstract model class for time stamping.
    """

    listed_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class PropertyBasicDetailMixin(models.Model):
    """
    Abstract model class for common basic property details.
    """

    ad_title = models.CharField(
        max_length=50, help_text="Mention the key features of your property"
    )
    description = models.CharField(
        max_length=128, help_text="Include condition, reason for selling, etc."
    )
    city = models.CharField(max_length=50)
    address = models.CharField(max_length=128)
    google_map = models.URLField(blank=True, verbose_name="Google Maps Link (Optional)")
    contact_info = models.CharField(
        max_length=128,
        blank=True,
        verbose_name="Contact number or email (Optional)",
        help_text="Your default phone number or email will be used if this field is not filled.",
    )
    sale_status = models.CharField(
        max_length=20,
        choices=SaleStatus.choices,
        default=SaleStatus.FOR_SALE,
        verbose_name="Sale Status",
    )
    slug = models.SlugField(unique=True)

    class Meta:
        abstract = True


class Apartment(PropertyBasicDetailMixin, TimeStampMixin):
    """
    Inherited model for listing apartments.
    """

    # Relationships
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="apartments")

    # Features of apartment
    bedroom = models.CharField(
        max_length=20,
        choices=CountChoice.choices,
        default=CountChoice.ONE,
        verbose_name="Bedrooms",
    )
    bathroom = models.CharField(
        max_length=20,
        choices=CountChoice.choices,
        default=CountChoice.ONE,
        verbose_name="Bathrooms",
    )
    area = models.PositiveIntegerField(
        default=0, verbose_name="Area (sqft)"
    )
    floor = models.PositiveSmallIntegerField(default=0, verbose_name="Total Floors")

    class Meta:
        ordering = ["-listed_on"]
        verbose_name = "Apartment"
        verbose_name_plural = "Apartments"

    def __str__(self):
        """
        String representation of the model objects.
        """

        return self.ad_title

    def _generate_slug(self):
        """
        Generate a unique slug for each apartment.
        """

        value = self.ad_title
        slug_candidate = slug_original = slugify(value)
        for i in itertools.count(1):
            if not Apartment.objects.filter(slug=slug_candidate).exists():
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
        Return the absolute url of the apartment.
        """

        return f"/apartment/{self.slug}/"


class ApartmentImage(TimeStampMixin):
    """
    Inherited model for apartment images.
    """

    apartment = models.ForeignKey(
        Apartment, on_delete=models.CASCADE, related_name="apartment_images"
    )
    image = models.ImageField(upload_to="uploads/apartments/%Y/%m/")

    class Meta:
        ordering = ["-listed_on"]
        verbose_name = "Apartment Image"
        verbose_name_plural = "Apartment Images"

    def __str__(self):
        """
        String representation of the model objects.
        """

        return f"Images of {self.apartment.ad_title}"

    def get_absolute_url(self):
        """
        Return the absolute url of the apartment image.
        """

        return f"/apartment-image/{self.apartment.slug}/"


class Commercial(PropertyBasicDetailMixin, TimeStampMixin):
    """
    Inherited model for listing commercial properties.
    """

    class CommercialType(models.TextChoices):
        SHOP = "Shop"
        OFFICE = "Office"
        COMPLEX = "Complex"

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="commercials")

    # Features of commercial property
    commercial_type = models.CharField(
        max_length=20,
        choices=CommercialType.choices,
        default=CommercialType.SHOP,
        verbose_name="Commercial Type",
    )
    area = models.PositiveIntegerField(
        default=0, verbose_name="Area (sqft)"
    )
    floor = models.PositiveSmallIntegerField(default=0, verbose_name="Total Floors")

    class Meta:
        ordering = ["-listed_on"]
        verbose_name = "Commercial"
        verbose_name_plural = "Commercials"

    def __str__(self):
        """
        String representation of the model objects.
        """

        return self.ad_title

    def _generate_slug(self):
        """
        Generate a unique slug for each commercial property.
        """

        value = self.ad_title
        slug_candidate = slug_original = slugify(value)
        for i in itertools.count(1):
            if not Commercial.objects.filter(slug=slug_candidate).exists():
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
        Return the absolute url of the commercial.
        """

        return f"/commercial/{self.slug}/"


class CommercialImage(TimeStampMixin):
    """
    Inherited model for commercial images.
    """

    commercial = models.ForeignKey(
        Commercial, on_delete=models.CASCADE, related_name="commercial_images"
    )
    image = models.ImageField(upload_to="uploads/commercials/%Y/%m/")

    class Meta:
        ordering = ["-listed_on"]
        verbose_name = "Commercial Image"
        verbose_name_plural = "Commercial Images"

    def __str__(self):
        """
        String representation of the model objects.
        """

        return f"Images of {self.commercial.ad_title}"

    def get_absolute_url(self):
        """
        Return the absolute url of the commercial image.
        """

        return f"/commercial-image/{self.commercial.slug}/"


class House(PropertyBasicDetailMixin, TimeStampMixin):
    """
    Inherited model for listing houses.
    """

    # Relationships
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="houses")

    # Features of house
    bedroom = models.CharField(
        max_length=20,
        choices=CountChoice.choices,
        default=CountChoice.ONE,
        verbose_name="Bedrooms",
    )
    bathroom = models.CharField(
        max_length=20,
        choices=CountChoice.choices,
        default=CountChoice.ONE,
        verbose_name="Bathrooms",
    )
    area = models.PositiveIntegerField(
        default=0, verbose_name="Area (sqft)"
    )
    floor = models.PositiveSmallIntegerField(default=0, verbose_name="Total Floors")

    class Meta:
        ordering = ["-listed_on"]
        verbose_name = "House"
        verbose_name_plural = "Houses"

    def __str__(self):
        """
        String representation of the model objects.
        """

        return self.ad_title

    def _generate_slug(self):
        """
        Generate a unique slug for each house.
        """

        # max_length = self._meta.get_field("slug").max_length
        value = self.ad_title
        slug_candidate = slug_original = slugify(value)
        for i in itertools.count(1):
            if not House.objects.filter(slug=slug_candidate).exists():
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
        Return the absolute url of the house.
        """

        # return reverse('houses:detail', kwargs={'slug': self.slug})
        return f"/house/{self.slug}/"


class HouseImage(TimeStampMixin):
    """
    Inherited model for house images.
    """

    house = models.ForeignKey(
        House, on_delete=models.CASCADE, related_name="house_images"
    )
    image = models.ImageField(upload_to="uploads/houses/%Y/%m/")

    class Meta:
        ordering = ["-listed_on"]
        verbose_name = "House Image"
        verbose_name_plural = "House Images"

    def __str__(self):
        """
        String representation of the model objects.
        """

        return f"Images of {self.house.ad_title}"

    def get_absolute_url(self):
        """
        Return the absolute url of the house image.
        """

        return f"/house-image/{self.house.slug}/"


class Land(PropertyBasicDetailMixin, TimeStampMixin):
    """
    Inherited model for listing lands.
    """

    class LandType(models.TextChoices):
        RESIDENTIAL = "Residential"
        COMMERCIAL = "Commercial"
        INDUSTRIAL = "Industrial"
        AGRICULTURAL = "Agricultural"
        OTHER = "Other"

    # Relationships
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="lands")

    # Features of land
    land_type = models.CharField(
        max_length=20,
        choices=LandType.choices,
        default=LandType.RESIDENTIAL,
        verbose_name="Land Type",
    )
    plot_area = models.PositiveIntegerField(default=0, verbose_name="Area (cent)")
    length = models.PositiveIntegerField(default=0, verbose_name="Length (ft)")
    breadth = models.PositiveIntegerField(default=0, verbose_name="Breadth (ft)")

    class Meta:
        ordering = ["-listed_on"]
        verbose_name = "Land"
        verbose_name_plural = "Lands"

    def __str__(self):
        """
        String representation of the model objects.
        """

        return self.ad_title

    def _generate_slug(self):
        """
        Generate a unique slug for each land.
        """

        value = self.ad_title
        slug_candidate = slug_original = slugify(value)
        for i in itertools.count(1):
            if not Land.objects.filter(slug=slug_candidate).exists():
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
        Return the absolute url of the land.
        """

        return f"/land/{self.slug}/"


class LandImage(TimeStampMixin):
    """
    Inherited model for land images.
    """

    land = models.ForeignKey(Land, on_delete=models.CASCADE, related_name="land_images")
    image = models.ImageField(upload_to="uploads/lands/%Y/%m/")

    class Meta:
        ordering = ["-listed_on"]
        verbose_name = "Land Image"
        verbose_name_plural = "Land Images"

    def __str__(self):
        """
        String representation of the model objects.
        """

        return f"Images of {self.land.ad_title}"

    def get_absolute_url(self):
        """
        Return the absolute url of the land image.
        """

        return f"/land-image/{self.land.slug}/"


class Villa(PropertyBasicDetailMixin, TimeStampMixin):
    """
    Inherited model for listing villas.
    """

    # Relationships
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="villas")

    # Features of villa
    bedroom = models.CharField(
        max_length=20,
        choices=CountChoice.choices,
        default=CountChoice.ONE,
        verbose_name="Bedrooms",
    )
    bathroom = models.CharField(
        max_length=20,
        choices=CountChoice.choices,
        default=CountChoice.ONE,
        verbose_name="Bathrooms",
    )
    area = models.PositiveIntegerField(
        default=0, verbose_name="Area (sqft)"
    )
    floor = models.PositiveSmallIntegerField(default=0, verbose_name="Total Floors")

    class Meta:
        ordering = ["-listed_on"]
        verbose_name = "Villa"
        verbose_name_plural = "Villas"

    def __str__(self):
        """
        String representation of the model objects.
        """

        return self.ad_title

    def _generate_slug(self):
        """
        Generate a unique slug for each villa.
        """

        value = self.ad_title
        slug_candidate = slug_original = slugify(value)
        for i in itertools.count(1):
            if not Villa.objects.filter(slug=slug_candidate).exists():
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
        Return the absolute url of the villa.
        """

        return f"/villa/{self.slug}/"


class VillaImage(TimeStampMixin):
    """
    Inherited model for villa images.
    """

    villa = models.ForeignKey(
        Villa, on_delete=models.CASCADE, related_name="villa_images"
    )
    image = models.ImageField(upload_to="uploads/villas/%Y/%m/")

    class Meta:
        ordering = ["-listed_on"]
        verbose_name = "Villa Image"
        verbose_name_plural = "Villa Images"

    def __str__(self):
        """
        String representation of the model objects.
        """

        return f"Images of {self.villa.ad_title}"

    def get_absolute_url(self):
        """
        Return the absolute url of the villa image.
        """

        return f"/villa-image/{self.villa.slug}/"
