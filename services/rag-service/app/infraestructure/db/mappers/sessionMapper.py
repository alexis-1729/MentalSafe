from app.domain.entities.session import Session
from app.infraestructure.db.models.sessionModel import SessionORM

class SessionMapper:

    @staticmethod
    def to_domain(orm: SessionORM) -> Session:
        return Session(
            id_session=orm.id_session,
            user_id=orm.user_id,
            title=orm.title,
            created_at=orm.created_at,
            updated_at=orm.updated_at
        )

    @staticmethod
    def to_orm(session: Session) -> SessionORM:
        return SessionORM(
            id_session=session.id_session,
            user_id=session.user_id,
            title=session.title
        )
