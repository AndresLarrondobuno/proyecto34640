from django.shortcuts import render
from .models import *
from .forms import *

def familia(request):
    mabel = Familiar(nombre="Mabel", edad=28, fecha_de_nacimiento="1993-12-12")
    alberto = Familiar(nombre="Alberto", edad=72, fecha_de_nacimiento="1950-17-3")
    abigail = Familiar(nombre="Abigail", edad=22, fecha_de_nacimiento="1993-11-2")
    mi_familia = {'familiares': [mabel, alberto, abigail]}
    return render(request, 'familiares1.html', mi_familia)


def familiaFormulario(request):

    if request.method == "POST":
        form = familiaForm(request.POST)
        print("-----")
        print(form)
        print("-----")
        if form.is_valid():
            informacion = form.cleaned_data
            print(informacion)


            nombrecito = request.POST["nombre"]
            edadcita = request.POST["edad"]
            fechita_de_nacimiento = request.POST["fecha_de_nacimiento"]

            miFamiliar = Familiar(nombre=nombrecito, edad=edadcita, fechita_de_nacimiento=fechita_de_nacimiento)
            miFamiliar.save()
            return render(request, "appFamilia/inicio.html")
    else:
        formulario = familiaForm()
    
    return(request, "appFamilia/familiaFormulario.html", {"form":formulario, "mensaje":"POKEMON CREADO CORRECTAMENTE"})


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
            return render(request, "appPokemon/inicio.html")
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

            entrenador = Entrenador(nombre=nombre_entrenador, tipo=cantidad_de_medallas_entrenador, nivel=region_entrenador)
            entrenador.save()
            return render(request, "appPokemon/inicio.html")
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
            return render(request, "appPokemon/inicio.html")
    else:
        formulario = HabilidadForm()
    
    return render(request, "habilidad_formulario.html", {"form":formulario, "mensaje":"HABILIDAD CREADA CORRECTAMENTE"})