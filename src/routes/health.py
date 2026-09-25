from fastapi import APIRouter

health_router = APIRouter()

@health_router.get("/health")
async def health() -> dict[str,str]:
    return{"message":"asmaaae meryem je vous aiiiiiiimes"}