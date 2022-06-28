import datetime as dt
from typing import Optional

from sqlalchemy import select, asc, desc, func
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.core import db
from app.models import CharityProject


class CRUDProject(CRUDBase):

    async def get_project_id_by_name(
            self,
            name: str,
            session: AsyncSession,
    ) -> Optional[int]:
        db_project = await session.execute(
            select(CharityProject.id).where(
                CharityProject.name == name
            )
        )
        db_project = db_project.scalars().first()
        return db_project


    async def get_projectinfo_by_date(
            self,
            session: AsyncSession,
            #reverse: bool = False
    ) -> list[dict[str, str]]:
        query = select(
            CharityProject.name,
            CharityProject.description,
            (
                func.julianday(CharityProject.close_date) -
                func.julianday(CharityProject.create_date)
            ).label('lifetime')
        )
        #query = (
            #query.order_by(asc('lifetime')),
            #query.order_by(desc('lifetime'))
        #)

        closed_projects = await session.execute(query)

        return closed_projects.all()


project_crud = CRUDProject(CharityProject)