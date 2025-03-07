# InkFlowCMS

# ⚡⚡InkFlowCMS - Potencia y Flexibilidad para tu Contenido

InkFlowCMS es un **sistema de gestión de contenido (CMS)** basado en **Django y PostgreSQL**, diseñado para ofrecer una solución **rápida, escalable y modular**. Ideal para tus blogs, páginas informativas y cualquier plataforma que requiera un flujo dinámico de contenido.

---

## 🚀 Características Destacadas
✔ **Interfaz Moderna y Amigable** - Basado en Bootstrap para una experiencia intuitiva.
✔ **Gestión de Usuarios** - Registro, autenticación y roles con permisos avanzados.
✔ **Sistema de Blog Integrado** - Publicación de artículos con categorías y etiquetas.
✔ **Editor de Páginas Dinámicas** - Crea y edita contenido de manera flexible.
✔ **Gestión de Archivos** - Soporte para imágenes, documentos y otros formatos multimedia.
✔ **API REST con DRF** - Accede a los datos de forma programática con Django Rest Framework.
✔ **Seguridad y Rendimiento** - Uso de HTTPS 2.1, autenticación con tokens JWT y caché optimizado.

---

## 🛠 Instalación y Configuración

### **1️⃣ Clonar el Repositorio**
```sh
 git clone https://github.com/ADRIDEV2024/InkFlowCMS.git
 cd InkFlowCMS
```

### **2️⃣ Crear un Entorno Virtual**
```sh
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

### **3️⃣ Instalar Dependencias**
```sh
pip install -r requirements.txt
```

### **4️⃣ Configurar Variables de Entorno**
Crea un archivo `.env` con los datos de la base de datos PostgreSQL y configuraciones de seguridad:
```ini
DB_NAME=inkflow_db
DB_USER=admin
DB_PASSWORD=superseguro
DB_HOST=localhost
DB_PORT=5432
SECRET_KEY=tu_clave_secreta
DEBUG=True
```

### **5️⃣ Ejecutar Migraciones y Superusuario**
```sh
python manage.py migrate
python manage.py createsuperuser
```

### **6️⃣ Iniciar el Servidor**
```sh
python manage.py runserver
```
Después accede a **http://www.inkflowCMS.com/** para explorar InkFlowCMS.

---

## 🏗️ Estructura del Proyecto
```
InkFlowCMS/
│── CMS/        # Configuración principal de Django
│── apps/
│   ├── users/         # Gestión de usuarios y roles
│   ├── blog/          # Publicación y gestión de artículos
│   ├── pages/         # Creación y edición de páginas
│   ├── media/         # Gestión de archivos multimedia
│── templates/         # Plantillas HTML para la interfaz
│── static/            # Archivos CSS, JS e imágenes
│── scripts/           # Scripts de mantenimiento y automatización
│── logs/              # Registros del sistema y errores
│── README.md          # Documentación del proyecto
│── requirements.txt   # Lista de dependencias
│── manage.py          # Comando principal de Django
```

---

## 🔑 Acceso a la Administración
Una vez ejecutado el servidor, accede a **http://www.inkflowCMS.com/admin/** e inicia sesión con tu superusuario.

---

## 🛡️ Seguridad y Despliegue
- Para producción, configura `DEBUG=False` en `.env`.
- Usa **Let's Encrypt** para habilitar **HTTPS**.
- Implementa **Nginx** para mejor rendimiento.
- Realiza backups periódicos con `scripts/backup_db.sh`.

---

## 📄 Licencia y Contribuciones
InkFlowCMS es un proyecto **open-source**. Las contribuciones son bienvenidas a través de *pull requests* en el repositorio.

---


