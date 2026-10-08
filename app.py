from dash import Dash, dcc, html
import dash_bootstrap_components as dbc

#padrão para inicializar uma aplicação Dash
app = Dash(__name__, 
           external_stylesheets=[dbc.themes.CERULEAN],
           suppress_callback_exceptions=True)