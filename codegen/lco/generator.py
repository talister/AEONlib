#!/usr/bin/env python3
import fileinput
import json
import sys
from pathlib import Path

from jinja2 import Environment, FileSystemLoader
from textcase import case, convert


def generate_instrument_configs(ins_s: str) -> str:
    """
    Generate instrument models based on the output of the OCS
    instrument data endpoint. For LCO, this endpoint resides
    at https://observe.lco.global/api/instruments/

    Args:
        ins_s (str): The input json containing instrument data.

    Returns:
        str: Generated Python Pydantic models as a string.
    """

    j_env = Environment(
        loader=FileSystemLoader(Path(__file__).parent / "templates"),
        trim_blocks=True,
        lstrip_blocks=True,
    )
    template = j_env.get_template("instruments.jinja")
    ins_data = json.loads(ins_s)
    instruments = []
    for code, ins in ins_data.items():
        config_types = [c["code"] for _, c in ins["configuration_types"].items()]
        readout_modes = [m["code"] for m in ins["modes"]["readout"]["modes"]]
        optical_elements = [
            {type: [v["code"] for v in values]}
            for type, values in ins["optical_elements"].items()
        ]
        # The Lco prefix is necessary because some instruments start with a number
        class_name = "Lco" + convert(code, case.PASCAL)
        instruments.append(
            {
                "type": ins["type"],
                "instrument_type": code,
                "class_name": class_name,
                "config_types": config_types,
                "readout_modes": readout_modes,
                "optical_elements": optical_elements,
            }
        )

    return template.render(instruments=instruments)


if __name__ == "__main__":
    # Accepts input from stdin or a file argument
    with fileinput.input() as f:
        ins_json = "".join(list(f))
        sys.stdout.write(generate_instrument_configs(ins_json))
