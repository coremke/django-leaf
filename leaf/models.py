import six

from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

PAGE_MODEL_CLASSES = []


class PageBase(models.base.ModelBase):

    """Automatiacally egister page models.

    This class is meant to be used as a __metaclass__:

    .. code-block:: python
        class Page(metaclass=Page):

    """

    def __init__(cls, name, bases, dct):
        super(PageBase, cls).__init__(name, bases, dct)

        if cls._deferred:
            return

        if not cls._meta.abstract:
            if not getattr(cls, 'identifier', None):
                cls.identifier = '{}.{}'.format(cls._meta.app_label, cls._meta.model_name)

            PAGE_MODEL_CLASSES.append(cls)


class Page(six.with_metaclass(PageBase, models.Model)):

    """Abstract base model for all leaf pages."""

    node = models.OneToOneField('PageNode', related_name='+')

    class Meta:
        abstract = True


class PageNode(MPTTModel):

    """Basic page node for all leaf pages."""

    slug = models.SlugField(max_length=50, unique=True)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True)
    template = models.CharField(max_length=255, blank=True)
    path = models.CharField(max_length=255, blank=True, db_index=True)

    class MPTTMeta:
        order_insertion_by = ['slug']

    class Meta:
        unique_together = ('slug', 'parent')
        verbose_name = "page"

    def __unicode__(self):
        return self.slug

    def save(self, *args, **kwargs):
        if self.parent:
            self.path = '{}/{}'.format(self.parent.path, self.slug)
        else:
            self.path = self.slug

        super(PageNode, self).save(*args, **kwargs)

        for c in self.get_children():
            c.save()
