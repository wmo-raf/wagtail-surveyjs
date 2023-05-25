from django.db import models
from django.urls import reverse
from wagtail.contrib.forms.models import AbstractFormSubmission
from wagtail.contrib.modeladmin.helpers import AdminURLHelper
from wagtail.contrib.settings.models import BaseSiteSetting
from wagtail.contrib.settings.registry import register_setting
from wagtail.models import Page
from django.utils.translation import gettext as _


@register_setting
class SurveySettings(BaseSiteSetting):
    has_license = models.BooleanField(default=False, verbose_name=_("Has Survey JS Licence"),
                                      help_text=_("Only check if you have purchased a SurveyJS License"))


class SurveyFormSubmission(AbstractFormSubmission):
    pass


class AbstractSurveyJsFormPage(Page):
    json = models.TextField(blank=True, default="")

    class Meta(object):
        abstract = True

    def get_survey_creator_url(self):
        return reverse("survey_creator", args=[self.pk])

    def get_survey_results_url(self):
        return reverse("survey_results", args=[self.pk])

    @property
    def survey_creator_update_url(self):
        return reverse("update_survey_json", args=[self.pk])

    def get_model_admin_list_url(self):
        admin_helper = AdminURLHelper(self)
        admin_list_url = admin_helper.get_action_url("index", self.pk)
        return admin_list_url

    @property
    def submit_url(self):
        return reverse("survey_data", args=[self.pk])

    @property
    def name(self):
        return self.title