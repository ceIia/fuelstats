def sort_by_essence_type(getback):
  monthly_average_by_essence_type = []
  essence_types = ['gazole', 'sp98', 'e10', 'e85', 'gplc']

  for essence in essence_types:
    monthly_average = []
    for i in range(1,13):
      averages = []
      for pump in getback:
        sublist = [ int(entry[2]) for entry in pump[1] if entry[0].lower() == essence and entry[1].month == i ]
        try:
          averages.append(round((sum(sublist)/len(sublist)/1000), 2))
        except ZeroDivisionError:
          averages.append(0)
      if sum(averages) != 0:  
        monthly_average.append((i, averages))
    monthly_average_by_essence_type.append((essence, monthly_average))
  return monthly_average_by_essence_type

def avg_by_essence_type(getback):
  essence_types = ['gazole', 'sp98', 'e10', 'e85', 'gplc']
  avg_by_essence_type = [] 
  
  for essence in essence_types:
    pump_avg = []
    for pump in getback:
      averages = []
      for i in range(1, 13):
        sublist = [ int(entry[2]) for entry in pump[1] if entry[0].lower() == essence and entry[1].month == i ]
        
        try:
          averages.append((round((sum(sublist)/len(sublist)/1000), 2)))
        except:
          pass
      try:
        pump_avg.append(round((sum(averages)/len(averages)),2))
      except:
        pump_avg.append(0)
      
    avg_by_essence_type.append((essence, pump_avg))
  return(avg_by_essence_type)
      
def avg_minimums(getback):
  essence_types = ['gazole', 'sp98', 'e10', 'e85', 'gplc']
  avg_minimums = []
  
  for essence in essence_types:
    lowest = []
    second_lowest = []
    
    for i in range(1,13):
      averages = []
      for pump in getback:
        sublist = [ int(entry[2]) for entry in pump[1] if entry[0].lower() == essence and entry[1].month == i ]
        try:
          averages.append(round((sum(sublist)/len(sublist)/1000), 2))
        except ZeroDivisionError:
          averages.append(0)
      if sum(averages) != 0:  
        sort = sorted(averages)
        sort_clean = [x for x in sort if x != 0]
        try:
          lowest.append(sort_clean[0])
        except IndexError:
          pass
        try:
          second_lowest.append(sort_clean[1])
        except IndexError:
          pass
    try:
      avg_minimums.append((essence, round((sum(lowest)/len(lowest)), 2), round((sum(lowest)/len(lowest)), 2)))
    except ZeroDivisionError:
      avg_minimums.append((essence, 0))

  return avg_minimums
  

def avg_by_essence_type_totalb(getback):
  essence_types = ['gazole', 'sp98', 'e10', 'e85', 'gplc']
  avg_by_essence_type_totalb = [] 
  
  
  for essence in essence_types:
    pump_avg = []
    for pump in getback:
      averages = []
      for i in range(1, 13):
        if 'total' in pump[0][0].lower():
          sublist = [ int(entry[2]) for entry in pump[1] if entry[0].lower() == essence and entry[1].month == i ]
          try:
            averages.append((round((sum(sublist)/len(sublist)/1000), 2)))
          except:
            pass
      try:
        pump_avg.append(round((sum(averages)/len(averages)),2))
      except:
        pass
    try:
      avg_by_essence_type_totalb.append((essence, (round((sum(pump_avg)/len(pump_avg)),2))))
    except ZeroDivisionError:
      avg_by_essence_type_totalb.append((essence, 0))
  return(avg_by_essence_type_totalb)

def sort_by_essence_type_totalb(getback):
  monthly_average_by_essence_type_totalb = []
  essence_types = ['gazole', 'sp98', 'e10', 'e85', 'gplc']
  
  for essence in essence_types:
    monthly_average = []
    for i in range(1,13):
      averages = []
      for pump in getback:
        if 'total' in pump[0][0].lower():
          sublist = [ int(entry[2]) for entry in pump[1] if entry[0].lower() == essence and entry[1].month == i ]
          try:
            averages.append(round((sum(sublist)/len(sublist)/1000), 2))
          except ZeroDivisionError:
            averages.append(0)
      if sum(averages) != 0:
        monthly_average.append((round((sum(averages)/len(averages)), 2)))
    monthly_average_by_essence_type_totalb.append((essence, monthly_average))
    
  return monthly_average_by_essence_type_totalb
  
def build_pump_list_infos(getback):
  pumps_infos = []
  
  for pump in getback:
    pumps_infos.append(pump[0])
    
  return pumps_infos