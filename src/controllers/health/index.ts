import { Elysia } from "elysia";

import config from "../../config";
import { HealthResponse } from "@/models/health.model";

export default new Elysia().group("/health", (app) =>
  app.get(
    "/",
    () => ({
      version: config.app.version,
      status: "ok" as const,
    }),
    {
      response: {
        200: HealthResponse,
      },
      detail: {
        summary: "Get health",
        tags: ["Health"],
      },
    },
  ),
);
