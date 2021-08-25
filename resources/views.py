from django.shortcuts import render, redirect
from .models import FilesAdmin
from django.http import HttpResponse, Http404
from .forms import AddFilesAdmin
from .filters import FilesAdminFilter
# Create your views here.


def home(request):
    if request.method == 'POST':
        form = AddFilesAdmin(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('/')
    else:
        form = AddFilesAdmin()
    files = FilesAdmin.objects.all()
    myFilter = FilesAdminFilter(request.GET, queryset=files)
    files = myFilter.qs
    context = {'myFilter': myFilter, 'files': files, 'form': form}
    return render(request, "resources/files.html", context)


def download(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(
                fh.read(), content_type='application/adminUpload')
            response['Content-Disposition'] = 'inline;filename=' + \
                os.path.basename(file_path)
            return response

    raise Http404
