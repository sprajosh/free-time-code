# Eye Protector
we all love our eyes. this code will help you give some rest to your eyes.
The screen goes off for 20 seconds every 20 minutes, something that has worked for me quite well.
happy seeing.. <3

###### Packages required: 
xbacklight, time

###### Why these packages
**xbacklight** is a package used for setting display brightness through cli

**time** is used to give a delay of 20 minutes and 20 seconds for screen ON and OFF, respectively.

###### Ubuntu package: 
`sudo apt-get installl xbacklight`
###### Python package: 
`pip install time`

If you wanna learn more about the packages used please go to:
[time](https://docs.python.org/2/library/time.html)

[xbacklight](https://www.x.org/releases/X11R7.6/doc/man/man1/xbacklight.1.xhtml)

xbacklight doesn't always seem to work. Doesn't work for me in i3 window manager, anyway. But luckily we have an alternative, light.

###### Light
[light](https://github.com/haikarainen/light) -- used to set display brightness through cli

###### Installing light
- clone the github repo
	`git clone https://github.com/haikarainen/light`
- run these commands - install missing packages (if any)
	`sudo make`
	`sudo make install`
- run to check if everything worked fine
	`light --help`

###### light examples:
	Increase brightness by 5:
		`light -A 5`
	Decrease brightness by 5:
		`light -U 5`
	Set Brightness value to 30
		`light -S 30`