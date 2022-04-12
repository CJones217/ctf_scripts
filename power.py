
with open('dates_power.txt'),'r') as f:
    contents = f.readlines()

count = 0
s=[]
for l in contents:
    reading=l.split('% ')[1].strip()
    s.append((l[:10],reading))

dates_and_readings = []
dates='blahblah'
numba=0
for c in s:
    if(c[0] == date):
        numba = numba + int(c[1])
    else:
        dates_and_readings.append((date,numba))
        date=c[0]
        numba=0

dates_and_readings.append((date,numba))
print(dates_and_readings)
