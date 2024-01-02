def get_val(collection, key, default='git'):
    """
    Возвращает значение из словаря по переданному ключу, если ключ существует
    :param collection: исходный словарь
    :param key: ключ, по которому осуществляется поиск
    :param default: значение, которе возвращает функция, если заданный ключ отсутсвует в словаре
    :return: значение в словаре по заданному ключу, если ключ существует
    в противном случае возвращает 'git'
    """
    if key in collection:
        return collection[key]
    return default
