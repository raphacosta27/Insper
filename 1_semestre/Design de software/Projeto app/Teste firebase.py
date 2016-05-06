from firebase import firebase
firebase = firebase.FirebaseApplication('https://torrid-inferno-4691.firebaseio.com/', None)
result = firebase.get('Rapha', None)
print (result)