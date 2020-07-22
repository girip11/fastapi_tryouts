from fastapi import APIRouter, Path

router = APIRouter()


# Alias parameter in path should match the path parameter
# defined in the route
@router.get("/path_params_validation/{id}")
async def path_params_validation(
    item_id: int = Path(
        ..., title="Item ID", description="ID of the item", alias="id", le=1000, ge=1
    )
):
    return {"item_id": item_id}
