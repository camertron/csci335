FROM mcr.microsoft.com/vscode/devcontainers/universal:focal

# Install basic build tools
RUN apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
    mysql-server

USER root
RUN service mysql start; mysqladmin --user=root password "password"
