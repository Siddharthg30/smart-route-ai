from uuid import UUID

from sqlalchemy.orm import Session

from domain.intersection.schemas import IntersectionCreate

from .models import Intersection

class IntersectionRepository:
    """
    Handles all database operations for Intersection.
    """

    def __init__(self, db: Session):
        self.db = db

    def create(
        self,
        data: IntersectionCreate,
    ) -> Intersection:

        intersection = Intersection(
            **data.model_dump()
        )

        self.db.add(intersection)
        self.db.commit()
        self.db.refresh(intersection)

        return intersection
    
    def get_by_id(
        self,
        intersection_id: UUID,
    ) -> Intersection | None:

        return (
            self.db.query(Intersection)
            .filter(
                Intersection.id == intersection_id
            )
            .first()
        )
    
    def get_all(self) -> list[Intersection]:

        return (
            self.db.query(Intersection)
            .all()
        )
    
    def get_by_name(
        self,
        name: str,
    ) -> Intersection | None:
        """
        Retrieve an intersection by its name.
        """

        return (
            self.db.query(Intersection)
            .filter(
                Intersection.name == name
            )
            .first()
        )