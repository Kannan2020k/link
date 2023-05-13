

#COPY start.sh /start.sh


FROM python:3.9-alpine

WORKDIR /app

COPY requirements.txt ./

RUN pip3 install -U pip && pip3 install -U -r requirements.txt

COPY . .

CMD ["python3","-m","Adarsh"]
