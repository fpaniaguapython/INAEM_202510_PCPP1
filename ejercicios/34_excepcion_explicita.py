class RocketNotReadyError(Exception):
    pass

def personnel_check():
    try:
        print("\tThecaptain'snameis", crew[0])
        print("\tThepilot'snameis", crew[1])
        print("\tThemechanic'snameis", crew[2])
        print("\tThenavigator'snameis", crew[3])
    except IndexError as e:
        raise RocketNotReadyError('Crewisincomplete') from e

crew= ['John', 'Mary', 'Mike']
print('Final checkprocedure')

try:
    personnel_check()
except RocketNotReadyError as f:
    print('General exception: "{}", caused by"{}"'.format(f, f.__cause__))