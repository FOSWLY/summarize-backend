import { Elysia } from "elysia";

import { NeuroClient, NeuroWorkerClient } from "@toil/neurojs";

import config from "@/config";
import {
  GetSharingBody,
  GetSharingResponse,
  GetSharingUrlAPITokenNotFound,
  GetSharingUrlBody,
  GetSharingUrlNotFound,
  GetSharingUrlResponse,
} from "@/models/sharing.model";
import { SharingAPITokenNotFoundError, SharingUrlNotFoundError } from "@/errors";

const {
  client: { useWorker, workerHost, workerHostTH, sessionId: sessionIdCookie, apiToken },
} = config;

const client = useWorker
  ? new NeuroWorkerClient({
      host: workerHost,
      hostTH: workerHostTH,
      sessionIdCookie,
      apiToken,
    })
  : new NeuroClient({
      sessionIdCookie,
      apiToken,
    });

export default new Elysia()
  .post(
    "/sharing",
    async ({ body: { token } }) => {
      return (await client.getSharingContent({
        token,
      })) as unknown as GetSharingResponse;
    },
    {
      body: GetSharingBody,
      response: {
        200: GetSharingResponse,
      },
      detail: {
        summary: "Get sharing content by token",
        tags: ["Sharing"],
      },
    },
  )
  .post(
    "/sharing-url",
    async ({ body: { url } }) => {
      if (!apiToken) {
        throw new SharingAPITokenNotFoundError();
      }

      try {
        return await client.getSharingUrl({
          url,
        });
      } catch {
        throw new SharingUrlNotFoundError();
      }
    },
    {
      body: GetSharingUrlBody,
      response: {
        200: GetSharingUrlResponse,
        404: GetSharingUrlNotFound,
        503: GetSharingUrlAPITokenNotFound,
      },
      detail: {
        summary: "Get sharing url",
        tags: ["Sharing"],
      },
    },
  );
