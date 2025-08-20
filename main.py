def find_missing_ranges(frames: list[int])-> dict:
    # define needed vars
    last_frame = max(frames)
    set_frames = set(frames) 
    gaps = []
    missing_count = 0
    start = None
    
    # logic of algorithms 
    for frame in range(1, last_frame + 1):        
        if frame not in set_frames:
            missing_count += 1
            if start is None:
                start = frame
        else:
            if start is not None:
                gaps.append([start, frame-1])
                start = None
        
    longest_gap = max(gaps, key=lambda x: x[1]-x[0]) if gaps else []
    
            
    return {
        "gaps": gaps,
        "longest_gap": longest_gap,
        "missing_count": missing_count,
    }


# show the result
frames = [10, 1, 6, 3, 5, 11, 2, 16]
print(find_missing_ranges(frames))



## by Jafer Nouri Talib, jafer@nouritb.com, +964 774 808 0089
