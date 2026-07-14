from uuid import UUID

from fastapi import APIRouter, Depends, status

from domain.intersection.dependencie import (
    get_intersection_service,
)
from domain.intersection.schemas import (
    IntersectionCreate,
    IntersectionListResponse,
    IntersectionResponse,
)
from domain.intersection.services import (
    IntersectionService,
)

router = APIRouter(
    prefix="/intersections",
    tags=["Intersections"],
)

@router.post(
    "",
    response_model=IntersectionResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_intersection(
    data: IntersectionCreate,
    service: IntersectionService = Depends(
        get_intersection_service,
    ),
):
    """
    Create a new intersection.
    """

    return service.create(data)

@router.get(
    "",
    response_model=IntersectionListResponse,
)
def get_intersections(
    service: IntersectionService = Depends(
        get_intersection_service,
    ),
):
    """
    Retrieve all intersections.
    """

    intersections = service.get_all()

    return {
        "items": intersections,
        "total": len(intersections),
    }

@router.get(
    "/{intersection_id}",
    response_model=IntersectionResponse,
)
def get_intersection(
    intersection_id: UUID,
    service: IntersectionService = Depends(
        get_intersection_service,
    ),
):
    """
    Retrieve an intersection by its ID.
    """

    return service.get_by_id(
        intersection_id,
    )