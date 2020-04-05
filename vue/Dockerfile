FROM node:11-alpine

WORKDIR /app

COPY docker-entrypoint.sh .

COPY ./dot-files .

ENTRYPOINT ["/app/docker-entrypoint.sh"]

CMD ["npm", "run", "dev"]
