def round_to_nearest_30(num):
    if num >= -30 and num < 0:
        # Handle numbers between -30 and 0
        return -30 if num <= -15 else 0
    elif num < -30:
        # For negative numbers less than -30, find nearest multiple of 30
        lower_multiple = (num // 30) * 30
        upper_multiple = lower_multiple + 30
        return lower_multiple if abs(num - lower_multiple) < abs(upper_multiple - num) else upper_multiple
    else:
        # For positive numbers, same logic
        lower_multiple = (num // 30) * 30
        upper_multiple = lower_multiple + 30
        return upper_multiple if num - lower_multiple >= 15 else lower_multiple


def round_to_nearest_80(num):
    if num >= -80 and num < 0:
        # Handle numbers between -80 and 0
        return -80 if num <= -40 else 0
    elif num < -80:
        # For negative numbers less than -80, find nearest multiple of 80
        lower_multiple = (num // 80) * 80
        upper_multiple = lower_multiple + 80
        return lower_multiple if abs(num - lower_multiple) < abs(upper_multiple - num) else upper_multiple
    else:
        # For positive numbers
        lower_multiple = (num // 80) * 80
        upper_multiple = lower_multiple + 80
        return upper_multiple if num - lower_multiple >= 40 else lower_multiple


for n in nuke.selectedNodes():
    ypos = int(n['ypos'].value()) - 24
    xpos = int(n['xpos'].value()) + 6

    rounded_y = round_to_nearest_30(ypos) + 24
    n['ypos'].setValue(rounded_y)
    
    rounded_x = round_to_nearest_80(xpos) - 6
    n['xpos'].setValue(rounded_x)
