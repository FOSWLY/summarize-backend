export class SharingUrlNotFoundError extends Error {
  constructor() {
    super("Sharing url not found");
  }
}

export class SharingAPITokenNotFoundError extends Error {
  constructor() {
    super("Server is missing an API token. This endpoint is unavailable");
  }
}
