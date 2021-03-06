# Generated by Django 2.2.1 on 2019-12-02 21:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('register_app', '0006_message'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('e_id', models.AutoField(primary_key=True, serialize=False)),
                ('e_name', models.CharField(max_length=30)),
                ('e_description', models.CharField(blank=True, max_length=100)),
                ('e_location', models.CharField(blank=True, max_length=50)),
                ('e_date', models.DateField()),
                ('e_time', models.TimeField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('pst_id', models.AutoField(primary_key=True, serialize=False)),
                ('pst_content', models.CharField(max_length=200)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('pst_filepath', models.FileField(blank=True, upload_to='')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('p_id', models.AutoField(primary_key=True, serialize=False)),
                ('p_name', models.CharField(max_length=30, verbose_name='Project name')),
                ('p_description', models.CharField(blank=True, max_length=100, verbose_name='Description')),
                ('p_start_date', models.DateField(null=True)),
                ('p_end_date', models.DateField(null=True)),
                ('p_budget', models.IntegerField(blank=True)),
                ('p_status', models.CharField(blank=True, max_length=10, verbose_name='Status')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('r_id', models.AutoField(primary_key=True, serialize=False)),
                ('r_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('tm_id', models.AutoField(primary_key=True, serialize=False)),
                ('tm_name', models.CharField(max_length=30, verbose_name='Team name')),
                ('tm_description', models.CharField(blank=True, max_length=100, verbose_name='Description')),
                ('tm_start_date', models.DateField()),
                ('tm_end_date', models.DateField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('project_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='register_app.Project')),
            ],
        ),
        migrations.AlterField(
            model_name='message',
            name='m_content',
            field=models.TextField(verbose_name='Content'),
        ),
        migrations.AlterField(
            model_name='message',
            name='m_filepath',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.CreateModel(
            name='Workspace',
            fields=[
                ('w_id', models.AutoField(primary_key=True, serialize=False)),
                ('w_name', models.CharField(max_length=30, verbose_name='Workspace name')),
                ('photo_address', models.ImageField(blank=True, upload_to='pictures/organizations/workspaces', verbose_name='Photo address')),
                ('w_address', models.CharField(blank=True, max_length=100, verbose_name='Address')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('organization_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='register_app.Organization')),
            ],
        ),
        migrations.CreateModel(
            name='user_workspace_relation',
            fields=[
                ('uwr_id', models.AutoField(primary_key=True, serialize=False)),
                ('r_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='register_app.Role')),
                ('u_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('w_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='register_app.Workspace')),
            ],
        ),
        migrations.CreateModel(
            name='user_team_relation',
            fields=[
                ('utr_id', models.AutoField(primary_key=True, serialize=False)),
                ('r_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='register_app.Role')),
                ('t_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='register_app.Team')),
                ('u_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='user_project_relation',
            fields=[
                ('upr_id', models.AutoField(primary_key=True, serialize=False)),
                ('p_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='register_app.Project')),
                ('r_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='register_app.Role')),
                ('u_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('t_id', models.AutoField(primary_key=True, serialize=False)),
                ('t_name', models.CharField(max_length=30)),
                ('t_description', models.CharField(blank=True, max_length=100)),
                ('t_start_date', models.DateField()),
                ('t_end_date', models.DateField()),
                ('t_status', models.CharField(choices=[(0, 'Created'), (1, 'Assigned'), (2, 'In progress'), (3, 'Completed'), (4, 'Submitted')], max_length=10)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('assigned_to', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='assigned_to', to=settings.AUTH_USER_MODEL)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_by', to=settings.AUTH_USER_MODEL)),
                ('team_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='register_app.Team')),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='workspace_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='register_app.Workspace'),
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('n_id', models.AutoField(primary_key=True, serialize=False)),
                ('n_title', models.CharField(max_length=20)),
                ('n_description', models.CharField(blank=True, max_length=50)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('n_from', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='n_from', to=settings.AUTH_USER_MODEL)),
                ('n_to', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='n_to', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('c_id', models.AutoField(primary_key=True, serialize=False)),
                ('c_content', models.CharField(max_length=200)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('post_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='register_app.Post')),
            ],
        ),
        migrations.CreateModel(
            name='WorkspacePost',
            fields=[
                ('post_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='register_app.Post')),
                ('wp_id', models.AutoField(primary_key=True, serialize=False)),
                ('post_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='workspace_post_pid', to='register_app.Post')),
                ('workspace_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='workspace_post_wid', to='register_app.Workspace')),
            ],
            bases=('register_app.post',),
        ),
        migrations.CreateModel(
            name='WorkspaceEvent',
            fields=[
                ('event_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='register_app.Event')),
                ('we_id', models.AutoField(primary_key=True, serialize=False)),
                ('event_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='workspace_event_eid', to='register_app.Event')),
                ('workspace_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='workspace_event_wid', to='register_app.Workspace')),
            ],
            bases=('register_app.event',),
        ),
        migrations.CreateModel(
            name='TeamPost',
            fields=[
                ('post_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='register_app.Post')),
                ('tp_id', models.AutoField(primary_key=True, serialize=False)),
                ('post_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='team_post_pid', to='register_app.Post')),
                ('team_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='team_post_tid', to='register_app.Team')),
            ],
            bases=('register_app.post',),
        ),
        migrations.CreateModel(
            name='TeamEvent',
            fields=[
                ('event_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='register_app.Event')),
                ('te_id', models.AutoField(primary_key=True, serialize=False)),
                ('event_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='team_event_eid', to='register_app.Event')),
                ('team_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='team_event_tid', to='register_app.Team')),
            ],
            bases=('register_app.event',),
        ),
        migrations.CreateModel(
            name='ProjectPost',
            fields=[
                ('post_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='register_app.Post')),
                ('pp_id', models.AutoField(primary_key=True, serialize=False)),
                ('post_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='project_post_post_id', to='register_app.Post')),
                ('project_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='project_post_project_id', to='register_app.Project')),
            ],
            bases=('register_app.post',),
        ),
        migrations.CreateModel(
            name='ProjectEvent',
            fields=[
                ('event_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='register_app.Event')),
                ('pe_id', models.AutoField(primary_key=True, serialize=False)),
                ('event_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='project_event_eid', to='register_app.Event')),
                ('project_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='project_event_pid', to='register_app.Project')),
            ],
            bases=('register_app.event',),
        ),
    ]
