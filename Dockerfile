FROM python:3.6

COPY requirements.txt requirements.txt
COPY src/pytorch2tensorflow.py src/pytorch2tensorflow.py

RUN pip3 install --upgrade pip \
    && pip3 install -r requirements.txt

ENTRYPOINT ["python", "src/pytorch2tensorflow.py"]