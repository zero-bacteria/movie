# Generated by Django 3.1.7 on 2021-05-26 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='rate',
            field=models.PositiveSmallIntegerField(choices=[(1, '1 - 안본눈 사고싶다.'), (2, '2 - 재활용 불가'), (3, '3 - 진짜 별로다'), (4, '4 - 그닥....'), (5, '5 - 그냥저냥'), (6, '6 - 타임킬링, 그럭저럭'), (7, '7 - 재밌었다.'), (8, '8 - 좋은 영화인거 같다.'), (9, '9 - 인생 영화'), (10, '10 - 띵작 오브 띵작')]),
        ),
    ]
