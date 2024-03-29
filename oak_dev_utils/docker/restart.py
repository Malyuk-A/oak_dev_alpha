import shlex
import subprocess

from oak_dev_utils.docker.common import check_docker_service_status
from oak_dev_utils.docker.enums import OakestraDockerComposeService


def restart_docker_service(docker_service: OakestraDockerComposeService):
    docker_cmd = f"docker restart {docker_service}"
    subprocess.run(
        shlex.split(docker_cmd),
        check=True,
        stderr=subprocess.PIPE,
        stdout=subprocess.PIPE,
        text=True,
    )
    check_docker_service_status(docker_service, "restarted")
