import argparse
import os
import serial
import time

import txaio
from ocs import ocs_agent, site_config
from ocs.ocs_twisted import TimeoutLock

from socs.Lakeshore import Lakeshore425 as ls

class HWPPhasecompensationAgent:
    """Agent for interfacing with a phase compensation unit.

    Args:
        agent (ocs.ocs_agent.OCSAgent): Instantiated OCSAgent class for this Agent
        port (int): Path to USB device in `/dev/`
    """

    def __init__(self, agent, port):

        self.agent: ocs_agent.OCSAgent = agent
        self.log = agent.log
        self.lock = TimeoutLock()

        self.port = port
        self.dev = None

        self.f_sample = f_sample

        self.initialized = False
        self.take_data = False

        # Registers Temperature and Voltage feeds
        agg_params = {'frame_length': 60}
        self.agent.register_feed('mag_field',
                                 record=True,
                                 agg_params=agg_params,
                                 buffer_time=1)

def make_parser(parser=None):
    if parser is None:
        parser = argparse.ArgumentParser()

    pgroup = parser.add_argument_group('Agent Options')
    pgroup.add_argument('--port', type=str,
                        help="Path to USB node for the phase compensation unit.")
    return parser

if(direction == "off"):
  serPort = serial.Serial(port_name, 19200, timeout=1)
  relay_off = [0, 1, 2, 5, 6, 7]
  for i in relay_off:
    serPort.write(str.encode("relay off "+str(i)+"\n\r"))
  serPort.close()

if(direction == "forward"):
  serPort = serial.Serial(port_name, 19200, timeout=1)
  relay_on = [0, 1, 2]
  relay_off = [5, 6, 7]
  for i in relay_off:
    serPort.write(str.encode("relay off "+str(i)+"\n\r"))
  for i in relay_on:
    serPort.write(str.encode("relay on "+str(i)+"\n\r"))
  serPort.close()

if(direction == "reverse"):
  serPort = serial.Serial(port_name, 19200, timeout=1)
  relay_on = [0, 1, 2, 5, 6, 7]
  for i in relay_on:
    serPort.write(str.encode("relay on "+str(i)+"\n\r"))
  serPort.close()

if(direction == "stop"):
  serPort = serial.Serial(port_name, 19200, timeout=1)
  relay_on = [0, 1, 2, 5]
  relay_off = [6, 7]
  for i in relay_off:
    serPort.write(str.encode("relay off "+str(i)+"\n\r"))
  for i in relay_on:
    serPort.write(str.encode("relay on "+str(i)+"\n\r"))
  serPort.close()
