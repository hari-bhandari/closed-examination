def add_triathlon_data(entry, records):
    athlete_entry = entry.split(',')
    if len(athlete_entry) != 4:
        return False
    else:
        name, swim, bike, run = athlete_entry
        try:
            if name in records:
                return False
            else:
                records[name] = {'run': int(run), 'swim': int(swim), 'bike': int(bike)}
                print(records)
                return True
        except ValueError:
            return False


print(add_triathlon_data('Hari Bhandarai,11,212,12', {'Hari Bhandari': {'run': 12, 'swim': 11, 'bike': 212}}))
