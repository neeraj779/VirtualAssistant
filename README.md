# Alexa-virtual-assistant
![image of voice assitant](https://miro.medium.com/max/3840/1*9IcqVZ48A0tQba1-F_yIpg.jpeg)

Alexa like virtual assistant written in Python which uses google's speech-to-text library to process voice input.

* Install the dependencies in a virtual environment (using conda or virtualenv) to avoid any issues. Use either pip2 or pip3 for python2 and python3 respectively.

If you are a linux user install the [say](https://askubuntu.com/questions/501910/how-to-text-to-speech-output-using-command-line) command using
```
sudo apt-get install gnustep-gui-runtime
```

```bash
pip2 install -r requirements.txt
pip3 install -r requirements.txt
```

* Usage
```bash
python code.py
````

Supported commands :
* Open youtube : Opens the youtube in default browser.
* Open google : Opens the google in default browser.
* Open website xyz.com : self-explanatory
* Tell a joke : Says a random joke.
* Tell weather in {cityname} : Tells you the current condition and temperture
* Tell forecast in {cityname} : Tells you the condition, highest and lowest temperture of the next two days
* Tell <computational and geographical questions> : it will answer your computational and geographical questions
* What is current time : Tells you current time 
* Wikipedia <query> : It will fetch data about your query from wikipedia