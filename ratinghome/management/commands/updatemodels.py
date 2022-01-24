from django.core.management.base import BaseCommand
import pandas as pd
from ratinghome.models import rateinfo
class Command(BaseCommand):
    help= 'import booms'
    def add_arguments(self, parser):
        pass
    def handle(self, *args, **options):
        df=pd.read_excel('Data.xlsx')
        for pid,pname,culture,adventure,wildlife,sightseeing,history,tag,province in zip(df.pID,df.pName,df.culture,df.adventure,df.wildlife,df.sightseeing,df.history,df.tags,df.province):
            models=rateinfo(pID=pid,pName=pname,culture=culture,adventure=adventure,wildlife=wildlife,sightseeing=sightseeing,history=history,tag_title=tag,province=province)
            models.save()

