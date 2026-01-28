FROM python:3.12-slim

WORKDIR /app

COPY pyproject.toml .
COPY identified/ identified/

RUN pip install --no-cache-dir .

# Bake the existing database into the image
RUN mkdir -p /app/var/identified-instance
COPY identified.sqlite /app/var/identified-instance/identified.sqlite

ENV FLASK_APP=identified
ENV SECRET_KEY=change-me
ENV INSTANCE_PATH=/app/var/identified-instance

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "identified:create_app()"]
