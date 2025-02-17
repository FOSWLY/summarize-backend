import { Type as t, type Static } from "@sinclair/typebox";

import { version } from "../../package.json";

export const LoggingLevel = t.Union(
  [
    t.Literal("info"),
    t.Literal("debug"),
    t.Literal("fatal"),
    t.Literal("error"),
    t.Literal("warn"),
    t.Literal("trace"),
  ],
  {
    default: "info",
  },
);

const license = "MIT";
const scalarCDN = "https://unpkg.com/@scalar/api-reference@1.25.118/dist/browser/standalone.js";

export const ConfigSchema = t.Object({
  server: t.Object({
    port: t.Number({ default: 3312 }),
    hostname: t.String({ default: "0.0.0.0" }),
  }),
  app: t.Object({
    name: t.String({ default: "[FOSWLY] Summarize" }),
    desc: t.String({
      default:
        "[FOSWLY] Summarize is a server that implements unified endpoints for summarize logic from @toil/neurojs library",
    }),
    version: t.Literal(version, { readOnly: true, default: version }),
    license: t.Literal(license, { readOnly: true, default: license }),
    github_url: t.String({
      default: "https://github.com/FOSWLY/summarize-backend",
    }),
    contact_email: t.String({ default: "me@toil.cc" }),
    scalarCDN: t.Literal(scalarCDN, { readOnly: true, default: scalarCDN }),
  }),
  cors: t.Object({
    "Access-Control-Allow-Origin": t.String({ default: "*" }),
    "Access-Control-Allow-Headers": t.String({ default: "*" }),
    "Access-Control-Allow-Methods": t.String({ default: "POST, GET, OPTIONS" }),
    "Access-Control-Max-Age": t.String({ default: "86400" }),
  }),
  logging: t.Object({
    level: LoggingLevel,
    logPath: t.String(),
    loki: t.Object({
      host: t.String({ default: "" }),
      user: t.String({ default: "" }),
      password: t.String({ default: "" }),
      label: t.String({ default: "summarize-backend" }),
    }),
  }),
  client: t.Object({
    // use yandex server directly by default
    useWorker: t.Boolean({ default: false }),
    workerHost: t.String({ default: "http://127.0.0.1:7674/browser" }),
    workerHostTH: t.String({ default: "http://127.0.0.1:7674/th" }),
    // allow get sharing url
    apiToken: t.Optional(t.String()),
    // use cookie Session_id instead of YaHMAC (summarize video support only YaHMAC)
    sessionId: t.Optional(t.String()),
  }),
});

export type ConfigSchemaType = Static<typeof ConfigSchema>;
