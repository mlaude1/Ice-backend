"""CreateIcesTable Migration."""

from masoniteorm.migrations import Migration


class CreateIcesTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("ices") as table:
            table.increments("id")
            table.string("name")
            table.string("image")
            table.string("caption")
            table.string("description")
            table.string("ingredients")
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("ices")
