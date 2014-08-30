__author__ = 'grant'

weather = 'rainy'
i_hope_its = 'sunny'

if weather == 'sunny':
    print('what a nice day for a hike')
elif weather == 'clear':
    print('not perfect, but hey its Portland')
else:
    print('better stay dry')

outside = input("what's it look like out there?")

weather = outside

if weather == 'sunny':
    print('what a nice day')
elif weather in ['clear', 'dry']:
    print("I'm not going to complain")
elif weather == 'awful':
    print("I think I'm going to stay inside today")
else:
    print('somebody should check the weather outside')


