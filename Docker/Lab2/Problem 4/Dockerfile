#base image
FROM node:alpine

# Create app directory
WORKDIR /node/weather-app

#copy data from src to working dir
COPY ./src /node/weather-app

#Install app dependencies 
COPY package*.json /node/weather-app   
#to ensure both package.json AND package-lock.json are copied
RUN npm install

#version argument
ARG APP_VERSION=latest

#envirnoment variable
ENV NODE_ENV=production

#8-
COPY /node/weather-app /var/weather-app

#change working dir
WORKDIR /var/weather-app

EXPOSE 3000

ENTRYPOINT ["./bin/www"]

CMD [ "node" ]