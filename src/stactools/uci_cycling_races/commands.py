import logging

import click
from click import Command, Group
from stactools.uci_cycling_races import stac

logger = logging.getLogger(__name__)


def create_ucicyclingraces_command(cli: Group) -> Command:
    """Creates the stactools-uci-cycling-races command line utility."""

    @cli.group(
        "ucicyclingraces",
        short_help=("Commands for working with stactools-uci-cycling-races"),
    )
    def ucicyclingraces() -> None:
        pass

    @ucicyclingraces.command(
        "create-collection",
        short_help="Creates a STAC collection",
    )
    @click.argument("destination")
    def create_collection_command(destination: str) -> None:
        """Creates a STAC Collection

        Args:
            destination: An HREF for the Collection JSON
        """
        collection = stac.create_collection()
        collection.set_self_href(destination)
        collection.save_object()

    @ucicyclingraces.command("create-item", short_help="Create a STAC item")
    @click.argument("source")
    @click.argument("destination")
    def create_item_command(source: str, destination: str) -> None:
        """Creates a STAC Item

        Args:
            source: HREF of the Asset associated with the Item
            destination: An HREF for the STAC Item
        """
        item = stac.create_item(source)
        item.save_object(dest_href=destination)

    return ucicyclingraces
