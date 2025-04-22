# AEONlib

A suite of modules to enable TDA/MMA observations

[code](https://github.com/AEONplus/AEONlib)

[issues](https://github.com/AEONplus/AEONlib/issues)

### Configuration
Many of the facilities and services accessed by AEONlib require specific configuration such
as api keys, urls, etc. All configuration can be supplied by either supplying a .env file or
setting environmental variables in the execution environment.

Example .env file:

```
AEON_LCO_API_ROOT="https://observe.lco.global/api"
AEON_LCO_TOKEN="my-api-token"
```

Or set environmental variables via the shell:

```bash
export AEON_LCO_API_ROOT="https://observe.lco.global/api"
export AEON_LCO_TOKEN="my-api-token"
```

All configuration keys are prefixed with AEON_ to prevent conflicts. See the documentation for
each service to see which configuration keys are available, or check
[conf.py](src/aeonlib/conf.py)

Environmental variables take precedence over .env files. See the
[pydantic-settings](https://docs.pydantic.dev/latest/concepts/pydantic_settings/) documentation
for more details.


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
