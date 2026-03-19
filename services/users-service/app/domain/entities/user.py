from datetime import datetime, date
from uuid import UUID

class User:

    def __init__(self, 
                 id: UUID,
                 id_auth: UUID,
                 full_name: str,
                 apellidos: str,
                 fecha_nac: date,
                 genero: str,
                 created_at: datetime,
                 updated_at: datetime) -> None:
        self.id = id
        self.id_auth = id_auth
        self.full_name = full_name
        self.apellidos = apellidos
        self.fecha_nac = fecha_nac
        self.genero = genero
        self.created_at = created_at
        self.updated_at = updated_at
        