""" A IceController Module """

from masonite.controllers import Controller
from masonite.request import Request
from app.Ice import Ice


class IceController(Controller):
    def __init__(self, request: Request):
        self.request = request

    def show(self):
        id = self.request.param("id")
        return Ice.find(id)

    def index(self):
        return Ice.all()

    def create(self):
        name = self.request.input("name")
        image = self.request.input("image")
        caption = self.request.input("caption")
        description = self.request.input("description")
        ingredients = self.request.input("ingredients")
        ice = Ice.create({
            "name": name,
            "image": image,
            "caption": caption,
            "description": description,
            "ingredients": ingredients
        })
        return ice

    def update(self):
        name = self.request.input("name")
        image = self.request.input("image")
        caption = self.request.input("caption")
        description = self.request.input("description")
        ingredients = self.request.input("ingredients")
        id = self.request.param("id")
        Ice.where("id", id).update({
            "name": name,
            "image": image,
            "caption": caption,
            "description": description,
            "ingredients": ingredients
        })
        return Ice.where("id", id).get()

    def destroy(self):
        id = self.request.param("id")
        ice = Ice.where("id", id).get()
        Ice.where("id", id).delete()
        return ice