FROM oven/bun:latest AS base
WORKDIR /usr/src/app

FROM base AS release
COPY package.json bun.lock tsconfig.json ./
COPY src src
RUN bun install

ENV SERVICE_PORT=3312
ENV LOG_TO_FILE=false
# ENV USE_WORKER="true"
# ENV WORKER_HOST="http://127.0.0.1:7674/browser"
# ENV WORKER_HOST_TH="http://127.0.0.1:7674/th"
# ENV API_TOKEN=""

ENTRYPOINT [ "bun", "run", "start" ]