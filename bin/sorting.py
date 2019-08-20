def get_total_monthly_average(getback):
  essence_types = ['gazole', 'sp98', 'e10', 'e85', 'gplc']
  totalb_monthly_average = []
  for essence in essence_types:
    averages = []
    for i in range(1,13):
      totalb_monthly_complete_values = []
      for pump in getback:
        if 'total' in pump[0][0].lower():
          sublist = [ int(entry[2]) for entry in pump[1] if entry[0].lower() == essence and entry[1].month == i ]
      
      try:
        if sublist:
          totalb_monthly_complete_values.extend(sublist)
      except UnboundLocalError:
        pass
      
      try:
        averages.append(round((sum(sublist)/len(sublist)/1000), 2))
      except ZeroDivisionError:
        averages.append(0)
      except UnboundLocalError:
        pass
      
    if sum(averages) != 0:
      totalb_monthly_average.append((essence, averages))
      
  return totalb_monthly_average

def get_non_total_monthly_average(getback):
  essence_types = ['gazole', 'sp98', 'e10', 'e85', 'gplc']
  totalb_monthly_average = []
  for essence in essence_types:
    averages = []
    for i in range(1,13):
      totalb_monthly_complete_values = []
      for pump in getback:
        if not 'total' in pump[0][0].lower():
          sublist = [ int(entry[2]) for entry in pump[1] if entry[0].lower() == essence and entry[1].month == i ]
      try:
        if sublist:
          totalb_monthly_complete_values.extend(sublist)
      except UnboundLocalError:
        pass
      
      try:
        averages.append(round((sum(sublist)/len(sublist)/1000), 2))
      except ZeroDivisionError:
        averages.append(0)
      except UnboundLocalError:
        pass
      
    if sum(averages) != 0:
      totalb_monthly_average.append((essence, averages))
      
  return totalb_monthly_average


# def get_monthly_lowest(getback):
  

# def get_monthly_second_lowest(getback):