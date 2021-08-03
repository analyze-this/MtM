from django.shortcuts import render

from mm.models import ControlTypes, WorkTypes, ControlStage


def index(request):
	title = "Work types"
	work_types = WorkTypes.objects.all()
	return render(request, template_name='index.html', context={'title': title, 'work_types': work_types})


def param(request, work_type_id):
	title = "Controlled parameters"
	params = ControlTypes.objects.filter(work_type_id=work_type_id)
	works = WorkTypes.objects.filter(id=work_type_id)

	# print(works.control_stage__set.all())

	return render(request, template_name='param.html', context={'title': title, 'works': works, 'params': params})


