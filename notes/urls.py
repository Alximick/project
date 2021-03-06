from django.conf.urls import url
import notes.views

urlpatterns = [
    url(r'^$', notes.views.notes),
    url(r'^mynotes/$', notes.views.my_notes, name='my_notes'),
    url(r'^sort/ajax/$', notes.views.my_notes, name='ajax_sort'),
    url(r'^create/$', notes.views.note_create, name='create'),
    url(r'^category/get/(?P<category_id>\d+)/$', notes.views.category,
        name='category'),
    url(r'^filter/date/$', notes.views.filter_date, name='filter_date'),
    url(r'^filter/favorites/$', notes.views.filter_favorites, name='filter_favorite'),
    url(r'^note/(?P<id>.+)(/del/)$', notes.views.note_del, name='del'),
    url(r'^note/(?P<id>.+)(/edit/)$', notes.views.note_edit, name='edit'),
    url(r'^note/(?P<id>.+)(/addfavorites/)$', notes.views.addfavorites, name='addfavorites'),
    url(r'^note/(?P<id>.+)(/removefavorites/)$', notes.views.removefavorites, name='removefavorites'),
    url(r'^note/(?P<id>.+)$', notes.views.note, name='note'),

]
