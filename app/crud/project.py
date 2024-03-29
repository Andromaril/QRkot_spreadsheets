from typing import Dict, List, Optional

from sqlalchemy import asc, func, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
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

    async def get_projects_by_completion_rate(
            self,
            session: AsyncSession,
    ) -> List[Dict[str, str]]:
        """получить список проетов"""
        projects = await session.execute(select([
            CharityProject.name,
            CharityProject.description,
            (func.julianday(CharityProject.close_date) -
             func.julianday(CharityProject.create_date)
             ).label('timedonat')]).order_by(asc('timedonat')))
        projects = projects.all()
        return projects


project_crud = CRUDProject(CharityProject)