#RepRasp Octoprint plugin

![promo image](https://raw.githubusercontent.com/johnny13/RepRasp/master/assets/art/move.png)


###Install via Pip

    pip install https://github.com/johnny13/OctoPrint-RepRasp/archive/master.zip

After running this command simply open up your Settings menu from Octoprint. If your screen width is below 600 pixel an hidden menu will appear so you can load RepRasp w/o needing a keyboard or anything. 


###Raspberry Pi Desktop Shortcut

You **really** need to setup a link on your **Raspberry Pi's Desktop** for this to work smoothly. An example can be found in /statc/shortcut. Put the reprasp.desktop file on your ~/home/Desktop folder. Then put the /static/shortcut/reprasp folder on ~/home/

When we get done, you will be launching the chromium-browser in a special "kiosk" mode that hides all the browser fluff and will fill your whole screen. If you dont have chromium installed you will need to install it on your Pi.

    apt-get install chromium-browser

Now the Link in reprasp.desktop should point to ~/home/reprasp/start.sh. 

The next step is important. Edit the start file and update with your API Key.

    nano ~/home/reprasp/start.sh

Find the last line and change the 123 to your key.

    chromium-browser --kiosk octopi.local/plugin/reprasp/?apikey=123

Great Job! Now an Icon should appear on your Raspberry Pi Desktop. If you touch it your raspberry will open straight into the touch screen. Skipping the main octoprint desktop.


### Details
Touchscreen user interface that works with OctoPrint and a Raspberry Pi. Allows you to attach a TFTScreen to your Pi and use that as your wireless and physical printer controller. No more green and black screen w/ push button knobs. 

This only allows you to install the plugin. If you want to mess around with the UI and all that fun stuff you'll need to visit the dev repo.
DevRepo Located Here [https://github.com/johnny13/RepRasp](https://github.com/johnny13/RepRasp)


### Developing

    pip install https://github.com/johnny13/OctoPrint-RepRasp/archive/master.zip
    
    python setup.py develop

You will need to run both commands each time.

