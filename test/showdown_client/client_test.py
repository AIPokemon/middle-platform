'''
Author:  Hata
Date: 2022-03-11 23:50:45
LastEditors: Hata
LastEditTime: 2022-03-14 00:02:14
FilePath: \middle-platform\test\showdown_client\client_test.py
Description: 
'''

import sys
import json
import unittest
from urllib import request

sys.path.append(".")
import showdown_client.client as client


class BaseTest(unittest.TestCase):

    def test_build_url_normal(self):
        self.assertEqual(
            client.build_url('https', 'pokemonshowdown.com',
                             'news', ['270.json'], query={}),
            'https://pokemonshowdown.com/news/270.json'
        )

        self.assertEqual(
            client.build_url('https', 'pokemonshowdown.com',
                             '', ['news', '270.json'], query={'empty_key': None}),
            'https://pokemonshowdown.com/news/270.json'
        )

        self.assertEqual(
            client.build_url('https', 'replay.pokemonshowdown.com', '', ['search.json'], query={
                'user': 'zarel', 'user2': 'yuyuko', 'format': 'gen7randombattle'
            }),
            'https://replay.pokemonshowdown.com/search.json?user=zarel&user2=yuyuko&format=gen7randombattle'
        )


class ClientTest(unittest.TestCase):

    def test_json_request(self):
        req = request.Request('https://pokemonshowdown.com/news/270.json', headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36',
            'Access-Control-Allow-Origin': '*',
        })
        resp = request.urlopen(req).read()

        c = client.Client()
        self.assertDictEqual(c._showdown_request(['news', '270.json']), json.loads(resp))

    def test_str_request(self):
        req = request.Request('https://pokemonshowdown.com/news/270.json', headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36',
            'Access-Control-Allow-Origin': '*',
        })
        resp = request.urlopen(req).read().decode('utf-8')

        c = client.Client()
        self.assertEqual(c._showdown_request(['news', '270.json'], resp_type='str'), resp)

    def test_response_request(self):
        c = client.Client()
        resp = c._showdown_request(['news', '270.json'], query={
                                   'empty_key': None}, resp_type='response')
        self.assertEqual(resp.status, 200)
        self.assertEqual(resp.url, 'https://pokemonshowdown.com/news/270.json')


if __name__ == "__main__":
    unittest.main()
