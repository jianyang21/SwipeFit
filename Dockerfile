FROM python:3.10

# Install dependencies
RUN apt-get update && apt-get install -y \
    wget curl unzip gnupg xvfb \
    && wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb \
    && apt install -y ./google-chrome-stable_current_amd64.deb \
    && rm google-chrome-stable_current_amd64.deb \
    && wget https://chromedriver.storage.googleapis.com/114.0.5735.90/chromedriver_linux64.zip \
    && unzip chromedriver_linux64.zip \
    && mv chromedriver /usr/bin/chromedriver \
    && chmod +x /usr/bin/chromedriver \
    && rm chromedriver_linux64.zip

WORKDIR /app
COPY . /app

RUN pip install -r requirements.txt

CMD ["xvfb-run", "python", "run_all.py"]
