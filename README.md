[![Build Status](https://travis-ci.org/sarah-story/shelterbot.svg?branch=master)](https://travis-ci.org/sarah-story/shelterbot)

# Shelterbot
Let's help people get shelter

## Running the app locally

1. Install and configure the [heroku cli tool](https://devcenter.heroku.com/articles/heroku-cli)

2. Setup a virtual environment and install all dependencies:
    ```
    virtualenv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
    ```

3. Setup your local sqlite database (setup superuser when prompted):
     ```
     python manage.py syncdb
     ```
     For python 3.6, need to install pysocks package:
      ```
      pip install pysocks 
      ```

4. Run locally using heroku:
    ```
    heroku local
    ```

## Running the tests

In your virtual environment:
```
python manage.py test
```

## Steps for working with Weather API .json files

1. To prevent making unnecessary API calls, make one and save the .json first

2. Use the following code to test the parsed .json. Note that from a file you use json.load vs. json.loads


```
# Scratch Files to work with this instead of doing API calls

# example:
file = open('C:\\localpath(change this)\\shelterbot\\shelterbot\\handlers\\Sample Forecast JSON.json')
d = json.load(file)
d['element 1'][0]
```