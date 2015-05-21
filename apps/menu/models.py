from django.db import models


TEA_KINDS = (
    ("english", "UnitedKingdom_style"),
    ("chinese", "China_style"),
    ("japanese", "Japan_style")
)


class TeaManager(models.Manager):
    def recommended(self):
        """Filter by only recommended menu"""

        return self.filter(is_flavor=True)


    def count_each_kind(self):
        """Return count of tea kinds with dictionary style"""

        result = self.values_list("kind").annotate(
                     count=models.Count("kind"))

        return dict(result)


class Tea(models.Model):
    objects = TeaManager()

    name  = models.CharField("name", max_length=255)
    kind  = models.CharField("kind", max_length=255, choices=TEA_KINDS)
    price = models.IntegerField("price")

    is_recommended = models.BooleanField("recommended_menu", default=False)
