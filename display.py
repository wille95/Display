from time import sleep          # Sleeo importieren
from machine import Pin, SoftSPI, SoftI2C   #Pin, SoftSPI und SoftI2C importieren für Sensor und Display
import st7789py as st7789       # Display importieren
from bmp180 import BMP180       # aus Bibliothek Sensor importieren

from romfonts import vga2_16x16 as font     # Darstellung importieren

bmp180 = BMP180(SoftI2C(scl=Pin(22), sda=Pin(21)))  # Sensor importieren

spi = SoftSPI(                  #Einstellung für Display
    baudrate = 20000000,        # Übertragungsrate
    polarity = 1,               
    phase = 0, 
    sck = Pin(18),              
    mosi = Pin(19), 
    miso = Pin(13)
    )

tft = st7789.ST7789(                # aus Klasse ST7789 Objekt bilden   dc=None, cs=None, backlight=None, rotation=0)
    spi,                            # Bus der verwendet wird
    135,                            # breite
    240,                            # höhe
    reset = Pin(23,Pin.OUT),        # Display resten
    cs = Pin(5,Pin.OUT),            # cs?
    dc = Pin(16,Pin.OUT),           # dc?
    backlight = Pin(4,Pin.OUT),     # Hintergrund
    rotation = 3                    # Bildschirmrotation
    )

tft.fill(st7789.BLACK)              # Display hintergrund füllen
line = 0
col = 0

while True:
    bmptemp = round(bmp180.temperature,2)   # Temperatur runden
    ausgabe = str(bmptemp)                  # als zeichenkette Temperatur ausgabe zuweisen
    tft.text(font, "aktuelle",10,10,st7789.RED,st7789.CYAN) # ausgabe text aktuelle
    tft.text(font, "Temperatur = ",10,30,st7789.BLACK,st7789.YELLOW)    # ausgabe text Temperatur =
    tft.text(font, ausgabe, 10, 50, st7789.BLUE, st7789.WHITE)     # ausgabe temperaturwert
    tft.text(font, "Grad Celcius!", 10, 70, st7789.RED,st7789.GREEN)    # ausfageb text Grad celcius
    tft.text(font, ":)  :D", 10, 100, st7789.YELLOW,st7789.BLACK)   # ausgabe Smileys :)




