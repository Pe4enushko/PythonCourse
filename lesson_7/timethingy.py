from time import time, gmtime, strftime
from random import randint
import os
import datetime

start = time()
num = randint(1000000,10000000)

for i in range(0,1000000):
    num ** randint(1,100)

end = time()

print(datetime.timedelta(seconds= end - start).seconds, 'seconds')