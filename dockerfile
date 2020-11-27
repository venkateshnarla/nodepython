# base image
FROM node:12.18.3

# set working directory
WORKDIR /

COPY package*.json ./
RUN npm install
# install and cache app dependencies
COPY . .

# TODO: Execute tests
RUN npm run start


EXPOSE 80
EXPOSE 4000
EXPOSE 56088
EXPOSE 56089
EXPOSE 56090
CMD [ "npm" , "start" ]
COPY nginx.conf /etc/nginx/conf.d/default.conf