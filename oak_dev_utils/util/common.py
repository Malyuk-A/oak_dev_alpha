import enum
import pathlib

DEV_UTILS_PATH = pathlib.Path("/home/alex/oak_dev_alpha/oak_dev_utils")
IP = "192.168.178.44"
PORT = 10000
CORE_URL = f"http://{IP}:{PORT}"


class CustomEnum(enum.Enum):
    def __str__(self) -> str:
        return self.value
