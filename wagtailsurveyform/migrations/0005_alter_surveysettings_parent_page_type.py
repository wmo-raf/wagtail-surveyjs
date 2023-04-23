# Generated by Django 4.1.8 on 2023-04-23 14:23

from django.db import migrations, models
import django.db.models.deletion
import wagtailsurveyform.models


class Migration(migrations.Migration):
    dependencies = [
        ('wagtailcore', '0083_workflowcontenttype'),
        ('wagtailsurveyform', '0004_surveysettings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='surveysettings',
            name='parent_page_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL,
                                    to='wagtailcore.page'),
        ),
    ]
