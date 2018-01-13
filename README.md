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

4. Run locally using heroku:
    ```
    heroku local
    ```
