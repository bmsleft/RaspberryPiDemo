
'''
For RaspberryPi
it will capture a picture from camera on RaspberryPi every 1(default) minute,
and upload it to Baidu netdisk
Make sure you can use bypy normally.(https://github.com/houtianze/bypy)
By bms
'''
from time import sleep
from datatime import datatime, timedelta
from picamera import PiCamera
from bypy import ByPy

def wait(delay_minute = 1):
    next_time = (datatime.now() + timedelta(minute=delay_minute)).replace(second=0, microsecond=0)
    delay = (next_time - datatime.now()).seconds
    sleep(delay)

by=ByPy()
camera = PiCamera()
camera.start_preview()
wait()

for filename in camera.capture_continuous('img{timestamp:%Y-%m-%d-%H-%M}.jpg')
    print('capture %s' % filename)
    by.upload(filename)
    wait()


