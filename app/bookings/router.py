from fastapi import APIRouter
from sqlalchemy import select

from app.bookings.dao import BookingDAO
from app.bookings.schemas import SBooking
from app.database import async_session_maker
from app.bookings.models import Bookings

router = APIRouter(
    prefix="/bookings",
    tags=["Бронирования"],
)


# @router.get("")
# async def get_bookings():
#     async with async_session_maker() as session:
#         query = select(Bookings)
#         result = await session.execute(query)
#         print(result.mappings().all())


@router.get("")
async def get_bookings() -> list[SBooking]:
    return await BookingDAO.find_all()
