declare module "bun" {
  interface Env {
    SERVICE_HOST: string;
    SERVICE_PORT: number;
    APP_NAME: string;
    APP_DESC: string;
    APP_CONTACT_EMAIL: string;
    LOG_TO_FILE: string;
    LOKI_HOST: string;
    LOKI_USER: string;
    LOKI_PASSWORD: string;
    LOKI_LABEL: string;
    USE_WORKER: string;
    WORKER_HOST: string;
    WORKER_HOST_TH: string;
    API_TOKEN: string;
    SESSION_ID_COOKIE: string;
    NODE_ENV: string;
  }
}
