'''
Author:  Hata
Date: 2022-03-11 23:34:18
LastEditors: Hata
LastEditTime: 2022-03-12 01:57:44
FilePath: \middle-platform\showdown_client\client.py
Description: 
'''

import json
from urllib import request
from urllib import parse

from showdown_client.exception import *


def build_url(scheme: str, domain: str, path: str, params: list, query: dict):
    path_str = parse.urljoin(path, *params)
    query_str = '&'.join([f'{k}={v}' for k, v in query.items()])
    return parse.urlunparse((scheme, domain, path_str, '', query_str, ''))


def do_request(method: str, scheme: str, domain: str,
               path: str = '', params: list = [], query: dict = {},
               data: dict = None, headers: dict = {}, resp_type: str = 'json'):

    url: str = build_url(scheme, domain, path, params, query)
    req = request.Request(
        url=url,
        data=json.dumps(data).encode('utf-8'),
        method=method,
        headers=headers
    )

    resp: bytes = request.urlopen(req).read()
    resp_type = resp_type.lower()

    if resp_type == 'json':
        return json.loads(resp)
    elif resp_type == 'str':
        return resp.decode('utf-8')
    else:
        return None


class Client:
    def __init__(self):
        self._scheme = "https"
        self._method = 'GET'
        self._domain = 'pokemonshowdown.com'
        self._agent = 'AIPokemon/1.00.0'
        self._path = ''

    def _showdown_request(self, params: list = [], query: dict = {}, data: dict = None, resp_type: str = 'json'):
        return do_request(
            method=self._method,
            scheme=self._scheme,
            domain=self._domain,
            path=self._path,
            params=params,
            query=query,
            data=data,
            headers=self.headers,
            resp_type=resp_type,
        )

    @property
    def headers(self) -> dict:
        return {
            'Host': self._domain,
            'User-Agent': self._agent,
            'Access-Control-Allow-Origin': '*',
        }
