from conectar_banco import nova_conexao as conectar
import pymysql
import pandas as pd

class Carros:
    def __init__(self):
        self.id_marcas = self.buscar_idmarcas()
        self.lista_inventario = pd.DataFrame()

    def inserir_marcas(self, id_m, modelo, motor, combustivel, transmissao):
        if conectar() != 0:
            inserir = f"""
            insert into inventario (marcas_id, modelo_inv, motor_inv, combustivel_inv,transmissao_inv) 
            values ('{id_m}', '{modelo}', '{motor}','{combustivel}','{transmissao}')"""
            with conectar() as conexao:
                try:
                    cursor = conexao.cursor()
                    cursor.execute(inserir)
                    conexao.commit()
                    return 1
                except pymysql.err.IntegrityError as intg:
                    return 2
                except ValueError as e:
                    print(e)
                    return 0

    def buscar_marcas(self):
        seleciona = f"select * from marcas"
        with conectar() as conexao:
            try:
                lista = []
                cursor = conexao.cursor()
                cursor.execute(seleciona)
                for i in cursor.fetchall():
                    lista.append(i[1])
                return lista
            except pymysql.err.IntegrityError as intg:
                print("Erro")
            except:
                print("Erro2")

    def buscar_idmarcas(self):
        seleciona = f"select id, nome_marca from marcas"
        with conectar() as conexao:
            try:
                lista = []
                cursor = conexao.cursor()
                cursor.execute(seleciona)
                for i in cursor.fetchall():
                    lista.append(i)
                return lista
            except pymysql.err.IntegrityError as intg:
                print("Erro")
            except:
                print("Erro2")

    def buscar_modelos(self):
        seleciona = """select inventario.modelo_inv, marcas.nome_marca, inventario.motor_inv, 
        inventario.combustivel_inv, inventario.transmissao_inv from inventario join marcas on 
        marcas.id = inventario.marcas_id"""
        with conectar() as conexao:
            try:
                cursor = conexao.cursor()
                cursor.execute(seleciona)
                for i in cursor.fetchall():
                    temp = pd.DataFrame({"MODELO": [i[0]], "MARCA": [i[1]], "MOTOR": [i[2]], "COMBUSTIVEL": [i[3]], "TRANSMISSAO": [i[4]]})
                    self.lista_inventario = pd.concat([self.lista_inventario, temp])
                return self.lista_inventario
            except pymysql.err.IntegrityError as intg:
                print("Erro")
            except:
                print("Erro2")
