# Academic System

Backend inicial en **Django** conectado a **MySQL en Aiven**, con los modelos Carrera, Instructor, Estudiante, Curso y Matrícula.

## Requisitos
- Python 3.10 o superior
- Git
- Un servicio MySQL en Aiven (host, puerto, usuario, contraseña y certificado `ca.pem`)

## Instalación
```bash
git clone <URL_DEL_REPOSITORIO>
cd academic_system

python -m venv venv
venv\Scripts\activate          # Windows
# source venv/bin/activate     # Linux / macOS

pip install -r requirements.txt
```

## Configuración
1. Copia `.env.example` como `.env` y completa los datos de tu base en Aiven.
2. Descarga el certificado CA desde el panel de Aiven y guárdalo como `ca.pem` en la raíz del proyecto.

## Migraciones
```bash
python manage.py makemigrations academic
python manage.py migrate
```

## Ejecución
```bash
python manage.py createsuperuser
python manage.py runserver
```
Abre http://127.0.0.1:8000/admin para gestionar las tablas desde Django Admin.

## Modelos
| Modelo | Campos principales |
|---|---|
| Carrera | nombre, codigo, duracion, modalidad, activa, fecha_creacion |
| Instructor | nombre, apellido, correo, telefono, especialidad, salario, activo |
| Estudiante | nombre, apellido, correo, documento, edad, direccion, telefono, activo |
| Curso | nombre, codigo, descripcion, intensidad_horaria, nivel, activo, carrera, instructor |
| Matricula | fecha_matricula, periodo, estado, nota_final, observaciones, estudiante, curso |

Relaciones: un Curso pertenece a una Carrera y tiene un Instructor; una Matrícula une un Estudiante con un Curso.

## Estructura
```
academic_system/
├── manage.py
├── requirements.txt
├── config/        # configuración del proyecto
└── academic/      # aplicación con modelos y admin
```
