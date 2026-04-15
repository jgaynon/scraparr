"""
Constants for Scraparr.
"""

SEERR_MIGRATION_DOCS_URL = "https://docs.seerr.dev/migration-guide"
SEERR_MIGRATION_WARNING  = "The '%s' connector is deprecated and has been replaced by '%s'. Jellyseerr and Overseerr have merged into Seerr ({SEERR_MIGRATION_DOCS_URL}). Legacy connectors may be removed in a future release."

ACTIVE_CONNECTORS = [
    'sonarr', 'radarr', 'prowlarr',
    'bazarr', 'readarr', 'seerr',
    'jellyseerr', 'overseerr', 'whisparr',
    'jellyfin', 'lidarr', 'kavita',
]

# Active but legacy connectors - still functional, emit a deprecation warning at startup.
DEPRECATED_CONNECTORS = {
    'jellyseerr': {
        'replacement': 'seerr',
        'log_warning': SEERR_MIGRATION_WARNING
    },
    'overseerr': {
        'replacement': 'seerr',
        'docs_url': SEERR_MIGRATION_WARNING
    },
}

API_VERSIONS = {
    "sonarr": "v3", 
    "radarr": "v3",
    "prowlarr": "v1",
    "bazarr": "dummy",
    "readarr": "v1", 
    "seerr": "v1",
    "jellyseerr": "v1", 
    "overseerr": "v1",
    "whisparr": "v3", 
    "jellyfin": "dummy",
    "lidarr": "v1", 
    "kavita": "dummy",
}

BEAUTIFUL_CONNECTORS = ", ".join(ACTIVE_CONNECTORS[:-1]) + " or " + ACTIVE_CONNECTORS[-1]

# Field names by type (for type coercion after env var parsing)
INT_FIELDS = {'interval', 'within', 'port', 'workers'}
BOOL_FIELDS = {'detailed', 'episode_quality_stats'}

# Service-specific fields (for env var parsing - distinguishes SONARR_URL from SONARR_PROD_URL)
SERVICE_FIELDS = {
    'url', 'api_key', 'alias', 'api_version',
    'interval', 'detailed', 'within', 'episode_quality_stats',
    'legacy_auth',
}
