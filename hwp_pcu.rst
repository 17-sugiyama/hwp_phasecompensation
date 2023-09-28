.. highlight:: rst

.. _hwp_pcu:

=============
HWP PCU Agent
=============

.. argparse::
    :filename: ../socs/agents/hwp_pcu/agent.py
    :func: make_parser
    :prog: python3 agent.py

Configuration File Examples
---------------------------

Below are configuration examples for the ocs config file and for running the
Agent in a docker container.

OCS Site Config
```````````````

An example site-config-file block::

      {'agent-class': 'HWPPCUAgent',
       'instance-id': 'hwp-pcu',
       'arguments': [['--port', '/dev/ttyACM0'],
                     ['--mode', 'acq']]},

Docker Compose
``````````````

An example docker-compose configuration::
  ocs-hwp-pcu:
    image: simonsobs/socs:latest
    hostname: ocs-docker
    environment:
      - INSTANCE_ID=hwp-pcu
    device:
      - /dev/ttyACM0:/dev/ttyACM0
    volumes:
      - ${OCS_CONFIG_DIR}:/config:ro


Agent API
---------

.. autoclass:: socs.agents.hwp_pcu.agent.HWPPCUAgent
    :members:
