# import the hardware interface modules
import Adafruit_LCD1602 as adf
import PCF8574 as chip

class Connecter(object):

    def __init__():

      # set up lcd screen

      PCF8574_address = 0x27  # I2C address of the PCF8574 chip.
      PCF8574A_address = 0x3F  # I2C address of the PCF8574A chip.

      try:
        mcp = chip.PCF8574_GPIO(PCF8574_address) 
      except:
        try:
          mcp = chip.PCF8574_GPIO(PCF8574A_address) 
        except:
          print ('I2C Address Error !')
          exit(1)
        
      lcd = adf.Adafruit_CharLCD(pin_rs=0, pin_e=2, pins_db=[4,5,6,7], GPIO=mcp)

      # set up pin pad

    def print_message(msg):
      lcd.message(msg)

    def get_char():
      pass

    def get_string(endChar):
      pass
