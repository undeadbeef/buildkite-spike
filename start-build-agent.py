#!/usr/bin/env python

import docker
import os
import random
import socket
import sys

# If we cannot find the buildkit-agent configuration file, don't bother starting container
buildkite_cfg = os.path.join(os.environ['HOME'], '.buildkite-agent', 'buildkite-agent.cfg')
if not os.path.exists(buildkite_cfg):
  print('Buildkite agent configuration {} does not exist'.format(buildkite_cfg))
  sys.exit(1)

# Environment variables -- we honor proxy configuration
buildkite_environment = {
  'http_proxy': os.environ['http_proxy'],
  'https_proxy': os.environ['https_proxy'],
  'no_proxy': os.environ['no_proxy'],
}

# Mount the configuration file as read-only inside container
buildkite_volume = {
  buildkite_cfg: {
    'bind': '/buildkite/buildkite-agent.cfg',
    'mode': 'ro',
  },
}

# Generate random container ID including hostname
buildkite_name='buildkite-%s-%08x' % (socket.gethostname(), random.randrange(0x00000000, 0xffffffff))

client = docker.from_env()
client.containers.run('buildkite/agent:latest',
  detach=True,
  environment=buildkite_environment,
  hostname=buildkite_name,
  mem_limit='512m',
  name=buildkite_name,
  remove=True,
  use_config_proxy=True,
  volumes=buildkite_volume)
