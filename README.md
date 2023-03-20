# TLC pipeline setup instructions

## Development mode

Quick setup instructions for booting the project in development and production mode.

### Development Environment

#### Getting started

1. Copy the environment variable to environment local: `cp .env .env.local`
2. Start the datasource services: `docker compose --profile datasource up -d`
3. run `docker compose --profile data-ingestion up -d` to ingest the initial data of tlc-yellow-cab in mysql database.
4. run `docker compose --profile warehouse up -d` to setup the dataware.

#### Adminer

**_NOTE:_** Server name on Adminer is the mysql service name on docker-compose file, mysql. User is root and password is defined in your `env.local`
