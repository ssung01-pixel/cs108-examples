# File: project/apps.py
# Author: Sarinna Sung, (ssung101@bu.edu), 04/26/2021
# Description: this page is used to register the models with the django admin appication project/apps.py

from django.apps import AppConfig


class ProjectConfig(AppConfig): # registering the project
    name = 'project'
