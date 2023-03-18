# TLC pipeline setup instructions

## Development mode

Quick setup instructions for booting the project in development and production mode.

### Development Environment

#### Getting started

1. Copy the environment variable to environment local: `cp .env .env.local`
2. Start the datasource services: `docker compose --profile datasource up -d`

#### Adminer

**_NOTE:_** Server name on Adminer is the mysql service name on docker-compose file, mysql. User is root and password is defined in your `env.local`
