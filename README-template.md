# stactools-uci-cycling-races

[![PyPI](https://img.shields.io/pypi/v/stactools-uci-cycling-races?style=for-the-badge)](https://pypi.org/project/stactools-uci-cycling-races/)
![GitHub Workflow Status (with event)](https://img.shields.io/github/actions/workflow/status/stactools-packages/uci-cycling-races/continuous-integration.yml?style=for-the-badge)

- Name: uci-cycling-races
- Package: `stactools.uci_cycling_races`
- [stactools-uci-cycling-races on PyPI](https://pypi.org/project/stactools-uci-cycling-races/)
- Owner: @githubusername
- [Dataset homepage](http://example.com)
- STAC extensions used:
  - [proj](https://github.com/stac-extensions/projection/)
- Extra fields:
  - `uci-cycling-races:custom`: A custom attribute
- [Browse the example in human-readable form](https://radiantearth.github.io/stac-browser/#/external/raw.githubusercontent.com/stactools-packages/uci-cycling-races/main/examples/collection.json)
- [Browse a notebook demonstrating the example item and collection](https://github.com/stactools-packages/uci-cycling-races/tree/main/docs/example.ipynb)

A short description of the package and its usage.

## STAC examples

- [Collection](examples/collection.json)
- [Item](examples/item/item.json)

## Installation

```shell
pip install stactools-uci-cycling-races
```

## Command-line usage

Description of the command line functions

```shell
stac uci-cycling-races create-item source destination
```

Use `stac uci-cycling-races --help` to see all subcommands and options.

## Contributing

We use [pre-commit](https://pre-commit.com/) to check any changes.
To set up your development environment:

```shell
pip install -e '.[dev]'
pre-commit install
```

To check all files:

```shell
pre-commit run --all-files
```

To run the tests:

```shell
pytest -vv
```

If you've updated the STAC metadata output, update the examples:

```shell
scripts/update-examples
```
