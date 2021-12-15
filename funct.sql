create function create_database()
	returns void language sql as $$
		create table if not exists "Doctors"(
			id integer primary key not null generated always as identity,
			FIO text not null,
			specialization text not null,
			education text not null
		);
		create table if not exists "Patients"(
			id integer primary key not null generated always as identity,
			FIO text not null,
			age integer not null,
			card_id integer not null
		);
		create table if not exists "Cabinets"(
		    number integer primary key not null,
		    specialization text not null,
		    fio_of_responsible_person text not null
		);
		create table if not exists "Card"(
		    id integer primary key not null generated always as identity,
		    last_update timestamptz default current_timestamp not null,
		    number_of_appointments integer not null,
		    owner_fio text not null

		);
		create table if not exists "Appointment"(
		    id integer primary key not null generated always as identity,
		    cabinet_number integer not null,
		    id_doctor integer not null,
		    id_patient integer not null
		);

		create index if not exists FIO on "Doctors" (FIO);

		create or replace function update_time()
			returns trigger as $u$
			begin
				new.last_update = current_timestamp;
				return new;
			end;
		$u$ language plpgsql;

		drop trigger if exists trigger_update on "Card";

		create trigger trigger_update before update on "Card"
			for row execute procedure update_time();
$$;

select "create_database"();

create function get_doctors()
	returns json language plpgsql as $$
		begin
			return (select json_agg(json_build_object(
				'id', "Doctors".id,
				'fio', "Doctors".FIO,
				'specialization', "Doctors".specialization
				'education', "Doctors".education
				)) from "Doctors");
		end
	$$;

create function get_patients()
	returns json language plpgsql as $$
		begin
			return (select json_agg(json_build_object(
				'id', "Patients".id,
				'fio', "Patients".FIO,
				'age', "Patients".age,
				'card_id', "Patients".card_id
				)) from "Patients");
		end
	$$;

create function get_cabinets()
	returns json language plpgsql as $$
		begin
			return (select json_agg(json_build_object(
				'number', "Cabinets".number,
				'specialization', "Cabinets".specialization,
				'fio_of_responsible_person', "Cabinets".fio_of_responsible_person,
				)) from "Cabinets");
		end
	$$;

create function get_cards()
	returns json language plpgsql as $$
		begin
			return (select json_agg(json_build_object(
				'id', "Card".id,
				'last_update', "Card".last_update,
				'number_of_appointments', "Card".number_of_appointments,
				'owner_fio', "Card".owner_fio
				)) from "Card");
		end
	$$;

create function get_appointments()
	returns json language plpgsql as $$
		begin
			return (select json_agg(json_build_object(
				'id', "Appointment".id,
				'cabinet_number', "Appointment".cabinet_number,
				'id_doctor', "Appointment".id_doctor,
				'id_patient',"Appointment".id_patient
				)) from "Appointment");
		end
	$$;


create function add_to_doctors(in FIO text, in specialization text,in education text)
	returns void language sql as $$
		insert into "Doctors"(FIO, specialization, education) values (FIO, specialization, education)
	$$;

create function add_to_patients(in FIO text, in age integer, in card_id integer)
	returns void language sql as $$
		insert into "Patients"(age, FIO, card_id) values (age, FIO, card_id)
	$$;

create function add_to_card(in owner_fio text, in number_of_appointments integer)
	returns void language sql as $$
		insert into "Card"(owner_fio, number_of_appointments) values (owner_fio, number_of_appointments)
	$$;

create function add_to_cabinets(in number integer, in specialization text, in fio_of_responsible_person text)
	returns void language sql as $$
		insert into "Cabinets"(number, specialization, fio_of_responsible_person) values (number, specialization, fio_of_responsible_person)
	$$;

create function add_to_appointment(in id_doctor integer, in cabinet_number integer, in id_patient integer)
	returns void language sql as $$
		insert into "Appointment"(cabinet_number, id_doctor, id_patient) values (cabinet_number, id_doctor, id_patient)
	$$;

create function clear_doctors()
	returns void language sql as $$
		truncate "Doctors"
	$$;

create function clear_patients()
	returns void language sql as $$
		truncate "Patients"
	$$;

create function clear_cabinets()
	returns void language sql as $$
		truncate "Cabinets"
	$$;

create function clear_cards()
	returns void language sql as $$
		truncate "Card"
	$$;

create function clear_appointments()
	returns void language sql as $$
		truncate "Appointment"
	$$;

create function clear_all()
	returns void language sql as $$
		truncate "Doctors",
		truncate "Patients",
		truncate "Cabinets",
		truncate "Card",
		truncate "Appointment"
	$$;

create function find_patient(in query text)
	returns json language plpgsql as $$
		begin
			return (select json_agg(json_build_object(
				'id', "Patients".id,
				'title', "Patients".title,
				'age', "Patients".age,
				'card_id', "Patients".card_id
				)) from "Patients" where "Patients".FIO like concat('%', query, '%'));
		end;
	$$;

create function find_department(in query text)
	returns json language plpgsql as $$
		begin
			return (select json_agg(json_build_object(
				'number', "Cabinets".number,
				'specialization', "Cabinets".specialization,
				'fio_of_responsible_person', "Cabinets".fio_of_responsible_person,
				)) from "Cabinets" where "Cabinets".fio_of_responsible_person like concat('%', query, '%')
				)
			);
		end;
	$$;

create function delete_patient_by_FIO(in FIO_ text)
	returns void language plpgsql as $$
		begin
			delete from "Patients" where FIO = FIO_;
		end;
	$$;

create function delete_doctor_chosen(in FIO_ text)
	returns void language plpgsql as $$
		begin
			delete from "Doctors" where FIO = FIO_;
		end;
	$$;

create function delete_patient_chosen(in id_ integer)
	returns void language plpgsql as $$
		begin
			delete from "Patients" where id = id_;
		end;
	$$;


create function update_cabinet_by_number(in new_specialization text, in number_ integer)
	returns void language plpgsql as $$
		begin
			update "Cabinet" set specialization = new_specialization where number = number_;
		end;
	$$;

create function update_patient_on_FIO(in new_FIO text, in id_ integer)
	returns void language plpgsql as $$
		begin
			update "Patients" set FIO = new_FIO where id = id_;
		end;
	$$;

create function update_patient_by_age(in new_age integer, in id_ integer)
	returns void language plpgsql as $$
		begin
			update "Patients" set age = new_age where id = id_;
		end;
	$$;
