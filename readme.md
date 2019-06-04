#CityLibraries
Simple web application build in Python flask and React to allow students search in multiple
libraries at the same time. It also allow users to share their books of interest of one week
with everyone else on the platform


## Install python dependencies:
```sh
python -m pip install -r requirements
```

## Create Web bundle for the frontend:
```sh
cd static
npm install
npm run build
```
## Run the application
```sh
python main.py
```
Navigate to http://localhost:5000

## Use docker
```sh
docker build -t cityapp .
docker run -p 5000:5000 cityapp
```

## Run the tests
```sh
python -m unittest
```

