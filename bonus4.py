def moon_phase(phase):
    moon_phase = ['New Moon', 'Waxing Crescent', 'First Quarter', 'Waxing Gibbous', 'Full Moon', 'Waning Gibbous', 'Last Quarter', 'Waning Crescent']
    for moons in range(len(moon_phase)):
        if moon_phase[moons] == phase:
            index_tracker = moons
    moon_phases_emoji = ['🌑', '🌒', '🌓', '🌔', '🌕', '🌖', '🌗','🌘']
    return moon_phases_emoji[index_tracker]

answer = moon_phase('New Moon')
print(answer)  