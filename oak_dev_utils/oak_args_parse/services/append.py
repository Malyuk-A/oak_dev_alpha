import argparse
from typing import Any

from oak_dev_utils.oak_args_parse.types import Subparsers
from oak_dev_utils.services.append import append_service


def prepare_services_append_argparser(services_subparsers: Subparsers) -> None:
    HELP_TEXT = "append a service to an already existing app"
    service_create_parser = services_subparsers.add_parser(
        "append",
        aliases=["a"],
        help=HELP_TEXT,
        description=HELP_TEXT,
        formatter_class=argparse.RawTextHelpFormatter,
    )
    service_create_parser.set_defaults(func=lambda _: append_service())
