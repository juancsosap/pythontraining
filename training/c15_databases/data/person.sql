DROP TABLE IF EXISTS 'person';

CREATE TABLE 'person' (
  'rut' char(15) NOT NULL default '',
  'name' char(100) NOT NULL default '',
  'age' int(11) NOT NULL default '0'
);

INSERT INTO 'person' VALUES ('12.345.678-9','Juan Sosa',30);
INSERT INTO 'person' VALUES ('23.456.789-0','Luis Roca',35);
INSERT INTO 'person' VALUES ('13.579.246-8','Pepe Lepe',40);
INSERT INTO 'person' VALUES ('24.680.135-7','Jose Peña',45);
