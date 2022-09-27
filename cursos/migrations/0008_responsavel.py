# Generated by Django 3.2.15 on 2022-09-23 18:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0007_auto_20220920_1628'),
    ]

    operations = [
        migrations.CreateModel(
            name='Responsavel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150, verbose_name='Nome completo do responsável')),
                ('celular', models.CharField(max_length=15, verbose_name='Celular p/ contato do responsável')),
                ('email', models.EmailField(max_length=254, verbose_name='Email p/ contato do responsável')),
                ('dt_nascimento', models.DateField(verbose_name='Data de Nascimento')),
                ('sexo', models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino')], max_length=1, verbose_name='Qual foi o sexo atribuído no seu nascimento?')),
                ('cep', models.CharField(max_length=9, verbose_name='CEP')),
                ('endereco', models.CharField(max_length=150, null=True, verbose_name='Endereço do responsável')),
                ('bairro', models.CharField(max_length=80, null=True)),
                ('cpf', models.CharField(max_length=150, verbose_name='CPF')),
                ('rg', models.CharField(blank=True, max_length=12, verbose_name='RG')),
                ('profissão', models.CharField(max_length=150, verbose_name='Profissão')),
                ('estado_civil', models.CharField(choices=[('s', 'Solteiro(a)'), ('c', 'Casado(a)'), ('s', 'Separado(a)'), ('d', 'Divorciado(a)'), ('v', 'Viúvo(a)')], max_length=1, verbose_name='Estado Civil')),
                ('aluno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cursos.aluno')),
            ],
        ),
    ]