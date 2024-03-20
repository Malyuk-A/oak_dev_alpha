import json

import requests

from oak_dev_utils.applications.get import get_applications
from oak_dev_utils.util.api import check_api_response, create_api_query
from oak_dev_utils.util.common import DEV_UTILS_PATH


def append_service() -> None:
    sla_file_name = "single_service.SLA.json"
    SLA = ""
    with open(DEV_UTILS_PATH / "util" / "SLAs" / sla_file_name, "r") as f:
        SLA = json.load(f)

    current_application = get_applications()[0]
    service_id = current_application["microservices"][0]

    # Note simply updating the app does not work - the service is not created in the DB, etc.
    # #url, headers, data = create_api_query(f"/api/application/{application_id}", data=current_application)

    url, headers, data = create_api_query(f"/api/service/{service_id}", data=SLA)
    response = requests.put(url, headers=headers, json=data)
    check_api_response(response, what_should_happen="Apend service")
