from django.shortcuts import render

# Create your views here.
def setsession(request):
    request.session['name']= 'Pratik'
    request.session.set_expiry(300)
    return render(request,'setsession.html')

def getsession(request):
    name = request.session.get('name',default='Guest')
    # keys = request.session.keys()
    # items = request.session.items()
    print(request.session.get_session_cookie_age())
    print(request.session.get_expiry_age())
    print(request.session.get_expiry_date())
    print(request.session.get_expire_at_browser_close())
    context={
        'name':name,
        # 'keys':keys,
        # 'items':items
    }
    return render(request,'getsession.html',context)


def deletesession(request):
    # if 'name' in request.session:
    #     del request.session['name']
    request.session.flush()
    request.session.clear_expired()
    return render(request,'deletesession.html')