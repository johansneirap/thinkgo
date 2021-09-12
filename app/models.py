# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Area(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=70)

    class Meta:
        managed = False
        db_table = 'area'


class Cargo(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'cargo'


class Competencia(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=80)
    definicion = models.CharField(max_length=1000)
    tipo_competencia = models.ForeignKey('TipoCompetencia', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'competencia'


class CompetenciaPerfilevaluacion(models.Model):
    perfil_evaluacion = models.OneToOneField('PerfilEvaluacion', models.DO_NOTHING, primary_key=True)
    competencia = models.ForeignKey(Competencia, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'competencia_perfilevaluacion'
        unique_together = (('perfil_evaluacion', 'competencia'),)


class Evaluacion(models.Model):
    id = models.AutoField(primary_key=True)
    fecha_creacion = models.DateField()
    fecha_realizacion = models.DateField(blank=True, null=True)
    fase = models.BigIntegerField()
    estado = models.BigIntegerField()
    descripcion_accion1 = models.CharField(max_length=1000, blank=True, null=True)
    medicion_accion1 = models.CharField(max_length=1000, blank=True, null=True)
    competencia_accion1 = models.CharField(max_length=70, blank=True, null=True)
    descripcion_accion2 = models.CharField(max_length=1000, blank=True, null=True)
    medicion_accion2 = models.CharField(max_length=1000, blank=True, null=True)
    competencia_accion2 = models.CharField(max_length=70, blank=True, null=True)
    usuario_rut = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='usuario_rut')
    comentario_calibrador = models.CharField(max_length=500, blank=True, null=True)
    fase_0 = models.ForeignKey('Fase', models.DO_NOTHING, db_column='fase_id')  # Field renamed because of name conflict.

    class Meta:
        managed = False
        db_table = 'evaluacion'


class EvaluacionPregunta(models.Model):
    evaluacion = models.OneToOneField(Evaluacion, models.DO_NOTHING, primary_key=True)
    pregunta = models.ForeignKey('Pregunta', models.DO_NOTHING)
    nota_evaluador = models.BigIntegerField(blank=True, null=True)
    nota_evluado = models.BigIntegerField(blank=True, null=True)
    perfil_evaluacion = models.ForeignKey('PerfilEvaluacion', models.DO_NOTHING)
    competencia = models.ForeignKey('Competencia', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'evaluacion_pregunta'
        unique_together = (('evaluacion', 'pregunta', 'perfil_evaluacion', 'competencia'),)


class Fase(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=70)
    descripcion = models.CharField(max_length=500)

    class Meta:
        managed = False
        db_table = 'fase'


class FaseActual(models.Model):
    fecha_cambio = models.DateField(blank=True, null=True)
    fase_0 = models.ForeignKey(Fase, models.DO_NOTHING, db_column='fase_id')  # Field renamed because of name conflict.

    class Meta:
        managed = False
        db_table = 'fase_actual'


class Gerencia(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'gerencia'


class PerfilEvaluacion(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=70)

    class Meta:
        managed = False
        db_table = 'perfil_evaluacion'


class PerfilUsuario(models.Model):
    id = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'perfil_usuario'


class Pregunta(models.Model):
    id = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=255)
    orden = models.BigIntegerField()
    perfil_evaluacion = models.ForeignKey(PerfilEvaluacion, models.DO_NOTHING)
    competencia = models.ForeignKey(Competencia, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'pregunta'
        unique_together = (('id', 'perfil_evaluacion', 'competencia'),)


class Subgerencia(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=80)
    gerencia = models.ForeignKey(Gerencia, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'subgerencia'


class TipoCompetencia(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=70)

    class Meta:
        managed = False
        db_table = 'tipo_competencia'


class Usuario(models.Model):
    rut = models.CharField(primary_key=True, max_length=15)
    usuario = models.CharField(max_length=100)
    contrasena = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    fecha_ingreso = models.DateField()
    correo = models.CharField(max_length=50)
    evaluador = models.BigIntegerField(blank=True, null=True)
    calibrador = models.BigIntegerField(blank=True, null=True)
    cargo = models.ForeignKey(Cargo, models.DO_NOTHING)
    perfil_eval = models.ForeignKey(PerfilEvaluacion, models.DO_NOTHING)
    subgerencia = models.ForeignKey(Subgerencia, models.DO_NOTHING)
    perfil_usuario = models.ForeignKey(PerfilUsuario, models.DO_NOTHING)
    area = models.ForeignKey(Area, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'usuario'
