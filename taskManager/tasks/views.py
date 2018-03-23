from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils import timezone
from django.views import generic

from .models import Note, Priority, Status, Task
# Create your views here.

class IndexView(generic.ListView):
    model = Task

    template_name = 'tasks/index.html'
    context_object_name = 'active_tasks_list'

    def get_queryset(self):
        """Return active tasks."""
        return Task.objects.order_by('-creation_date')

 #   def get_contex_data(self, **kwargs ):
 #       context=super(IndexView, self ).get_context_data( **kwargs )
 ##       context['notes']= Note.objects.filter(fk_task=self.pk)
 #       #context['notes']= self.model.objects.filter(fk_task=self.pk)
 #       return context

class DetailView( generic.DetailView ):
    model = Task
    template_name = 'tasks/detail.html'

#class ResultsView(generic.DetailView):
#    model = Question
#    template_name = 'polls/results.html'
#
#def vote(request, question_id):
#    question = get_object_or_404(Question, pk=question_id)
#    try:
#        selected_choice = question.choice_set.get(pk=request.POST['choice'])
#    except (KeyError, Choice.DoesNotExist):
#        # Redisplay the question voting form.
#        return render(request, 'polls/detail.html', {
#            'question': question,
#            'error_message': "You didn't select a choice.",
#        })
#    else:
#        selected_choice.votes += 1
#        selected_choice.save()
#        # Always return an HttpResponseRedirect after successfully dealing
#        # with POST data. This prevents data from being posted twice if a
#        # user hits the Back button.
#        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
