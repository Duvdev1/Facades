from DbRepo import DbRepo
from Facade import Facade
from Tourist import Tourist
from visit import visit
from attraction import attraction
from db_config import local_session, create_all_entities
# create tables
create_all_entities()

repo = DbRepo(local_session)

# adding data to tables
'''
repo.add_all(
    [attraction(name='Movie', price=10), attraction(name='Restaurant', price=40), attraction(name='Bar', price=50),
     attraction(name='Park')])

repo.add_all([Tourist(name='Moshe'), Tourist(name='Kobi'), Tourist(name='Roy'), Tourist(name='Levi')])

repo.add_all([visit(t_id=1, a_id=2), visit(t_id=3, a_id=2), visit(t_id=2, a_id=3),visit(t_id=2, a_id=2)])
'''

print(repo.get_by_column_value(visit, visit.t_id, '1'))
print(repo.get_by_column_value(attraction, attraction.id, '1'))

def get_attractions_by_tourist_name(tName):
    tourist = repo.get_by_column_value(Tourist, Tourist.name, tName)[0]
    visits = repo.get_by_column_value(visit, visit.t_id, tourist.id)
    attractions_names = []
    for v in visits:
        attrt = repo.get_by_id(attraction, v.a_id)
        attractions_names.append(attrt.name)

    print('--------------------------')
    print(attractions_names)
    print('--------------------------')

get_attractions_by_tourist_name('Moshe')

faced = Facade()
faced.add_tourist_and_atraction(Tourist(name='Yoram'), attraction(name='Dance Room', price=10))






# get_all
# users = local_session.query(User).all()
# users = repo.get_all(User)
# print(users)
# companies = repo.get_all_limit(Company, 3)
# print(companies)
#
# users = repo.get_all_order_by(Company, Company.name, asc)
# print('asc', users)
#
# users = repo.get_all_order_by(Company, Company.name, desc)
# print('desc', users)
'''
# select * from users where username like '%moshe%'
if len(local_session.query(User).filter(User.username.ilike('%moshe%')).all()) > 0:
    local_session.query(User).filter(User.id >= 1).delete(synchronize_session=False)
    local_session.commit()

# Insert
moshe = User(username='moshe', email='moshe@jb.com')
local_session.add(moshe)
#local_session.add(User(username='moshe', email='moshe@jb.com'))
local_session.commit()

users_list = [User(username='rob', email='rob@rob.com'), User(username='job', email='job@job.com')]
local_session.add_all(users_list)
local_session.commit()

local_session.query(User).filter(User.username == 'moshe').update({User.username: 'new moshe', 'email':'moshe@walla.com'},\
                                                                  synchronize_session=False)
local_session.commit()

local_session.query(Company).filter(Company.id >= 1).delete(synchronize_session=False)

local_session.add(Company(name='Elad', age=22, address='Sokolov 11', salary='60000'))
local_session.commit()

com1 = Company(name='Yishay', age=22, address='Sokolov 11', salary='60000')
com2 = Company(name='Uri', age=22, address='Sokolov 11', salary='60000')
com_ls = [com1, com2]
local_session.add_all(com_ls)
local_session.commit()

'''
