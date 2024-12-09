import psycopg2
import psycopg2.extras
from clientOut import ClientOut


class Account:
    def __init__(self, client_id, balance=0, id=None):
        assert client_id, "Client_id is mandatory"
        assert isinstance(client_id, int), "Client_id must be an integer"
        assert isinstance(balance, int), "Balance must be number"
        client = ClientOut.get_client_by_id(client_id)
        assert client, f"Client with id {client_id} not found "
        self.client_id = client.id
        self.__balance = balance
        self.id = id
        conn = psycopg2.connect(
            dbname="bank-app", user="postgres", password="karim123", host="localhost"
        )
        with conn:
            with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
                try:
                    cur.execute(
                        """INSERT INTO accounts (client_id,balance) VALUES(%s,%s)""",
                        (self.client_id, self.__balance),
                    )
                except Exception as e:
                    print("error is : ", e)
        conn.close()

    def __repr__(self):
        return f"client_id = {self.client_id}, balance = {self.balance}"

    # getter
    @property
    def balance(self):
        return self.__balance

    # setter
    @balance.setter
    def balance(self, new_balance):
        self.__balance = new_balance
