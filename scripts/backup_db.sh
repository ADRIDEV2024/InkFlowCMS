

DB_NAME="cms_db"
DB_USER="cms_user"
BACKUP_DIR="/backups"
DATE=$(date +"%Y-%m-%d_%H-%M-%S")
BACKUP_FILE="$BACKUP_DIR/$DB_NAME-$DATE.sql"

mkdir -p $BACKUP_DIR
pg_dump -U $DB_USER -F c $DB_NAME > $BACKUP_FILE

echo "Backup completado: $BACKUP_FILE"
