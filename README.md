# AEONlib

A suite of modules to enable TDA/MMA observations

[code](https://github.com/AEONplus/AEONlib)

[issues](https://github.com/AEONplus/AEONlib/issues)


### Testing
This project uses [pytest](https://docs.pytest.org/) to run tests:

```shell
pytest
```

Some tests are marked as `online`. These tests make real http requests in order
to test interfaces with various services. To run them:

```shell
pytest -m online
```

CI does not run tests marked as online.

### Linting
All code is formatted via [ruff](https://astral.sh/ruff).

### Code Generation
Las Cumbres Observatory [instrument classes](src/aeonlib/ocs/lco/instruments.py)
are generated via the [generator.py](codegen/lco/generator.py) script. This script
takes as input the [OCS instruments api](https://observe.lco.global/api/instruments/)
in order to produce definitions of all instruments currently available on the network.

To update the definitions, first make sure you have installed the `codegen` dependency
group:

```shell
uv sync --group codegen  # or poetry install --with codegen
```

This ensures regular users of the library do not need to install these dependencies.

The `generate.py` script takes as input JSON as produced by the instruments endpoint:

```shell
codegen/lco/generator.py instruments.json
```

Or directly from stdin using a pipe:

```shell
curl https://observe.lco.global/api/instruments/ | codegen/lco/generator.py
```

If the output looks satisfactory, you can redirect the output to overwrite the
LCO instruments definition file:

```shell
curl https://observe.lco.global/api/instruments/ | codegen/lco/generator.py > src/aeonlib/ocs/lco/instruments.py
```
