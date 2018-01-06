# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-06 06:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('emp_id', models.CharField(max_length=32, primary_key=True, serialize=False, verbose_name='员工ID')),
                ('working_state', models.CharField(choices=[('in', '在职'), ('leave', '离职')], max_length=12, verbose_name='在职状态')),
                ('name', models.CharField(max_length=32, verbose_name='英文名')),
                ('gender', models.CharField(choices=[('M', '男'), ('F', '女')], max_length=6, verbose_name='性别')),
                ('mbti', models.CharField(blank=True, max_length=12, null=True, verbose_name='职业性格测试')),
                ('birthday', models.CharField(blank=True, max_length=8, null=True, verbose_name='出生日期')),
                ('mobile', models.CharField(blank=True, max_length=16, null=True, verbose_name='电话电话')),
                ('hire_date', models.DateField(blank=True, null=True, verbose_name='录入日期')),
                ('education', models.TextField(blank=True, null=True, verbose_name='教育经历')),
                ('work_exp', models.TextField(blank=True, null=True, verbose_name='工作经历')),
                ('tenure', models.CharField(blank=True, max_length=32, null=True, verbose_name='在职日期')),
                ('recruited', models.CharField(blank=True, max_length=32, null=True, verbose_name='招聘渠道')),
                ('promotion', models.TextField(blank=True, null=True, verbose_name='晋升经历')),
                ('about', models.TextField(blank=True, null=True, verbose_name='关于')),
                ('professional_aspirations', models.TextField(blank=True, null=True, verbose_name='职业意向')),
                ('user_guide', models.CharField(blank=True, max_length=255, null=True)),
                ('favorites', models.TextField(blank=True, null=True, verbose_name='兴趣爱好')),
                ('training_sessions', models.TextField(blank=True, null=True, verbose_name='培训课程')),
                ('name_cn', models.CharField(blank=True, max_length=16, null=True, verbose_name='中文名')),
                ('id1', models.CharField(blank=True, max_length=32, null=True, verbose_name='身份证号')),
                ('id2', models.CharField(blank=True, max_length=32, null=True, verbose_name='护照号')),
                ('join_date', models.DateField(blank=True, null=True, verbose_name='入职日期')),
                ('level', models.CharField(blank=True, max_length=255, null=True, verbose_name='级别')),
                ('loc', models.CharField(blank=True, max_length=255, null=True, verbose_name='办公地点')),
                ('module', models.CharField(blank=True, max_length=255, null=True)),
                ('ra_ten', models.CharField(blank=True, max_length=255, null=True)),
                ('a_ten', models.CharField(blank=True, max_length=255, null=True)),
                ('sa_ten', models.CharField(blank=True, max_length=255, null=True)),
                ('asc_w_ten', models.CharField(blank=True, max_length=255, null=True)),
                ('asc_ten', models.CharField(blank=True, max_length=255, null=True)),
                ('login_mobile', models.CharField(blank=True, max_length=255, null=True)),
                ('openid', models.CharField(blank=True, max_length=32, null=True)),
                ('leave_date', models.CharField(blank=True, max_length=32, null=True)),
                ('email', models.CharField(blank=True, max_length=255, null=True, verbose_name='电子邮箱')),
                ('company', models.CharField(blank=True, max_length=255, null=True, verbose_name='就职公司')),
            ],
            options={
                'db_table': 'OA_Employee',
            },
        ),
        migrations.CreateModel(
            name='EmployeeProject',
            fields=[
                ('id', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('emp_order', models.IntegerField(default=0, null=True)),
                ('emp_name', models.CharField(blank=True, max_length=255, null=True)),
                ('role', models.CharField(blank=True, max_length=8, null=True)),
                ('emp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='OA.Employee')),
            ],
            options={
                'db_table': 'OA_Employee_Project',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('pro_id', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('code', models.CharField(blank=True, max_length=12, null=True)),
                ('client', models.CharField(blank=True, max_length=32, null=True)),
                ('engagement', models.CharField(blank=True, max_length=255, null=True)),
                ('industry', models.CharField(blank=True, max_length=255, null=True)),
                ('function', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('team', models.CharField(blank=True, max_length=255, null=True)),
                ('duration', models.CharField(blank=True, max_length=32, null=True)),
                ('start_date', models.DateField(blank=True, max_length=64, null=True)),
                ('sub_industry', models.CharField(blank=True, max_length=255, null=True)),
                ('sub_function', models.CharField(blank=True, max_length=255, null=True)),
                ('ed', models.CharField(blank=True, max_length=255, null=True)),
                ('ap', models.CharField(blank=True, max_length=255, null=True)),
                ('asc_pro', models.CharField(blank=True, max_length=255, null=True)),
                ('account', models.CharField(blank=True, max_length=255, null=True)),
                ('end_date', models.DateField(blank=True, max_length=64, null=True)),
                ('key_issue', models.CharField(blank=True, max_length=255, null=True)),
                ('solutions_and_impacts', models.CharField(blank=True, max_length=556, null=True)),
                ('status', models.CharField(blank=True, max_length=255, null=True)),
                ('type', models.CharField(blank=True, max_length=255, null=True)),
                ('sector', models.CharField(blank=True, max_length=255, null=True)),
                ('contacts', models.CharField(blank=True, max_length=255, null=True)),
                ('fee', models.CharField(blank=True, max_length=255, null=True)),
                ('target', models.CharField(blank=True, max_length=255, null=True)),
                ('lop', models.CharField(blank=True, max_length=255, null=True)),
                ('deck', models.CharField(blank=True, max_length=255, null=True)),
                ('model', models.CharField(blank=True, max_length=255, null=True)),
                ('data', models.CharField(blank=True, max_length=255, null=True)),
                ('interview_guide', models.CharField(blank=True, max_length=255, null=True)),
                ('focus_gp', models.CharField(blank=True, max_length=255, null=True)),
                ('survey', models.CharField(blank=True, max_length=255, null=True)),
                ('resources', models.CharField(blank=True, max_length=255, null=True)),
                ('collected', models.CharField(blank=True, max_length=255, null=True)),
                ('state', models.CharField(blank=True, max_length=255, null=True)),
                ('comments', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'OA_Project',
            },
        ),
        migrations.AddField(
            model_name='employeeproject',
            name='pro',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='OA.Project'),
        ),
        migrations.AddField(
            model_name='employee',
            name='project',
            field=models.ManyToManyField(through='OA.EmployeeProject', to='OA.Project'),
        ),
    ]
