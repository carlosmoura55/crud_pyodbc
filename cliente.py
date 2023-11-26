import pyodbc

class Cliente:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

    def save(self):
        connection = pyodbc.connect(
            'Driver={SQL Server Native Client 11.0};'
            'Server=NOTOURA;'
            'Database=loja;'
            'Trusted_Connection=yes;'
        )

        try:
            with connection.cursor() as cursor:
                sql = 'INSERT INTO cliente (nome, email) VALUES (?, ?)'
                cursor.execute(sql, (self.nome, self.email))
            connection.commit()
        finally:
            connection.close()

    def delete(self, cliente_id):
        connection = pyodbc.connect(
            'Driver={SQL Server Native Client 11.0};'
            'Server=NOTMOURA;'
            'Database=loja;'
            'Trusted_Connection=yes;'
        )

        try:
            with connection.cursor() as cursor:
                sql = 'DELETE FROM cliente WHERE id = ?'
                cursor.execute(sql, cliente_id)
            connection.commit()
        finally:
            connection.close()

    @staticmethod
    def get_all():
        connection = pyodbc.connect(
            'Driver={SQL Server Native Client 11.0};'
            'Server=NOTMOURA;'
            'Database=loja;'
            'Trusted_Connection=yes;'
        )

        try:
            with connection.cursor() as cursor:
                sql = 'SELECT * FROM cliente'
                cursor.execute(sql)
                result = cursor.fetchall()
            return result
        finally:
            connection.close()

    def update(self):
        connection = pyodbc.connect(
            'Driver={SQL Server Native Client 11.0};'
            'Server=NOTMOURA;'
            'Database=loja;'
            'Trusted_Connection=yes;'
        )

        try:
            with connection.cursor() as cursor:
                sql = 'UPDATE cliente SET nome = ?, email = ? WHERE id = ?'
                cursor.execute(sql, (self.nome, self.email, self.id))
            connection.commit()
        finally:
            connection.close()

if __name__ == '__main__':
    novo_cliente = Cliente('Carlos Daniel', 'carlosexample@email.com')
    novo_cliente.save()

    clientes = Cliente.get_all()
    print('Clientes:', clientes)

    cliente_para_deletar_id = clientes[0]['id']
    Cliente.delete(cliente_para_deletar_id)

    clientes_apos_exclusao = Cliente.get_all()
    print('Clientes após exclusão:', clientes_apos_exclusao)
