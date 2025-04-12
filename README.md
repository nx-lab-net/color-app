# Verify Service Catalog

This catalog tracks all resources for the Verify product across environments. Use this to find details about APIs, databases, frontends, and more.

## Catalog

| Resource Name | Type          | Description                       | Environment | Status  | Owner         | Contact            | Notes                |
|---------------|---------------|-----------------------------------|-------------|---------|---------------|--------------------|----------------------|
| Verify-API    | API           | Handles identity verification     | Dev         | Active  | Identity Team | #identity-team     | Testing v2.1         |
| Verify-API    | API           | Handles identity verification     | Prod        | Active  | Identity Team | #identity-team     | [API Docs](#)        |
| Verify-DB     | Database      | Stores verification data          | Prod        | Active  | DB Team       | db@example.com     | Postgres v15         |
| Verify-UI     | Frontend      | User interface for verification   | Staging     | Testing | UI Team       | #ui-team           | Deployed: 4/10/2025  |
| Verify-Queue  | Message Queue | Queues verification requests      | Dev         | Inactive| Infra Team    | #infra             | RabbitMQ v3.9        |
| Verify-Auth   | Service       | Authenticates users               | Prod        | Active  | Security Team | #security          | Keycloak v20         |

## How to Use
- **Search**: Use **Ctrl+F** to find resources or environments.
- **Update**: Edit this file via GitHub or submit a pull request.
- **Contact**: Reach out to owners via listed contact methods.

## Legend
- **Type**: API, Database, Frontend, Queue, Service, etc.
- **Environment**: Dev, Staging, Prod.
- **Status**: Active, Inactive, Testing, Deprecated.
- **Notes**: Links to docs, versions, or other details.

**Last Updated**: April 12, 2025

## Questions?
Ping the DevOps team in #devops on Slack.
