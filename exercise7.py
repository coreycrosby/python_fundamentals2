
def gather_input(id):
    print(f"How far did person {id} run (in metres)?")
    distance = float(input())
    print(f"How long (in minutes) did person {id} run take to run {distance} metres?")
    mins = float(input())
    speed = distance / (mins * 60)
    return {
        "id": id,
        "speed": speed
    }

# runner_ids = [1,2,3]

print(f"How many racers in this race?")
runner_ids = range(1, int(input()) + 1 )

results = []
for id in runner_ids:
    result = gather_input(id)
    results.append(result)

sorted_results = sorted(results, key=lambda runner: runner['speed'], reverse=True)

winner = sorted_results[0]

def announce_winner(id, speed):
    print(f"Person {id} was the fastest at {speed} m/s")

announce_winner(winner['id'], winner['speed'])

# if (speed3 > speed2) and (speed3 > speed1):
#   announce_winner(3, speed3)

# elif speed2 > speed3 and speed2 > speed1:
#   announce_winner(2, speed2)

# elif speed1 > speed3 and speed1 > speed2:
#   announce_winner(1, speed1)

# elif speed1 == speed2 and speed2 == speed3:
#   print(f"Everyone tied at {speed1} m/s")

# else:
#   print("Well done everyone!")
