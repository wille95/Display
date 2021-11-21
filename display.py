from time import sleep
from machine import Pin, SoftSPI, SoftI2C
import st7789py as st7789
from bmp180 import BMP180

from romfonts import vga2_16x16 as font

bmp180 = BMP180(SoftI2C(scl=Pin(22), sda=Pin(21)))  # Sensor importieren

spi = SoftSPI(
    baudrate = 20000000, 
    polarity = 1,
    phase = 0, 
    sck = Pin(18), 
    mosi = Pin(19), 
    miso = Pin(13)
    )

tft = st7789.ST7789(
    spi, 
    135,
    240, 
    reset = Pin(23,Pin.OUT), 
    cs = Pin(5,Pin.OUT),
    dc = Pin(16,Pin.OUT),
    backlight = Pin(4,Pin.OUT),
    rotation = 3
    )

tft.fill(st7789.BLACK)
line = 0
col = 0

while True:
    bmptemp = round(bmp180.temperature,2)
    ausgabe = str(bmptemp) 
    tft.text(font, "aktuelle",10,10,st7789.RED,st7789.CYAN)
    tft.text(font, "Temperatur = ",10,30,st7789.BLACK,st7789.YELLOW)
    tft.text(font, ausgabe, 10, 50, st7789.BLUE, st7789.WHITE)
    tft.text(font, "Grad Celcius!", 10, 70, st7789.RED,st7789.GREEN)
    tft.text(font, ":)  <3  :D", 10, 100, st7789.YELLOW,st7789.BLACK)




