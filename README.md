# Event-course2
it is manual without .devcontainer and docker compose. so, first run the lines below:
for running the broker: 
docker run -d \
  --name my-manual-rabbitmq \
  -p 5672:5672 \
  -p 15672:15672 \
  -e RABBITMQ_DEFAULT_USER=guest \
  -e RABBITMQ_DEFAULT_PASS=guest \
  rabbitmq:4-management

and then activate the venv and install the packages.

after these steps, you can run the consumer in one terminal and then producer in another one to see how they are passing messages in the system