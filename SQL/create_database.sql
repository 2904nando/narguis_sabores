-- Database: narguis

-- DROP DATABASE narguis;

/*
CREATE DATABASE narguis
    WITH 
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'C'
    LC_CTYPE = 'C'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1;
*/

CREATE TABLE essencia (
	cd_essencia serial PRIMARY KEY,
	nm_essencia VARCHAR (100) NOT NULL,
	ds_marca VARCHAR (100) NOT NULL,
	pr_preco_medio FLOAT (2) NOT NULL,
	ds_descricao VARCHAR (2000) NOT NULL,
	ds_foto VARCHAR (255) NOT NULL,
	qt_pacote INT NOT NULL
);

CREATE TABLE categoria (
	cd_categoria serial PRIMARY KEY,
	nm_categoria VARCHAR (100) NOT NULL,
	ds_descricao VARCHAR (1000) NOT NULL
);

CREATE TABLE mistura (
	cd_mistura serial PRIMARY KEY,
	nm_mistura VARCHAR (100) NOT NULL,
	ds_mistura VARCHAR (2000) NOT NULL,
	fk_essencia_1 integer REFERENCES essencia(cd_essencia) ON DELETE CASCADE,
	fk_essencia_2 integer REFERENCES essencia(cd_essencia) ON DELETE CASCADE,
	nr_porcentagem_1 INT NOT NULL,
	nr_porcentagem_2 INT NOT NULL
);

CREATE TABLE essencia_categoria (
	cd_essencia integer NOT NULL,
	cd_categoria integer NOT NULL,
	PRIMARY KEY (cd_essencia, cd_categoria),
	CONSTRAINT essencia_categoria_essencia_fkey FOREIGN KEY (cd_essencia)
		REFERENCES essencia (cd_essencia) MATCH SIMPLE
		ON UPDATE NO ACTION ON DELETE NO ACTION,
	CONSTRAINT essencia_categoria_categoria_fkey FOREIGN KEY (cd_categoria)
		REFERENCES categoria (cd_categoria) MATCH SIMPLE
		ON UPDATE NO ACTION ON DELETE NO ACTION
);

CREATE TABLE mistura_categoria (
	cd_mistura integer NOT NULL,
	cd_categoria integer NOT NULL,
	PRIMARY KEY (cd_mistura, cd_categoria),
	CONSTRAINT mistura_categoria_essencia_fkey FOREIGN KEY (cd_mistura)
		REFERENCES mistura (cd_mistura) MATCH SIMPLE
		ON UPDATE NO ACTION ON DELETE NO ACTION,
	CONSTRAINT mistura_categoria_categoria_fkey FOREIGN KEY (cd_categoria)
		REFERENCES categoria (cd_categoria) MATCH SIMPLE
		ON UPDATE NO ACTION ON DELETE NO ACTION
);

CREATE TABLE usuario (
	cd_usuario serial PRIMARY KEY,
	nm_usuario VARCHAR (200) NOT NULL,
	dt_nascimento DATE NOT NULL,
	ds_email VARCHAR (200) NOT NULL,
	nr_pontos INTEGER DEFAULT 0 NOT NULL
);

CREATE TABLE comentario_essencia (
	cd_comentario serial PRIMARY KEY,
	cd_essencia integer REFERENCES essencia (cd_essencia) ON DELETE CASCADE,
	cd_usuario integer REFERENCES usuario (cd_usuario) ON DELETE CASCADE,
	ds_titulo VARCHAR (100) NOT NULL,
	ds_descricao VARCHAR (2000) NOT NULL,
	fl_nota FLOAT (2) NOT NULL
);

CREATE TABLE comentario_mistura (
	cd_comentario serial PRIMARY KEY,
	cd_mistura integer REFERENCES mistura (cd_mistura) ON DELETE CASCADE,
	cd_usuario integer REFERENCES usuario (cd_usuario) ON DELETE CASCADE,
	ds_titulo VARCHAR (100) NOT NULL,
	ds_descricao VARCHAR (2000) NOT NULL,
	fl_nota FLOAT (2) NOT NULL
);

/*

DROP TABLE categoria;
DROP TABLE essencia_categoria;
DROP TABLE mistura_categoria;
DROP TABLE comentario_essencia;
DROP TABLE comentario_mistura;
DROP TABLE essencia;
DROP TABLE mistura;
DROP TABLE usuario;
*/