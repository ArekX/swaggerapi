from .endpoint import parse as parse_endpoint
from .model import parse as parse_model

parsers = {
    "endpoint": parse_endpoint,
    "model": parse_model
}
