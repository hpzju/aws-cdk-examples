#!/usr/bin/env python3

from aws_cdk import core

from examples.examples_stack import ExamplesStack


app = core.App()
ExamplesStack(app, "examples")

app.synth()
