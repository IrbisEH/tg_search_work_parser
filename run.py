from ConfigManager import ConfigManager
from TelegramParser import TelegramParser
from telethon.tl.functions.messages import GetHistoryRequest
import telethon
from telethon.tl.types import PeerUser, PeerChat, PeerChannel
import pprint


ConfigManager = ConfigManager()
tg = TelegramParser(ConfigManager)

user_id = 214893352
channel_id = 1000735083

# async def main():
#     dialogs = await tg.client.get_dialogs()
#     print(dialogs[0].stringify())
#
#
# with tg.client:
#     tg.client.loop.run_until_complete(main())

with tg.client:
    res = tg.client.loop.run_until_complete(tg.get_new_channel_id())

print(res)
