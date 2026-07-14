from fastapi import APIRouter
from domain.intersection.router import router as intersection_router
from api.routes.health import router as health_router

router = APIRouter()

router.include_router(health_router)

api_router = APIRouter()

api_router.include_router(intersection_router)