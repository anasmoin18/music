from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from forms import SignUpForm

@csrf_protect
def sign_up(request):
    if request.method == 'POST':
        print request.POST
        data = request.POST.copy()
        data['username'] = data['username']
        form = SignUpForm(data)

        if form.is_valid():
            user = form.save()
            return render_to_response('gaana/sign_up_success.html')
    else:
        form = SignUpForm()

    return render_to_response('gaana/sign_up.html', {'form': form},
                              context_instance=RequestContext(request))

@csrf_protect
def login(request):
    return render_to_response('gaana/login.html', { 'user': request.user })

@csrf_protect
def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/login/')


@csrf_protect
def home(request):
    return render_to_response('gaana/home.html', { 'user': request.user })
