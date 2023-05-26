CREATE TABLE feriados
(
id  uuid primary key DEFAULT gen_random_uuid(),
codigo varchar(30),
data date	
)