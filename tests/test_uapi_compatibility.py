import io
import json
import unittest
from unittest.mock import patch
from urllib.parse import parse_qs, urlsplit

import requests

from balderich import NSSClient
from balderich.utils.exceptions import UserImageNotExistException


class UapiCompatibilityTests(unittest.TestCase):
    def setUp(self):
        self.client = NSSClient(key='sdk-test-key', secret='sdk-test-secret')
        sender = patch.object(requests.Session, 'send')
        self.send = sender.start()
        self.addCleanup(sender.stop)

    def respond(self, data=None, *, code=10000, content_type='application/json', content=None):
        response = requests.Response()
        response.status_code = 200
        response.headers['Content-Type'] = content_type
        response._content = json.dumps({'code': code, 'data': data}).encode() if content is None else content
        self.send.return_value = response

    def request(self, method, path):
        request = self.send.call_args.args[0]
        url = urlsplit(request.url)
        self.assertEqual((request.method, url.path), (method, '/v2/api/' + path))
        self.assertEqual(set(parse_qs(url.query)), {'key', 'time', 'sign'})
        return request

    def test_uid_and_pending_contests_use_signed_get(self):
        self.respond({'uid': 42})
        self.assertEqual(self.client.user.get_self_uid(), 42)
        self.request('GET', 'user/info/')
        contests = [{'id': 8, 'start_date': 1794556800}]
        self.respond(contests)
        self.assertEqual(self.client.contest.get_pending_contests(), contests)
        self.request('GET', 'contest/list/pending/')

    def test_batch_state_and_team_analysis_send_json(self):
        states = [{'id': 12, 'solved': True, 'tried': True}]
        self.respond(states)
        self.assertEqual(self.client.problem.get_problem_states([12]), states)
        request = self.request('POST', 'problem/statistics/state/')
        self.assertEqual(request.headers['Content-Type'], 'application/json')
        self.assertEqual(json.loads(request.body), {'pids': [12]})
        self.respond({})
        self.client.team.post_team_analysis_solves_curve([42, 43])
        request = self.request('POST', 'team/analysis/solves/curve/')
        self.assertEqual(json.loads(request.body), {'uids': [42, 43]})

    def test_put_with_a_body_uses_json(self):
        self.respond({'state': True})
        self.client._put('team/clockin/', {'enabled': True})
        request = self.request('PUT', 'team/clockin/')
        self.assertEqual(request.headers['Content-Type'], 'application/json')
        self.assertEqual(json.loads(request.body), {'enabled': True})

    def test_picturebed_usage_and_listing_preserve_legacy_paged_call(self):
        self.respond({'used_mem': 42, 'total': 1, 'max_mem': 100})
        self.assertEqual(self.client.user.get_user_picturebed_used()['used_mem'], 42)
        self.request('GET', 'user/picturebed/used/')
        self.respond({'pictures': [{'id': 7}], 'total': 1})
        self.assertEqual(self.client.user.get_user_picturebed_list(2, 5)['total'], 1)
        self.request('GET', 'user/picturebed/list/2/5/')
        self.assertEqual(self.client.user.get_user_picturebed_used(page=2, size=5)['total'], 1)
        self.request('GET', 'user/picturebed/list/2/5/')

    def test_picturebed_multipart_upload_and_binary_download(self):
        self.respond({'id': 7})
        self.assertEqual(self.client.user.post_user_picturebed_upload('test.png', io.BytesIO(b'example')), {'id': 7})
        request = self.request('POST', 'user/picturebed/upload/')
        self.assertTrue(request.headers['Content-Type'].startswith('multipart/form-data; boundary='))
        self.assertIn(b'name="image"; filename="test.png"', request.body)
        for mime in ('image/webp', 'application/octet-stream'):
            self.respond(content_type=mime, content=b'image bytes')
            self.assertEqual(self.client.user.post_user_picturebed_download(7).read(), b'image bytes')
            self.request('POST', 'user/picturebed/7/download/')
        self.respond(code=11007)
        with self.assertRaises(UserImageNotExistException):
            self.client.user.post_user_picturebed_download(7)

    def test_team_rank_page_size_is_explicit_or_uses_legacy_default(self):
        self.respond({'solves': [], 'total': 0})
        self.client.team.get_team_contest_rank_list_by_page(8, 2)
        self.request('GET', 'team/contest/8/rank/list/2/15/')
        self.client.team.get_team_contest_rank_list_by_page(8, 2, size=5)
        self.request('GET', 'team/contest/8/rank/list/2/5/')
