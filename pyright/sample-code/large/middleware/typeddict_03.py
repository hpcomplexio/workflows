"""TypedDict definitions for middleware."""
from typing import TypedDict, Optional, List, Literal, NotRequired
from datetime import datetime


class PrimaryMiddlewareInfoConfig(TypedDict):
    """Configuration for primarymiddlewareinfo."""

    enabled: bool
    max_retries: int
    timeout_seconds: float
    log_level: Literal["DEBUG", "INFO", "WARNING", "ERROR"]
    tags: List[str]


class PrimaryMiddlewareInfoRequest(TypedDict):
    """Request payload for primarymiddlewareinfo API."""

    action: Literal["create", "update", "delete", "read"]
    resource_id: str
    payload: dict[str, object]
    metadata: NotRequired[dict[str, str]]
    trace_id: NotRequired[str]


class PrimaryMiddlewareInfoResponse(TypedDict):
    """Response from primarymiddlewareinfo API."""

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


class PrimaryMiddlewareInfoListResponse(TypedDict):
    """Paginated list response."""

    items: List[PrimaryMiddlewareInfoResponse]
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
