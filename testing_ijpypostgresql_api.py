#!/usr/bin/python

# ---------------------------------------
# importing modules
# ---------------------------------------
from ijpypostgresql import Crud_oper as crud
from ijpypostgresql import ModulePostgreSQLdb as pgdb
from ijpypostgresql import HandleDataFromTerminal as dt


# the main method of testing app
def test_ijpostgresql_api():

    pgdbo = pgdb.ModulePostgreSQLdb()
    crud_op = crud.Crud_oper()
    dto = dt.HandleDataFromTerminal()

    # con, cur = pgdbo.connectbyconfigfile()

    conn, cursor = pgdbo.connect2db()

    # conn, cursor = pgdbo.connect2db_sem_db()

    # pgdbo.close_pg_con(conn, cursor)
    # pgdbo.verification(cursor, 'db')
    # crud_op.read_all(cursor, pgdbo.person_table)
    # pgdbo.create_db(cursor, pgdbo.db_test)

    # pgdbo.create_table(cursor, pgdbo.tb_test)

    # drop
    # pgdbo.alter_table(cursor, pgdbo.tb_test, 'drop', 'gender')
    # pgdbo.alter_table(cursor, pgdbo.tb_test, 'drop', 'age')

    # add
    # pgdbo.alter_table(cursor, pgdbo.tb_test, 'add', 'role')
    # pgdbo.alter_table(cursor, pgdbo.tb_test, 'add', 'adress')

    # data_one = dto.data_terminal()

    # crud_op.create(conn, cursor, pgdbo.dev_tb, data_one)

    crud_op.read_one(cursor, pgdbo.dev_tb)
    crud_op.read_all(cursor, pgdbo.tb_test)

    # pgdbo.drop_struct(conn, cursor, 'tb', pgdbo.tb_test)
    # pgdbo.truncate(conn, cursor, pgdbo.tb_test)

    # close conn and cursor
    pgdbo.close_pg_con(conn, cursor)


if __name__=='__main__':
    test_ijpostgresql_api()
