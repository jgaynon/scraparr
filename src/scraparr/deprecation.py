"""Startup deprecation warnings for legacy connector sections."""

import logging

from scraparr.const import DEPRECATED_CONNECTORS


def warn_deprecated_connectors(config):
    """Emit a startup warning for each legacy connector still configured.

    Jellyseerr and Overseerr have been unified under a single `seerr` connector
    (GitHub #171/#172). Legacy sections keep working for now but will be
    removed in a future release. Migrating renames Prometheus series
    (e.g. jellyseerr_request_total -> seerr_request_total), so dashboards and
    alerts must be updated at the same time as config.
    """
    for legacy, replacement in DEPRECATED_CONNECTORS.items():
        if legacy in config and config[legacy]:
            logging.warning(
                "The '%s' connector is deprecated and will be removed in a "
                "future release. Migrate your config to '%s:'. "
                "IMPORTANT: metric names change (%s_* -> %s_*), so update "
                "Grafana dashboards and Prometheus alerts accordingly.",
                legacy, replacement, legacy, replacement,
            )
