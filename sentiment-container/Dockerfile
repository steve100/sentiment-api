# Base image with Python and system tools
FROM python:3.10-slim

# Avoid interactive prompts
ENV DEBIAN_FRONTEND=noninteractive

# Install basic dependencies
RUN apt-get update 
RUN apt-get install -y git 
#RUN  rm -rf /var/lib/apt/lists/*

WORKDIR /app


# Install Python dependencies
RUN pip install --no-cache-dir --upgrade pip 

# Create a virtual environment -- less warnings
RUN python -m venv venv
RUN . venv/bin/activate


# Install the requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Install the gunicorn application
COPY app.py .


# Expose the app port
# Change this as necessary
EXPOSE 8000

# Start with gunicorn using config file
#CMD ["gunicorn", "-c", "gunicorn_config.py", "app:app"]
CMD ["gunicorn", "-w 4", "-b 0.0.0.0:8000", "app:app"]

