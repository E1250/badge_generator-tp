from base import types
def link_prepare(url:str , type:types) ->str :
    """Preparing links for badges
    Args:
        url (str): Link of the notebook in github or kaggle
        type (str): Type of the badge (Colab - Codespace - Livebook - Binder - Kaggle) 
    Return:
        str: Link of badge type
    """
    match(type):
        case types.kaggle:
            return url
        case types.binder:
            pass
        case types.colab:
            pass
        case types.codespace:
            pass
        case types.livebook:
            return url
        case types.githubdev:
            pass
        case _:
            raise("Invalid Input")