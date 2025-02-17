import * as path from "node:path";

import { Value } from "@sinclair/typebox/value";

import { ConfigSchema } from "@/schemas/config";

export default Value.Parse(ConfigSchema, {
  server: {
    port: Bun.env.SERVICE_PORT,
    hostname: Bun.env.SERVICE_HOST,
  },
  app: {
    name: Bun.env.APP_NAME,
    desc: Bun.env.APP_DESC,
    contact_email: Bun.env.APP_CONTACT_EMAIL,
  },
  cors: {
    "Access-Control-Allow-Origin": "*",
    "Access-Control-Allow-Headers": "*",
    "Access-Control-Allow-Methods": "GET, POST, OPTIONS",
    "Access-Control-Max-Age": "86400",
  },
  logging: {
    level: Bun.env.NODE_ENV === "production" ? "info" : "debug",
    logPath: path.join(__dirname, "..", "logs"),
    logToFile: Bun.env.LOG_TO_FILE === "true",
    loki: {
      host: Bun.env.LOKI_HOST,
      user: Bun.env.LOKI_USER,
      password: Bun.env.LOKI_PASSWORD,
      label: Bun.env.LOKI_LABEL,
    },
  },
  client: {
    useWorker: Bun.env.USE_WORKER === "true",
    workerHost: Bun.env.WORKER_HOST,
    workerHostTH: Bun.env.WORKER_HOST_TH,
    apiToken: Bun.env.API_TOKEN,
    sessionId: Bun.env.SESSION_ID_COOKIE,
  },
});
