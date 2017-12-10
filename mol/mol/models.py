from django.db import models
from django.utils.translation import ugettext_lazy as _


class CompoundManager(models.Manager):

    def get_with_same_components(self, ):


class Compound(models.Model):
    smiles =
    components =
    created_at = models.DateTimeField(
        _("created at"),
        auto_now_add=True,
        )
    objects = CompoundManager()

    def __unicode__(self):
        return self.smiles


class ComponentRelation(models.Model):
    parent =
    component =
    multiplicity =
