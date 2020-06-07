# https://pythonspeed.com/articles/activate-virtualenv-dockerfile/

FROM ubuntu:18.04
RUN apt-get update && apt-get install \
  -y --no-install-recommends python3 python3-virtualenv

RUN python3 -m virtualenv --python=/usr/bin/python3 /opt/venv

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m virtualenv --python=/usr/bin/python3 $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"



# Install dependencies:
COPY requirements.txt .
RUN pip install -r requirements.txt

ENV LISTEN_PORT=8000
EXPOSE 8000 
USER root
RUN chmod 755 /opt/venv/bin/activate

# Run the application:
COPY main.py .
COPY . .
CMD ["python", "main.py"]

# docker build -t lapredict .

# docker run -d -p 8000:8000 --name predictor lapredict
