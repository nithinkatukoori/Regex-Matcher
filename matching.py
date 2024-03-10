import re

def find_matches_with_groups(sentence, pattern):
    # Compile the regular expression pattern
    regex = re.compile(pattern)

    # Find all matches of the pattern in the sentence
    matches = regex.finditer(sentence)

    # Initialize list to store match and group positions
    match_results = []

    # Iterate over matches
    for match in matches:
        match_start = match.start()
        match_end = match.end()
        groups = match.groups()
        group_positions = [(match_start + match.group().index(group), match_start + match.group().index(group) + len(group)) for group in groups]

        match_results.append(((match_start, match_end), group_positions))
    
    ans = []
    # Print the match positions and group positions
    if match_results:
        ans.append("Matches found:")
        for match_idx, ((match_start, match_end), group_positions) in enumerate(match_results, start=1):
            ans.append(f"Match {match_idx} found from position {match_start} to {match_end}:")
            ans.append(sentence[match_start:match_end])
            ans.append("Group positions:")
            for group_idx, (group_start, group_end) in enumerate(group_positions, start=1):
                ans.append(f"Group {group_idx} position: {group_start} to {group_end}")
            ans.append("")  # Empty line for readability
    else:
        ans.append("No matches found.")
    
    return ans

