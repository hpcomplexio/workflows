"""TypedDict definitions for controllers."""
from typing import TypedDict, Optional, List, Literal, NotRequired
from datetime import datetime


class BaseControllersRecordConfig(TypedDict):
    """Configuration for basecontrollersrecord."""

    enabled: bool
    max_retries: int
    timeout_seconds: float
    log_level: Literal["DEBUG", "INFO", "WARNING", "ERROR"]
    tags: List[str]


class BaseControllersRecordRequest(TypedDict):
    """Request payload for basecontrollersrecord API."""

    action: Literal["create", "update", "delete", "read"]
    resource_id: str
    payload: dict[str, object]
    metadata: NotRequired[dict[str, str]]
    trace_id: NotRequired[str]


class BaseControllersRecordResponse(TypedDict):
    """Response from basecontrollersrecord API."""

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


class BaseControllersRecordListResponse(TypedDict):
    """Paginated list response."""

    items: List[BaseControllersRecordResponse]
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
