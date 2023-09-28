# SOCS HWP PMX Agent
# socs Agent container for interacting with a PMX Kikusui power supply.

# Use socs base image
FROM simonsobs/socs

# Set the working directory to registry directory
WORKDIR /app/socs/agents/hwp_pcu/

# Copy this agent into the app/agents directory
COPY . .

# Run registry on container startup
ENTRYPOINT ["dumb-init", "python3", "-u", "agent.py"]

CMD ["--site-hub=ws://crossbar:8001/ws", \
     "--site-http=http://crossbar:8001/call"]
