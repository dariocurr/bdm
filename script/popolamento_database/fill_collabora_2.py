import random
from database_connection import database_connection


def creazione_collabora2():
    for db in  ["bdm_unipa", "bdm_unina", "bdm_unito", "bdm_unimi"]:
        sql = database_connection(db)
        eventi = list(sql.execute_query("SELECT id_evento, data FROM evento"))
        agenzie_esterne = list(sql.execute_query("SELECT id_agenzia, descrizione FROM agenzia_esterna"))
        for evento in eventi:
            eventi_agenzie = list()
            for _ in range(0, random.randint(1,4)):
                agenzia_random = agenzie_esterne[random.randint(0, len(agenzie_esterne)-1)][0]
                if agenzia_random not in eventi_agenzie:
                    eventi_agenzie.append(agenzia_random)
            for agenzia in eventi_agenzie:
                collabora2 = (evento[0], agenzia, evento[1], "finanziamento per organizzazione evento")
                query = "INSERT INTO collabora_2 VALUES ("
                for value in collabora2:
                    query += "'" + str(value) + "',"
                sql.execute_query(query[:-1] + ")")


creazione_collabora2()
