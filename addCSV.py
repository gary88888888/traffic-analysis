import csv
import os
import django
import os.path
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'datacenter.settings')
django.setup()
from mysite.models import SpeedMeasuring

my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, "data.csv")

with open(path , encoding='utf-8') as csvfile:
	rows = csv.reader(csvfile, delimiter=",")
	for d in rows:
		print(d[0], d[2])
		newdata = SpeedMeasuring(cameraID = d[0],cameraType = d[1],location = d[2],direction = d[3],limit = d[4],dist = d[5],ViolationType = d[6],positionX = d[7],positionY = d[8])
		newdata.save()