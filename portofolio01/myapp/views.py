from django.shortcuts import render, HttpResponse
from .forms import PostForm


# Create your views here.
def home(request):
    if request.method == 'POST':
        details = PostForm(request.POST)

        if details.is_valid():
            post = details.save(commit=False)
            post.save()
            return HttpResponse("data submitted successfully")

        else:
            return render(request, "home.html", {'form': details})

    else:
        form = PostForm(None)
        return render(request, 'home.html', {'form': form})
