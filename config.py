# -----------------------------------------------
# 🔸 StrangerMusic Project
# 🔹 Developed & Maintained by: Shashank Shukla (https://github.com/itzshukla)
# 📅 Copyright © 2022 – All Rights Reserved
#
# 📖 License:
# This source code is open for educational and non-commercial use ONLY.
# You are required to retain this credit in all copies or substantial portions of this file.
# Commercial use, redistribution, or removal of this notice is strictly prohibited
# without prior written permission from the author.
#
# ❤️ Made with dedication and love by ItzShukla
# -----------------------------------------------

import re
from os import getenv
from dotenv import load_dotenv
from pyrogram import filters

# Load environment variables
load_dotenv()

# Required credentials
API_ID = int(getenv("14579176"))
API_HASH = getenv("39ac717c9b38891c6a4351fe8ea376f2")
BOT_TOKEN = getenv("8287823604:AAHt3Q0ymjikNChgl8949lBxb0Ulc_N9S3g")

# Bot and owner info
OWNER_USERNAME = getenv("OWNER_USERNAME", "RICHEDxD")
BOT_USERNAME = getenv("BOT_USERNAME", "mahavirmusicbot")
BOT_NAME = getenv("BOT_NAME", "Riched")
ASSUSERNAME = getenv("ASSUSERNAME", "richedcheats")

# MongoDB
MONGO_DB_URI = getenv("MONGO_DB_URI", mongodb+srv://mahavirkumar:mahavirkumar>@cluster0.3t52j36.mongodb.net/?appName=Cluster0)

# Limits and IDs
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 17000))
LOGGER_ID = int(getenv("LOGGER_ID", -1003904556542))
OWNER_ID = int(getenv("OWNER_ID", 8329778041))

# Heroku
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
DEEP_API = getenv("DEEP_API")

# Git
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/itzshukla/STRANGER-MUSIC")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv("GIT_TOKEN", None)

# Support
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/+AEbif9fb9pszODM1")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/+KrBRT9foT-ljMTFl")

# Assistant settings
AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", "True")
AUTO_LEAVE_ASSISTANT_TIME = int(getenv("ASSISTANT_LEAVE_TIME", "9000"))

# Song download limits
SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION", "9999999"))
SONG_DOWNLOAD_DURATION_LIMIT = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "9999999"))

# Spotify
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "1c21247d714244ddbb09925dac565aed")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "709e1a2969664491b58200860623ef19")

# Playlist limit
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))

# Telegram file limits
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "5242880000"))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "5242880000"))

# Session strings
STRING1 = getenv("STRING_SESSION", BQDedegAJ_j1m6gjqA30-T_cSW5tlPYwIS5i82wO0EgfjvmIGTg5OInwHIrDzTfnmZsg_v-4x-3TetbW7lz4eEb7LxZVbfQoBLXDRCJI7PmIYzHArxh0VuedBVUwb04ChjveRs37yoP9dZbmo4Ve2xeB1fqzT8bNg_x9o2uauVYKxjOelRF27DUbQ0_xQTQrXC68RopsuoZ1HA9g7nBSERkSLmQI8lsiRHt2dHOfW0hXOtmasWtFMQrM604byB2yq1N6cpJC_-H-nfAWfGPeawkI5Kcg-rnZ4fE3aeGLodhtzA3zpqqgCfi6S4rWF1d_z95SQPvAx_rhTnObUVCgiDnJ2FjNRwAAAAHwflN5AA)
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)
STRING6 = getenv("STRING_SESSION6", None)
STRING7 = getenv("STRING_SESSION7", None)

# Miscellaneous
BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}

DEBUG_IGNORE_LOG = True

###### IMAGE URLS ######

START_IMG_URL = getenv("START_IMG_URL", "https://files.catbox.moe/ak96mx.jpg")
PING_IMG_URL = getenv("PING_IMG_URL", "https://files.catbox.moe/ak96mx.jpg")
PLAYLIST_IMG_URL = "https://files.catbox.moe/lrwbj6.jpg"
STATS_IMG_URL = "https://files.catbox.moe/ak96mx.jpg"
TELEGRAM_AUDIO_URL = "https://files.catbox.moe/aesldg.jpg"
TELEGRAM_VIDEO_URL = "https://files.catbox.moe/aesldg.jpg"
STREAM_IMG_URL = "https://files.catbox.moe/aesldg.jpg"
SOUNCLOUD_IMG_URL = "https://files.catbox.moe/aesldg.jpg"
YOUTUBE_IMG_URL = "https://files.catbox.moe/aesldg.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://files.catbox.moe/aesldg.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://files.catbox.moe/aesldg.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://files.catbox.moe/aesldg.jpg"


SHASHANK_IMG = [
    "https://files.catbox.moe/dw0as6.jpg",
    "https://files.catbox.moe/t2m1pv.jpg",
    "https://files.catbox.moe/lsbotb.jpg",
    "https://files.catbox.moe/huuy1f.jpg",
    "https://files.catbox.moe/7vfivr.jpg",
    "https://files.catbox.moe/dqtuv2.jpg",
    "https://files.catbox.moe/ac3tzn.jpg"
]


# Helper function
def time_to_seconds(time: str) -> int:
    """Convert time string (MM:SS) to total seconds."""
    return sum(int(x) * 60**i for i, x in enumerate(reversed(time.split(":"))))

# Calculate total duration limit in seconds
DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))

# Validate URLs
if SUPPORT_CHANNEL and not re.match(r"(?:http|https)://", SUPPORT_CHANNEL):
    raise SystemExit("[ERROR] - Your SUPPORT_CHANNEL url is invalid. It must start with https://")

if SUPPORT_CHAT and not re.match(r"(?:http|https)://", SUPPORT_CHAT):
    raise SystemExit("[ERROR] - Your SUPPORT_CHAT url is invalid. It must start with https://")
