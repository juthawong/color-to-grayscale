FROM node

VOLUME /app/code
VOLUME /app/static

ADD bower.json   /app/fe/
ADD package.json /app/fe/

WORKDIR /app/fe

RUN npm install
RUN npm install -g bower
RUN npm install -g grunt-cli
RUN bower install --allow-root

# Ruby & Sass dependencies
RUN apt-get update
RUN apt-get install -y ruby
RUN gem install sass

ADD Gruntfile.coffee /app/fe/
