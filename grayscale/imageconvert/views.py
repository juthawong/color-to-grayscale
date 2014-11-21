from django.views.generic.edit import CreateView
from django.http import HttpResponse

from .models import Image
from .tasks import handle_upload, convert_to_gray

import json


class HomeView(CreateView):
    model = Image
    fields = ['color_file']
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['object_list'] = self.model.objects.all()
        return context

    def render_to_json_response(self, context, **response_kwargs):
        data = json.dumps(context)
        response_kwargs['content_type'] = 'application/json'
        return HttpResponse(data, **response_kwargs)

    def form_invalid(self, form):
        response = super(CreateView, self).form_invalid(form)
        if self.request.is_ajax():
            return self.render_to_json_response(form.errors, status=400)
        else:
            return response

    def form_valid(self, form):
        response = super(CreateView, self).form_valid(form)
        task_id = handle_upload(self.object)
        if self.request.is_ajax():
            data = {
                'pk': self.object.pk,
                'task_id': task_id
            }
            return self.render_to_json_response(data)
        else:
            return response


def task_status(request, task_id):
    task = convert_to_gray.AsyncResult(task_id)
    return HttpResponse(task.status)


def task_result(request, task_id):
    task = convert_to_gray.AsyncResult(task_id)
    if task.status == 'SUCCESS':
        return HttpResponse(task.get())
    else:
        return HttpResponse("nil")
