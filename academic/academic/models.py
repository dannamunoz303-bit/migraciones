from django.db import models


class Carrera(models.Model):
    MODALIDADES = [
        ("presencial", "Presencial"),
        ("virtual", "Virtual"),
        ("mixta", "Mixta"),
    ]
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=20, unique=True)
    duracion = models.PositiveIntegerField(help_text="Duración en semestres")
    modalidad = models.CharField(max_length=20, choices=MODALIDADES)
    activa = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.codigo} - {self.nombre}"


class Instructor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20, blank=True)
    especialidad = models.CharField(max_length=100)
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    documento = models.CharField(max_length=20, unique=True)
    edad = models.PositiveSmallIntegerField()
    direccion = models.CharField(max_length=200, blank=True)
    telefono = models.CharField(max_length=20, blank=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Curso(models.Model):
    NIVELES = [
        ("basico", "Básico"),
        ("intermedio", "Intermedio"),
        ("avanzado", "Avanzado"),
    ]
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=20, unique=True)
    descripcion = models.TextField(blank=True)
    intensidad_horaria = models.PositiveIntegerField(help_text="Horas totales")
    nivel = models.CharField(max_length=20, choices=NIVELES)
    activo = models.BooleanField(default=True)
    # Relaciones (no listadas en el enunciado, necesarias para conectar las tablas)
    carrera = models.ForeignKey(Carrera, on_delete=models.PROTECT, related_name="cursos")
    instructor = models.ForeignKey(Instructor, on_delete=models.SET_NULL, null=True, blank=True, related_name="cursos")

    def __str__(self):
        return f"{self.codigo} - {self.nombre}"


class Matricula(models.Model):
    ESTADOS = [
        ("activa", "Activa"),
        ("aprobada", "Aprobada"),
        ("reprobada", "Reprobada"),
        ("cancelada", "Cancelada"),
    ]
    fecha_matricula = models.DateField()
    periodo = models.CharField(max_length=20, help_text="Ej: 2026-2")
    estado = models.CharField(max_length=20, choices=ESTADOS, default="activa")
    nota_final = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True)
    observaciones = models.TextField(blank=True)
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE, related_name="matriculas")
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name="matriculas")

    class Meta:
        verbose_name = "matrícula"
        verbose_name_plural = "matrículas"
        unique_together = ("estudiante", "curso", "periodo")

    def __str__(self):
        return f"{self.estudiante} - {self.curso} ({self.periodo})"
