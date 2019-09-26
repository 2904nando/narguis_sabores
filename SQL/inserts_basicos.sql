-- Database: narguis

-- INSERT ESSENCIAS
INSERT INTO essencia (nm_essencia, ds_marca, pr_preco_medio, ds_descricao, ds_foto, qt_pacote)
	VALUES ('Swiss Alps', 'Zomo', 12.5, 'Essência gelada', 'zomo_swiss_alps.png', 50);
INSERT INTO essencia (nm_essencia, ds_marca, pr_preco_medio, ds_descricao, ds_foto, qt_pacote)
	VALUES ('Strawberry Creamy', 'Zomo', 12.5, 'Essência doce, com gosto de morango', 'zomo_strawberry_creamy.png', 50);
INSERT INTO essencia (nm_essencia, ds_marca, pr_preco_medio, ds_descricao, ds_foto, qt_pacote)
	VALUES ('Skull Mint', 'Dark Smoke', 6.0, 'Essência gelada, base para muitas misturas', 'dark_smoke_skull_mint.png', 50);
INSERT INTO essencia (nm_essencia, ds_marca, pr_preco_medio, ds_descricao, ds_foto, qt_pacote)
	VALUES ('Nuts Cake', 'Dark Smoke', 6.0, 'Essência doce e gelada, com leve sabor de nozes', 'dark_smoke_skull_mint.png', 50);

-- INSERT CATEGORIAS
INSERT INTO categoria (nm_categoria, ds_descricao)
	VALUES ('Gelada', 'Essências geladas e refrescantes');
INSERT INTO categoria (nm_categoria, ds_descricao)
	VALUES ('Doce', 'Essências doces e geralmente um pouco quentes');

-- INSERT MISTURAS
INSERT INTO mistura (nm_mistura, ds_mistura, fk_essencia_1, fk_essencia_2, nr_porcentagem_1, nr_porcentagem_2)
	VALUES ('Morango Congelado',
			'Mistura refrescante, levemente gelada e doce, com sabor de morango e chantily.',
		   	1, 2, 30, 70);
INSERT INTO mistura (nm_mistura, ds_mistura, fk_essencia_1, fk_essencia_2, nr_porcentagem_1, nr_porcentagem_2)
	VALUES ('Bolo de Nozes Gelado',
			'Mistura refrescante com sabor doce de bolo de nozes, mas ainda refrescante.',
		   	3, 4, 30, 70);

-- INSERT ESSENCIA-CATEGORIAS
INSERT INTO essencia_categoria (cd_essencia, cd_categoria)
	VALUES (1,1);
INSERT INTO essencia_categoria (cd_essencia, cd_categoria)
	VALUES (2,2);
INSERT INTO essencia_categoria (cd_essencia, cd_categoria)
	VALUES (3,1);
INSERT INTO essencia_categoria (cd_essencia, cd_categoria)
	VALUES (4,2);
	
-- INSERT MISTURA-CATEGORIAS
INSERT INTO mistura_categoria (cd_mistura, cd_categoria)
	VALUES (1,1);
INSERT INTO mistura_categoria (cd_mistura, cd_categoria)
	VALUES (1,2);
INSERT INTO mistura_categoria (cd_mistura, cd_categoria)
	VALUES (2,1);
INSERT INTO mistura_categoria (cd_mistura, cd_categoria)
	VALUES (2,2);
	