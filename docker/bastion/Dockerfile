FROM python

WORKDIR /home

COPY bastion .

RUN pip install --upgrade pip
RUN pip install requests

CMD ["python", "bastion.py"]
