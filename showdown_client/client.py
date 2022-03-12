'''
Author:  Hata
Date: 2022-03-11 23:34:18
LastEditors: Hata
LastEditTime: 2022-03-13 23:41:55
FilePath: \middle-platform\showdown_client\client.py
Description: 
'''

import json
from urllib import request
from urllib import parse

from showdown_client.exception import *


def build_url(scheme: str, domain: str, path: str, params: list, query: dict):
    path_str = '/'.join([path, *params])
    query_list = []

    for k, v in query.items():
        if k and v:
            query_list.append(f'{k}={v}')

    query_str = '&'.join(query_list)
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

    resp = request.urlopen(req)
    resp_bytes = resp.read()
    resp_type = resp_type.lower()

    if resp_type == 'json':
        return json.loads(resp_bytes)
    elif resp_type == 'str':
        return resp_bytes.decode('utf-8')
    elif resp_type == 'response':
        return resp
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
