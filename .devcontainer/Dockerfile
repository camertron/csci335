FROM mcr.microsoft.com/vscode/devcontainers/universal:focal

# Install basic build tools
RUN apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
    mysql-server

USER root
RUN service mysql start; \
    mysql -u root -e 'UPDATE mysql.user SET plugin = "mysql_native_password" WHERE user = "root" AND plugin IN ("unix_socket", "auth_socket"); FLUSH PRIVILEGES;'; \
    mysqladmin --host=127.0.0.1 --user=root password "password"
