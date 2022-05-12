from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_toy_alter_feeding_date_finch_toys'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='feeding',
            options={'ordering': ['-date']},
        ),
    ]