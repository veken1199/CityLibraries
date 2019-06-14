[![CircleCI](https://circleci.com/gh/veken1199/CityLibraries.svg?style=svg)](https://circleci.com/gh/veken1199/CityLibraries)

# CityLibraries
Simple web application build in Python flask and React to allow students to search in multiple
public libraries at the same time. It also allows users to share their books of interest for one week
with everyone else on the platform

![untitled](https://user-images.githubusercontent.com/15069757/52685848-4338e200-2f19-11e9-951f-a7d7db797109.gif)


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

