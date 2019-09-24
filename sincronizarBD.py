from models import Essencia, Categoria, Mistura

categorias = [Categoria(1, 'Gelado', 'Sabor gelado, geralmente consumidas em dias quentes por sua característica refrescante.'),
              Categoria(2, 'Doce', 'Sabor doce e quente, geralmente consumidos em dias mais frios.')]

essencias = [Essencia(1,
                      'Swiss Alps',
                      'Zomo', 12.5,
                      'Essência gelada, base para muitas misturas',
                      'zomo_swiss_alps.png',
                      '50',
                      [categorias[0]]),
             Essencia(2,
                      'Strawberry Creamy',
                      'Zomo',
                      '12.5',
                      'Essência doce, com sabor de morango e chantily.',
                      'zomo_strwberry_creamy.png',
                      '50',
                      [categorias[1]])]

misturas = [Mistura(1,
                    'Morango gelado',
                    'Fumo doce e levemente gelado com sabor de morango. Refrescante.',
                    essencias[0],
                    essencias[1],
                    70,
                    30,
                    [categorias[0], categorias[1]])]


