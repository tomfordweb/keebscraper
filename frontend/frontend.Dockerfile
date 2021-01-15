FROM node:latest
 
WORKDIR /app

COPY package.json package-lock.json ./
RUN npm install

COPY assets components layouts middleware pages plugins static store test  ./

COPY .babelrc jest.config.js jsconfig.json ./
EXPOSE 5000