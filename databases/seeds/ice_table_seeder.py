"""IceTableSeeder Seeder."""

from masoniteorm.seeds import Seeder
from app.Ice import Ice


class IceTableSeeder(Seeder):
    def run(self):
        Ice.create({
            "name": "Somewhere Over the Rain-Dough",
            "image": "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.coldstonecreamery.com%2Fassets%2Fimg%2Fproducts%2Fsignaturecreations%2Fsomewherewvertheraindough.jpg&f=1&nofb=1",
            "caption": "Way better than Kansas",
            "description": "This creation made with Classic Cookie Dough Ice Cream tastes just like Sugar Cookie Dough!",
            "ingredients": "Classic Cookie Dough Ice Cream, Frosting, Rainbow Sprinkles and Sugar Crystals"
        })
        Ice.create({
            "name": "Mango Tango",
            "image": "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fcdn2.momjunction.com%2Fwp-content%2Fuploads%2F2020%2F12%2FMango-tango-ice-cream.jpg&f=1&nofb=1",
            "caption": "The vibrant flavor of this ice cream will make you dance all night long",
            "description": "Luscious mango ice cream dancing with a tangy mangy ribbon",
            "ingredients": "Mango Flavored Ice Cream, Mango Syrup"
        })
        Ice.create({
            "name": "Cookie Mintster",
            "image": "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.coldstonecreamery.com%2Fassets%2Fimg%2Fproducts%2Fsignaturecreations%2Fcookiemintser.jpg&f=1&nofb=1",
            "caption": "For the little Mintster inside of us all...",
            "description": "It’s mint and chocolate. What more could you ask for?? Oh, wait, ask for OREO® Cookies. It comes with OREO® Cookies!",
            "ingredients": "Mint Ice Cream with double the OREO® Cookies and Fudge"
        })
