def recommend_songs_bruteforce(playlists, query_songs):
    recommendations = []
    query_set = set(query_songs)  # for faster lookup

    for playlist in playlists:
        playlist_set = set(playlist)  # also improves lookup time

        # Check whether playlist contains ALL query songs (no all() used)
        contains_all = True
        for song in query_set:
            if song not in playlist_set:   # missing query song
                contains_all = False
                break

        # If playlist contains all query songs, recommend the remaining songs
        if contains_all:
            for song in playlist:
                if song not in query_set:
                    recommendations.append(song)

    return recommendations

# Step-by-step breakdown
# Step 1 — Build songToPeople map

# For each playlist and each song inside it, map:

# song - set of person indexes


# Example:

# Playlists:
# 0 - [rock, pop, jazz]
# 1 - [jazz, afro, pop]
# 2 - [rock, blues, soul]


# songToPeople becomes:

# rock - {0, 2}
# pop  - {0, 1}
# jazz - {0, 1}
# blues - {2}
# soul - {2}
# afro - {1}

# Step 2 — For the query songs, find common people using set intersection
# Query = ["rock", "pop"]


# People with rock - {0, 2}
# People with pop - {0, 1}

# Intersection - {0}

# So only Playlist 0 contains all the query songs.

# Instead of checking every playlist, we instantly narrowed it down to one candidate.

# Step 3 — Extract recommendations only from those playlists

# Playlist 0 = [rock, pop, jazz]

# Ignore the query songs - recommend "jazz".


def recommend_songs_optimized(playlists, query_songs):
    from collections import defaultdict

    # Build reverse index mapping a song to the people that listen to it
    songToPeople = defaultdict(set)
    for i, playlist in enumerate(playlists):
        for song in playlist:
            songToPeople[song].add(i)

    # Find people who have ALL query songs,
    #  we do this by finding the insertion between the people that listen to a song
    candidate_people = None
    for song in query_songs:
        if candidate_people is None:
            candidate_people = songToPeople[song].copy()
        else:
            candidate_people &= songToPeople[song]

    # Collect recommendations from ONLY those people's playlists
    # here we convert query songs to a set, 
    # then go through the people that lisiten to all songs, note: we store just their index
    # then we perform the set difference between the person set and the query song, 
    # this adds the sogns in the persons playlist (set) but not in the query songs set to the recommendation output.

    query_songs_set = set(query_songs)
    recommendations = []
    for person_idx in candidate_people:
        recommendations.extend(set(playlists[person_idx]) - query_songs_set)

    return recommendations

playlists = [
    ["rock", "pop", "jazz"],
    ["pop", "afro", "jazz"],
    ["rock", "blues", "soul"]
]

query_songs = ["rock", "pop"]

print(recommend_songs_optimized(playlists, query_songs))
