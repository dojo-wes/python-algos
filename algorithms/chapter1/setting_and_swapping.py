import random

session = {}
if 'activities' not in session:
  session['activities'] = []

def process(form):
  location_map = {
    'cave': random.randint(0, 3),
    'farm': random.randint(5, 10),
    'house': random.randint(10, 20),
    'casino': random.randint(-50, 50)
  }

  # if form['location'] is 'cave', we're essentially accessing location_map['cave'], which is a random int between 0 and 3
  gold = location_map[form['location']]

  activity = {}
  if gold > 0:
    activity['css_color'] = 'green'
    activity['content'] = "You earned {} golds from the {}".format(gold, form['location'])
  else:
    activity['css_color'] = "red"
    activity['content'] = "You lost {} golds from the {}".format(gold, form['location'])

  session['activities'].append(activity)
  return session['activities']

form = {
  'location': 'cave'
}
form2 = {
  'location': 'house'
}

print(process(form))
print(process(form2))
print(process(form))
print(process(form2))