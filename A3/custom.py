def comp1(crewmate1, crewmate2):
	return (crewmate1.completion_time, crewmate1.id) < (crewmate2.completion_time, crewmate2.id)

def comp2(treasure1, treasure2):
	return (treasure1.arrival_time + treasure1.rem_size, treasure1.id) < (treasure2.arrival_time + treasure2.rem_size, treasure2.id)
