import csv
from telethon import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty
from telethon.tl.types import PeerUser, PeerChat, PeerChannel
from telethon.tl.functions.messages import GetHistoryRequest


class TelegramParser:
    def __init__(self, ConfigManager):
        self.ConfigManager = ConfigManager
        self.api_id = self.ConfigManager.api_id
        self.api_hash = self.ConfigManager.api_hash
        self.phone = self.ConfigManager.phone_num
        self.session_name = 'anon'
        self.client = TelegramClient(self.session_name, self.api_id, self.api_hash)

    async def get_new_channel_id(self):
        my_client_user = PeerUser(214893352)
        messages = await self.client(
            GetHistoryRequest(
                peer=my_client_user,
                offset_id=0,
                offset_date=None,
                add_offset=0,
                limit=1,
                max_id=0,
                min_id=0,
                hash=0
            )
        )
        last_message = messages.messages[0]
        channel_id = last_message.fwd_from.from_id.channel_id


        return(last_message.fwd_from)


    async def get_messages(self, channel_id, min_id=0):
        channel = PeerChannel(channel_id)
        channel_messages = await self.client(
            GetHistoryRequest(
                peer=channel,
                offset_id=0,
                offset_date=None,
                add_offset=0,
                limit=5,
                max_id=0,
                min_id=min_id,
                hash=0
            )
        )
        return channel_messages.messages



