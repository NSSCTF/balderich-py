from __future__ import annotations

class Collection:
    """
    A base class fro representing all objects of a particular type on the server.
    """

    def __init__(self, client = None):
        self.client = client
