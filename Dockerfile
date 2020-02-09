FROM python:3
RUN apt-get update ; apt-get install -y fortune
RUN pip install requests
COPY fortunehook.py fortunehook.py
CMD python fortunehook.py
