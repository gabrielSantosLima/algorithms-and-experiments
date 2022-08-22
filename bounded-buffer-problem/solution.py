# |---------------------------------------------------------------------------------------------------------------------|
# |Problema - Bounded Buffer - Implementação por Gabriel Lima (github.com/gabrielSantosLima)                            |
# |--------------------------|------------------------------------------------------------------------------------------|
# |Resumo: Há dois ou mais processos que concorrem pelo acesso a um mesmo buffer limitado. Na estratégia                |
# |produtos/consumidor:                                                                                                 |
# | 1. O produtor produz informações que são colocados no buffer                                                        |
# | 2. O Consumidor consome as informações do buffer                                                                    |
# |Caso as Threads não estejam sincronizadas, o processo de produção/consumo pode entrar em conflito. Sendo necessário a|
# |utilização de Semáforos.                                                                                             |
# ----------------------------------------------------------------------------------------------------------------------|
