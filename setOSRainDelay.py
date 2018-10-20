# OpenSprinkler API from https://rayshobby.net/docs/os_fw214_api.pdf
# https://openweathermap.org/current
#/usr/bin/python

import urllib2
import json
import requests

osIpAddr = '1.2.3.4'
osPwMD5 = 'md5hashofossprinkler'
rDelayHrs = '24'
rDelayOff = '0'
avgWindOff = 10
owlocation = 'Sydney,au'
owApiId = 'APPIDPASSWORD'

def getWindAvg():
        url = "http://api.openweathermap.org/data/2.5/weather"
        querystring = {"q":owlocation ,"APPID":owApiId}
        headers = {
                'cache-control': "no-cache",
                }
        response = requests.request("GET", url, headers=headers, params=querystring)
        data = response.json()
        avgWind = data["wind"]["speed"]
        return avgWind

def setOsData(rdVal):
        url = "http://" + osIpAddr + "/cv"
        querystring = {"pw":osPwMD5 , "rd":rdVal}
        headers = {
                'cache-control': "no-cache",
                }
        response = requests.request("POST", url, headers=headers, params=querystring)
        #print(response.text)
        #error handling goes here

def checkWindSetRd():
        wind = getWindAvg()
        print("Wind speed is " + str(wind))
        if wind > avgWindOff:
                rdVal = rDelayHrs
                setOsData(rdVal)
                print("Wind speed greater than 10, OpenSprinkler Rain Delay on for " + rDelayHrs + " hours.")
        else:
                rdVal = rDelayOff
                setOsData(rdVal)
                print("Wind speed less than 10, OpenSprinkler Rain Delay Off")
                
checkWindSetRd()
