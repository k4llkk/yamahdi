from sample_config import Config
class Development(Config):
    # get this values from the my.telegram.org
    APP_ID = 9352594
    API_HASH = "e17bf200759a2ce0b9b012d2f1bf859d"
    # the name to display in your alive message
    ALIVE_NAME = "danhuso"
    # create any PostgreSQL database (i recommend to use elephantsql) and paste that link here
    DB_URI = "postgresql://postgres:youpassord@localhost:5432/aljokker"
    # After cloning the repo and installing requirements do python3 telesetup.py an fill that value with this
    STRING_SESSION = "1ApWapzMBu419bXSO2e6eVji8rSr69hw4FCQ7LNgUmyXLvdWKRxOZqPnRUpinEp6srha0wSFgufonrZ8pBxs_7eRzgIabj06QXXpWZoc-tsfKPpC4XcG_XYkVaKylkfD1ovQ1WD0ACmvKJYO3VgFhkfKNSOD9gRlSu8YDKs4sYcX372lM1kTPn4BbLhgyBtiS7yfzov0e72XZkMFrS6_lwahzHTWJ8yNf4IjWy6Yrw9ouj4tZbjH0GuiMbXeWdY_dUdd_wrvsDuRVKeoomoqBEChyH7YLuRrJRe2wolAg-gSLtbATj3e1eMu0Iwj6dgPEKBBAUOnFwoMy1gdHumzWPFEWYUxAyHE="
    # create a new bot in @botfather and fill the following vales with bottoken and username respectively
    TG_BOT_TOKEN = "7033420362:AAFpLS812vL9Flclxz7qQwQng1UWiDCLvms"
    # command handler
    COMMAND_HAND_LER = "."
    # sudo enter the id of sudo users userid's in that array
    SUDO_USERS = []
    # command hanler for sudo
    SUDO_COMMAND_HAND_LER = "."
