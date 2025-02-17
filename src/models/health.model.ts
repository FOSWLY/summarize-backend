import { t } from "elysia";

export const HealthResponse = t.Object({
  version: t.String(),
  status: t.Literal("ok", {
    default: "ok",
  }),
});
