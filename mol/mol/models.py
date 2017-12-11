from django.db import models
from django.utils.translation import ugettext_lazy as _


class CompoundManager(models.Manager):

    def get_with_same_components(self, ):
        pass


class Compound(models.Model):
    # replace None with field definitions
    smiles = None
    components = None
    created_at = models.DateTimeField(
        _("created at"),
        auto_now_add=True,
        )
    objects = CompoundManager()

    def __unicode__(self):
        return self.smiles


class ComponentRelation(models.Model):
    # replace None with field definitions
    parent = None
    component = None
    multiplicity = None
