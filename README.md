# EuroPython 2019 🇨🇭

_Wednesday 10th July 2019, 14.00, Singapore Room, Congress Center Basel._

## Dash: INTERACTIVE DATA VISUALIZATION WEB APPS WITH NO JAVASCRIPT

**Please note the examples in this repository require Python >= 3.6 - official python 3.5 support is being withdrawn in January 2020...**

The slides relating to this talk are available here: [http://bit.ly/ep2019dash](http://bit.ly/ep2019dash).

### Example Applications

Run the apps in this repository to see how Dash can be used.

### JGMTFC: Run Everything with Docker-compose

    docker-compose -f docker-compose-talk.yml up

This will make the links on the slides work: [http://bit.ly/ep2019dash](http://bit.ly/ep2019dash)

#### Install

This is a freeze of my environment in which all these worked.

    pip install -r requirements.txt

#### Run Individually

**Hello World**

Greet the world in Dash style.

    python app00.py


**Interactive Hello World**

Your first interactive Dash app.

    python app01.py


**Data Table (bad)**

Using global state is not referenced in this talk, but I've left it in here as an example of a bad thing to do!

    python app02.py


**Data Table (Good)**

List the Titanic Dataset using just a few lines of code.

    python app03.py

**Events: To Do App**

A basic todo app, in Dash. But without a proper data store!

    python app04.py


**Splitting Up App: To Do**

Split up your app.

    python -m app05


**Factory Functions**

And use factory functions!

    python -m app06
