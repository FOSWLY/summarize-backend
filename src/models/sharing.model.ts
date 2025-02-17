import { GetSharingUrlSuccess as GetSharingUrlSuccessOG } from "@toil/neurojs/typebox/thapi";
import {
  TextSummarizeResponse as TextSummarizeResponseOG,
  ArticleSummarizeResponse as ArticleSummarizeResponseOG,
  SharingVideoSummarizeResponse as SharingVideoSummarizeResponseOG,
} from "@toil/neurojs/typebox/yandex";
import { t, Static } from "elysia";

export const GetSharingBody = t.Object({
  token: t.String({
    description: "Token from sharing url",
    examples: ["hoOAM7gs"],
  }),
});

export const GetSharingUrlBody = t.Object({
  url: t.String({
    description: "Url for summarize",
    format: "uri",
    examples: ["https://habr.com/ru/news/729422"],
  }),
});

// use composite for fix binding types with elysia typebox
export const GetSharingResponse = t.Union([
  TextSummarizeResponseOG,
  ArticleSummarizeResponseOG,
  SharingVideoSummarizeResponseOG,
]);
export type GetSharingResponse = Static<typeof GetSharingResponse>;

export const GetSharingUrlResponse = t.Composite([GetSharingUrlSuccessOG]);
export type GetSharingUrlResponse = Static<typeof GetSharingUrlResponse>;

export const GetSharingUrlNotFound = t.Object({
  error: t.Literal("Sharing url not found", {
    default: "Sharing url not found",
  }),
});

export const GetSharingUrlAPITokenNotFound = t.Object({
  error: t.Literal("Server is missing an API token. This endpoint is unavailable", {
    default: "Server is missing an API token. This endpoint is unavailable",
  }),
});
