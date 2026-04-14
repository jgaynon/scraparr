"""Startup deprecation warnings for legacy connector sections."""

import logging

from scraparr.const import DEPRECATED_CONNECTORS

MIGRATION_DOCS_URL = "https://docs.seerr.dev/migration-guide"


def warn_deprecated_connectors(config):
    """Emit a startup warning for each legacy connector still configured.

    Context: Jellyseerr and Overseerr merged into a single project, Seerr
    (https://docs.seerr.dev/blog/seerr-release). Existing instances
    auto-migrate on first startup — there's no new service to deploy, your
    existing Jellyseerr/Overseerr *becomes* Seerr. The v1 API is preserved,
    so this exporter's `jellyseerr`, `overseerr`, and `seerr` connectors are
    all interchangeable against the same live instance.

    What to tell the user:
      1. Rename the config section to `seerr:` once upstream has migrated.
      2. Metric series rename (jellyseerr_*/overseerr_* -> seerr_*), so
         update Grafana dashboards and Prometheus alerts at the same time.
      3. If both the legacy section and `seerr:` point at the same URL,
         the instance is being scraped twice — drop the legacy section.
    """
    has_seerr = bool(config.get('seerr'))

    for legacy, replacement in DEPRECATED_CONNECTORS.items():
        legacy_cfg = config.get(legacy)
        if not legacy_cfg:
            continue

        logging.warning(
            "The '%s' connector is deprecated. Jellyseerr and Overseerr have "
            "merged into Seerr (%s); rename this section to '%s:' once your "
            "upstream instance has auto-migrated. NOTE: metric names change "
            "(%s_* -> %s_*), so update Grafana dashboards and Prometheus "
            "alerts at the same time. Legacy sections will be removed in a "
            "future release.",
            legacy, MIGRATION_DOCS_URL, replacement, legacy, replacement,
        )

        if has_seerr and _shares_url(legacy_cfg, config['seerr']):
            logging.warning(
                "Both '%s:' and 'seerr:' reference the same URL. The same "
                "instance is being scraped twice with duplicate metrics under "
                "different names. Drop the '%s:' section.",
                legacy, legacy,
            )


def _shares_url(a_cfg, b_cfg):
    """Return True if any instance in a_cfg shares a URL with any in b_cfg."""
    return bool(_urls(a_cfg) & _urls(b_cfg))


def _urls(cfg):
    """Extract the set of URLs from a config section (dict or list-of-dicts)."""
    if isinstance(cfg, dict):
        url = cfg.get('url')
        return {url} if url else set()
    if isinstance(cfg, list):
        return {item.get('url') for item in cfg
                if isinstance(item, dict) and item.get('url')}
    return set()
