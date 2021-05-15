from django.core.exceptions import ValidationError
from django.db import models

# Create your models here.
from django.db import models


class BaseModel(models.Model):
    id = models.AutoField(primary_key=True)

    class Meta:
        abstract = True  # specify this model as an Abstract Model
        app_label = 'compliance'


def validate_only_one_instance(obj):
    model = obj.__class__
    if (model.objects.count() > 0 and
            obj.pk != model.objects.get().pk):
        raise ValidationError("Can only create 1 %s instance" % model.__name__)


class Imprint(BaseModel):
    url = models.TextField()

    def clean(self):
        validate_only_one_instance(self)

    def __str__(self):
        return "Redirect to {}".format(repr(self.url))


class PrivacyPolicy(BaseModel):
    url = models.TextField()

    def clean(self):
        validate_only_one_instance(self)

    def __str__(self):
        return "Redirect to {}".format(repr(self.url))
