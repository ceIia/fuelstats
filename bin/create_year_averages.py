def yearly_average_constructor(raw_array): 
  year_averages = []
  essence_types = ['gazole', 'sp98', 'e10', 'e85', 'gplc']
  
  for raw_array_entry in raw_array:
    for entry in raw_array_entry[1]:
      averages_by_type = []

      for requested_fuel_type in essence_types:
        averages = []
        for month in range(1,13):
          sublist = [ int(entry[2]) for entry in raw_array_entry[1] if entry[0].lower() == requested_fuel_type and entry[1].month == month]
          try:
            averages.append(round((sum(sublist)/len(sublist)/1000), 2))
          except ZeroDivisionError:
            averages.append(0)
        if sum(averages) != 0:
          averages_by_type.append((requested_fuel_type, averages))
    try:
      year_averages.append((raw_array_entry[0], averages_by_type))
    except UnboundLocalError:
      year_averages.append((raw_array_entry[0], []))
  
  return year_averages
