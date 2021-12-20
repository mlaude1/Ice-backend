"""Web Routes."""

from masonite.routes import Get, Post, Put, Delete, RouteGroup

ROUTES = [
    Get("/", "WelcomeController@show").name("welcome"),
    
    RouteGroup([
        Get("/", "IceController@index").name("index"),
        Get("/@id", "IceController@show").name("show"),
        Post("/", "IceController@create").name("create"),
        Put("/@id", "IceController@update").name("update"),
        Delete("/@id", "IceController@destroy").name("destroy")
    ], prefix="/ices", name="ices")
]
