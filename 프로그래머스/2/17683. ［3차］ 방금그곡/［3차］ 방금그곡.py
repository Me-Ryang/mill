# 19:30 ~

def convert(melody):
    return melody.replace('C#', 'c').replace('D#', 'd').replace('F#', 'f').replace('G#', 'g').replace('A#', 'a').replace('B#', 'b')

def solution(m, musicinfos):
    
    musics = []
    
    for idx, musicinfo in enumerate(musicinfos):

        m = convert(m)
        
        start, end, title, melody = musicinfo.split(',')
        sh, sm = map(int, start.split(':'))
        eh, em = map(int, end.split(':'))
        time = (eh * 60 + em) - (sh * 60 + sm)
            
        melody = convert(melody)
        play = melody * (time // len(melody)) + melody[:time % len(melody)]
        if m in play:
            musics.append((time, idx, title))

    musics.sort(key = lambda x : (-x[0], x[1]))
    result = '(None)'
    if musics:
        result = musics[0][2]
    
    return result