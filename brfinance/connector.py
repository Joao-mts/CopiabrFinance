from requests import Session
import requests




class CVMHttpClientConnector():

    def __init__(self) -> None:
        self.CONNECTOR = Session()

    def get_connector(self):
        return self.CONNECTOR
