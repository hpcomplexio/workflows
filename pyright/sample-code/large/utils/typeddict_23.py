"""TypedDict definitions for utils."""
from typing import TypedDict, Optional, List, Literal, NotRequired
from datetime import datetime


class AbstractUtilsDataConfig(TypedDict):
    """Configuration for abstractutilsdata."""

    enabled: bool
    max_retries: int
    timeout_seconds: float
    log_level: Literal["DEBUG", "INFO", "WARNING", "ERROR"]
    tags: List[str]


class AbstractUtilsDataRequest(TypedDict):
    """Request payload for abstractutilsdata API."""

    action: Literal["create", "update", "delete", "read"]
    resource_id: str
    payload: dict[str, object]
    metadata: NotRequired[dict[str, str]]
    trace_id: NotRequired[str]


class AbstractUtilsDataResponse(TypedDict):
    """Response from abstractutilsdata API."""

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


class AbstractUtilsDataListResponse(TypedDict):
    """Paginated list response."""

    items: List[AbstractUtilsDataResponse]
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
