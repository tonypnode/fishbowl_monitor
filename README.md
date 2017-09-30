# FishBowl Monitor
Just a fun project for me to learn some Python, Django and work with some
sensors and the raspberry pi 3. I will attempt to use [Test Driven Development
(TDD) to accomplish this project](https://www.obeythetestinggoat.com).

### What do I want it to do right now?
I'm hoping, it will do the following:
 *  Provide a web interface (Done)
 *  Display fishbowl water temperature (Done)

### Future features I want to add
 * Show data trends over time (grpahs n stuff) (Version 2 coming up)
 * Take a pic of the fishy every once in a while
 * a button to push when someone feeds the fish
 * Track who feeds the fish (picture?)
 * Track fishbowl ph balance

Hardware (still a work in progress):
1. Betta Fish and Fishbowl :)
2. RaspberryPi v3
3. DS18B20 Waterproof Thermal Temp. Sensor
4. Bread board
5. 4K ohm resister (I used 2x 2.2K resistors)


## Resources
* This is the site I used to get the temp sensor working
 and collecting data https://pimylifeup.com/raspberry-pi-temperature-sensor/
. It worked perfectly. I did modify the function a little to clean it up though.

## Database Schtuff

temperature model
* Date time
* temperature

and that should be it for now...

Eventually I'm thinking about adding..:
feeding model
* date time
* image location? if a picture is being taken


## Updates:
* 29 Sep 17: Well, it's been up for a while and it's working great
    * I was concerned about the size of the db, but, with 8K entries it's still only 495K
    I did end up adding in the auto clean up, so every time an entry gets added,
    the oldest gets deleted. I will want to up the time frame eventually so that 
    I can get at least 30 days worth, then roll up 30-90, 90-180, and 180-365 for
    averages. I'm still runing on the dev server so I everytime I want to see the website i have
    loginto the pi and start the process.I will eventually move it to nginx and gunicorn
* Next up is version 2. AJAX and a graph.