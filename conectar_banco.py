def nova_conexao():
    import pymysql
    config = {
        'user': 'root',
        'password': 'teste',
        'host': '127.0.0.1',
        'database': 'carros'
    }

    try:
        conection = pymysql.connect(**config)
        return conection
    except pymysql.err.OperationalError as erro:
        print(f"Erro {erro}")
        return 0
    except:
        print("ERRO DE CONEXÃO DESCONHECIDO.")
        return 0
