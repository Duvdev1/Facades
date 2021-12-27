from DbRepo import DbRepo
from db_config import local_session, create_all_entities
from visit import visit

repo = DbRepo(local_session)


class Facade:
    def add_tourist_and_atraction(self, tourist, attraction):
        repo.add(tourist)
        repo.add(attraction)
        repo.add(visit(t_id=tourist.id, a_id=attraction.id))