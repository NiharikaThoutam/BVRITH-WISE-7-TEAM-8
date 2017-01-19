from pyramid.view import view_config


#@view_config(route_name='home', renderer='templates/mytemplate.pt')
#def my_view(request):
 #   return {'project': 'scaffolds'}


#@view_config(route_name='home', renderer='templates/login.pt')
#def my_view(request):
#    return {}


@view_config(route_name='home', renderer='templates/hrview.pt')
def hr_view(request):
    return {}

@view_config(route_name='select', renderer='templates/selectstu.pt')
def select_view(request):
    return {}

@view_config(route_name='eligible', renderer='templates/eligiblestu.pt')
def elegible_view(request):
    return {}
