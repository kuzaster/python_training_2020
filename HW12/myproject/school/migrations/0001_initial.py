# Generated by Django 3.1.4 on 2020-12-28 09:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Homework",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("text", models.TextField(unique=True)),
                ("deadline", models.DurationField()),
                ("created", models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name="HomeworkResult",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("solution", models.TextField()),
                ("created", models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name="Student",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(max_length=250)),
                ("last_name", models.CharField(max_length=250)),
                ("age", models.IntegerField()),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Teacher",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(max_length=250)),
                ("last_name", models.CharField(max_length=250)),
                (
                    "homework_done",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="school.homeworkresult",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.AddField(
            model_name="homeworkresult",
            name="author",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="school.student"
            ),
        ),
        migrations.AddField(
            model_name="homeworkresult",
            name="homework",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="school.homework",
                to_field="text",
            ),
        ),
    ]