from django.shortcuts import render
from .models import *
from .forms import *


def inicio(request):
    return render(request, "inicio.html")


def equipo_pokemon(request):
    charmander = Pokemon(nombre="charmander", tipo="fuego", nivel=1)
    squirtle = Pokemon(nombre="squirtle", tipo="agua", nivel=2)
    bulbasaur = Pokemon(nombre="bulbasaur", tipo="planta", nivel=4)
    mi_equipo = {'pokemons': [charmander, squirtle, bulbasaur]}
    return render(request, 'equipo_pokemon.html', mi_equipo)


def entrenadores(request):
    andres = Entrenador(nombre="andres", cantidad_de_medallas=8, region="Jhoto")
    ash = Entrenador(nombre="ash", cantidad_de_medallas=7, region="Kanto")
    entrenadores = {'entrenadores': [andres, ash]}
    return render(request, 'entrenadores.html', entrenadores)


def habilidades(request):
    lanza_llamas = Habilidad(nombre="lanza llamas", tipo="fuego")
    rayo_burbuja = Habilidad(nombre="rayo burbuja", tipo="agua")
    hoja_afilada = Habilidad(nombre="hoja afilada", tipo="planta")
    habilidades = {'habilidades': [lanza_llamas, rayo_burbuja, hoja_afilada]}
    return render(request, 'habilidades.html', habilidades)


def pokemon_formulario(request):

    if request.method == "POST":
        form = PokemonForm(request.POST)

        if form.is_valid():
            informacion = form.cleaned_data

            nombre_pokemon = informacion["nombre"]
            tipo_pokemon = informacion["tipo"]
            nivel_pokemon = informacion["nivel"]

            pokemon = Pokemon(nombre=nombre_pokemon, tipo=tipo_pokemon, nivel=nivel_pokemon)
            pokemon.save()
            return render(request, "inicio.html")
    else:
        formulario = PokemonForm()
    
    return render(request, "pokemon_formulario.html", {"form":formulario, "mensaje":"POKEMON CREADO CORRECTAMENTE"})
                           #intente con appPokemon/pokemon_formulario.html y pincho


def entrenador_formulario(request):

    if request.method == "POST":
        form = EntrenadorForm(request.POST)

        if form.is_valid():
            informacion = form.cleaned_data

            nombre_entrenador = informacion["nombre"]
            cantidad_de_medallas_entrenador = informacion["cantidad_de_medallas"]
            region_entrenador = informacion["region"]

            entrenador = Entrenador(nombre=nombre_entrenador, cantidad_de_medallas=cantidad_de_medallas_entrenador, region=region_entrenador)
            entrenador.save()
            return render(request, "inicio.html")
    else:
        formulario = EntrenadorForm()
    
    return render(request, "entrenador_formulario.html", {"form":formulario, "mensaje":"ENTRENADOR CREADO CORRECTAMENTE"})


def habilidad_formulario(request):

    if request.method == "POST":
        form = HabilidadForm(request.POST)

        if form.is_valid():
            informacion = form.cleaned_data

            nombre_habilidad = informacion["nombre"]
            tipo_habilidad = informacion["tipo"]


            habilidad = Habilidad(nombre=nombre_habilidad, tipo=tipo_habilidad)
            habilidad.save()
            return render(request, "inicio.html")
    else:
        formulario = HabilidadForm()
    
    return render(request, "habilidad_formulario.html", {"form":formulario, "mensaje":"HABILIDAD CREADA CORRECTAMENTE"})


def busqueda_pokemon(request):
    return render(request, "busqueda_pokemon.html")


def buscar(request):
    if "nombre" in request.GET:
        nombre = request.GET["nombre"]
        pokemons = Pokemon.objects.filter(nombre__icontains=nombre) #lista de pokemons con atributo nombre = "nombre"
        return render(request, "resultado_busqueda.html", {"pokemons":pokemons})
    else:
        return render(request, "busqueda_pokemon.html", {"mensaje":"Porfavor ingresa un TIPO de pokemon"})


    

