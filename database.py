import psycopg2 as ps
from psycopg2 import sql
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


class Database(object):
    def __init__(self, name, user, password, host, port):
        self.dbname = name
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.connectDB("postgres")
        self.cursor.execute("SELECT * FROM pg_catalog.pg_database WHERE datname = %s", (self.dbname,))
        flag = self.cursor.fetchone()
        if flag is None:
            self.cursor.execute(sql.SQL("CREATE DATABASE {}").format(sql.Identifier(self.dbname)))
        self.connection.close()
        self.connectDB(self.dbname)
        if flag is None:
            with self.connection.cursor() as cursor_:
                cursor_.execute(open("funct.sql", "r").read())

    def connectDB(self, name):
        self.connection = ps.connect(
            dbname=name,
            user=self.user,
            password=self.password,
            host=self.host,
            port=self.port
        )
        self.connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        self.cursor = self.connection.cursor()

    def delete_database(self):
        self.connectDB("postgres")
        self.cursor.execute(sql.SQL(f"DROP DATABASE {self.dbname}"))
        self.connection.close()
        del self

    def create_database(self):
        self.cursor.callproc("create_database")

    def get_doctors(self):
        self.cursor.callproc("get_doctors")
        return self.cursor.fetchone()[0]

    def get_patients(self):
        self.cursor.callproc("get_patients")
        return self.cursor.fetchone()[0]

    def get_cabinets(self):
        self.cursor.callproc("get_cabinets")
        return self.cursor.fetchone()[0]

    def get_cards(self):
        self.cursor.callproc("get_cards")
        return self.cursor.fetchone()[0]

    def get_appointments(self):
        self.cursor.callproc("get_appointments")
        return self.cursor.fetchone()[0]

    def add_to_doctors(self, FIO, specialization, education):
        self.cursor.callproc("add_to_doctors", (FIO, specialization,education))

    def add_to_patients(self, title, FIO, card_id):
        self.cursor.callproc("add_to_patients", (title, FIO, card_id))

    def add_to_card(self, owner_fio, number_of_appointments):
        self.cursor.callproc("add_to_card", (owner_fio, number_of_appointments))

    def add_to_cabinets(self, number, specialization, fio_of_responsible_person):
        self.cursor.callproc("add_to_patients", (number, specialization, fio_of_responsible_person))

    def add_to_appointment(self, cabinet_number, id_doctor, id_patient):
        self.cursor.callproc("add_to_patients", (cabinet_number, id_doctor, id_patient))

    def clear_doctors(self):
        self.cursor.callproc("clear_doctors")

    def clear_patients(self):
        self.cursor.callproc("clear_patients")

    def clear_persons(self):
        self.cursor.callproc("clear_persons")

    def clear_cabinets(self):
        self.cursor.callproc("clear_cabinets")

    def clear_cards(self):
        self.cursor.callproc("clear_cards")

    def clear_appointments(self):
        self.cursor.callproc("clear_appointments")

    def clear_all(self):
        self.cursor.callproc("clear_all")

    def find_patient_by_FIO(self, FIO):
        self.cursor.callproc("find_patient", (FIO,))
        return self.cursor.fetchone()[0]

    def find_cabinet(self, FIO):
        self.cursor.callproc("find_cabinet", (FIO,))
        return self.cursor.fetchone()[0]

    def delete_patient_by_FIO(self, FIO):
        self.cursor.callproc("delete_patient_by_FIO", (FIO,))

    def delete_doctor_chosen(self, id):
        self.cursor.callproc("delete_doctor_chosen", (id,))

    def delete_patient_chosen(self, id):
        self.cursor.callproc("delete_patient_chosen", (id,))

    def update_doctor_by_ID(self, newID, id):
        self.cursor.callproc("update_doctor_by_id", (newID, id,))

    def update_person_by_title(self, newtitle, id):
        self.cursor.callproc("update_cabinet_by_number", (newtitle, id,))

    def  update_patient_by_FIO(self, newFIO, id):
        self.cursor.callproc(" update_patient_by_FIO", (newFIO, id,))

    def update_patient_by_age(self, new_age, id):
        self.cursor.callproc("update_patient_by_age", (new_age, id,))

    def disconnect(self):
        self.connection.close()
