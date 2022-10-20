

def highlight_spotlight_finding(finding: str, start_pos: int):

    print("finding text: {}".format(finding))

    open_tick = -1
    
    try:
        open_tick = finding.find("`", start_pos)
    except:
        pass
    
    print("open_tick pos: {}".format(open_tick))

    if open_tick == -1:
        return finding

    close_tick = -1

    try:
        close_tick = finding.find("`", open_tick + 1)
    except:
        pass

    print("close_tick pos: {}".format(close_tick))

    if close_tick == -1:
        return finding

    begin_text = finding[:open_tick]

    highligh_text = finding[(open_tick+1):close_tick]

    highligh_text = '<span style="background-color: #ffff00; font-weight: bold;">'+ highligh_text +'</span>'

    end_text = finding[(close_tick+1):]
    
    print("highligh_text: {}".format(highligh_text))
    print("begin_text: {}".format(begin_text))
    

    new_text = begin_text+highligh_text+end_text
    
    print("new_text: {}".format(new_text))
    print("\n\n")

    if len(end_text) > 0:
        return highlight_spotlight_finding(new_text, close_tick)
    else:
        return new_text

text = "`I love you`, but I m`cant stand you`. Yeah yea yea, I cant x`hold it anymore`b. what you `think?"

highlighted_text = highlight_spotlight_finding(text,0)

print("\nhighlighted_text: {}".format(highlighted_text))