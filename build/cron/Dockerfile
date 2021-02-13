FROM python:3.9-alpine3.13

WORKDIR /app


RUN mkdir -p /app
RUN adduser -Ds /bin/ash python
RUN chown -R python:python /app
RUN chmod 755 /app

COPY --chown=python:python ./cron/requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

COPY --chown=python:python ./build/cron/entrypoint /entrypoint
RUN sed -i 's/\r$//g' /entrypoint
RUN chmod +x /entrypoint

USER python


ENTRYPOINT ["sh", "/entrypoint"]
