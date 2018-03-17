from .device import Device
from .api import Api
from typing import List


class Remo:

    def __str__(self) -> str:
        return "\n".join([
            f"{x.ljust(20)}= {getattr(self, x)}" for x in [
                y for y in dir(self) if not y.startswith("__") and not y.endswith("__")
            ]
        ])

    def __init__(self, token: str):
        self.devices: List[Device] = None
        self.id: str = None
        self.nickname: str = None
        self.api: Api = Api(token=token)

        self.fetch_user()
        self.fetch_devices()

    def fetch_user(self) -> None:
        result: dict = self.api.get(path="/users/me")
        self.id = result["id"]
        self.nickname = result["nickname"]

    def fetch_devices(self) -> None:
        result: dict = self.api.get(path="/devices")

        self.devices = [Device(device_data=device) for device in result]

        [print(device) for device in self.devices]