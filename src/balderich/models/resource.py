from __future__ import annotations
from balderich.client import NSSClient

class Collection:
    """
    A base class fro representing all objects of a particular type on the server.
    """

    def __init__(self, client: NSSClient=None):
        self.client = client
