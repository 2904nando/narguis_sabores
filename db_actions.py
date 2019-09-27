import db_connection

def getAllEssencias():
    connection = db_connection.connection
    cursor = connection.cursor()

    cursor.execute("""
    SELECT
        essencia.cd_essencia,
        essencia.nm_essencia,
        essencia.ds_marca,
        essencia.pr_preco_medio,
        essencia.ds_descricao,
        essencia.ds_foto,
        essencia.qt_pacote,
        array_agg(categoria.cd_categoria),
        array_agg(categoria.nm_categoria),
        array_agg(categoria.ds_descricao)
    FROM essencia
        INNER JOIN essencia_categoria ON essencia_categoria.cd_essencia = essencia.cd_essencia
        INNER JOIN categoria ON essencia_categoria.cd_categoria = categoria.cd_categoria
    GROUP BY essencia.cd_essencia
    ORDER BY cd_essencia;
    """)
    return cursor.fetchall()

def getAllEssenciasSimple():
    connection = db_connection.connection
    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            essencia.nm_essencia,
            essencia.ds_marca,
            essencia.ds_foto,
            array_agg(categoria.nm_categoria),
            array_agg(categoria.ds_descricao)
        FROM essencia
            INNER JOIN essencia_categoria ON essencia_categoria.cd_essencia = essencia.cd_essencia
            INNER JOIN categoria ON essencia_categoria.cd_categoria = categoria.cd_categoria
        GROUP BY essencia.cd_essencia
        ORDER BY ds_marca;
        """)
    return cursor.fetchall()

def getAllMisturas():
    connection = db_connection.connection
    cursor = connection.cursor()

    cursor.execute("""
    SELECT 
        mistura.cd_mistura,
        mistura.nm_mistura,
        mistura.ds_mistura,
        es1.cd_essencia essencia_1,
        es1.nm_essencia,
        mistura.nr_porcentagem_1,
        es2.cd_essencia essencia_2,
        es2.nm_essencia,
        mistura.nr_porcentagem_2,
        array_agg(categoria.cd_categoria),
        array_agg(categoria.nm_categoria),
        array_agg(categoria.ds_descricao)
    FROM mistura
        INNER JOIN mistura_categoria ON mistura_categoria.cd_mistura = mistura.cd_mistura
        INNER JOIN categoria ON categoria.cd_categoria = mistura_categoria.cd_categoria
        INNER JOIN essencia AS es1 ON es1.cd_essencia = mistura.fk_essencia_1
        INNER JOIN essencia AS es2 ON es2.cd_essencia = mistura.fk_essencia_2
    GROUP BY (mistura.cd_mistura, es1.cd_essencia, es2.cd_essencia)
    ORDER BY mistura.cd_mistura;
    """)
    return cursor.fetchall()

def getAllMisturasSimple():
    connection = db_connection.connection
    cursor = connection.cursor()

    cursor.execute("""
        SELECT 
            mistura.nm_mistura,
            mistura.ds_mistura,
            es1.nm_essencia,
            es1.ds_marca,
            mistura.nr_porcentagem_1,
            es2.nm_essencia,
            es2.ds_marca,
            mistura.nr_porcentagem_2,
            array_agg(categoria.nm_categoria),
            array_agg(categoria.ds_descricao)
        FROM mistura
            INNER JOIN mistura_categoria ON mistura_categoria.cd_mistura = mistura.cd_mistura
            INNER JOIN categoria ON categoria.cd_categoria = mistura_categoria.cd_categoria
            INNER JOIN essencia AS es1 ON es1.cd_essencia = mistura.fk_essencia_1
            INNER JOIN essencia AS es2 ON es2.cd_essencia = mistura.fk_essencia_2
        GROUP BY (mistura.cd_mistura, es1.cd_essencia, es2.cd_essencia)
        ORDER BY mistura.cd_mistura;
        """)
    return cursor.fetchall()

def getEssenciaByCode(codigo):
    connection = db_connection.connection
    cursor = connection.cursor()

    cursor.execute("""
    SELECT
        essencia.cd_essencia,
        essencia.nm_essencia,
        essencia.ds_marca,
        essencia.pr_preco_medio,
        essencia.ds_descricao,
        essencia.ds_foto,
        essencia.qt_pacote,
        array_agg(categoria.cd_categoria),
        array_agg(categoria.nm_categoria),
        array_agg(categoria.ds_descricao)
    FROM essencia
        INNER JOIN essencia_categoria ON essencia_categoria.cd_essencia = essencia.cd_essencia
        INNER JOIN categoria ON essencia_categoria.cd_categoria = categoria.cd_categoria
    WHERE essencia.cd_essencia = """ + str(codigo) + """
    GROUP BY essencia.cd_essencia;
    """)
    return cursor.fetchall()

def getMisturaByCode(codigo):
    connection = db_connection.connection
    cursor = connection.cursor()

    cursor.execute("""
            SELECT 
                mistura.cd_mistura,
                mistura.nm_mistura,
                mistura.ds_mistura,
                es1.cd_essencia essencia_1,
                es1.nm_essencia,
                mistura.nr_porcentagem_1,
                es2.cd_essencia essencia_2,
                es2.nm_essencia,
                mistura.nr_porcentagem_2,
                array_agg(categoria.cd_categoria),
                array_agg(categoria.nm_categoria),
                array_agg(categoria.ds_descricao)
            FROM mistura
                INNER JOIN mistura_categoria ON mistura_categoria.cd_mistura = mistura.cd_mistura
                INNER JOIN categoria ON categoria.cd_categoria = mistura_categoria.cd_categoria
                INNER JOIN essencia AS es1 ON es1.cd_essencia = mistura.fk_essencia_1
                INNER JOIN essencia AS es2 ON es2.cd_essencia = mistura.fk_essencia_2
            WHERE mistura.cd_mistura = 1
            GROUP BY (mistura.cd_mistura, es1.cd_essencia, es2.cd_essencia);
            """)
    return cursor.fetchall()

def getCategoriaByCode(codigo):
    connection = db_connection.connection
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM categoria WHERE cd_categoria=" + str(codigo) + ";")
    return cursor.fetchall()

