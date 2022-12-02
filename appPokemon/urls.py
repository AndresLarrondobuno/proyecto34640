from django.urls import path
from appPokemon.views import *

urlpatterns = [
    path('equipo_pokemon/', equipo_pokemon, name="equipo_pokemon"),
    path('entrenadores/', entrenadores, name="entrenadores"),
    path('habilidades/', habilidades, name="habilidades"),
    path('pokemon_formulario/', pokemon_formulario, name="pokemon_formulario"),
    path('entrenador_formulario/', entrenador_formulario, name="entrenador_formulario"),
    path('habilidad_formulario/', habilidad_formulario, name="habilidad_formulario"),
    path('busqueda_pokemon/', busqueda_pokemon, name="busqueda_pokemon"),
    path('buscar/', buscar, name="buscar"),
    path('', inicio, name="inicio"),
    
]

