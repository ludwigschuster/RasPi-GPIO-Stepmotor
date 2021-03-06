
# This is a Stepmotor Python class
It is based on this [article](http://www.elektronx.de/tutorials/schrittmotorsteuerung-mit-dem-raspberry-pi/).
The Stepmotors described there can be found [here] (http://www.ebay.de/itm/290974735618?clk_rvr_id=1055052146819&rmvSB=true) or [here](https://www.amazon.de/28BYJ-48-28BYJ48-4-Phase-Arduino-Stepper/dp/B00ATA5MFE?ie=UTF8&camp=1638&creative=19454&creativeASIN=B00ATA5MFE&linkCode=as2&redirect=true&ref_=as_li_ss_tl&tag=christhimbee-21). Those are unipolar 5 pin motors. This is the [datasheet](http://www.raspberrypi-spy.co.uk/wp-content/uploads/2012/07/Stepper-Motor-28BJY-48-Datasheet.pdf).

<p style="float: right;">
  <a href="https://raw.githubusercontent.com/ludwigschuster/RasPi-GPIO-Stepmotor/master/img/IMG_0655.jpg" target="_blank" alt="Stepmotor"><img src="https://raw.githubusercontent.com/ludwigschuster/RasPi-GPIO-Stepmotor/master/img/IMG_0655.jpg" width=350px/>
</p>

##Usage

Put stepmotor.py (located in /bin) into your working directory and import it with `from stepmotor import Stepmotor`. You can now create an object with `motor = Stepmotor()` and use this object. 

Following methods are available: 

*	 use `turnSteps(n)` for turning n steps
*	 use `turnDegrees(n)` for turning n degrees (small values can lead to inaccuracy)
*	 use `turnDistance(distance, radius)` turn for translation of wheels or a coil (inaccuracies involved e.g. due to thickness of rope)

See the example below. 

```python
from stepmotor import Stepmotor
from time import sleep

print("moving started")
motor = Stepmotor()
print("One Step")
motor.turnSteps(1)
sleep(0.5)
print("20 Steps")
motor.turnSteps(20)
sleep(0.5)
print("quarter turn")
motor.turnDegrees(90)
print("moving stopped")
motor.close()
```

> It is important, that you close with `close()` when you are done. 
