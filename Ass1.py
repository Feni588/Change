from random import shuffle
import tkinter as tk
from tkinter import ttk

def create_match_pairs(teams):
    pairs = []
    for i in range(len(teams)):
        for j in range(i+1, len(teams)):
            pairs.append((teams[i], teams[j]))
    return pair

def create_match_schedule(teams, num_matches, venues, rival_matches):
    all_pairs = create_match_pairs(teams)
    shuffle(all_pairs)

    for rm in rival_matches:
        if rm in all_pairs:
            all_pairs.remove(rm)

    weekend_matches = min(len(rival_matches), 2 * len(venues))
    weekday_matches = num_matches - weekend_matches

    temp_schedule = rival_matches[:weekend_matches] + all_pairs[:weekday_matches]
    shuffle(temp_schedule)

    

def show_schedule_in_gui(schedule_str, match_schedule, rival_matches, venues):
    root = tk.Tk()
    root.title("Match Schedule")
    root.geometry('400x500')

    style = ttk.Style(root)
    style.configure("Treeview", rowheight=35, background="#f0f0f5", foreground="black", font=('Arial', 15))
    style.configure("Treeview.Heading", font=('Arial', 20, 'bold'))

    tree = ttk.Treeview(root, columns=('Day', 'Type', 'Venue', 'Match'), show='headings')
    tree.heading('Day', text='Day')
    tree.heading('Type', text='Type')
    tree.heading('Venue', text='Venue')
    tree.heading('Match', text='Match')
    
    tree.column("Day", width=50, anchor='center')
    tree.column("Type", width=100, anchor='center')
    tree.column("Venue", width=100, anchor='center')
    tree.column("Match", width=150, anchor='center')

    tree.pack(padx=10, pady=20, fill=tk.BOTH, expand=True)

    day = 1
    for i, match in enumerate(match_schedule):
        venue = venues[day % len(venues)]
        day_type = "Weekend" if match in rival_matches else "Weekday"

        color = "pink" if day_type == "Weekend" else "aliceblue"
        tree.insert("", "end", values=(f"Day {day}", day_type, venue, f"{match[0]} vs {match[1]}"), tags=(color,))
        tree.tag_configure(color, background=color)

        day += 1

    root.mainloop()

def main():
    print("=== MATCH SCHEDULER ===")

    num_teams = int(input("Enter the number of teams (Minimum 2 teams required): "))
    if num_teams < 2:
        print("\nError: You need at least 2 teams for matches.")
        return

    teams = []
    for i in range(1, num_teams + 1):
        team_name = input(f"Enter name for Team {i}: ")
        while team_name in teams:
            print("That team name is already taken. Please choose a different name.")
            team_name = input(f"Enter name for Team {i}: ")
        teams.append(team_name)

    max_possible_matches = (num_teams * (num_teams - 1)) // 2
    num_matches = int(input(f"Enter the total number of matches (Maximum {max_possible_matches}): "))

    if num_matches > max_possible_matches:
        print(f"\nError: You can schedule up to {max_possible_matches} matches for the given teams without repetition.")
        return

    num_venues = int(input("\nEnter the number of venues: "))
    venues = []
    for i in range(num_venues):
        venue_name = input(f"Venue {i + 1} name: ")
        while venue_name in venues:
            print("That venue name is already taken. Please choose a different name.")
            venue_name = input(f"Venue {i + 1} name: ")
        venues.append(venue_name)

    num_rivals = int(input("\nEnter the number of special rival matches: "))
    rival_matches = [(input(f"Team A for Rival Match {i+1}: "), input(f"Team B for Rival Match {i+1}: ")) for i in range(num_rivals)]

    match_schedule = create_match_schedule(teams, num_matches, venues, rival_matches)
    show_schedule_in_gui("Match Schedule", match_schedule, rival_matches, venues)

if __name__ == "__main__":
    main()
