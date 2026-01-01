# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01

# Changed from buster to bullseye to fix the 404 repository error
FROM python:3.10-slim-bullseye

# Combining update and install to ensure it runs smoothly
RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y git && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt /requirements.txt

RUN pip3 install -U pip && pip3 install -U -r /requirements.txt

# Setting up the working directory
RUN mkdir /VJ-FILTER-BOT
WORKDIR /VJ-FILTER-BOT
COPY . /VJ-FILTER-BOT

# Run the bot
CMD ["python3", "bot.py"]
