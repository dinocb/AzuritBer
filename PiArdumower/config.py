import os

cwd = os.getcwd()


if (os.name=='nt'):
    print('Windows Platform')
    myComPort = 'COM9'
    myFrameWidth = 800
    myFrameHeight = 430
    myBaudRate = 115200
    myOS="Windows"
    GpsConnectedOnPi=False
    GpsIsM6n=True
    RfidConnectedOnPi=False
    NanoConnectedOnPi=False
    Esp32ConnectedOnPi=False
    DueConnectedOnPi=False
    AutoRecordBatCharging=False

if (os.name=='posix'):
    print('Linux Platform')
    myComPort = '/dev/ttyACM0'
    myFrameWidth = 800
    myFrameHeight = 430
    myBaudRate = 250000
    myOS="Linux"
    GpsConnectedOnPi=False
    GpsIsM6n=False
    RfidConnectedOnPi=False
    NanoConnectedOnPi=True
    Esp32ConnectedOnPi=False
    DueConnectedOnPi=True
    AutoRecordBatCharging=True
    

