counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

voting_data = [{"county":"Arapahoe", 
"registered_voters": 422829}, 
{"county":"Denver", "registered_voters": 463353}, 
{"county":"Jefferson", "registered_voters": 432438}]

message_to_candidate = (
    f"You received {candidate_votes:,} number of votes. "
    f"The total number of votes in the election was {total_votes:,}. "
    f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")


if 1 > 2:
 print("Five is greater than two!")
else:
    print("you lose")