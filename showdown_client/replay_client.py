'''
Author:  Hata
Date: 2022-03-12 01:19:12
LastEditors: Hata
LastEditTime: 2022-03-12 12:24:08
FilePath: \middle-platform\showdown_client\replay_client.py
Description: 
'''

from showdown_client import client


class ReplayClient(client.Client):
    def __init__(self):
        super().__init__()
        self._domain = 'replay.pokemonshowdown.com'

    def search(self, user=None, user2=None, format=None, page=None):
        query = {
            'uaer': user,
            'user2': user2,
            'format': format,
            'page': page,
        }
        return self._showdown_request(params=['search.json'], query=query)

    def get_replay(self, replay_id: str):
        return self._showdown_request(params=[f'{replay_id}.json'])

    def get_log(self, replay_id: str):
        return self._showdown_request(params=[f'{replay_id}.log'], resp_type='str')
