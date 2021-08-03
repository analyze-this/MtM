from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
	pass
	# add additional fields here later


class WorkGroups(models.Model):
	"""
	Группа работ
	"""
	work_group = models.CharField(max_length=150, blank=True, verbose_name='Группа работ')

	def __str__(self):
		return self.work_group

	class Meta:
		verbose_name = 'Группа работ'
		verbose_name_plural = 'Группы работ'


class WorkTypes(models.Model):
	"""
	Вид работ, который принадлежит определенной группе работ со ссылками на названия нормативных документов
	"""
	work_type = models.CharField(max_length=150, blank=True, verbose_name='Вид работ')
	work_group = models.ForeignKey('WorkGroups', on_delete=models.CASCADE, verbose_name='Группа работ')
	control_stage = models.ManyToManyField("ControlStage", through='ControlTypes')
	scope_of_control = models.ManyToManyField("ScopeOfControl", through='ControlTypes')
	control_method = models.ManyToManyField("ControlMethod", through='ControlTypes')

	def __str__(self):
		return self.work_type

	class Meta:
		verbose_name = 'Вид работ'
		verbose_name_plural = 'Виды работ'


class ControlStage(models.Model):
	"""Стадии производства для контроля качества"""
	control_stage = models.CharField(max_length=120, verbose_name="Стадия контроля")

	def __str__(self):
		return self.control_stage

	class Meta:
		verbose_name = 'Стадия контроля'
		verbose_name_plural = 'Стадии контроля'


class ScopeOfControl(models.Model):
	"""Объем контроля качества"""
	scope_of_control = models.CharField(max_length=120, verbose_name="Объем контроля")

	def __str__(self):
		return self.scope_of_control

	class Meta:
		verbose_name = 'Объем контроля'
		verbose_name_plural = 'Объем контроля'


class ControlMethod(models.Model):
	"""Методы контроля качества"""
	control_method = models.CharField(max_length=120, verbose_name="Метод контроля")

	def __str__(self):
		return self.control_method

	class Meta:
		verbose_name = 'Метод контроля'
		verbose_name_plural = 'Методы контроля'


class ControlTypes(models.Model):
	work_type = models.ForeignKey('WorkTypes', on_delete=models.CASCADE)
	number = models.PositiveIntegerField(verbose_name="Номер по порядку")
	control_stage = models.ForeignKey("ControlStage", on_delete=models.CASCADE)
	scope_of_control = models.ForeignKey("ScopeOfControl", on_delete=models.CASCADE)
	control_method = models.ForeignKey("ControlMethod", on_delete=models.CASCADE)

	def __str__(self):
		return "Controlled parameter"

	class Meta:
		verbose_name = 'Номер по порядку'
		verbose_name_plural = 'Номера по порядку'
