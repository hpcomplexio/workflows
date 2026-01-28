"""Utility functions for middleware."""
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
    groups: Dict[K, List[T]] = {}
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
