"""Protocol definitions for models."""
from typing import Protocol, TypeVar, Generic, List, Optional, Callable, Any
from abc import abstractmethod


T = TypeVar("T")
K = TypeVar("K")
V = TypeVar("V")


class BaseModelsSpecProtocol(Protocol):
    """Protocol for basemodelsspec operations."""

    @property
    def id(self) -> str:
        """Unique identifier."""
        ...

    def validate(self) -> bool:
        """Validate the instance."""
        ...

    def serialize(self) -> dict[str, Any]:
        """Serialize to dictionary."""
        ...


class Repository(Protocol[T]):
    """Generic repository protocol."""

    def get(self, id: str) -> Optional[T]:
        """Get item by ID."""
        ...

    def list(self, limit: int = 100, offset: int = 0) -> List[T]:
        """List items with pagination."""
        ...

    def create(self, item: T) -> T:
        """Create new item."""
        ...

    def update(self, id: str, item: T) -> T:
        """Update existing item."""
        ...

    def delete(self, id: str) -> bool:
        """Delete item by ID."""
        ...


class Cache(Protocol[K, V]):
    """Generic cache protocol."""

    def get(self, key: K) -> Optional[V]:
        """Get value by key."""
        ...

    def set(self, key: K, value: V, ttl: Optional[int] = None) -> None:
        """Set value with optional TTL."""
        ...

    def delete(self, key: K) -> bool:
        """Delete key."""
        ...

    def clear(self) -> None:
        """Clear all entries."""
        ...


class EventHandler(Protocol[T]):
    """Event handler protocol."""

    def handle(self, event: T) -> None:
        """Handle the event."""
        ...

    def can_handle(self, event: T) -> bool:
        """Check if handler can process event."""
        ...
