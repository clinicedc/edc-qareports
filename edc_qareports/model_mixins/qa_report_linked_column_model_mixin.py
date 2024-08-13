from django.apps import apps as django_apps
from django.db import models
from edc_constants.constants import FEEDBACK, NEW
from edc_model.models import BaseUuidModel
from edc_sites.model_mixins import SiteModelMixin
from edc_utils import get_utcnow

from edc_qareports.choices import QA_REPORT_LINKED_COLUMN_STATUSES


class QaReportWithLinkedColumnModelMixin(SiteModelMixin, BaseUuidModel):
    """Model mixin to link form to a data query report, such as,
    unmanaged views.

    See also, QaReportWithLinkedColumnModelAdminMixin
    """

    report_model = models.CharField(max_length=150)

    report_datetime = models.DateTimeField(default=get_utcnow)

    note = models.TextField(null=True, blank=True)

    status = models.CharField(
        max_length=25, default=NEW, choices=QA_REPORT_LINKED_COLUMN_STATUSES
    )

    def save(self, *args, **kwargs):
        if self.status == NEW:
            self.status = FEEDBACK
        super().save(*args, **kwargs)

    @property
    def report_model_cls(self):
        return django_apps.get_model(self.report_model)

    class Meta:
        abstract = True
