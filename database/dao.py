from database.DB_connect import DBConnect
from model.bonifico import Bonifico
from model.filiale import Filiale


class DAO:
    """
        Implementare tutte le funzioni necessarie a interrogare il database.
        """
    # TODO

    @staticmethod
    def read_all_bonifici():
        cnx = DBConnect.get_connection()
        result = {}
        if cnx is None:
            print("❌ Errore di connessione al database.")
            return None

        cursor = cnx.cursor(dictionary=True)
        query = """ SELECT * FROM bonifico ORDER BY id"""
        try:
            cursor.execute(query)
            for row in cursor:
                bonifico = Bonifico(id=row["id"],
    id_banca=row["id_banca"],
    codice_operazione=row["codice_operazione"],
    id_filiale_origine=row["id_filiale_origine"],
    id_filiale_destinazione=row["id_filiale_destinazione"],
    data_disposizione=row["data_disposizione"],
    commissione=row["commissione"],
    data_accredito=row["data_accredito"],
    importo=row["importo"]
    )
                result[bonifico.id] = bonifico
        except Exception as e:
            print(f"Errore durante la query read_all_bonifici: {e}")
            result = None
        finally:
            cursor.close()
            cnx.close()

        return result

    @staticmethod
    def get_all_filiali():
        cnx = DBConnect.get_connection()
        result = {}
        if cnx is None:
            print("❌ Errore di connessione al database.")
            return None

        cursor = cnx.cursor(dictionary=True)
        query = """ SELECT * FROM filiale ORDER BY id"""
        try:
            cursor.execute(query)
            for row in cursor:
                filiale = Filiale(  id=row["id"],
    codice=row["codice"],
    nome=row["nome"],
    citta=row["citta"],
    provincia=row["provincia"],
    latitudine=row["latitudine"],
    longitudine=row["longitudine"]
)
                result[filiale.id] = filiale
        except Exception as e:
            print(f"Errore durante la query get_alla_filiali: {e}")
            result = None
        finally:
            cursor.close()
            cnx.close()


        return result

