# Generated by Django 3.1 on 2021-08-12 03:24

import accueil.models.contenttype
import accueil.models.devoir
import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accueil', '0021_auto_20210801_1318'),
    ]

    operations = [
        migrations.CreateModel(
            name='Information',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expediteur', models.PositiveSmallIntegerField(choices=[(1, 'Administrateur'), (2, 'Secrétariat')], default=1, verbose_name='Expéditeur')),
                ('destinataire', models.PositiveSmallIntegerField(choices=[(1, 'Colleurs'), (2, 'Élèves'), (3, 'Tout le monde')], verbose_name='destinataires')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('message', ckeditor.fields.RichTextField(blank=True, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='creneau',
            name='heure',
            field=models.PositiveSmallIntegerField(choices=[(480, '8h00'), (510, '8h30'), (540, '9h00'), (570, '9h30'), (600, '10h00'), (630, '10h30'), (660, '11h00'), (690, '11h30'), (720, '12h00'), (750, '12h30'), (780, '13h00'), (810, '13h30'), (840, '14h00'), (870, '14h30'), (900, '15h00'), (930, '15h30'), (960, '16h00'), (990, '16h30'), (1020, '17h00'), (1050, '17h30'), (1080, '18h00'), (1110, '18h30'), (1140, '19h00'), (1170, '19h30')], default=480),
        ),
        migrations.AlterField(
            model_name='message',
            name='corps',
            field=ckeditor.fields.RichTextField(blank=True, max_length=2000, null=True),
        ),
        migrations.CreateModel(
            name='TD',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.PositiveSmallIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18), (19, 19), (20, 20), (21, 21), (22, 22), (23, 23), (24, 24), (25, 25), (26, 26), (27, 27), (28, 28), (29, 29), (30, 30), (31, 31), (32, 32), (33, 33), (34, 34), (35, 35), (36, 36), (37, 37), (38, 38), (39, 39), (40, 40), (41, 41), (42, 42), (43, 43), (44, 44), (45, 45), (46, 46), (47, 47), (48, 48), (49, 49), (50, 50), (51, 51), (52, 52), (53, 53), (54, 54), (55, 55), (56, 56), (57, 57), (58, 58), (59, 59), (60, 60), (61, 61), (62, 62), (63, 63), (64, 64), (65, 65), (66, 66), (67, 67), (68, 68), (69, 69), (70, 70), (71, 71), (72, 72), (73, 73), (74, 74), (75, 75), (76, 76), (77, 77), (78, 78), (79, 79), (80, 80), (81, 81), (82, 82), (83, 83), (84, 84), (85, 85), (86, 86), (87, 87), (88, 88), (89, 89), (90, 90), (91, 91), (92, 92), (93, 93), (94, 94), (95, 95), (96, 96), (97, 97), (98, 98), (99, 99), (100, 100)], verbose_name='Numéro')),
                ('detail', models.TextField(blank=True, null=True, verbose_name='Détails')),
                ('date_affichage', models.DateTimeField(auto_now_add=True)),
                ('fichier', accueil.models.contenttype.ContentTypeRestrictedFileField(blank=True, null=True, upload_to=accueil.models.devoir.TD.update_name, verbose_name='Fichier(pdf)')),
                ('classe', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='classetd', to='accueil.classe')),
                ('matiere', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='matieretd', to='accueil.matiere')),
            ],
            options={
                'ordering': ['-numero'],
                'unique_together': {('classe', 'matiere', 'numero')},
            },
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(blank=True, max_length=80, null=True)),
                ('detail', models.TextField(blank=True, null=True, verbose_name='Détails')),
                ('date_affichage', models.DateTimeField(auto_now_add=True)),
                ('fichier', accueil.models.contenttype.ContentTypeRestrictedFileField(blank=True, null=True, upload_to=accueil.models.devoir.Document.update_name, verbose_name='Fichier(pdf)')),
                ('classe', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='classedocument', to='accueil.classe')),
                ('matiere', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='matieredocument', to='accueil.matiere')),
            ],
            options={
                'ordering': ['-date_affichage'],
                'unique_together': {('classe', 'matiere', 'titre')},
            },
        ),
        migrations.CreateModel(
            name='Cours',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.PositiveSmallIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18), (19, 19), (20, 20), (21, 21), (22, 22), (23, 23), (24, 24), (25, 25), (26, 26), (27, 27), (28, 28), (29, 29), (30, 30), (31, 31), (32, 32), (33, 33), (34, 34), (35, 35), (36, 36), (37, 37), (38, 38), (39, 39), (40, 40), (41, 41), (42, 42), (43, 43), (44, 44), (45, 45), (46, 46), (47, 47), (48, 48), (49, 49), (50, 50), (51, 51), (52, 52), (53, 53), (54, 54), (55, 55), (56, 56), (57, 57), (58, 58), (59, 59), (60, 60), (61, 61), (62, 62), (63, 63), (64, 64), (65, 65), (66, 66), (67, 67), (68, 68), (69, 69), (70, 70), (71, 71), (72, 72), (73, 73), (74, 74), (75, 75), (76, 76), (77, 77), (78, 78), (79, 79), (80, 80), (81, 81), (82, 82), (83, 83), (84, 84), (85, 85), (86, 86), (87, 87), (88, 88), (89, 89), (90, 90), (91, 91), (92, 92), (93, 93), (94, 94), (95, 95), (96, 96), (97, 97), (98, 98), (99, 99), (100, 100)], verbose_name='Numéro')),
                ('detail', models.TextField(blank=True, null=True, verbose_name='Détails')),
                ('date_affichage', models.DateTimeField(auto_now_add=True)),
                ('fichier', accueil.models.contenttype.ContentTypeRestrictedFileField(blank=True, null=True, upload_to=accueil.models.devoir.Cours.update_name, verbose_name='Fichier(pdf)')),
                ('classe', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='classecours', to='accueil.classe')),
                ('matiere', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='matierecours', to='accueil.matiere')),
            ],
            options={
                'ordering': ['-numero'],
                'unique_together': {('classe', 'matiere', 'numero')},
            },
        ),
    ]
