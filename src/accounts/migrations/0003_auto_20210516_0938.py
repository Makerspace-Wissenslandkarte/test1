# Generated by Django 3.2.3 on 2021-05-16 09:38

from django.db import migrations, models

# https://docs.djangoproject.com/en/3.2/topics/migrations/#data-migrations
def combine_names(apps, schema_editor):
    # We can't import the Person model directly as it may be a newer
    # version than this migration expects. We use the historical version.
    User = apps.get_model('accounts', 'User')
    for person in User.objects.all():
        person.full_name = '%s %s' % (person.first_name, person.last_name)
        person.display_name = person.full_name
        person.save()

class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_user_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='display_name',
            field=models.CharField(blank=True, max_length=300, verbose_name='display name'),
        ),
        migrations.AddField(
            model_name='user',
            name='full_name',
            field=models.CharField(blank=True, max_length=300, verbose_name='full name'),
        ),
        migrations.RunPython(combine_names),
        migrations.RemoveField(
            model_name='user',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='last_name',
        ),
    ]
