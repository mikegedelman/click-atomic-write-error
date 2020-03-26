FROM python:3.7.3

WORKDIR /work

RUN pip install click>=7
COPY main.py /work

CMD ["python3", "/work/main.py"]
