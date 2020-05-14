from aws_cdk import core
import aws_cdk.aws_ec2 as ec2
import os

from utils.load_config import load_config


class ExampleStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # The code that defines your stack goes here


def get_config():
    cwd = os.path.abspath(os.path.dirname(__file__))
    config = load_config(os.path.join(cwd, "config.yml"))
    return config
