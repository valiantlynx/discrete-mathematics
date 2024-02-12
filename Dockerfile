FROM python:3.11-slim

WORKDIR /code 

COPY ./requirements.txt ./

RUN apt-get update && apt-get install git -y

RUN pip install --no-cache-dir -r requirements.txt

COPY ./src ./src

EXPOSE 8000

ENV WAKATIME_API_KEY=waka_24758ef6-c9ff-41b0-bdcd-483f7289b05a

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
