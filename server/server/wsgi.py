"""
WSGI config for server project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

from api.management.commands.parser_data import GoogParser
from api.models import DataList


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'server.settings')

application = get_wsgi_application()


'''
Checking data in the database.

If there is no data in database, 
then the data will be written to the base
'''
result = DataList.objects.all()
if len(result) == 0:
    data = GoogParser().soup_parser()
    for value in data:
            p = DataList(
                title=value['title'],
                date_2019=value['date_12_30_2019'],
                date_2018=value['date_12_30_2018'],
                date_2017=value['date_12_30_2017'],
                date_2016=value['date_12_30_2016']
            ).save()
else:
    pass

