FROM node:lts-alpine
 
WORKDIR /app

COPY package.json package-lock.json ./
RUN npm install


COPY . ./
EXPOSE 5000