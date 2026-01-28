"""Data models for handlers."""
from dataclasses import dataclass, field
from typing import Optional, List, Dict, Any
from datetime import datetime


@dataclass
class BaseHandlersEntity:
    """Represents a basehandlersentity entity."""

    id: str
    name: str
    created_at: datetime = field(default_factory=datetime.now)
    metadata: Dict[str, Any] = field(default_factory=dict)
    tags: List[str] = field(default_factory=list)
    parent_id: Optional[str] = None
    is_active: bool = True

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary representation."""
        return {
            "id": self.id,
            "name": self.name,
            "created_at": self.created_at.isoformat(),
            "metadata": self.metadata,
            "tags": self.tags,
            "parent_id": self.parent_id,
            "is_active": self.is_active,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "BaseHandlersEntity":
        """Create instance from dictionary."""
        return cls(
            id=data["id"],
            name=data["name"],
            created_at=datetime.fromisoformat(data.get("created_at", datetime.now().isoformat())),
            metadata=data.get("metadata", {}),
            tags=data.get("tags", []),
            parent_id=data.get("parent_id"),
            is_active=data.get("is_active", True),
        )


@dataclass
class BaseHandlersEntityCollection:
    """Collection of basehandlersentity items."""

    items: List[BaseHandlersEntity] = field(default_factory=list)
    total_count: int = 0
    page: int = 1
    page_size: int = 50

    def add(self, item: BaseHandlersEntity) -> None:
        """Add item to collection."""
        self.items.append(item)
        self.total_count += 1

    def filter_active(self) -> List[BaseHandlersEntity]:
        """Return only active items."""
        return [item for item in self.items if item.is_active]
