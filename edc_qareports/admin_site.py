from edc_model_admin.admin_site import EdcAdminSite

from .apps import AppConfig

edc_qareports_admin = EdcAdminSite(name="edc_qareports_admin", app_label=AppConfig.name)
