"""TypedDict definitions for services."""
from typing import TypedDict, Optional, List, Literal, NotRequired
from datetime import datetime


class CustomServicesInfoConfig(TypedDict):
    """Configuration for customservicesinfo."""

    enabled: bool
    max_retries: int
    timeout_seconds: float
    log_level: Literal["DEBUG", "INFO", "WARNING", "ERROR"]
    tags: List[str]


class CustomServicesInfoRequest(TypedDict):
    """Request payload for customservicesinfo API."""

    action: Literal["create", "update", "delete", "read"]
    resource_id: str
    payload: dict[str, object]
    metadata: NotRequired[dict[str, str]]
    trace_id: NotRequired[str]


class CustomServicesInfoResponse(TypedDict):
    """Response from customservicesinfo API."""

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


class CustomServicesInfoListResponse(TypedDict):
    """Paginated list response."""

    items: List[CustomServicesInfoResponse]
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
