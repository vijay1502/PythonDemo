from datetime import datetime

n = int(input())

for _ in range(n):
    t1 = datetime.strptime(input(), "%a %d %b %Y %H:%M:%S %z")
    t2 = datetime.strptime(input(), "%a %d %b %Y %H:%M:%S %z")
    # print(t1, t2)
    print(abs(int((t1 - t2).total_seconds())))

# Adding extra content# Adding extra content
