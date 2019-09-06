# tables for game data and logic
# events = [0, "text", [[1, "opt text"], [2, "opt text"], [3, "opt text"]]]
# print(events[2][2][1])
import adventurestrings as ads
events = [
    ["0", ads.loc1event0, [["1", ads.loc1event0opt1], [
        "2", ads.loc1event0opt2], ["3", ads.loc1event0opt3]]],
    ["1", ads.loc1event1, ["0", ads.loc1event1opt1]],
    ["2", ads.loc1event2, [["0", ads.loc1event2opt1], ["3", ads.loc1event2opt2]]],
    ["3", ads.loc1event3, ["0", ads.loc1event3opt1]]
]


locations = {1: events}
