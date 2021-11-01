def add_triathlon_data(entry, records):
    """
       adds data to existing dictionary if the value doesn't exists
       Args:
           entry (str): string that contains name and times for run, swim and bike.
           records (object): existing object where the data want to be added

       Returns:
           bool : returns true if the item is added and false if it's not

       Raises:
           KeyError: Raises an exception when int value isn't provided.
       """
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
                return True
        except ValueError:
            return False


