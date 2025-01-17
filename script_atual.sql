CREATE TABLE Responsável 
( 
 id_responsavel VARCHAR(10) PRIMARY KEY,  
 nome_responsavel VARCHAR(45),  
 telefone_responsavel BIGINT,  
 endereco_cadastro VARCHAR(45),  
 bairro_cadastro VARCHAR(20),  
 endereco_atual VARCHAR(45),  
 bairro_atual VARCHAR(20)
); 

CREATE TABLE Cadastro 
( 
 id_cadastro VARCHAR(10) PRIMARY KEY,  
 peso FLOAT,  
 altura INT,  
 semanas_gestacao INT,  
 sexo CHAR(1),  
 scanner VARCHAR(20),  
 data_coleta DATE,  
 observacao VARCHAR(100),  
 nome_hospital VARCHAR(30),  
 nome_coletista VARCHAR(45),  
 id_responsavel VARCHAR(10)  
); 

CREATE TABLE Recoleta 
( 
 id_recoleta INT PRIMARY KEY,  
 scanner VARCHAR(20),  
 data_recoleta DATE,  
 idCadastro VARCHAR(10) 
); 

CREATE TABLE Coletista 
( 
 Nome VARCHAR(45) PRIMARY KEY
); 

CREATE TABLE Hospital 
( 
 Nome VARCHAR(45) PRIMARY KEY  
); 

CREATE TABLE Materiais 
( 
 id_materiais INT PRIMARY KEY,  
 carteirinha BOOLEAN,  
 mordedor BOOLEAN,  
 gorro BOOLEAN,  
 id_cadastro VARCHAR(10)
); 

CREATE TABLE Desvinculo 
( 
 id_desvinculo INT PRIMARY KEY,  
 data_desvinculo DATE,  
 motivo VARCHAR(50),  
 id_cadastro VARCHAR(10),  
 idResponsável VARCHAR(10)  
); 

CREATE TABLE Agenda 
( 
 id_agenda INT PRIMARY KEY,  
 data_agenda DATE,  
 tipo_rc INT,  
 id_cadastro VARCHAR(10),  
 id_responsavel VARCHAR(10),  
 id_recoleta INT
); 



CREATE TABLE Material Coletado 
( 
 id_material INT PRIMARY KEY,  
 nome_material INT,  
 referencia INT,  
 mao_coletada VARCHAR(n),  
 dedo_coletado VARCHAR(n),  
 caracteristicas_material VARCHAR(n),  
 id_cadastro INT,  
 id_recoleta INT 
); 

CREATE TABLE Material Segmentado 
( 
 id_material_seg INT PRIMARY KEY,  
 caracteristicas_material_seg VARCHAR(n),  
 id_material_coletado INT,  
); 

-- Adicionando chaves estrangeiras na tabela Cadastro
ALTER TABLE Cadastro
ADD CONSTRAINT fk_nome_hospital FOREIGN KEY (nome_hospital) REFERENCES Hospital (Nome),
ADD CONSTRAINT fk_nome_coletista FOREIGN KEY (nome_coletista) REFERENCES Coletista (Nome),
ADD CONSTRAINT fk_id_responsavel FOREIGN KEY (id_responsavel) REFERENCES Responsável (id_responsavel);

-- Adicionando chave estrangeira na tabela Recoleta
ALTER TABLE Recoleta
ADD CONSTRAINT fk_idCadastro FOREIGN KEY (idCadastro) REFERENCES Cadastro (id_cadastro);

-- Adicionando chave estrangeira na tabela Materiais
ALTER TABLE Materiais
ADD CONSTRAINT fk_id_cadastro FOREIGN KEY (id_cadastro) REFERENCES Cadastro (id_cadastro);

-- Adicionando chaves estrangeiras na tabela Desvinculo
ALTER TABLE Desvinculo
ADD CONSTRAINT fk_id_cadastro_desvinculo FOREIGN KEY (id_cadastro) REFERENCES Cadastro (id_cadastro),
ADD CONSTRAINT fk_idResponsavel FOREIGN KEY (idResponsável) REFERENCES Responsável (id_responsavel);

-- Adicionando chaves estrangeiras na tabela Agenda
ALTER TABLE Agenda
ADD CONSTRAINT fk_id_cadastro_agenda FOREIGN KEY (id_cadastro) REFERENCES Cadastro (id_cadastro),
ADD CONSTRAINT fk_id_responsavel_agenda FOREIGN KEY (id_responsavel) REFERENCES Responsável (id_responsavel),
ADD CONSTRAINT fk_id_recoleta FOREIGN KEY (id_recoleta) REFERENCES Recoleta (id_recoleta);

-- Inserindo dados na tabela Responsável
INSERT INTO Responsável (id_responsavel, nome_responsavel, telefone_responsavel, endereco_cadastro, bairro_cadastro, endereco_atual, bairro_atual)
VALUES ('MS', 'Maria Silva', 11987654321, 'Rua das Flores, 123', 'Centro', 'Rua Nova, 45', 'Jardins'),
       ('JP', 'João Pereira', 11912345678, 'Av. Paulista, 1000', 'Bela Vista', 'Rua Azul, 250', 'Vila Mariana');

-- Inserindo dados na tabela Hospital
INSERT INTO Hospital (Nome)
VALUES ('Hospital das Clínicas'), ('Hospital São Paulo');

-- Inserindo dados na tabela Coletista
INSERT INTO Coletista (Nome)
VALUES ('Dr. Carlos Almeida'), ('Enf. Ana Souza');

-- Inserindo dados na tabela Cadastro
INSERT INTO Cadastro (id_cadastro, peso, altura, semanas_gestacao, sexo, scanner, data_coleta, observacao, nome_hospital, nome_coletista, id_responsavel)
VALUES ('MS', 3.2, 50, 39, 'M', 'Scanner001', '2024-11-01', 'Nenhuma observação', 'Hospital das Clínicas', 'Dr. Carlos Almeida', 'MS'),
       ('JP', 2.8, 48, 38, 'F', 'Scanner002', '2024-11-02', 'Teste de rotina', 'Hospital São Paulo', 'Enf. Ana Souza', 'JP');

-- Inserindo dados na tabela Recoleta
INSERT INTO Recoleta (id_recoleta, scanner, data_recoleta, idCadastro)
VALUES (1, 'Scanner003', '2024-11-05', 'MS'),
       (2, 'Scanner004', '2024-11-06', 'JP');

-- Inserindo dados na tabela Materiais
INSERT INTO Materiais (id_materiais, carteirinha, mordedor, gorro, id_cadastro)
VALUES (1, TRUE, FALSE, TRUE, 'MS'),
       (2, FALSE, TRUE, FALSE, 'JP');

-- Inserindo dados na tabela Desvinculo
INSERT INTO Desvinculo (id_desvinculo, data_desvinculo, motivo, id_cadastro, idResponsável)
VALUES (1, '2024-11-07', 'Desistência voluntária', 'MS', 'MS'),
       (2, '2024-11-08', 'Mudança de cidade', 'JP', 'JP');

-- Inserindo dados na tabela Agenda
INSERT INTO Agenda (id_agenda, data_agenda, tipo_rc, id_cadastro, id_responsavel, id_recoleta)
VALUES (1, '2024-11-10', 1, 'MS', 'MS', 1),
       (2, '2024-11-11', 2, 'JP', 'JP', 2);


SELECT *FROM cadastro as c
inner join Responsável as r on c.id_responsavel = r.id_responsavel;

