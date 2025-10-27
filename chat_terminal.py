"""
Terminal chat client using ChatterBot.

Run with:
    python terminalbot/chat_terminal.py

This script creates/loads a ChatterBot instance backed by sqlite (db for the bot).
It trains on the built-in english corpus the first time (trainer.train will be fast on subsequent runs
because ChatterBot caches knowledge in the sqlite db).

Notes:
- If you re-train every run, comment out the trainer.train(...) line after first successful run to speed start-up.
- If training fails due to package issues, ensure requirements are installed in your virtualenv.
"""

import os
import sys
import logging
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer


# Optional: make chatterbot logs less verbose
logging.basicConfig(level=logging.WARNING)

# Ensure the script works when run from project root in PyCharm / terminal
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)


def create_chatbot(database_path='sqlite:///db.sqlite3'):
    """
    Create and return a ChatBot instance.
    database_path: SQLAlchemy database URI for ChatterBot storage.
                   Default uses a sqlite DB in project root named db.sqlite3
                   (This is separate from Django's db.sqlite3 file if desired).
    """
    bot = ChatBot(
        'TerminalBot',
        # Storage adapter stores conversation in the database specified below
        storage_adapter='chatterbot.storage.SQLStorageAdapter',
        database_uri=database_path,
        read_only=False,
        logic_adapters=[
            {
                'import_path': 'chatterbot.logic.BestMatch'
            }
        ]
    )
    return bot


def train_bot(chatbot_instance, corpus_list=('chatterbot.corpus.english',)):
    """
    Train the ChatBot on the supplied corpus list.
    For large corpora, training may take some time on first run.
    """
    trainer = ChatterBotCorpusTrainer(chatbot_instance)
    try:
        # Training can be commented out after first successful run to speed subsequent runs.
        trainer.train(*corpus_list)
    except Exception as e:
        print("Warning: Training failed or skipped. Error:", str(e))


def main():
    print("Starting TerminalBot (Django + ChatterBot example). Type 'exit' or 'quit' to stop.\n")
    # Use sqlite database in project root. Change path if you want a separate file.
    db_uri = 'sqlite:///db.sqlite3'
    bot = create_chatbot(database_path=db_uri)

    # Train on english corpus if the DB is empty. This step can be slow first time.
    # If you want to avoid training every run, comment the next line after first run.
    train_bot(bot, ('chatterbot.corpus.english',))

    try:
        while True:
            user_input = input("You: ").strip()
            if not user_input:
                continue
            if user_input.lower() in ('exit', 'quit'):
                print("Bot: Goodbye! Have a great day.")
                break
            # Get response from ChatterBot
            response = bot.get_response(user_input)
            print("Bot:", response)
    except (KeyboardInterrupt, EOFError):
        print("\nBot: Goodbye! (terminated)")
    except Exception as e:
        print("An error occurred:", e)


if __name__ == '__main__':
    main()
