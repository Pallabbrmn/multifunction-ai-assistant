class LLMProviderError(Exception):
    """Raised when the LLM provider fails."""
    pass


class ConfigurationError(Exception):
    """Raised when required configuration is missing."""
    pass