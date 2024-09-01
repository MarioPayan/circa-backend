from typing import List, T
from models import Coffee, Variety


class Data:
    varieties = [
        Variety(name="Arabica", slug="arabica"),
        Variety(name="Robusta", slug="robusta"),
    ]
    coffees = [
        Coffee(
            name="Caturra",
            slug="caturra",
            varieties=[varieties[0]],
            cop_price=7000,
        ),
        Coffee(
            name="Castillo",
            slug="castillo",
            varieties=[varieties[1]],
            cop_price=5000,
        ),
    ]

    def get(self, id: str, entities: List[T], key="slug") -> T:
        return next((e for e in entities if getattr(e, key, None) == id), None)

    def get_coffees(self):
        return self.coffees

    def get_coffee_by_slug(self, slug):
        return self.get(slug, self.coffees)

    def get_varieties(self):
        return self.varieties

    def get_variety_by_slug(self, slug):
        return self.get(slug, self.varieties)


data = Data()
