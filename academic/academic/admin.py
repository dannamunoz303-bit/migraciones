from django.contrib import admin

from .models import Carrera, Curso, Estudiante, Instructor, Matricula


@admin.register(Carrera)
class CarreraAdmin(admin.ModelAdmin):
    list_display = ("codigo", "nombre", "duracion", "modalidad", "activa")
    list_filter = ("modalidad", "activa")
    search_fields = ("nombre", "codigo")


@admin.register(Instructor)
class InstructorAdmin(admin.ModelAdmin):
    list_display = ("nombre", "apellido", "correo", "especialidad", "activo")
    list_filter = ("activo",)
    search_fields = ("nombre", "apellido", "correo")


@admin.register(Estudiante)
class EstudianteAdmin(admin.ModelAdmin):
    list_display = ("nombre", "apellido", "documento", "correo", "activo")
    list_filter = ("activo",)
    search_fields = ("nombre", "apellido", "documento", "correo")


@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ("codigo", "nombre", "nivel", "carrera", "instructor", "activo")
    list_filter = ("nivel", "activo", "carrera")
    search_fields = ("nombre", "codigo")


@admin.register(Matricula)
class MatriculaAdmin(admin.ModelAdmin):
    list_display = ("estudiante", "curso", "periodo", "estado", "nota_final", "fecha_matricula")
    list_filter = ("estado", "periodo")
