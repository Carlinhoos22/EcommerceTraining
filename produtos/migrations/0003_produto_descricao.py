# Generated by Django 4.2.6 on 2023-10-17 02:27

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("produtos", "0002_alter_produto_preco"),
    ]

    operations = [
        migrations.AddField(
            model_name="produto",
            name="descricao",
            field=models.TextField(default=0, max_length=255),
        ),
    ]
