from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _



class ModelSearchConfig(AppConfig):
    name = 'sw_modelclone'
    verbose_name = _("Model Clone")


default_app_config = 'sw_modelclone.ModelSearchConfig'

