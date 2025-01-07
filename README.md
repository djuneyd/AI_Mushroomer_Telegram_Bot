# Mushroom Recognition Bot

This project is a Telegram bot that helps recognize mushrooms from a photo and provides additional information about them.

## Installation

1. Clone the repository:
    ```sh
    git clone <https://github.com/djuneyd/AI_Mushroomer_Telegram_Bot.git>
    ```

2. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

3. Create a [private.py](http://_vscodecontentref_/10) file and add your tokens and API keys:
    ```py
    TOKEN = 'your_telegram_bot_token'
    DATABASE = 'project/data_bases/user_manager.db'

    # Yandex GPT data
    server = 'your_server'
    api_key = 'your_api_key'
    ```

## Usage

1. Run the bot:
    ```sh
    python project/bot.py
    ```

2. In Telegram, find your bot and start with the `/start` command.

3. To recognize a mushroom, send a photo of the mushroom and use the `/recognize` command.

## Project Files

- [AI_mushroom_recognizer.py](http://_vscodecontentref_/11): Script for recognizing mushrooms using a Keras model.
- [keras_model.h5](http://_vscodecontentref_/12): Pre-trained Keras model.
- [labels.txt](http://_vscodecontentref_/13): Labels for mushroom classes.
- [simple_gpt_yandex.py](http://_vscodecontentref_/14): Script for interacting with Yandex GPT.
- [private.py](http://_vscodecontentref_/15): Confidential data such as tokens and API keys.
- [user_manager.py](http://_vscodecontentref_/16): User and database management.
- [bot.py](http://_vscodecontentref_/17): Main script for the Telegram bot.

## License

This project is licensed under the MIT License. See the LICENSE file for details.