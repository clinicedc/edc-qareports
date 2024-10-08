from django.db import models


class OnStudyMissingValuesModelMixin(models.Model):
    original_id = models.UUIDField(null=True)

    label_lower = models.CharField(max_length=150, null=True)

    subject_visit_id = models.UUIDField(null=True)

    report_datetime = models.DateTimeField(null=True)

    label = models.CharField(max_length=50, null=True)

    visit_code = models.CharField(max_length=25, null=True)

    visit_code_sequence = models.IntegerField(null=True)

    schedule_name = models.CharField(max_length=25, null=True)

    modified = models.DateTimeField(null=True)

    class Meta:
        abstract = True
