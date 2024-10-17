people_to_poll = ['Alice', 'Bob', 'Charlie', 'David', 'Eva']

people_who_poll = {}
people_who_poll['Alice'] = True
people_who_poll['David'] = True

for person in people_to_poll:
    if person in people_who_poll:
        print(f"Thank you, {person}, for responding!")
    else:
        print(f"{person}, please take the poll!")
