def bloodgroupChild(bg1: str, bg2: str):
    rhesuses = {'-'}
    if '+' in {bg1[-1], bg2[-1]}:
        rhesuses.add('+')
    bg1, bg2 = bg1[:-1], bg2[:-1]
    bloodgroups = {bg1, bg2}
    if 'AB' in {bg1, bg2}:
        bloodgroups.update({'A', 'B'})
        if 'O' in bloodgroups:
            bloodgroups.remove('O')
            bloodgroups.remove('AB')
    else:
        bloodgroups.add('O')
    if {bg1, bg2} == {'A', 'B'}:
        bloodgroups.add('AB')
    return {group + rhesus for rhesus in rhesuses for group in bloodgroups}


def bloodgroupParent(parent: str, child: str):
    return {group for group in {'A+', 'A-', 'AB+', 'AB-', 'B+', 'B-', 'O+', 'O-'}
            if child in bloodgroupChild(parent, group)}
