# Generated by Django 4.0.3 on 2022-08-24 07:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0009_alter_category_options_alter_item_options_and_more'),
        ('chat', '0002_messagetext_remove_chatroom_profile1_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='chatroom',
            options={'ordering': ['-created_at']},
        ),
        migrations.AlterModelOptions(
            name='message',
            options={'ordering': ['-created_at']},
        ),
        migrations.AddField(
            model_name='chatroom',
            name='item',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='chatrooms', to='market.item'),
        ),
    ]
