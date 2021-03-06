from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.core import serializers
from django.core.serializers import serialize
from django.db.models import Q
from .models import (Hmis10IndiStlevel,GapAnalysis,PopuStaticData, TargetAchieved,HmisStChldImmunzt, HmisStChldDisease, PieState, PieChldDisease, PieChldImmunzt, GeojsonIndiaLevel,Hmis10IndiStlevel)

# Create your views here.

class HMISDashboardView(LoginRequiredMixin, TemplateView):
    template_name = "dashboard/dash_base.html"
    
class stack(LoginRequiredMixin, TemplateView):
    # st_name = Hmis10IndiStlevel.objects.values('state').distinct().order_by('state')

    # template_name = "hmis_dash/stack_area.html"
    def get(self,request,fy=None, dist_name = None):
        fy_name = request.GET.get('fy', fy)
        fyList = GapAnalysis.objects.values('year').distinct().order_by('year')
        data = GapAnalysis.objects.all().order_by('month').exclude(month='All')
        st_name = GapAnalysis.objects.values('state').distinct().order_by('state')
        monthName = Hmis10IndiStlevel.objects.order_by('month').values_list('month', flat=True).distinct()
        month=list(monthName)
        jsondata = serializers.serialize('json',data)
        # monthjson = serializers.serialize('json',monthName)
        return render(request,'hmis_dash/stack_area.html', {'data':jsondata,'state':st_name,'month':month,'fyList':fyList,'fy':fy_name})
    
class hmisBarChart(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = 'login'

    def get(self, request, fy= None, dist_name = None):
        district = request.GET.get('dist_name', dist_name) 
        fy_name = request.GET.get('fy', fy) 
        data = Hmis10IndiStlevel.objects.filter(Q(year=fy_name)).exclude(state='India')
        jsondata = serializers.serialize('json', data)
        
        return render(request,'hmis_dash/barchart.html', {'data':jsondata, 'fy': fy_name, 'dist_name': district})


class hmisLineChart(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = 'login'

    def get(self,request,fy=None):
        fy_name = request.GET.get('fy', fy) 
        data = Hmis10IndiStlevel.objects.filter(Q(year=fy_name)).order_by('month').exclude(month='All')
        st_name = Hmis10IndiStlevel.objects.values('state').distinct().order_by('state')
        jsondata = serializers.serialize('json',data)

        return render(request,'hmis_dash/linechart.html', {'data':jsondata, 'fy': fy_name, 'state':st_name})


class fyLine(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = 'login'

    def get(self,request,fy=None, dist_name = None):
        district = request.GET.get('dist_name', dist_name) 
        fy_name = request.GET.get('fy', fy) 
        data = Hmis10IndiStlevel.objects.all().order_by('month').exclude(month='All')
        st_name = Hmis10IndiStlevel.objects.values('state').distinct().order_by('state')
        fyList = Hmis10IndiStlevel.objects.values('year').distinct().order_by('year')
        jsondata = serializers.serialize('json',data)

        return render(request,'hmis_dash/fy_line.html', {'data':jsondata, 'fy': fy_name, 'fyList':fyList, 'dist_name': district, 'state':st_name})


class fyLineNum(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = 'login'

    def get(self,request,fy=None, dist_name = None):
        district = request.GET.get('dist_name', dist_name) 
        fy_name = request.GET.get('fy', fy) 
        data = Hmis10IndiStlevel.objects.all().order_by('month').exclude(month='All')
        st_name = Hmis10IndiStlevel.objects.values('state').distinct().order_by('state')
        fyList = Hmis10IndiStlevel.objects.values('year').distinct().order_by('year')
        jsondata = serializers.serialize('json',data)

        return render(request,'hmis_dash/fy_lineNum.html', {'data':jsondata, 'fy': fy_name, 'fyList':fyList, 'dist_name': district, 'state':st_name})


class hmisBarNumericChart(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = 'login'

    def get(self, request, fy= None, dist_name = None):
        district = request.GET.get('dist_name', dist_name) 
        fy_name = request.GET.get('fy', fy) 
        data = Hmis10IndiStlevel.objects.filter(Q(year=fy_name)).exclude(state='India')
        jsondata = serializers.serialize('json', data)
        
        return render(request,'hmis_dash/barNumericChart.html', {'data':jsondata, 'fy': fy_name, 'dist_name': district})


class hmisLineNumericChart(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = 'login'

    def get(self,request,fy=None):
        fy_name = request.GET.get('fy', fy) 
        data = Hmis10IndiStlevel.objects.filter(Q(year=fy_name)).order_by('month').exclude(month='All')
        st_name = Hmis10IndiStlevel.objects.values('state').distinct().order_by('state')
        jsondata = serializers.serialize('json',data)

        return render(request,'hmis_dash/lineNumericChart.html', {'data':jsondata, 'fy': fy_name, 'state':st_name})


class chldImmuBar(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = 'login'

    def get(self, request, fy= None, dist_name = None):
        district = request.GET.get('dist_name', dist_name) 
        fy_name = request.GET.get('fy', fy) 
        data = HmisStChldImmunzt.objects.filter(Q(year=fy_name)).exclude(state='India')
        jsondata = serializers.serialize('json', data)
        
        return render(request,'hmis_dash/chldImmuBar.html', {'data':jsondata, 'fy': fy_name, 'dist_name': district})


class chldImmuLine(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = 'login'

    def get(self,request,fy=None):
        fy_name = request.GET.get('fy', fy) 
        data = HmisStChldImmunzt.objects.filter(Q(year=fy_name)).order_by('month').exclude(month='All')
        st_name = HmisStChldImmunzt.objects.values('state').distinct().order_by('state')
        jsondata = serializers.serialize('json',data)

        return render(request,'hmis_dash/chldImmuLine.html', {'data':jsondata, 'fy': fy_name, 'state':st_name})


class chldImmuBarNumeric(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = 'login'

    def get(self, request, fy= None, dist_name = None):
        district = request.GET.get('dist_name', dist_name) 
        fy_name = request.GET.get('fy', fy) 
        data = HmisStChldImmunzt.objects.filter(Q(year=fy_name)).exclude(state='India')
        jsondata = serializers.serialize('json', data)
        
        return render(request,'hmis_dash/chldImmuBarNumeric.html', {'data':jsondata, 'fy': fy_name, 'dist_name': district})


class chldImmuLineNumeric(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = 'login'

    def get(self,request,fy=None):
        fy_name = request.GET.get('fy', fy) 
        data = HmisStChldImmunzt.objects.filter(Q(year=fy_name)).order_by('month').exclude(month='All')
        st_name = HmisStChldImmunzt.objects.values('state').distinct().order_by('state')
        jsondata = serializers.serialize('json',data)

        return render(request,'hmis_dash/chldImmuLineNumeric.html', {'data':jsondata, 'fy': fy_name, 'state':st_name})


class chldDiseaseBar(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = 'login'

    def get(self, request, fy= None, dist_name = None):
        district = request.GET.get('dist_name', dist_name) 
        fy_name = request.GET.get('fy', fy) 
        data = HmisStChldDisease.objects.filter(Q(year=fy_name)).exclude(state='India')
        jsondata = serializers.serialize('json', data)
        
        return render(request,'hmis_dash/chldDiseaseBar.html', {'data':jsondata, 'fy': fy_name, 'dist_name': district})


class chldDiseaseLine(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = 'login'

    def get(self,request,fy=None):
        fy_name = request.GET.get('fy', fy) 
        data = HmisStChldDisease.objects.filter(Q(year=fy_name)).order_by('month').exclude(month='All')
        st_name = HmisStChldDisease.objects.values('state').distinct().order_by('state')
        jsondata = serializers.serialize('json',data)

        return render(request,'hmis_dash/chldDiseaseLine.html', {'data':jsondata, 'fy': fy_name, 'state':st_name})


class chldDiseaseBarNumeric(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = 'login'

    def get(self, request, fy= None, dist_name = None):
        district = request.GET.get('dist_name', dist_name) 
        fy_name = request.GET.get('fy', fy) 
        data = HmisStChldDisease.objects.filter(Q(year=fy_name)).exclude(state='India')
        jsondata = serializers.serialize('json', data)
        
        return render(request,'hmis_dash/chldDiseaseBarNumeric.html', {'data':jsondata, 'fy': fy_name, 'dist_name': district})


class chldDiseaseLineNumeric(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = 'login'

    def get(self,request,fy=None):
        fy_name = request.GET.get('fy', fy) 
        data = HmisStChldDisease.objects.filter(Q(year=fy_name)).order_by('month').exclude(month='All')
        st_name = HmisStChldDisease.objects.values('state').distinct().order_by('state')
        jsondata = serializers.serialize('json',data)

        return render(request,'hmis_dash/chldDiseaseLineNumeric.html', {'data':jsondata, 'fy': fy_name, 'state':st_name})

    
class hmisTableChart(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = 'login'

    def get(self,request,fy=None):
        fy_name = request.GET.get('fy', fy) 
        pw_data = Hmis10IndiStlevel.objects.filter(Q(year=fy_name)).order_by('month') 
        childIm_data=HmisStChldImmunzt.objects.filter(Q(year=fy_name)).order_by('month')
        childDi_data=HmisStChldDisease.objects.filter(Q(year=fy_name)).order_by('month')
        st_name = Hmis10IndiStlevel.objects.values('state').distinct().order_by('state')
        json_childIm_data = serializers.serialize('json',childIm_data)
        json_childDi_data = serializers.serialize('json',childDi_data)
        jsonpw_data = serializers.serialize('json',pw_data)

        context = {
            'chilIm_data': json_childIm_data,
            'childDi_data': json_childDi_data,
            'pw_data': jsonpw_data
        }

        return render(request,'hmis_dash/tableOverview.html', {'context':context, 'fy': fy_name, 'state':st_name})


class pieStateLevel(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = 'login'

    def get(self, request, fy= None):
        fy_name = request.GET.get('fy', fy) 
        data = PieState.objects.filter(Q(year=fy_name))
        jsondata = serializers.serialize('json', data)

        return render(request,'hmis_dash/piechart_stlvl.html', {'data':jsondata, 'fy': fy_name})


class pieChildImmu(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = 'login'

    def get(self, request, fy= None):
        fy_name = request.GET.get('fy', fy) 
        data = PieChldImmunzt.objects.filter(Q(year=fy_name))
        jsondata = serializers.serialize('json', data)

        return render(request,'hmis_dash/pieChldImmu.html', {'data':jsondata, 'fy': fy_name})


class pieChildDisease(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = 'login'

    def get(self, request, fy= None):
        fy_name = request.GET.get('fy', fy) 
        data = PieChldDisease.objects.filter(Q(year=fy_name))
        jsondata = serializers.serialize('json', data)

        return render(request,'hmis_dash/pieChldDisease.html', {'data':jsondata, 'fy': fy_name})


class mapStPW(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = 'login'

    def get(self,request,fy=None):
        fy_name = request.GET.get('fy', fy) 
        st_data = Hmis10IndiStlevel.objects.filter(Q(year=fy_name)).exclude(state='India')
        
        st_jsondata = serializers.serialize('json', st_data)
        
        st_geodata = serialize('geojson', GeojsonIndiaLevel.objects.all(),
                                geometry_field = 'wkb_geometry',
                                fields = ('ogc_fid','state'))
        
        context = {
            'st_data': st_jsondata,
            'st_geodata': st_geodata
        }

        return render(request,'hmis_dash/mapPW.html', {'context':context, 'fy': fy_name})


class mapStChldImmu(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = 'login'

    def get(self,request,fy=None):
        fy_name = request.GET.get('fy', fy) 
        st_data = HmisStChldImmunzt.objects.filter(Q(year=fy_name)).exclude(state='India')
        
        st_jsondata = serializers.serialize('json', st_data)
        
        st_geodata = serialize('geojson', GeojsonIndiaLevel.objects.all(),
                                geometry_field = 'wkb_geometry',
                                fields = ('ogc_fid','state'))
        
        context = {
            'st_data': st_jsondata,
            'st_geodata': st_geodata
        }

        return render(request,'hmis_dash/mapChldImmu.html', {'context':context, 'fy': fy_name})


class mapStChldDisease(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = 'login'

    def get(self,request,fy=None):
        fy_name = request.GET.get('fy', fy) 
        st_data = HmisStChldDisease.objects.filter(Q(year=fy_name)).exclude(state='India')
        
        st_jsondata = serializers.serialize('json', st_data)
        
        st_geodata = serialize('geojson', GeojsonIndiaLevel.objects.all(),
                                geometry_field = 'wkb_geometry',
                                fields = ('ogc_fid','state'))
        
        context = {
            'st_data': st_jsondata,
            'st_geodata': st_geodata
        }

        return render(request,'hmis_dash/mapChldDisease.html', {'context':context, 'fy': fy_name})


class fyChldImmuLine(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = 'login'

    def get(self,request,fy=None, dist_name = None):
        district = request.GET.get('dist_name', dist_name) 
        fy_name = request.GET.get('fy', fy) 
        data = HmisStChldImmunzt.objects.all().order_by('month').exclude(month='All')
        st_name = HmisStChldImmunzt.objects.values('state').distinct().order_by('state')
        fyList = HmisStChldImmunzt.objects.values('year').distinct().order_by('year')
        jsondata = serializers.serialize('json',data)

        return render(request,'hmis_dash/fy_ci_line.html', {'data':jsondata, 'fy': fy_name, 'fyList':fyList, 'dist_name': district, 'state':st_name})


class fyChldImmuLineNum(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = 'login'

    def get(self,request,fy=None, dist_name = None):
        district = request.GET.get('dist_name', dist_name) 
        fy_name = request.GET.get('fy', fy) 
        data = HmisStChldImmunzt.objects.all().order_by('month').exclude(month='All')
        st_name = HmisStChldImmunzt.objects.values('state').distinct().order_by('state')
        fyList = HmisStChldImmunzt.objects.values('year').distinct().order_by('year')
        jsondata = serializers.serialize('json',data)

        return render(request,'hmis_dash/fy_ci_lineNum.html', {'data':jsondata, 'fy': fy_name, 'fyList':fyList, 'dist_name': district, 'state':st_name})


class fyChldDiseaseLine(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = 'login'

    def get(self,request,fy=None, dist_name = None):
        district = request.GET.get('dist_name', dist_name) 
        fy_name = request.GET.get('fy', fy) 
        data = HmisStChldDisease.objects.all().order_by('month').exclude(month='All')
        st_name = HmisStChldDisease.objects.values('state').distinct().order_by('state')
        fyList = HmisStChldDisease.objects.values('year').distinct().order_by('year')
        jsondata = serializers.serialize('json',data)

        return render(request,'hmis_dash/fy_cd_line.html', {'data':jsondata, 'fy': fy_name, 'fyList':fyList, 'dist_name': district, 'state':st_name})


class fyChldDiseaseLineNum(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = 'login'

    def get(self,request,fy=None, dist_name = None):
        district = request.GET.get('dist_name', dist_name) 
        fy_name = request.GET.get('fy', fy) 
        data = HmisStChldDisease.objects.all().order_by('month').exclude(month='All')
        st_name = HmisStChldDisease.objects.values('state').distinct().order_by('state')
        fyList = HmisStChldDisease.objects.values('year').distinct().order_by('year')
        jsondata = serializers.serialize('json',data)

        return render(request,'hmis_dash/fy_cd_lineNum.html', {'data':jsondata, 'fy': fy_name, 'fyList':fyList, 'dist_name': district, 'state':st_name})


class XmRChart(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = 'login'

    def get(self,request,fy=None, dist_name = None):
        district = request.GET.get('dist_name', dist_name) 
        fy_name = request.GET.get('fy', fy) 
        data = Hmis10IndiStlevel.objects.all().order_by('month').exclude(month='All')
        ta_data = TargetAchieved.objects.all()
        st_name = Hmis10IndiStlevel.objects.values('state').distinct().order_by('state')
        fyList = Hmis10IndiStlevel.objects.values('year').distinct().order_by('year')
        jsondata = serializers.serialize('json',data)
        ta_json = serializers.serialize('json',ta_data)
        context = {
            
            'ta_data':ta_json
        }
        return render(request,'hmis_dash/xmrChart.html', {'data':jsondata,'context':context, 'fy': fy_name, 'fyList':fyList, 'dist_name': district, 'state':st_name})

class XmRChartPercent(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = 'login'

    def get(self,request,fy=None, dist_name = None):
        district = request.GET.get('dist_name', dist_name) 
        fy_name = request.GET.get('fy', fy) 
        data = Hmis10IndiStlevel.objects.all().order_by('month').exclude(month='All')
        ta_data = TargetAchieved.objects.all()
        st_name = Hmis10IndiStlevel.objects.values('state').distinct().order_by('state')
        fyList = Hmis10IndiStlevel.objects.values('year').distinct().order_by('year')
        jsondata = serializers.serialize('json',data)
        ta_json = serializers.serialize('json',ta_data)
        context = {
            
            'ta_data':ta_json
        }
        return render(request,'hmis_dash/xmrChart_percent.html', {'data':jsondata,'context':context, 'fy': fy_name, 'fyList':fyList, 'dist_name': district, 'state':st_name})