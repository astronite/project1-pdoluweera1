# Project Overview 
This website is written in python 3.7.5 and deployed via heroku and can be found at the following link [pdoluweera1project1](https://pdoluweera1project1.herokuapp.com/).

## Requirements

To run this app you need a Python Version 3.7.5 or greater and the following modules that can be found in the requirements.txt file:

1. requests
2. Flask
3. python-dotenv
 
Create a folder on your local machine. Open that folder and clone this repository with the command ```git clone https://github.com/csc4350-f21/project1-pdoluweera1 ```. 

After this you will need to create a [Spotify](https://developer.spotify.com/) developer account along with a [Genius](https://genius.com/developers) developer account to obtain the tokens and the keys needed to run the app on your local machine. These keys will be stored in your own ".env" file and the names should match what are listed in the code. 

To deploy the app, you need to create a [Heroku](https://signup.heroku.com/). This allows you push your local app. 
 
## Technical Problems encountered
One problem that I encountered in the initial development was naming the ".env" file as "env". This caused my api keys to malfunction.

A major issue I had with pushing my app to heroku was making sure my heroku config vars matched with what was in my ".env" file. In my case there was a mismatch in the name of the vars. The name on heroku config vars must match the ".env" file. This caused my genius calls specifically to malfunction on heroku despite working fine in my local testing environment.

An important command when investigating deployment issues on heroku was 
```heroku logs --tail --app [app name]``` This gave specific error messages which could be easily googled. 

## Future Features 
I would like to implement user inputs for artists. Those artits could then be used instead of the hardcoded artist id's. This can be done by using Flask forms via html. 
Another feature could be pulling artists directly from  a personal spotify account. 