def get_software_name(version):
    if version <= 5:
        return f'Baby'
    elif version <= 10:
        return f'Junior'
    elif version <= 15:
        return f'Senior'
    elif version <= 20:
        return f'Elite'
    elif version <= 25:
        return f'Master'
    else:
        return f'Best'
