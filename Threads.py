from threading import *
from time import sleep
a=5
class Messenger1(Thread):
    def run(self):
        global a;
        for i in range(5):
            a=a+1;
            print("Hello:",a);
            sleep(1)

class Messenger2(Thread):
    def run(self):
        global a;
        for i in range(5):
            a+=2;
            print("Hi:",a);
            sleep(1)


m1=Messenger1();
m2=Messenger2();
m1.start();
sleep(0.2)
m2.start();
m1.join()
m2.join()
print("Bye")