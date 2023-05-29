import os
from dotenv import load_dotenv

load_dotenv()


class ConfigManager:
    def __init__(self):
        self.api_id = os.getenv('API_ID', '')
        self.api_hash = os.getenv('API_HASH', '')
        self.phone_num = os.getenv('PHONE_NUM', '')
        self.check_config()

    def check_config(self):
        for key, value in self.__dict__.items():
            if not value:
                raise ValueError(f'Can\'t find {key}! Please add {key} in .env')
