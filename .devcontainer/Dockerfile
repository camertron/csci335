FROM mcr.microsoft.com/vscode/devcontainers/universal:focal

# Install basic build tools
RUN apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
    mysql-server

RUN echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] http://packages.cloud.google.com/apt cloud-sdk main" | tee -a /etc/apt/sources.list.d/google-cloud-sdk.list && \
    curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key --keyring /usr/share/keyrings/cloud.google.gpg add - && \
    apt-get update -y && \
    apt-get install google-cloud-cli google-cloud-sdk-gke-gcloud-auth-plugin -y

RUN curl -LO "https://dl.k8s.io/release/v1.26.3/bin/linux/amd64/kubectl" && \
    sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl

USER root
RUN service mysql start; \
    mysql -u root -e 'UPDATE mysql.user SET plugin = "mysql_native_password" WHERE user = "root" AND plugin IN ("unix_socket", "auth_socket"); FLUSH PRIVILEGES;'; \
    mysqladmin --host=127.0.0.1 --user=root password "password"
