import re
import datetime


names=["Vijaya Kanugovi","Uma Kappagantula","Subramanyam Kanugovi"]
for i in names:
    if re.search("^(V|U|S).*(i|a)",i):
        print(i)
    if re.findall("(Ka|ka)",i):
        print("Found "+i)

datet=datetime.datetime(2023,4,5,13,44,23)
timest=int(round(datet.timestamp()));
print(datetime.datetime.fromtimestamp(timest).strftime("%d %B %A %Y %H %M %p"))
print(datet.strftime("%d %B %A %Y %H %M %p"))
