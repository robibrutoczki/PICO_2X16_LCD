from pico_i2c_lcd import I2cLcd

from machine import I2C
from machine import Pin
import utime as time
import network   # handles connecting to WiFi
import urequests # handles making and servicing network requests



# Connect to network
wlan = network.WLAN(network.STA_IF)
wlan.active(True)

# Fill in your network name (ssid) and password here:
ssid = ''
password = ''
wlan.connect(ssid, password)




print("ETH GBP ")
r = urequests.get("https://www.bitstamp.net/api/v2/ticker/ethgbp")

print(r.json()['last'])
r.close()

# Example 2. urequests can also handle basic json support! Let's get the current time from a server
print("THE TIME IS :")
b = urequests.get("https://www.timeapi.io/api/Time/current/zone?timeZone=Europe/London") # Server that returns the current GMT+0 time.
print(b.json()['date'] +" " + b.json()['time'])
b.close()
 
 
i2c =machine.I2C(0,scl=Pin(1),sda=Pin(0),freq=40000)
lcd = I2cLcd(i2c, 0x27, 4, 20)
 
while True:
      r = urequests.get("https://www.bitstamp.net/api/v2/ticker/ethgbp")
      b = urequests.get("http://date.jsontest.com")
      date=str(time.gmtime())
      lcd.clear()
      lcd.move_to(6,0)
      lcd.putstr ('ETH GBP:')
      lcd.move_to(7,1)
      lcd.putstr (r.json()['last'])
      lcd.move_to(3,2)
      lcd.putstr('DATE AND TIME:')
      lcd.move_to(5,3)
      lcd.putstr (b.json()['date'] )
      time.sleep(1)
      lcd.move_to(6,3)
      lcd.putstr (' ')
      lcd.move_to(5,3)
      lcd.putstr (b.json()['time'])