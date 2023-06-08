from threading import *
from time import sleep
output="";
count=0;
flag=0;
class FileReading(Thread):
    def run(self):
        global output
        global flag
        f = open('MavenDependencies.txt','r');
        for i in f.read().split("\n"):
                output=i;
                if output==None:
                    flag=1;
                    break
                sleep(0.5)

class FileStringCounter(Thread):

    def run(self):
        global output
        global count
        global flag
        while flag!=1:
            if output.__contains__("spring"):
                count+=1;
                print("count:",count," output:",output)
                sleep(0.5)
        else:
            return count;


file=FileReading();
fileCount=FileStringCounter();
file.start()
sleep(0.2)
fileCount.start()
