# StockDistributor
A cmd Python app for baying stocks on  XTB for a specific amount of money

# Install
To install you are going to need python and some libraries

* websocket-client==1.4.1
* termtables
* pytz
* decimal

if you heave pip you can run imports.bat to install them all at once

get python here:
https://www.python.org/downloads/

and pip here:
https://pypi.org/project/pip/
# How to use 
Lunch the app.py in your cmd and follow the instructions.
# Features
In this app, you can log in to your XTB account via the API and select a certain amount of balance to be distributed between stocks of your choosing and parachuted with minimal amount not spend.

* you can save several accounts in the accounts.json file, so you don't heave to type out the ID every time (format: [Lp, ID, demo/real, note]).
* You can import .json files with stocks to sped up your operation (check out exp_Indexes.json).
* If an exchange is closed, the app can wait until its opening.
* in the minimumTarnsactions.txt you can specify minimum values of different types of instruments (the API does not provide this value)
# Disclaimer
Read the code at your own risk!

This is the first code I have ever written, so it is horrendous, but hey it does the job.

If you can bare it, feel free to contribute!

# Credits
Big thanks to Saitama298 on GitHub for making the API.py part of this app, I would not be able to do this without it,

but you still heave to use the version from this repository because I modified the original code.
