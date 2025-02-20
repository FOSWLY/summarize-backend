import fs from "node:fs/promises";

import { Elysia } from "elysia";
import { swagger } from "@elysiajs/swagger";
import { cors } from "@elysiajs/cors";
import { HttpStatusCode } from "elysia-http-status-code";

import config from "./config";
import { log } from "./logging";

import health from "./controllers/health";
import summarizeController from "./controllers/summarize";
import sharingController from "./controllers/sharing";
import { SharingAPITokenNotFoundError, SharingUrlNotFoundError } from "./errors";

if (config.logging.logToFile && !(await fs.exists(config.logging.logPath))) {
  await fs.mkdir(config.logging.logPath, { recursive: true });
  log.info(`Created log directory`);
}

const app = new Elysia({
  prefix: "/v2",
})
  .use(
    swagger({
      path: "/docs",
      scalarCDN: config.app.scalarCDN,
      scalarConfig: {
        spec: {
          url: "/v2/docs/json",
        },
      },
      documentation: {
        info: {
          title: config.app.name,
          description: config.app.desc,
          version: config.app.version,
          license: {
            name: config.app.license,
          },
          contact: {
            name: "Developer",
            url: config.app.github_url,
            email: config.app.contact_email,
          },
        },
      },
    }),
  )
  .use(HttpStatusCode())
  .use(cors(config.cors))
  .error({
    SHARING_URL_NOT_FOUND: SharingUrlNotFoundError,
    SHARING_API_TOKEN_NOT_FOUND: SharingAPITokenNotFoundError,
  })
  .onError(({ set, code, error, httpStatus }) => {
    switch (code) {
      case "NOT_FOUND":
        return {
          detail: "Route not found :(",
        };
      case "SHARING_URL_NOT_FOUND":
        set.status = httpStatus.HTTP_400_BAD_REQUEST;
        break;
      case "SHARING_API_TOKEN_NOT_FOUND":
        set.status = httpStatus.HTTP_503_SERVICE_UNAVAILABLE;
        break;
      case "VALIDATION":
        return error.all;
    }

    log.error(
      {
        message: error.message,
      },
      code,
    );

    return {
      error: error.message,
    };
  })
  .use(health)
  .use(summarizeController)
  .use(sharingController)
  .listen({
    port: config.server.port,
    hostname: config.server.hostname,
  });

log.info(`🦊 Elysia is running at ${app.server?.hostname}:${app.server?.port}`);
