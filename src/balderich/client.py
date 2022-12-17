import time
import json
import hashlib
import requests
from typing import Tuple, Union, IO
from balderich.models.user import UserCollection
from balderich.models.contest import ContestCollection
from balderich.models.problem import ProblemCollection
from balderich.models.team import TeamCollection

class AuthConfig:
    """
    Client authorized configure setting

    Example:

        >>> config = AuthConfig(key, secret)
    
        or

        >>> config = AuthConfig.load_config_file('config.json')
        >>> config = AuthConfig.load_config_file(open('config.json', 'rb'))
    """
    def __init__(self, key: str, secret: str) -> None:
        self.key = key
        self.secret = secret
    
    @staticmethod
    def load_config_file(filepath: Union[str, IO]):
        if isinstance(filepath, str):
            file = open(filepath, 'rb')
        else:
            file = filepath
        
        data = json.load(file)

        self = AuthConfig(data['key'], data['secret'])
        return self

    def sign(self, path: str, timestamp: int = None, prefix: str='/v2/api/') -> Tuple[str, int]:
        if timestamp is None:
            timestamp = int(time.time())
        
        res = hashlib.sha256(f'{prefix}{path}#{self.key}#{timestamp}#{self.secret}'.encode()).hexdigest()

        return res, timestamp


class NSSClient:
    """
    A client for communication with Balderich

    Example:
        
        >>> import balderich

        then 
        
        >>> client = balerich.NSSClient(key='****', secret='*****')

        or

        >>> client = balderich.NSSClient(balderich.AuthConfig.load_config_file('key.json'))
    """
    def __init__(self,
        auth_cofig: AuthConfig=None,
        key: str=None,
        secret: str=None,
        url: str=None
    ) -> None:
        if url is None:
            url = 'https://www.ctfer.vip/v2/api/'
        if auth_cofig is None:
            auth_cofig = AuthConfig(key, secret)
        
        self.url = url
        self.auth_config = auth_cofig

    @property
    def user(self):
        return UserCollection(client=self)

    @property
    def problem(self):
        return ProblemCollection(client=self)

    @property
    def contest(self):
        return ContestCollection(client=self)

    @property
    def team(self):
        return TeamCollection(client=self)
    
    @property
    def key(self):
        return self.auth_config.key

    def _get(self, path: str) -> Tuple[int, Union[int, str, float, bool, list, dict]]:
        sign, timestamp = self.auth_config.sign(path)
        res = requests.get(self.url+path, params={
            'key': self.key,
            'time': timestamp,
            'sign': sign
        })

        res = res.json()
        code = res['code']
        data = res['data']

        return code, data

    def _post(self, path: str, data: dict=None, files: dict=None, parse: bool=True) -> Union[requests.Response, Tuple[int, Union[int, str, float, bool, list, dict]]]:
        if data is None:
            dict = {}
        
        if files is None:
            files = files or {}
        
        sign, timestamp = self.auth_config.sign(path)
        res = requests.post(self.url+path, params={
            'key': self.key,
            'time': timestamp,
            'sign': sign
        }, data=data, files=files)
        print(res)
        if not parse:
            return res
        
        res = res.json()

        code = res['code']
        data = res['data']

        return code, data
    
    def _put(self, path: str, data: dict=None) -> Tuple[int, Union[int, str, float, bool, list, dict]]:
        if data is None:
            dict = {}

        sign, timestamp = self.auth_config.sign(path)
        res = requests.put(self.url+path, params={
            'key': self.key,
            'time': timestamp,
            'sign': sign
        }, data=data).json()

        code = res['code']
        data = res['data']

        return code, data
