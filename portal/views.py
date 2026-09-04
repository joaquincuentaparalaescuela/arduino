from django.shortcuts import render
def inicio(request):
	"""Vista para la página de inicio"""
	return render(request, 'portal/inicio.html')

def tipos(request):
	"""Vista para el catálogo de tipos de placas"""
	return render(request, 'portal/tipos.html')
def proyectos(request):
    """Vista para el catálogo de proyectos"""
    return render(request, 'portal/proyectos.html')
def perfil(request):
    """Vista para la página de perfil"""
    return render(request, 'portal/perfil.html')