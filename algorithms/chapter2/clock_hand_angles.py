# For any given amount of seconds
  # Divide to get the number of hours
    # divide seconds by 3600.0
    # convert to degrees
      # multiply by 30.0
  # Divide to get number of minutes
    # divide remainder of hours by 60.0
    # convert to degrees
      # multiply by 6.0
  # Divide to get number of seconds
    # divide remainder of minutes by 60.0
    # convert to degrees
      # multiply by 6.0


def clock_hand_angles(sec):
  sec = sec % (3600 * 12)
  denoms = [
    [3600.0, 30.0],
    [60.0, 6.0],
    [1.0, 6.0]
  ]
  result = []
  for denom in denoms:
    sec = float(sec)
    result.append(round((sec / denom[0]) * denom[1], 2))
    sec = int(sec)
    sec = sec % denom[0]

  return "hours: {}, minutes: {}, seconds: {}".format(result[0], result[1], result[2])
  
print clock_hand_angles(119730)