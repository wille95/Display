from time import sleep                                              # für alle 10 Sekunden Temperatur messen
from machine import Pin, SoftSPI, SoftI2C                           # Pin (BMP180, TFT Dispay), SoftSPI (Bus TFT), SoftI2C (Bus BMP180)
import st7789py as st7789                                           # TFT Display
from bmp180 import BMP180                                           # BMP180 Sensor
from bh1750 import BH1750                                       
from romfonts import vga2_16x16 as font                             # Schriftart laden

i2c = SoftI2C(scl=Pin(22), sda=Pin(21))                             # I2C(BMP180) # Schnittstelle für Sensor
bmp180 = BMP180(i2c)                                                # Objekt bmp180 aus der Klasse BMP180 initialisieren 
bh = BH1750(i2c)
               
spi = SoftSPI(                                                      # Objekt SPI (TFT) initalisieren
    baudrate = 20000000,                                            # Übertragungsrate, Kommunikatiosngeschwindigkeit
    polarity = 1,                                    
    phase = 0,                                      
    sck = Pin(18),                                   
    mosi = Pin(19),                                 
    miso = Pin(13)                                  
    )
#tft Display
tft = st7789.ST7789(                                                # Objekt tft instanzieren # aus Bibliothek Basisklasse wählen
    spi,                                                            # Schnittstelle
    135,                                                            # Pixel x - Achse (hochkant)
    240,                                                            # Pixel y - Achse (hochkant)
    reset = Pin(23,Pin.OUT),        
    cs = Pin(5,Pin.OUT),            
    dc = Pin(16,Pin.OUT),           
    backlight = Pin(4,Pin.OUT),     
    rotation = 3                                                    # Bildschirmrotation 1=90 Grad
    )

led_green = Pin(25,Pin.OUT)                                         # led_green initalisieren 
led_yellow = Pin(26,Pin.OUT)                                        # led_yellow initalisieren
led_red = Pin(27,Pin.OUT)                                           # led_red initalisieren

#------------Initalisierung Ende -----------------------------------#   alles was ich für das programm brauche um das Programm zu starten

tft.fill(st7789.BLACK)                                              # Hintergrundfarbe schwarz
line = 0                                                            # Zeile
col = 0                                                             # Spalte

while True:
    bmpTemp = round(bmp180.temperature,2)                           # Temperatur runden
    ausgabe_temp = str(bmpTemp)                                     # Temperatur als String "ausgabe_temp" zuweisen

    bmpPress = round(bmp180.pressure)                               # Druck runden
    ausgabe_press=str(bmpPress)                                     # Druck als string "ausgabe_press" zuweisen
    
    bh_Licht = round(bh.luminance(0x10))
    ausgabe_bh1750 = str(bh_Licht)                               

    tft.text(font, "Temperatur = ",10,10,st7789.BLACK,st7789.YELLOW)
    tft.text(font, ausgabe_temp + " \xF8C", 10,30, st7789.BLUE, st7789.WHITE)      
    tft.text(font, "Druck = ",10,50,st7789.BLACK,st7789.YELLOW)
    tft.text(font, ausgabe_press + " hPa", 10,70, st7789.BLUE, st7789.WHITE)  
    tft.text(font, "Lichtsensor = ",10,90,st7789.BLACK,st7789.YELLOW) 
    tft.text(font, ausgabe_bh1750 + " LUX", 10, 110,st7789.BLUE, st7789.WHITE)

    #Interpreter der es interpretiert auf dem controller
    # tft = Objekt
    # .txt = methode 

    if bmpTemp <= 23: 
        led_green.value(1)
    else: 
        led_green.value(0)
    
    if (bmpTemp > 23) and (bmpTemp <= 24):
        led_yellow.value(1)
    else: 
        led_yellow.value(0)
