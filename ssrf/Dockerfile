FROM python:3.11-alpine@sha256:af8fef83397b3886ed93d2c81bf3b4e70d39c0789c1c6feb1ecb86ca9bc42a0a

# ENV
ENV user chall
ENV port 8000

RUN adduser --disabled-password $user

RUN mkdir /app
ADD ./deploy/requirements.txt  /app/
WORKDIR /app
RUN pip install -r requirements.txt

ADD ./deploy/ /app

RUN chown $user:$user /app

# RUN
USER $user
EXPOSE $port

ENTRYPOINT ["python"]
CMD ["app.py"]