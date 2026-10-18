FROM python:3.14-slim

WORKDIR /app


RUN apt-get update \
    && apt-get install -y --no-install-recommends curl ca-certificates gnupg \
    && curl -sSL -O https://packages.microsoft.com/config/debian/$(. /etc/os-release && echo "$VERSION_ID" | cut -d. -f1)/packages-microsoft-prod.deb \
    && dpkg -i packages-microsoft-prod.deb \
    && rm packages-microsoft-prod.deb \
    && apt-get update \
    && ACCEPT_EULA=Y apt-get install -y --no-install-recommends msodbcsql18 unixodbc-dev libgssapi-krb5-2 \
    && rm -rf /var/lib/apt/lists/*

COPY backend/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY backend ./backend
COPY frontend ./frontend

WORKDIR /app/backend

EXPOSE 5000

CMD ["python", "app.py"]