# This is a Stepmotor Python class 
It is based on this [article] (http://www.elektronx.de/tutorials/schrittmotorsteuerung-mit-dem-raspberry-pi/).
The Stepmotors described there can be found [here] (http://www.ebay.de/itm/290974735618?clk_rvr_id=1055052146819&rmvSB=true) or [here](https://www.amazon.de/28BYJ-48-28BYJ48-4-Phase-Arduino-Stepper/dp/B00ATA5MFE?ie=UTF8&camp=1638&creative=19454&creativeASIN=B00ATA5MFE&linkCode=as2&redirect=true&ref_=as_li_ss_tl&tag=christhimbee-21). Those are unipolar 5 pin motors. This is the [datasheet](http://www.raspberrypi-spy.co.uk/wp-content/uploads/2012/07/Stepper-Motor-28BJY-48-Datasheet.pdf). 

Inline-style: 
![Stepmotor](https://github.com/ludwigschuster/RasPi-GPIO-Stepmotor/blob/master/img/stepmotor.jpg "Stepmotor") 

##Usage
The clas can be used like this:
```python
from stepmotor import Stepmotor

print("full turn")
motor = Stepmotor()
motor.turn360()
motor.close()
```


