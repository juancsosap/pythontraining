DROP TABLE IF EXISTS 'person';

CREATE TABLE 'person' (
  'id' int(11) NOT NULL,
  'rut' char(15) NOT NULL default '',
  'firstname' char(100) NOT NULL default '',
  'lastname' char(100) NOT NULL default '',
  'email' char(100) NOT NULL default '',
  'password' char(100) NOT NULL default '',
  'age' int(11) NOT NULL default '0',
  PRIMARY KEY  ('id')
);

INSERT INTO 'person' VALUES (1,'12.345.678-9','Juan','Sosa','juan.sosa@mail.com','juan123',30);
INSERT INTO 'person' VALUES (2,'23.456.789-0','Luis','Roca','luis.roca@mail.com','luis123',35);
INSERT INTO 'person' VALUES (3,'13.579.246-8','Pepe','Lepe','pepe.lepe@mail.com','pepe123',40);
INSERT INTO 'person' VALUES (4,'24.680.135-7','Jose','Peña','jose.pena@mail.com','jose123',45);
