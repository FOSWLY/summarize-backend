import {
  TextSummarizeResponse as TextSummarizeResponseOG,
  ArticleSummarizeResponse as ArticleSummarizeResponseOG,
  VideoSummarizeResponse as VideoSummarizeResponseOG,
} from "@toil/neurojs/typebox/yandex";
import { t, Static } from "elysia";

export const SessionId = t.String({
  description: "Session ID from first response",
  examples: ["xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"],
});

export const BypassCache = t.Boolean({
  description: "Bypass cache",
  default: false,
  examples: [false],
});

export const TextSummarizeBody = t.Object({
  text: t.String({
    minLength: 300,
    description: "Text for summarize",
    examples: ["Very long text with 300+ symbols"],
  }),
  sessionId: t.Optional(SessionId),
  bypassCache: t.Optional(BypassCache),
});

export const ArticleSummarizeBody = t.Object({
  url: t.String({
    description: "Url for summarize",
    format: "uri",
    examples: ["https://toil.cc"],
  }),
  sessionId: t.Optional(SessionId),
  bypassCache: t.Optional(BypassCache),
});

export const VideoSummarizeBody = t.Object({
  url: t.String({
    description: "Video url for summarize",
    format: "uri",
    examples: ["https://youtu.be/dQw4w9WgXcQ"],
  }),
  language: t.String({
    description: "Video language",
    default: "en",
  }),
  videoTitle: t.Optional(
    t.String({
      description: "Video title",
      examples: ["Rick Astley - Never Gonna Give You Up (Official Music Video)"],
    }),
  ),
  sessionId: t.Optional(SessionId),
  bypassCache: t.Optional(BypassCache),
});

// use composite for fix binding types with elysia typebox
export const TextSummarizeResponse = t.Composite([TextSummarizeResponseOG]);
export type TextSummarizeResponse = Static<typeof TextSummarizeResponse>;
export const ArticleSummarizeResponse = t.Composite([ArticleSummarizeResponseOG]);
export type ArticleSummarizeResponse = Static<typeof ArticleSummarizeResponse>;
export const VideoSummarizeResponse = t.Composite([VideoSummarizeResponseOG]);
export type VideoSummarizeResponse = Static<typeof VideoSummarizeResponse>;
