# Generated by Django 5.0.3 on 2024-03-23 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pet_patients', '0004_remove_petpatient_owner_petpatient_user_delete_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='petpatient',
            name='species',
            field=models.CharField(choices=[('Dog', 'Dog'), ('Cat', 'Cat'), ('Bird', 'Bird'), ('Rabbit', 'Rabbit'), ('Hamster', 'Hamster'), ('Fish', 'Fish'), ('Turtle', 'Turtle'), ('Guinea Pig', 'Guinea Pig'), ('Snake', 'Snake'), ('Horse', 'Horse'), ('Other', 'Other')], max_length=25),
        ),
        migrations.DeleteModel(
            name='Species',
        ),
    ]
