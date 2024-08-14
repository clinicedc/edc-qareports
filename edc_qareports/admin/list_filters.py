from django.contrib.admin import SimpleListFilter
from django.db.models import Count, QuerySet
from edc_constants.constants import FEEDBACK, NEW

from ..choices import NOTE_STATUSES


class NoteStatusListFilter(SimpleListFilter):
    title = "QA Status"
    parameter_name = "note_status"

    note_model_cls = None

    def __init__(self, request, params, model, model_admin):
        self.note_model_cls = model_admin.note_model_cls
        super().__init__(request, params, model, model_admin)

    def lookups(self, request, model_admin):
        status_dict = {tpl[0]: tpl[1] for tpl in NOTE_STATUSES}
        names = [(NEW, status_dict[NEW])]
        qs = (
            self.note_model_cls.objects.values("status")
            .order_by("status")
            .annotate(cnt=Count("status"))
        )

        for obj in qs:
            names.append((f"{obj.get('status')}", status_dict[obj.get("status")]))
        return tuple(names)

    @staticmethod
    def report_model(queryset: QuerySet) -> str:
        qs = (
            queryset.values("report_model")
            .order_by("report_model")
            .annotate(cnt=Count("report_model"))
        )
        for obj in qs:
            return obj.get("report_model")

    def queryset(self, request, queryset):
        if self.value() and self.value() != "none":
            if report_model := self.report_model(queryset):
                if self.value() == FEEDBACK:
                    qs = self.note_model_cls.objects.values("subject_identifier").filter(
                        report_model=report_model, status=FEEDBACK
                    )
                    queryset = queryset.filter(
                        subject_identifier__in=[obj.get("subject_identifier") for obj in qs]
                    )
                elif self.value() == NEW:
                    qs = self.note_model_cls.objects.values("subject_identifier").filter(
                        report_model=report_model,
                        status=FEEDBACK,
                    )
                    queryset = queryset.exclude(
                        subject_identifier__in=[obj.get("subject_identifier") for obj in qs]
                    )
        return queryset
