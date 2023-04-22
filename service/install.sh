#!/bin/bash

if [[ $EUID -ne 0 ]]; then
   echo "Este script deve ser executado como root"
   exit 1
fi

# Define o nome do serviço e o caminho do script Python
SERVICE_NAME="meu_servico"
SCRIPT_PATH="/caminho/do/meu/script.py"

# Cria um arquivo de serviço para o systemd
SERVICE_FILE="/etc/systemd/system/${SERVICE_NAME}.service"
sudo touch $SERVICE_FILE

# Adiciona o conteúdo ao arquivo de serviço
sudo tee $SERVICE_FILE > /dev/null << EOF
[Unit]
Description=Meu serviço Python

[Service]
Type=simple
ExecStart=/usr/bin/python ${SCRIPT_PATH}
Restart=always
User=root

[Install]
WantedBy=multi-user.target
EOF

# Habilita e inicia o serviço
sudo systemctl enable $SERVICE_NAME
sudo systemctl start $SERVICE_NAME

# Verifica o status do serviço
sudo systemctl status $SERVICE_NAME
