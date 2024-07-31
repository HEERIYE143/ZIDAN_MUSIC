from PICKUPMUSIC.core.bot import Line
from PICKUPMUSIC.core.dir import dirr
from PICKUPMUSIC.core.git import git
from PICKUPMUSIC.core.userbot import Userbot
from PICKUPMUSIC.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Line()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
