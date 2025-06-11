from ics import Calendar, Event
from datetime import datetime, timedelta

calendar = Calendar()

start_date = datetime(2024, 9, 16) #Inceput de an scolar 2024
end_date = datetime(2026, 6, 12)  #Sfarsit de an scoalar 2026

vacante = [
    (datetime(2026, 2, 16), datetime(2026, 2, 22)), #vacanta ski
    (datetime(2025, 10, 27), datetime(2025, 10, 31)), #vacanta toamna
    (datetime(2025, 12, 22), datetime(2026, 1, 7)), #vacanta iarna
    (datetime(2026, 4, 6), datetime(2026, 4,14)) #vacanta primavara

]

zile_libere = [
    datetime(2025, 12, 1),
    datetime(2026, 5, 1),
    datetime(2026, 12, 1),
    datetime(2025, 5, 1),
    datetime(2024, 12, 1),
    datetime(2024, 10, 5),
    datetime(2024, 11, 30),
    datetime(2025, 1, 24),
    datetime(2025, 6, 8),
    datetime(2025, 6, 9)
]
current_date = start_date


while current_date <= end_date:
    in_vacanta = any(start_vac <= current_date <= end_vac for start_vac, end_vac in vacante) #verificare pt vacanta
    e_zi_libera = current_date in zile_libere # verificare pt sarbatori legale

    if not in_vacanta and not e_zi_libera: # ignora zile de vacanta
        if current_date.weekday() == 0: #0 = Luni
            event = Event(
            name = "Chimie",
            begin = current_date.replace(hour=8, minute=0),
            end = current_date.replace(hour=8, minute=50),
            description= "Prof Name"
        )
            event.alarms.append([timedelta(minutes=-5), "display"]) #5 min Alert
            calendar.events.add(event)

            event2 = Event(
                name = "Limba și literatura română",
                begin = current_date.replace(hour=9, minute=0),
                end = current_date.replace(hour=9, minute=50),
                description = "Prof Name"
            )
            event2.alarms.append([timedelta(minutes=-5), "display"]) #5 min Alert
            calendar.events.add(event2)

            event3 = Event(
                name = "Limba și literatura germană",
                begin = current_date.replace(hour=10, minute=10),
                end = current_date.replace(hour=11, minute=0),
                description= "Prof Name"
            )
            event3.alarms.append([timedelta(minutes=-5), "display"])  # 5 min Alert
            calendar.events.add(event3)

            event4 = Event(
                name="Fizică",
                begin=current_date.replace(hour=11, minute=10),
                end=current_date.replace(hour=12, minute=0),
                description="Prof Name"
            )
            event4.alarms.append([timedelta(minutes=-5), "display"])  # 5 min Alert
            calendar.events.add(event4)

            event5 = Event(
                name="Educație fizică și sport",
                begin=current_date.replace(hour=12, minute=10),
                end=current_date.replace(hour=13, minute=0),
                description="Prof Name"
            )
            event5.alarms.append([timedelta(minutes=-5), "display"])  # 5 min Alert
            calendar.events.add(event5)

            event6 = Event(
                name="Matematică",
                begin=current_date.replace(hour=13, minute=10),
                end=current_date.replace(hour=14, minute=0),
                description="Prof Name"
            )
            event6.alarms.append([timedelta(minutes=-5), "display"])  # 5 min Alert
            calendar.events.add(event6)

            event7 = Event(
                name="Educație plastică",
                begin=current_date.replace(hour=14, minute=10),
                end=current_date.replace(hour=15, minute=0),
                description="Prof Name"
            )
            event7.alarms.append([timedelta(minutes=-5), "display"])  # 5 min Alert
            calendar.events.add(event7)

        elif current_date.weekday() == 1: #1 = Marti
            event = Event(
                name="Limba și literatura germană",
                begin=current_date.replace(hour=8, minute=0),
                end=current_date.replace(hour=8, minute=50),
                description="Prof Name"
            )
            event.alarms.append([timedelta(minutes=-5), "display"])  # 5 min Alert
            calendar.events.add(event)

            event2 = Event(
                name="Matematică",
                begin=current_date.replace(hour=9, minute=0),
                end=current_date.replace(hour=9, minute=50),
                description="Prof Name"
            )
            event2.alarms.append([timedelta(minutes=-5), "display"])  # 5 min Alert
            calendar.events.add(event2)

            event3 = Event(
                name="Istoria și Tradiția Minorităților",
                begin=current_date.replace(hour=10, minute=10),
                end=current_date.replace(hour=11, minute=0),
                description="Prof Name"
            )
            event3.alarms.append([timedelta(minutes=-5), "display"])  # 5 min Alert
            calendar.events.add(event3)

            event4 = Event(
                name="Limba și literatura română",
                begin=current_date.replace(hour=11, minute=10),
                end=current_date.replace(hour=12, minute=0),
                description="Prof Name"
            )
            event4.alarms.append([timedelta(minutes=-5), "display"])  # 5 min Alert
            calendar.events.add(event4)

            event5 = Event(
                name="Educație fizică și sport",
                begin=current_date.replace(hour=12, minute=10),
                end=current_date.replace(hour=13, minute=0),
                description="Prof Name"
            )
            event5.alarms.append([timedelta(minutes=-5), "display"])  # 5 min Alert
            calendar.events.add(event5)

            event6 = Event(
                name="Educație tehnologică",
                begin=current_date.replace(hour=13, minute=10),
                end=current_date.replace(hour=14, minute=0),
                description="Prof Name"
            )
            event6.alarms.append([timedelta(minutes=-5), "display"])  # 5 min Alert
            calendar.events.add(event6)

            event7 = Event(
                name="Consiliere și orientare",
                begin=current_date.replace(hour=14, minute=10),
                end=current_date.replace(hour=15, minute=0),
                description="Prof Name"
            )
            event7.alarms.append([timedelta(minutes=-5), "display"])  # 5 min Alert
            calendar.events.add(event7)

        elif current_date.weekday() == 2: # 2 = Miercuri
            event = Event(
                name="Limba engleză",
                begin=current_date.replace(hour=8, minute=0),
                end=current_date.replace(hour=9, minute=50),
                description="Prof Name"
            )
            event.alarms.append([timedelta(minutes=-5), "display"])  # 5 min Alert
            calendar.events.add(event)

            event2 = Event(
                name="Limba și literatura română",
                begin=current_date.replace(hour=9, minute=0),
                end=current_date.replace(hour=9, minute=50),
                description="Prof Name"
            )
            event2.alarms.append([timedelta(minutes=-5), "display"])  # 5 min Alert
            calendar.events.add(event2)

            event3 = Event(
                name="Fizică",
                begin=current_date.replace(hour=10, minute=10),
                end=current_date.replace(hour=11, minute=0),
                description="Prof Name"
            )
            event3.alarms.append([timedelta(minutes=-5), "display"])  # 5 min Alert
            calendar.events.add(event3)

            event4 = Event(
                name="Matematică",
                begin=current_date.replace(hour=11, minute=10),
                end=current_date.replace(hour=12, minute=0),
                description="Prof Name"
            )
            event4.alarms.append([timedelta(minutes=-5), "display"])  # 5 min Alert
            calendar.events.add(event4)

            event5 = Event(
                name="Limba și literatura germană",
                begin=current_date.replace(hour=12, minute=10),
                end=current_date.replace(hour=13, minute=0),
                description="Prof Name"
            )
            event5.alarms.append([timedelta(minutes=-5), "display"])  # 5 min Alert
            calendar.events.add(event5)

            event6 = Event(
                name="Chimie",
                begin=current_date.replace(hour=13, minute=10),
                end=current_date.replace(hour=14, minute=0),
                description="Prof Name"
            )
            event6.alarms.append([timedelta(minutes=-5), "display"])  # 5 min Alert
            calendar.events.add(event6)

            event7 = Event(
                name="Religie",
                begin=current_date.replace(hour=14, minute=10),
                end=current_date.replace(hour=15, minute=0),
                description="Prof Name"
            )
            event7.alarms.append([timedelta(minutes=-5), "display"])  # 5 min Alert
            calendar.events.add(event7)

        elif current_date.weekday() == 3: # 3 = Joi
            event = Event(
                name="Limba și literatura română",
                begin=current_date.replace(hour=8, minute=0),
                end=current_date.replace(hour=8, minute=50),
                description="Prof Name"
            )
            event.alarms.append([timedelta(minutes=-5), "display"])  # 5 min Alert
            calendar.events.add(event)

            event2 = Event(
                name="Limba si literatura germană",
                begin=current_date.replace(hour=9, minute=0),
                end=current_date.replace(hour=9, minute=50),
                description="Prof Name"
            )
            event2.alarms.append([timedelta(minutes=-5), "display"])  # 5 min Alert
            calendar.events.add(event2)

            event3 = Event(
                name="Educație Socială",
                begin=current_date.replace(hour=10, minute=10),
                end=current_date.replace(hour=11, minute=0),
                description="Prof Name"
            )
            event3.alarms.append([timedelta(minutes=-5), "display"])  # 5 min Alert
            calendar.events.add(event3)

            event4 = Event(
                name="Limba latină",
                begin=current_date.replace(hour=11, minute=10),
                end=current_date.replace(hour=12, minute=0),
                description="Prof Name"
            )
            event4.alarms.append([timedelta(minutes=-5), "display"])  # 5 min Alert
            calendar.events.add(event4)

            event5 = Event(
                name="Educație Muzică",
                begin=current_date.replace(hour=12, minute=10),
                end=current_date.replace(hour=13, minute=0),
                description= "Prof Name"
            )
            event5.alarms.append([timedelta(minutes=-5), "display"])  # 5 min Alert
            calendar.events.add(event5)

            event6 = Event(
                name="Biologie",
                begin=current_date.replace(hour=13, minute=10),
                end=current_date.replace(hour=14, minute=0),
                description="Prof Name"
            )
            event6.alarms.append([timedelta(minutes=-5), "display"])  # 5 min Alert
            calendar.events.add(event6)

            event7 = Event(
                name="Geografie",
                begin=current_date.replace(hour=14, minute=10),
                end=current_date.replace(hour=15, minute=0),
                description="Prof Name"
            )
            event7.alarms.append([timedelta(minutes=-5), "display"])  # 5 min Alert
            calendar.events.add(event7)

        elif current_date.weekday() == 4: # 4 = Vineri
            event = Event(
                name="Matematică",
                begin=current_date.replace(hour=8, minute=0),
                end=current_date.replace(hour=8, minute=50),
                description="Prof Name"
            )
            event.alarms.append([timedelta(minutes=-5), "display"])  # 5 min Alert
            calendar.events.add(event)

            event2 = Event(
                name="Informatica și TIC",
                begin=current_date.replace(hour=9, minute=0),
                end=current_date.replace(hour=9, minute=50),
                description="Prof Name"
            )
            event2.alarms.append([timedelta(minutes=-5), "display"])  # 5 min Alert
            calendar.events.add(event2)

            event3 = Event(
                name="Biologie",
                begin=current_date.replace(hour=10, minute=10),
                end=current_date.replace(hour=11, minute=0),
                description="Prof Name"
            )
            event3.alarms.append([timedelta(minutes=-5), "display"])  # 5 min Alert
            calendar.events.add(event3)

            event4 = Event(
                name="Limba engleză",
                begin=current_date.replace(hour=11, minute=10),
                end=current_date.replace(hour=12, minute=0),
                description="Prof Name"
            )
            event4.alarms.append([timedelta(minutes=-5), "display"])  # 5 min Alert
            calendar.events.add(event4)

            event5 = Event(
                name="Istorie",
                begin=current_date.replace(hour=12, minute=10),
                end=current_date.replace(hour=13, minute=0),
                description="Prof Name"
            )
            event5.alarms.append([timedelta(minutes=-5), "display"])  # 5 min Alert
            calendar.events.add(event5)

            event6 = Event(
                name = "Opțional Germană",
                begin=current_date.replace(hour=13, minute=10),
                end=current_date.replace(hour=14, minute=0),
                description="Prof Name"
            )
            event6.alarms.append([timedelta(minutes=-5), "display"])  # 5 min Alert
            calendar.events.add(event6)

    current_date += timedelta(days=1)

with open("calendar_cursuri.ics", "w", encoding="utf-8") as f:
    f.write(calendar.serialize())

print("Calendar generat cu succes")