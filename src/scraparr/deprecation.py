"""
Startup deprecation warnings for legacy connectors.
"""

import logging

from scraparr.const import DEPRECATED_CONNECTORS

def warn_deprecated_connectors(config):
    """Emit a startup warning for each legacy connector still configured"""

    for connector_name, data in DEPRECATED_CONNECTORS.items():
        if not config.get(connector_name):
            continue

        logging.warning(
            data.get('log_warning'),
            connector_name, data.get('replacement')
        )

