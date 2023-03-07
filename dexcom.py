from pydexcom import Dexcom

from time import *

import I2C_LCD_driver

dexcom = Dexcom("username", "password")



mylcd = I2C_LCD_driver.lcd()

while True:
        bg = dexcom.get_current_glucose_reading()

        mylcd.lcd_display_string("My Glucose is", 1)
        mylcd.lcd_display_string(str(bg.value), 2)
        mylcd.lcd_display_string(str(bg.trend_description), 2, 5)
        sleep(60)
        mylcd.lcd_clear()
