import psycopg2

try:
    connection = psycopg2.connect(user = "vqntlmgadwynwp",
                                  password = "4ba9d7a162791ede90a0a267292b6922fdc9ec7aa321a4ff6396d64b736e0603",
                                  host = "ec2-54-235-163-246.compute-1.amazonaws.com",
                                  port = "5432",
                                  database = "da2fg0dip1jn7u")

except:
    print('Erro de conexão com PostgreSQL')