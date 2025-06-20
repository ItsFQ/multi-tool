FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt
RUN apt-get update
RUN apt-get install -y iputils-ping

COPY . ./

EXPOSE 8501

CMD [ "streamlit", "run", "main.py" ]
