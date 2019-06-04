FROM nikolaik/python-nodejs

ADD . /app

WORKDIR /app

# Install our flask app dependencies
RUN pip install -r requirements.txt

# install install npm modules and build bundle
WORKDIR /app/static

RUN npm install
RUN npm run build

WORKDIR /app

# Run the app
EXPOSE 5000

# give main.app execution privileges due to ERRNO 8 when running flask app
RUN chmod 644 main.py
ENTRYPOINT ["python", "main.py"]