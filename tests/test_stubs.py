from microbit import *
import power
import speech
import radio
import music

radio.on()
radio.config(group=26)
display.scroll("Hello")
audio.play(Sound.YAWN)
i2c.init(2323, pin19, pin15)
compass.calibrate()
pin15.read_digital()
pin0.read_analog()
button_a.was_pressed()
speech.say("Test")
music.play(music.BA_DING)
display.show(Image.HAPPY)
sleep(1000)
display.clear()

radio.off()
power.off()
