'''
Author:  Hata
Date: 2022-03-12 01:22:44
LastEditors: Hata
LastEditTime: 2022-03-14 14:40:01
FilePath: \middle-platform\test\showdown_client\replay_client_test.py
Description: 
'''

import unittest
import sys

sys.path.append(".")
import showdown_client.replay_client as replay_client


class ReplayClientTest(unittest.TestCase):

    def test_search(self):
        c = replay_client.ReplayClient()
        result = c.search(format='gen8ou', page=2)
        self.assertTrue(result)

    def test_get(self):
        c = replay_client.ReplayClient()
        logs = c.search(format='gen8ou', page=2)
        for replay in logs[:3]:
            replay_json = c.get_replay(replay['id'])
            replay_log = c.get_log(replay['id'])
            self.assertEqual(replay_log, replay_json['log'])

if __name__ == "__main__":
    unittest.main()
