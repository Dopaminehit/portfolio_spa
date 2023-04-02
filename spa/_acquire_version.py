# Copyright (c) 2023 Dopamine Inc.
# All rights reserved.  See https://{placeholder_for_url}.

"""Manage Package Version State."""

from pathlib import Path

here = Path(__file__).resolve().parent
version_file_path = here / "VERSION"

with open(version_file_path) as version_file:
    version = version_file.read().strip()

__version__ = version
