#!/usr/bin/env python3
"""
Generate synthetic Python code for PyRight multithreading benchmarks.

Creates three test codebases of varying sizes:
- small: ~15 files (baseline)
- medium: ~75 files
- large: ~250 files

The generated code uses realistic type annotations including:
- Basic types (str, int, bool, list, dict)
- Generics (TypeVar, Generic)
- Protocols
- TypedDict
- Optional, Union
- Callable
- Cross-module imports (to simulate real dependency graphs)
"""

import os
import random
from pathlib import Path
from typing import Dict, List

# Configuration for each size
SIZES = {
    "small": {"modules": 3, "files_per_module": 5},
    "medium": {"modules": 5, "files_per_module": 15},
    "large": {"modules": 10, "files_per_module": 25},
}

MODULE_NAMES = [
    "core",
    "models",
    "services",
    "utils",
    "handlers",
    "validators",
    "transformers",
    "repositories",
    "controllers",
    "middleware",
]

TEMPLATES = {
    "dataclass": '''"""Data models for {module}."""
from dataclasses import dataclass, field
from typing import Optional, List, Dict, Any
from datetime import datetime


@dataclass
class {class_name}:
    """Represents a {class_name_lower} entity."""

    id: str
    name: str
    created_at: datetime = field(default_factory=datetime.now)
    metadata: Dict[str, Any] = field(default_factory=dict)
    tags: List[str] = field(default_factory=list)
    parent_id: Optional[str] = None
    is_active: bool = True

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary representation."""
        return {{
            "id": self.id,
            "name": self.name,
            "created_at": self.created_at.isoformat(),
            "metadata": self.metadata,
            "tags": self.tags,
            "parent_id": self.parent_id,
            "is_active": self.is_active,
        }}

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "{class_name}":
        """Create instance from dictionary."""
        return cls(
            id=data["id"],
            name=data["name"],
            created_at=datetime.fromisoformat(data.get("created_at", datetime.now().isoformat())),
            metadata=data.get("metadata", {{}}),
            tags=data.get("tags", []),
            parent_id=data.get("parent_id"),
            is_active=data.get("is_active", True),
        )


@dataclass
class {class_name}Collection:
    """Collection of {class_name_lower} items."""

    items: List[{class_name}] = field(default_factory=list)
    total_count: int = 0
    page: int = 1
    page_size: int = 50

    def add(self, item: {class_name}) -> None:
        """Add item to collection."""
        self.items.append(item)
        self.total_count += 1

    def filter_active(self) -> List[{class_name}]:
        """Return only active items."""
        return [item for item in self.items if item.is_active]
''',
    "protocol": '''"""Protocol definitions for {module}."""
from typing import Protocol, TypeVar, Generic, List, Optional, Callable, Any
from abc import abstractmethod


T = TypeVar("T")
K = TypeVar("K")
V = TypeVar("V")


class {class_name}Protocol(Protocol):
    """Protocol for {class_name_lower} operations."""

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
''',
    "service": '''"""Service layer for {module}."""
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
        logger.info(f"Executing {{func.__name__}}")
        try:
            result = func(*args, **kwargs)
            logger.info(f"{{func.__name__}} completed successfully")
            return result
        except Exception as e:
            logger.error(f"{{func.__name__}} failed: {{e}}")
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
            self.metadata = {{}}

    @classmethod
    def ok(cls, data: T, **metadata: Any) -> "ServiceResult[T]":
        """Create successful result."""
        return cls(success=True, data=data, metadata=metadata)

    @classmethod
    def fail(cls, error: str, **metadata: Any) -> "ServiceResult[T]":
        """Create failed result."""
        return cls(success=False, error=error, metadata=metadata)


class {class_name}Service:
    """Service for {class_name_lower} operations."""

    def __init__(self, config: Dict[str, Any]) -> None:
        self._config = config
        self._cache: Dict[str, Any] = {{}}

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
        transformations = self._config.get("transformations", {{}})
        result = data.copy()

        for key, transform in transformations.items():
            if key in result and callable(transform):
                result[key] = transform(result[key])

        return result

    def batch_process(self, items: List[Dict[str, Any]]) -> List[ServiceResult[Dict[str, Any]]]:
        """Process multiple items."""
        return [self.process(item) for item in items]
''',
    "typeddict": '''"""TypedDict definitions for {module}."""
from typing import TypedDict, Optional, List, Literal, NotRequired
from datetime import datetime


class {class_name}Config(TypedDict):
    """Configuration for {class_name_lower}."""

    enabled: bool
    max_retries: int
    timeout_seconds: float
    log_level: Literal["DEBUG", "INFO", "WARNING", "ERROR"]
    tags: List[str]


class {class_name}Request(TypedDict):
    """Request payload for {class_name_lower} API."""

    action: Literal["create", "update", "delete", "read"]
    resource_id: str
    payload: dict[str, object]
    metadata: NotRequired[dict[str, str]]
    trace_id: NotRequired[str]


class {class_name}Response(TypedDict):
    """Response from {class_name_lower} API."""

    success: bool
    data: Optional[dict[str, object]]
    error: NotRequired[str]
    timestamp: str
    request_id: str


class Pagination(TypedDict):
    """Pagination parameters."""

    page: int
    page_size: int
    total_count: int
    has_next: bool
    has_previous: bool


class {class_name}ListResponse(TypedDict):
    """Paginated list response."""

    items: List[{class_name}Response]
    pagination: Pagination


class ErrorDetail(TypedDict):
    """Error detail information."""

    code: str
    message: str
    field: NotRequired[str]
    details: NotRequired[dict[str, object]]


class ValidationResult(TypedDict):
    """Validation result."""

    is_valid: bool
    errors: List[ErrorDetail]
    warnings: NotRequired[List[ErrorDetail]]
''',
    "utils": '''"""Utility functions for {module}."""
from typing import TypeVar, List, Optional, Callable, Any, Iterable, Dict
from functools import reduce
import hashlib
import json
from datetime import datetime, timezone


T = TypeVar("T")
K = TypeVar("K")
V = TypeVar("V")


def chunk_list(items: List[T], chunk_size: int) -> List[List[T]]:
    """Split list into chunks of specified size."""
    return [items[i:i + chunk_size] for i in range(0, len(items), chunk_size)]


def flatten(nested: List[List[T]]) -> List[T]:
    """Flatten nested list."""
    return [item for sublist in nested for item in sublist]


def unique_by(items: List[T], key: Callable[[T], K]) -> List[T]:
    """Return unique items based on key function."""
    seen: set[K] = set()
    result: List[T] = []
    for item in items:
        k = key(item)
        if k not in seen:
            seen.add(k)
            result.append(item)
    return result


def group_by(items: Iterable[T], key: Callable[[T], K]) -> Dict[K, List[T]]:
    """Group items by key function."""
    groups: Dict[K, List[T]] = {{}}
    for item in items:
        k = key(item)
        if k not in groups:
            groups[k] = []
        groups[k].append(item)
    return groups


def first(items: List[T], predicate: Optional[Callable[[T], bool]] = None) -> Optional[T]:
    """Return first item matching predicate, or first item if no predicate."""
    if predicate is None:
        return items[0] if items else None
    for item in items:
        if predicate(item):
            return item
    return None


def pipe(*functions: Callable[[Any], Any]) -> Callable[[Any], Any]:
    """Compose functions left to right."""
    def piped(value: Any) -> Any:
        return reduce(lambda v, f: f(v), functions, value)
    return piped


def hash_dict(d: Dict[str, Any]) -> str:
    """Create deterministic hash of dictionary."""
    serialized = json.dumps(d, sort_keys=True, default=str)
    return hashlib.sha256(serialized.encode()).hexdigest()


def now_utc() -> datetime:
    """Get current UTC datetime."""
    return datetime.now(timezone.utc)


def safe_get(d: Dict[K, V], *keys: K, default: Optional[V] = None) -> Optional[V]:
    """Safely get nested dictionary value."""
    current: Any = d
    for key in keys:
        if isinstance(current, dict) and key in current:
            current = current[key]
        else:
            return default
    return current
''',
}


def generate_class_name(module: str, index: int) -> str:
    """Generate a class name based on module and index."""
    prefixes = ["Base", "Core", "Main", "Primary", "Default", "Custom", "Extended", "Abstract"]
    suffixes = ["Entity", "Model", "Item", "Record", "Data", "Info", "Spec", "Entry"]

    prefix = prefixes[index % len(prefixes)]
    suffix = suffixes[(index + len(module)) % len(suffixes)]
    module_part = module.capitalize()

    return f"{prefix}{module_part}{suffix}"


def write_init_file(module_path: Path, file_names: List[str]) -> None:
    """Write __init__.py with exports."""
    exports: List[str] = []
    imports: List[str] = []

    for fname in file_names:
        module_name = fname.replace(".py", "")
        imports.append(f"from .{module_name} import *")

    content = f'''"""{module_path.name} module."""
{chr(10).join(imports)}

__all__: list[str] = []
'''

    init_path = module_path / "__init__.py"
    init_path.write_text(content)


def generate_module(base_path: Path, module_name: str, file_count: int) -> None:
    """Generate a module with specified number of files."""
    module_path = base_path / module_name
    module_path.mkdir(parents=True, exist_ok=True)

    template_names = list(TEMPLATES.keys())
    file_names: List[str] = []

    for i in range(file_count):
        template_key = template_names[i % len(template_names)]
        template = TEMPLATES[template_key]

        class_name = generate_class_name(module_name, i)
        class_name_lower = class_name.lower()

        content = template.format(
            module=module_name,
            class_name=class_name,
            class_name_lower=class_name_lower,
        )

        file_name = f"{template_key}_{i:02d}.py"
        file_path = module_path / file_name
        file_path.write_text(content)
        file_names.append(file_name)
        print(f"  Created: {file_path.relative_to(base_path.parent)}")

    write_init_file(module_path, file_names)
    print(f"  Created: {module_path / '__init__.py'}")


def generate_codebase(size_name: str, config: Dict[str, int]) -> None:
    """Generate a codebase of specified size."""
    base_path = Path(__file__).parent / "sample-code" / size_name

    # Clean existing
    if base_path.exists():
        import shutil
        shutil.rmtree(base_path)

    base_path.mkdir(parents=True, exist_ok=True)

    num_modules = config["modules"]
    files_per_module = config["files_per_module"]

    print(f"\nGenerating {size_name} codebase ({num_modules} modules, {files_per_module} files each):")

    modules_to_use = MODULE_NAMES[:num_modules]

    for module_name in modules_to_use:
        generate_module(base_path, module_name, files_per_module)

    # Create root __init__.py
    root_init = base_path / "__init__.py"
    root_init.write_text(f'''"""{size_name.capitalize()} test codebase for PyRight benchmarks."""
__version__ = "0.1.0"
''')
    print(f"  Created: {root_init.relative_to(base_path.parent)}")

    total_files = num_modules * files_per_module + num_modules + 1  # +1 for root __init__
    print(f"  Total: {total_files} files")


def main() -> None:
    """Generate all sample codebases."""
    print("PyRight Multithreaded Benchmark - Sample Code Generator")
    print("=" * 60)

    for size_name, config in SIZES.items():
        generate_codebase(size_name, config)

    print("\n" + "=" * 60)
    print("Generation complete!")
    print("\nNext steps:")
    print("  1. cd pyright")
    print("  2. pyright                  # Single-threaded baseline")
    print("  3. pyright --threads        # Multi-threaded comparison")


if __name__ == "__main__":
    main()
