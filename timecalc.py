def add_time(start, duration, startday=""):
  splitup = start.split()
  time_1 = splitup[0].split(":")
  hours = int(time_1[0])
  mins = int(time_1[1])
  multiplier = splitup[1]

  day = ""
  newduration = duration.split(":")
  durhours = int(newduration[0])
  durmins = int(newduration[1])

  totalhours = None
  totalmins = None
  pm_am = None
  daysafter = 0
  weekdays = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")

  if multiplier == "PM":
    hours = hours + 12
  else:
    hours = hours

  totalhours = hours + durhours
  totalmins = mins + durmins

  if mins + durmins >= 60:
    totalmins = mins + durmins - 60
    totalhours = totalhours + 1

  pm_am_mult = totalhours

  if totalmins < 10:
    totalmins = f"0{totalmins}"

  pm_am_mult2 = pm_am_mult // 12
  if pm_am_mult2 % 2 == 0:
    pm_am = "AM"
  elif pm_am_mult2 % 2 > 0:
    pm_am = "PM"

  daysafter = totalhours // 24
  takehours = daysafter * 24
  if daysafter >= 1:
    totalhours = totalhours - takehours

  if pm_am == "PM":
    totalhours = totalhours - 12

  if totalhours == 0:
    totalhours = 12

  if startday:
    index = weekdays.index(startday.title())
    multindex = index + daysafter
    newindex = multindex % 7
    day = weekdays[newindex]
  new_time = f"{totalhours}:{totalmins} {pm_am}"
  if daysafter > 1:
    new_time = f"{totalhours}:{totalmins} {pm_am} ({daysafter} days later)"
  elif daysafter == 1:
    new_time = f"{totalhours}:{totalmins} {pm_am} (next day)"
  if day != "":
    new_time = f"{totalhours}:{totalmins} {pm_am}, {day}"
    if daysafter > 1:
      new_time = f"{totalhours}:{totalmins} {pm_am}, {day} ({daysafter} days later)"
    elif daysafter == 1:
      new_time = f"{totalhours}:{totalmins} {pm_am}, {day} (next day)"
  return new_time
