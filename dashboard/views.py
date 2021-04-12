from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.db.models import Q
from .models import (HmisStatePw,PopuStaticData, HmisStChldImmunzt, HmisStChldDisease,TargetAchieved,Hmis10IndiStlevel)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core import serializers
from django.core.serializers import serialize
from .serializers import HmisStatePwSerializer, HmisStCdSerializer, HmisStCiSerializer,TargetAcheivedSerializer
import json
from django.http import JsonResponse


# Create your views here.

def create_post_area(request, fy=None, dist_name=None):
    dist = request.GET.get('dist_name', dist_name) 
    areaSelected = request.GET.get('area')
    monthSelected = request.GET.get('month')
    fy_name = request.GET.get('fy', fy) 
    print(fy_name)

    pw_data = HmisStatePw.objects.filter(Q(state=areaSelected) & Q(year=fy_name) & Q(month=monthSelected))
    ci_data = HmisStChldImmunzt.objects.filter(Q(state=areaSelected) & Q(year=fy_name) & Q(month=monthSelected))
    cd_data = HmisStChldDisease.objects.filter(Q(state=areaSelected) & Q(year=fy_name) & Q(month=monthSelected))

    pw_json = json.dumps(HmisStatePwSerializer(pw_data,  many=True).data)
    ci_json = json.dumps(HmisStCiSerializer(ci_data,  many=True).data)
    cd_json = json.dumps(HmisStCdSerializer(cd_data,  many=True).data)
    context = {
        'pw_data':pw_json,
        'ci_data':ci_json,
        'cd_data':cd_json
    }

    return JsonResponse({'context':context, 'dist_name': areaSelected})

class DashboardView(TemplateView):
    def get(self,request):
       
        return render(request,'dashboard/dash.html')

class RegionOverview(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = 'login'
    def get(self,request):
        # username = request.user.username
        # fy_name = request.POST['fy_select']
      
        district_name ='India'
        pw_data = Hmis10IndiStlevel.objects.filter(Q(state='India') & Q(year='2019-2020') & Q(month='All'))
        ta_data = TargetAchieved.objects.filter(Q(year='2019-2020'))
        ci_data = HmisStChldImmunzt.objects.filter(Q(state='India') & Q(year='2019-2020') & Q(month='All'))
        cd_data = HmisStChldDisease.objects.filter(Q(state='India') & Q(year='2019-2020') & Q(month='All'))
        dt_name = Hmis10IndiStlevel.objects.values('state').distinct().order_by('state')
        month_name = HmisStatePw.objects.filter(Q(year='2019-2020')).values('month').distinct().order_by('month')
        data = Hmis10IndiStlevel.objects.filter(Q(year='2019-2020')).order_by('month').exclude(month='All')
        popu_data = PopuStaticData.objects.filter(Q(year='2019-2020'))
        print(data)
        st_name = Hmis10IndiStlevel.objects.values('state').distinct().order_by('state')
        fyList = Hmis10IndiStlevel.objects.values('year').distinct().order_by('year')
        jsondata = serializers.serialize('json',data)
        pw_json = serializers.serialize('json',pw_data)
        ci_json = serializers.serialize('json',ci_data)
        cd_json = serializers.serialize('json',cd_data)
        ta_json = serializers.serialize('json',ta_data)
        popu_json = serializers.serialize('json',popu_data)
        context = {
            'pw_data':pw_json,
            'ci_data':ci_json,
            'cd_data':cd_json,
            'ta_data':ta_json,
            'popu_data':popu_json
        }
        return render(request,'dashboard/dt_dashboard.html', {'data':jsondata, 'fy': '2019-2020', 'fyList':fyList, 'state':st_name,'dd_dt_data':dt_name, 'context':context, 'dist_name':district_name, 'months':month_name})


def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect('/')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request = request,
                    template_name = "dashboard/login.html",
                    context={"form":form})

def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("/")