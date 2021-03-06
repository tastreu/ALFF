# Generated by Django 2.1.4 on 2019-03-28 18:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_auto_20190315_1944'),
    ]

    operations = [
        migrations.CreateModel(
            name='SearchCriteria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.CharField(default='20', max_length=30)),
                ('device', models.CharField(choices=[('ps4', 'Playstation'), ('xb1', 'Xbox'), ('pc', 'PC'), ('none', 'NONE')], default='none', max_length=4)),
                ('hasMic', models.BooleanField(default=False)),
                ('location', models.CharField(default='NYA', max_length=100)),
                ('charactor', models.CharField(choices=[('Bangalore', 'Bangalore'), ('Gibraltar', 'Gibraltar'), ('Mirage', 'Mirage'), ('Lifeline', 'Lifeline'), ('Bloodhound', 'Bloodhound'), ('Caustic', 'Caustic'), ('Octane', 'Octane'), ('Pathfinder', 'Pathfinder'), ('Wraith', 'Wraith'), ('none', 'NYA')], default='none', max_length=15)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='charactor',
            field=models.CharField(choices=[('Bangalore', 'Bangalore'), ('Gibraltar', 'Gibraltar'), ('Mirage', 'Mirage'), ('Lifeline', 'Lifeline'), ('Bloodhound', 'Bloodhound'), ('Caustic', 'Caustic'), ('Octane', 'Octane'), ('Pathfinder', 'Pathfinder'), ('Wraith', 'Wraith'), ('none', 'NYA')], default='none', max_length=15),
        ),
        migrations.AddField(
            model_name='user',
            name='device',
            field=models.CharField(choices=[('ps4', 'Playstation'), ('xb1', 'Xbox'), ('pc', 'PC'), ('none', 'NONE')], default='none', max_length=4),
        ),
        migrations.AddField(
            model_name='user',
            name='hasMic',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='location',
            field=models.CharField(default='NYA', max_length=100),
        ),
        migrations.AddField(
            model_name='user',
            name='criteria',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='webapp.SearchCriteria'),
        ),
    ]
