import platform

def get_yaml_path()-> str:
    path = ''
    if platform.system() == 'Windows':
        return r'\\192.168.1.247\共有\営業課ﾌｫﾙﾀﾞ\松戸\スタンレー検収\03_master\stanley_kensyu.yaml'
    if platform.system() == 'Linux':
        return r'/mnt/public/営業課ﾌｫﾙﾀﾞ/松戸/スタンレー検収/03_master/stanley_kensyu.yaml'
    return path

def get_format_excel_fullpath()-> str:
    path = ''
    if platform.system() == 'Windows':
        return r'\\192.168.1.247\共有\営業課ﾌｫﾙﾀﾞ\松戸\スタンレー検収\03_master\検収アウトプット_format.xlsx'
    if platform.system() == 'Linux':
        return r'/mnt/public/営業課ﾌｫﾙﾀﾞ/松戸/スタンレー検収/03_master/検収アウトプット_format.xlsx'
    return path

def get_kensyu_data_path()-> str:
    path = ''
    if platform.system() == 'Windows':
        return r'\\192.168.1.247\共有\営業課ﾌｫﾙﾀﾞ\松戸\スタンレー検収\01_検収データ'
    if platform.system() == 'Linux':
        return r'/mnt/public/営業課ﾌｫﾙﾀﾞ/松戸/スタンレー検収/01_検収データ'
    return path

def get_sql_python_module_path()-> str:
    path = ''
    if platform.system() == 'Windows':
        return r'\\192.168.1.247\共有\技術課ﾌｫﾙﾀﾞ\200. effit_data\ﾏｽﾀ\sql_python_module'
    if platform.system() == 'Linux':
        return r'/mnt/public/技術課ﾌｫﾙﾀﾞ/200. effit_data/ﾏｽﾀ/sql_python_module'
    return path
