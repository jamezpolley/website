from django.views.generic.list import ListView, TemplateResponseMixin
import wiki.models as models

class RecentChangesView(ListView, TemplateResponseMixin):

  template_name = "wiki/recent.html"
  allow_empty = True
  context_object_name = 'articles'
  paginate_by = 25

  def get_queryset(self):
    return models.Article.objects.filter(current_revision__deleted=False).order_by('-modified')

  def get_context_data(self, **kwargs):
    kwargs_listview = ListView.get_context_data(self, **kwargs)
    kwargs.update(kwargs_listview)
    return kwargs
