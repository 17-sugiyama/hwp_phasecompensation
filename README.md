# hwp_phasecompensation
This is a socs agent to control the phase compensation unit (PCU) for cryogenic half-wave plates.\
Installation & operation guide:
https://docs.google.com/presentation/d/1jbdmJdoj98kQmAiez3OXtEXVjHxMvFFvU_FDXhJINuw/edit?usp=sharing

## How to operate PCU
```
from ocs import matched_client
import numpy as np
import time

pcu = matched_client.OCSClient('hwp-pcu', args=['--site-http=http://127.0.0.1:8001/call'])

# Enable the phase compensation
pcu.send_command(command='on_1')

# Hold the HWP
pcu.send_command(command='hold')

# Get the status
pcu.acq().session
```
