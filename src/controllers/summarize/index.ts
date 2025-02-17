import { Elysia } from "elysia";

import { NeuroClient, NeuroWorkerClient } from "@toil/neurojs";

import config from "@/config";
import {
  ArticleSummarizeBody,
  TextSummarizeBody,
  VideoSummarizeBody,
  TextSummarizeResponse,
  ArticleSummarizeResponse,
  VideoSummarizeResponse,
} from "@/models/summarize.model";

const {
  client: { useWorker, workerHost, workerHostTH, sessionId: sessionIdCookie },
} = config;

const client = useWorker
  ? new NeuroWorkerClient({
      host: workerHost,
      hostTH: workerHostTH,
      sessionIdCookie,
    })
  : new NeuroClient({
      sessionIdCookie,
    });

export default new Elysia().group("/summarize", (app) =>
  app
    .post(
      "/text",
      async ({ body: { text, sessionId, bypassCache } }) => {
        return (await client.summarizeText({
          text,
          extraOpts: {
            sessionId,
            bypassCache,
          },
        })) as unknown as TextSummarizeResponse;
      },
      {
        body: TextSummarizeBody,
        response: {
          200: TextSummarizeResponse,
        },
        detail: {
          summary: "Summarize text",
          tags: ["Summarize"],
        },
      },
    )
    .post(
      "/article",
      async ({ body: { url, sessionId, bypassCache } }) => {
        return (await client.summarizeArticle({
          url,
          extraOpts: {
            sessionId,
            bypassCache,
          },
        })) as unknown as ArticleSummarizeResponse;
      },
      {
        body: ArticleSummarizeBody,
        response: {
          200: ArticleSummarizeResponse,
        },
        detail: {
          summary: "Summarize article",
          tags: ["Summarize"],
        },
      },
    )
    .post(
      "/video",
      async ({ body: { url, language, videoTitle, sessionId, bypassCache } }) => {
        return (await client.summarizeVideo({
          url,
          language,
          extraOpts: {
            sessionId,
            videoTitle,
            bypassCache,
          },
        })) as unknown as VideoSummarizeResponse;
      },
      {
        body: VideoSummarizeBody,
        response: {
          200: VideoSummarizeResponse,
        },
        detail: {
          summary: "Summarize video",
          tags: ["Summarize"],
        },
      },
    ),
);
