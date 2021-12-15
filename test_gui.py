from tkinter import *
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, ttk

window = Tk()

window.geometry("1400x800")
window.configure(bg = "#A18EEB")
window.title("Мед организация")
bg_color = "#A18EEB"
canvas = Canvas(
    window,
    bg = bg_color,
    height = 800,
    width = 1300,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)
canvas.place(x = 0, y = 0)

#######################search#######################
search_query = StringVar()

search_entry = Entry(textvariable=search_query)
search_entry.place(
    x=20,
    y=20,
    width=300,
    height=30)

search_patient = Button(
    text="Найти пациента",
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print(search_query.get()),
    relief="flat")

search_patient.place(
    x=340,
    y=20,
    width=140,
    height=30)


search_cabinet = Button(
    text="Найти кабинет по фио ответственного",
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print(search_query.get()),
    relief="flat")

search_cabinet.place(
    x=500,
    y=20,
    width=230,
    height=30)


search_patient = Button(
    text="Удалить пациента по фио",
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print(search_query.get()),
    relief="flat")

search_patient.place(
    x=750,
    y=20,
    width=200,
    height=30)


search_cabinet = Button(
    text="Удалить доктора по фио",
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print(search_query.get()),
    relief="flat")

search_cabinet.place(
    x=970,
    y=20,
    width=200,
    height=30)

search_cabinet = Button(
    text="Удалить пациента",
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print(search_query.get()),
    relief="flat")

search_cabinet.place(
    x=1190,
    y=20,
    width=130,
    height=30)

#######################general buttons#######################

LabelFrame(canvas, text="Общее", bg=bg_color).place(x=1060, y=440, width=160, height=230)

create_DB = Button(
    text="Создать базу данных",
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("DB created"),
    relief="flat")

create_DB.place(
    x=1070,
    y=460,
    width=140,
    height=40)

delete_DB = Button(
    text="Удалить базу данных",
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("DB deleted"),
    relief="flat")
delete_DB.place(
    x=1070,
    y=510,
    width=140,
    height=40)

clear_all = Button(
    text="Очистить все",
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("All clear"),
    relief="flat")
clear_all.place(
    x=1070,
    y=560,
    width=140,
    height=40)


####################################################

doctors = ttk.Treeview(canvas)
patients = ttk.Treeview(canvas)
cabinets = ttk.Treeview(canvas)
card = ttk.Treeview(canvas)
appointment = ttk.Treeview(canvas)

#############доктора############################
Label(text="Доктора", bg=bg_color).place(x=5, y=55, width=60, height=30)

add_doctor_id, add_doctor_fio, add_doctor_specialization, add_doctor_education = StringVar(),StringVar(),StringVar(),StringVar()

Entry(textvariable=add_doctor_fio).place(x=10,y=80,width=190,height=25)
Entry(textvariable=add_doctor_specialization).place(x=195,y=80,width=100,height=25)
Entry(textvariable=add_doctor_education).place(x=295,y=80,width=85,height=25)

Button(text="+",
       borderwidth=0,
       highlightthickness=0,
       command=lambda: print("adding doctor"),
       relief="flat").place(x=385,
                            y=80,
                            width=25,
                            height=25)

doctors['columns'] = ('id', 'fio', 'specialization', 'education')

doctors.column("#0", width=0,  stretch=NO)
doctors.column('id', anchor=CENTER, width=25)
doctors.column('fio', anchor=CENTER, width=160)
doctors.column('specialization', anchor=CENTER, width=100)
doctors.column('education', anchor=CENTER, width=80)


doctors.heading("#0",text="",anchor=CENTER)
doctors.heading('id',text="ID",anchor=CENTER)
doctors.heading('fio',text="ФИО",anchor=CENTER)
doctors.heading('specialization',text="Специальность",anchor=CENTER)
doctors.heading('education',text="Образование",anchor=CENTER)




doctors.place(
    x=10,
    y=110,
    width=370,
    height=200)

Button(text="Очистить список докторов",
       borderwidth=0,
       highlightthickness=0,
       command=lambda: print("doctors deleted"),
       relief="flat").place(
                        x=10,
                        y=320,
                        width=170,
                        height=40)
Button(text="Вывести список докторов",
       borderwidth=0,
       highlightthickness=0,
       command=lambda: print("doctors deleted"),
       relief="flat").place(
                        x=210,
                        y=320,
                        width=170,
                        height=40)

#############пациенты#####################
Label(text="Пациенты", bg=bg_color).place(x=440, y=55, width=60, height=30)

add_patient_id, add_patient_fio, add_patient_age, add_patient_card_id = StringVar(),StringVar(),StringVar(),StringVar()

Entry(textvariable=add_patient_fio).place(x=440,y=80,width=306,height=25)
Entry(textvariable=add_patient_age).place(x=698,y=80,width=60,height=25)
Entry(textvariable=add_patient_card_id).place(x=758,y=80,width=60,height=25)

Button(text="+",
       borderwidth=0,
       highlightthickness=0,
       command=lambda: print("adding patient"),
       relief="flat").place(x=823,
                            y=80,
                            width=25,
                            height=25)

patients['columns'] = ('id', 'fio', 'age', 'card_id')

patients.column("#0", width=0,  stretch=NO)
patients.column('id', anchor=CENTER, width=25)
patients.column('fio', anchor=CENTER, width=160)
patients.column('age', anchor=CENTER, width=25)
patients.column('card_id', anchor=CENTER, width=25)


patients.heading("#0",text="",anchor=CENTER)
patients.heading('id',text="ID",anchor=CENTER)
patients.heading('fio',text="ФИО",anchor=CENTER)
patients.heading('age',text="Возраст",anchor=CENTER)
patients.heading('card_id',text="ID карты",anchor=CENTER)



patients.place(
    x=440,
    y=110,
    width=380,
    height=200)

Button(text="Очистить список пациентов",
       borderwidth=0,
       highlightthickness=0,
       command=lambda: print("patients deleted"),
       relief="flat").place(
                        x=440,
                        y=320,
                        width=170,
                        height=40)
Button(text="Вывести список пациентов",
       borderwidth=0,
       highlightthickness=0,
       command=lambda: print("patients deleted"),
       relief="flat").place(
                        x=650,
                        y=320,
                        width=170,
                        height=40)
#############кабинеты#####################
Label(text="Кабинеты", bg=bg_color).place(x=880, y=55, width=60, height=30)

add_cabinet_number, add_cabinet_specialization, add_cabinet_fio_resp = StringVar(),StringVar(),StringVar()

Entry(textvariable=add_cabinet_number).place(x=880,y=80,width=56,height=25)
Entry(textvariable=add_cabinet_specialization).place(x=936,y=80,width=180,height=25)
Entry(textvariable=add_cabinet_fio_resp).place(x=1068,y=80,width=190,height=25)

Button(text="+",
       borderwidth=0,
       highlightthickness=0,
       command=lambda: print("adding cabinet"),
       relief="flat").place(x=1265,
                            y=80,
                            width=25,
                            height=25)

cabinets['columns'] = ('number', 'specialization', 'fio_of_responsible_person')

cabinets.column("#0", width=0,  stretch=NO)
cabinets.column('number', anchor=CENTER, width=25)
cabinets.column('specialization', anchor=CENTER, width=100)
cabinets.column('fio_of_responsible_person', anchor=CENTER, width=160)


cabinets.heading("#0",text="",anchor=CENTER)
cabinets.heading('number',text="Номер",anchor=CENTER)
cabinets.heading('specialization',text="Специализация",anchor=CENTER)
cabinets.heading('fio_of_responsible_person',text="Ответственное лицо",anchor=CENTER)



cabinets.place(
    x=880,
    y=110,
    width=380,
    height=200)

Button(text="Очистить список кабинетов",
       borderwidth=0,
       highlightthickness=0,
       command=lambda: print("cabinets deleted"),
       relief="flat").place(
                        x=880,
                        y=320,
                        width=170,
                        height=40)
Button(text="Вывести список кабинетов",
       borderwidth=0,
       highlightthickness=0,
       command=lambda: print("cabinets deleted"),
       relief="flat").place(
                        x=1090,
                        y=320,
                        width=170,
                        height=40)
############карты#####################
Label(text="Карты", bg=bg_color).place(x=190, y=385, width=60, height=30)

add_card_id, add_card_last_update, add_card_num_of_app, add_card_fio = StringVar(),StringVar(),StringVar(),StringVar()

Entry(textvariable=add_card_id).place(x=200,y=410,width=150,height=25)
Entry(textvariable=add_card_num_of_app).place(x=337,y=410,width=58,height=25)
Entry(textvariable=add_card_fio).place(x=394,y=410,width=186,height=25)

Button(text="+",
       borderwidth=0,
       highlightthickness=0,
       command=lambda: print("adding card"),
       relief="flat").place(x=585,
                            y=410,
                            width=25,
                            height=25)

card['columns'] = ('id', 'last_update', 'number_of_appointments', 'owner_fio')

card.column("#0", width=0,  stretch=NO)
card.column('id', anchor=CENTER, width=25)
card.column('last_update', anchor=CENTER, width=60)
card.column('number_of_appointments', anchor=CENTER, width=30)
card.column('owner_fio', anchor=CENTER, width=160)


card.heading("#0",text="",anchor=CENTER)
card.heading('id',text="ID",anchor=CENTER)
card.heading('last_update',text="Обновлено",anchor=CENTER)
card.heading('number_of_appointments',text="Приемы",anchor=CENTER)
card.heading('owner_fio',text="ФИО",anchor=CENTER)



card.place(
    x=200,
    y=440,
    width=380,
    height=200)

Button(text="Очистить список карт",
       borderwidth=0,
       highlightthickness=0,
       command=lambda: print("cards deleted"),
       relief="flat").place(
                        x=200,
                        y=650,
                        width=170,
                        height=40)

Button(text="Вывести список карт",
       borderwidth=0,
       highlightthickness=0,
       command=lambda: print("cards deleted"),
       relief="flat").place(
                        x=410,
                        y=650,
                        width=170,
                        height=40)
############приемы#####################
Label(text="Приемы", bg=bg_color).place(x=650, y=385, width=60, height=30)

add_appointment_id, add_appointment_cabinet_number, add_appointment_id_doctor, add_appointment_id_patient = StringVar(),StringVar(),StringVar(),StringVar()


Entry(textvariable=add_appointment_cabinet_number).place(x=650,y=410,width=208,height=25)
Entry(textvariable=add_appointment_id_doctor).place(x=858,y=410,width=86,height=25)
Entry(textvariable=add_appointment_id_patient).place(x=944,y=410,width=86,height=25)

Button(text="+",
       borderwidth=0,
       highlightthickness=0,
       command=lambda: print("adding card"),
       relief="flat").place(x=1035,
                            y=410,
                            width=25,
                            height=25)

appointment['columns'] = ('id', 'cabinet_number', 'id_doctor', 'id_patient')

appointment.column("#0", width=0,  stretch=NO)
appointment.column('id', anchor=CENTER, width=25)
appointment.column('cabinet_number', anchor=CENTER, width=60)
appointment.column('id_doctor', anchor=CENTER, width=25)
appointment.column('id_patient', anchor=CENTER, width=25)

appointment.heading("#0",text="",anchor=CENTER)
appointment.heading('id',text="ID",anchor=CENTER)
appointment.heading('cabinet_number',text="Номер кабинета",anchor=CENTER)
appointment.heading('id_doctor',text="ID врача",anchor=CENTER)
appointment.heading('id_patient',text="ID пациента",anchor=CENTER)



appointment.place(
    x=650,
    y=440,
    width=380,
    height=200
)
Button(text="Очистить список приемов",
       borderwidth=0,
       highlightthickness=0,
       command=lambda: print("appointments deleted"),
       relief="flat").place(
                        x=650,
                        y=650,
                        width=170,
                        height=40)

Button(text="Выаести список приемов",
       borderwidth=0,
       highlightthickness=0,
       command=lambda: print("appointments deleted"),
       relief="flat").place(
                        x=860,
                        y=650,
                        width=170,
                        height=40)


#######################update#######################

update_query_1,update_query_2 = StringVar(),StringVar()


update_entry = Entry(textvariable=update_query_1)
update_entry.place(
    x=20,
    y=750,
    width=250,
    height=30)


update_entry = Entry(textvariable=update_query_2)
update_entry.place(
    x=290,
    y=750,
    width=100,
    height=30)

update_cabinet = Button(
    text="Изменить специализацию кабинета",
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("All clear"),
    relief="flat")
update_cabinet.place(
    x=410,
    y=750,
    width=200,
    height=40)


update_patient =Button(
    text="Изменить фио пациента",
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("All clear"),
    relief="flat")

update_patient.place(
    x=630,
    y=750,
    width=140,
    height=40)


update_patient_age=Button(
    text="Изменить возраст пациента",
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("All clear"),
    relief="flat")

update_patient_age.place(
    x=790,
    y=750,
    width=160,
    height=40)

window.resizable(False, False)
window.mainloop()
