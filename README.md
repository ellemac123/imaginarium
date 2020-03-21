# WIP: Imaginarium Card Categories Personal Project

This project was created to categorise the cards for the Russian board game Imaginarium. 
I own six very different decks and I want to mix them up, but would like to know
which original decks they came in, in case I ever want to reorganise. So here is this project. 
It is a work in progress, as I have very little time to contribute to this project, but
hopefully one day I will be able to mix my cards up and have one MASSIVE deck!

## Running the Code

### Installing Required Libraries

#### PIP

To install the required libraries, use pip! Just run `pip install -r requirements.txt`
in the top level directory. This will install all the libraries needed to run!

#### Poetry

The following Poetry installation is intended for MacOS. 

1. Install Poetry `curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python`
2. Source the newly installed poetry env `source $HOME/.poetry/env`
3. Install the dependencies with `poetry install`

### Running the Django Application
This application is built of the Django Framework. Here are the steps to run it. 
1. Make all database migrations with `python manage.py makemigrations`. Followed by
`python manage.py migrate`.
2. Run the application server on localhost `python manage.py runserver`.
3. Open your chosen browser and navigate to `localhost:8000`!
4. Voila

## Sentry and Error Handling

Monitoring of errors is handled by [Sentry](https://sentry.io). To access the errors, you must have
permission to my `imaginarium-categories` project. All errors thrown by Django will be picked up 
by the sentry integration to the settings and will be displayed in detail in the Sentry UI. To 
gain access to this dashboard, contact me directly haha.

## Further Readings and Associated Links

1. [Imaginarium Rules](https://boardgamegeek.com/boardgame/146548/imaginarium) from board game geek. 
2. [Official Imaginarium Game Site](https://cosmodrome.games/catalog/for_all/imadzhinarium-klassika/)


## Next steps

1. Use Docker
2. Tests
3. User authentication, with default open login
4. Celery?
5. Make it look pretty!