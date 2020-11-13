FROM tensorflow/tensorflow:latest

RUN python -m pip install --upgrade pip
RUN pip install tensorflow-text
RUN pip install t5

# setting up work directory
RUN mkdir /app
WORKDIR /app