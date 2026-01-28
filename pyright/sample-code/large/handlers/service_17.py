"""Service layer for handlers."""
from typing import Optional, List, Dict, Any, TypeVar, Generic, Callable
from dataclasses import dataclass
from functools import wraps
import logging

logger = logging.getLogger(__name__)

T = TypeVar("T")
R = TypeVar("R")


def log_operation(func: Callable[..., R]) -> Callable[..., R]:
    """Decorator to log service operations."""
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> R:
        logger.info(f"Executing {func.__name__}")
        try:
            result = func(*args, **kwargs)
            logger.info(f"{func.__name__} completed successfully")
            return result
        except Exception as e:
            logger.error(f"{func.__name__} failed: {e}")
            raise
    return wrapper


@dataclass
class ServiceResult(Generic[T]):
    """Generic service result wrapper."""

    success: bool
    data: Optional[T] = None
    error: Optional[str] = None
    metadata: Dict[str, Any] = None  # type: ignore

    def __post_init__(self) -> None:
        if self.metadata is None:
            self.metadata = {}

    @classmethod
    def ok(cls, data: T, **metadata: Any) -> "ServiceResult[T]":
        """Create successful result."""
        return cls(success=True, data=data, metadata=metadata)

    @classmethod
    def fail(cls, error: str, **metadata: Any) -> "ServiceResult[T]":
        """Create failed result."""
        return cls(success=False, error=error, metadata=metadata)


class CoreHandlersModelService:
    """Service for corehandlersmodel operations."""

    def __init__(self, config: Dict[str, Any]) -> None:
        self._config = config
        self._cache: Dict[str, Any] = {}

    @log_operation
    def process(self, data: Dict[str, Any]) -> ServiceResult[Dict[str, Any]]:
        """Process incoming data."""
        if not self._validate(data):
            return ServiceResult.fail("Validation failed")

        result = self._transform(data)
        return ServiceResult.ok(result)

    def _validate(self, data: Dict[str, Any]) -> bool:
        """Validate input data."""
        required_fields = self._config.get("required_fields", [])
        return all(field in data for field in required_fields)

    def _transform(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Transform data according to rules."""
        transformations = self._config.get("transformations", {})
        result = data.copy()

        for key, transform in transformations.items():
            if key in result and callable(transform):
                result[key] = transform(result[key])

        return result

    def batch_process(self, items: List[Dict[str, Any]]) -> List[ServiceResult[Dict[str, Any]]]:
        """Process multiple items."""
        return [self.process(item) for item in items]
