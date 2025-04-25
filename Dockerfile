# podman build --tag fastapi-ping:v1 .
# podman run --rm --interactive --tty --name fastapi-ping fastapi-ping:v1 --help
# podman run --rm --detach --tty --publish 8895:8000/tcp --name fastapi-ping fastapi-ping:v1 --log-level warning
# Use a smaller image
FROM docker.io/library/python:3.12-alpine

# Install the required Python modules
COPY requirements.txt /python_fastapi_ping/requirements.txt
RUN pip install --no-cache-dir -r /python_fastapi_ping/requirements.txt

# Copy the required source files for the project
COPY handlers/*.py /python_fastapi_ping/handlers/
COPY *.py /python_fastapi_ping/

# Set the working directory
WORKDIR /python_fastapi_ping

# Add a user account
# No need to run as root in the container
RUN addgroup -S appgroup \
    && adduser -S appuser -G appgroup

# Run all future commands as appuser
USER appuser

# Default port
EXPOSE 8000

# Set the command to run on start up
ENTRYPOINT ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]