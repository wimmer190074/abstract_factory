
from typing import List
from .._message import AbstractMessage
import json


class JsonMessage(AbstractMessage):
    def getMessages(self) -> List[object]:
        
