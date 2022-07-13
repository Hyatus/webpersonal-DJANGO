from django.shortcuts import render, HttpResponse

# HttpRespones nos permite devolver un código cuando recibe una petición 
# Create your views here.
# Se definen las vista de una app
# Se define la lógica cuando se hace una petición a nuestra web 


html_base = '''
<h1>Mi Web Personal</h1>
<ul>
    <li><a href="/">Portada</li>
    <li><a href="/about-me/">Acerda de</li>
    <li><a href="/portfolio/">Portafolio</li>
    <li><a href="/contact/">Contacto</li>
</ul>
'''
def home(request):
    # html_response = ""
    # html_response += html_base
    # html_response += "<h2>Portada</h2>"
    # return HttpResponse(html_response)
    return render(request,"core/home.html") 

def about(request):
    # return HttpResponse(html_base + "<h1>Acerca de: </h1><p>Me llamo Cristian y soy programador</p>")
    return render(request,"core/about.html")

def contact(request):
    # return HttpResponse(html_base+"<h2>Puden contactarme por aquí</h2>")
    return render(request,"core/contact.html")
    