
echo "Actualizando código..."
git pull origin main

echo "Aplicando migraciones..."
python manage.py migrate

echo "Recopilando archivos estáticos..."
python manage.py collectstatic --noinput

echo "Reiniciando servicios..."
sudo systemctl restart gunicorn
sudo systemctl restart nginx

echo "✅ Despliegue completado."
