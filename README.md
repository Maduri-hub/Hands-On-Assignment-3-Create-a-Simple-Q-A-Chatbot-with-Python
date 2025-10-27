\# Django + ChatterBot Terminal Chatbot



\## Overview

This project contains a minimal Django project and a `terminalbot` app. The terminal chatbot script uses ChatterBot and runs from the terminal.



\## Setup (PyCharm)

1\. Open PyCharm → Open an existing project and select this project folder.

2\. Create a new virtual environment (PyCharm will prompt to create one) or use an existing venv.

3\. Install dependencies:

&nbsp;  - Open Terminal in PyCharm and run:

&nbsp;    ```

&nbsp;    pip install -r requirements.txt

&nbsp;    ```

&nbsp;  - If you face C compilation issues for `spacy`, try:

&nbsp;    ```

&nbsp;    pip install -U pip setuptools wheel

&nbsp;    pip install spacy==3.5.0

&nbsp;    ```



\## Run the Terminal Chat

1\. In PyCharm open `terminalbot/chat\_terminal.py`.

2\. Run the script:

&nbsp;  - Right-click -> Run `chat\_terminal` or

&nbsp;  - Use Terminal and execute:

&nbsp;    ```

&nbsp;    python terminalbot/chat\_terminal.py

&nbsp;    ```



\## Notes

\- On first run the bot will train on the `chatterbot.corpus.english` dataset. This may take a minute.

\- After first successful run you can comment out the `trainer.train(...)` line in `chat\_terminal.py` to speed start-up.

\- The bot uses an sqlite DB file `db.sqlite3` in the project folder for storage.



\## Deliverables for assignment

\- Python source code (this repo)

\- `requirements.txt` (manifest)

\- Screenshot: Run the terminal client, take a screenshot of the conversation, include it in your Word document

\- Upload code to GitHub and share the repository URL with your submission



