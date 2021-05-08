FROM nginx:alpine

RUN mkdir /logs
RUN rm /etc/nginx/conf.d/default.conf

COPY nginx.conf /etc/nginx/conf.d/default.conf
