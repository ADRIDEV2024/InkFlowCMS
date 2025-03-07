#!/bin/bash

DB_NAME="cms_db"
DB_USER="cms_user"
BACKUP_FILE=$1  # Se pasa como argumento

if [ -z "$BACKUP_FILE" ]; then
  echo "Uso: $0 <archivo_de_respaldo.sql>"
  exit 1
fi

pg_restore -U $DB_USER -d $DB_NAME $BACKUP_FILE
echo "Restauración completada."
