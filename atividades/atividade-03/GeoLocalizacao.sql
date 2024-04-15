BEGIN TRANSACTION;
DROP TABLE IF EXISTS "tb_microregiao";
CREATE TABLE IF NOT EXISTS "tb_microregiao" (
	"id"	INTEGER,
	"nome"	TEXT,
	PRIMARY KEY("id")
);
DROP TABLE IF EXISTS "tb_municipios";
CREATE TABLE IF NOT EXISTS "tb_municipios" (
	"id"	INTEGER,
	"nome"	TEXT,
	"latitude"	decimal(8, 6),
	"longitude"	decimal(9, 6),
	"id_microregiao"	INTEGER,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("id_microregiao") REFERENCES "tb_microregiao"("id")
);
INSERT INTO "tb_microregiao" ("id","nome") VALUES (8,'Itapioca'),
 (9,'Baixo Curu'),
 (10,'Uruburetama'),
 (11,'Médio Curu'),
 (12,'Canindé'),
 (13,'Baturité'),
 (14,'Chorozinho'),
 (15,'Cascavel');
INSERT INTO "tb_municipios" ("id","nome","latitude","longitude","id_microregiao") VALUES (1,'Amontada',-3.363285,-39.827958,8),
 (2,'Itapipoca',-3.501042,-39.579436,8),
 (3,'Trairi',-3.265893,-39.274583,8),
 (4,'Paracuru',-3.408865,-39.029867,9),
 (5,'Paraipaba',-3.437627,-39.148108,9),
 (6,'São Gonçalo do Amarante',-3.611728,-38.96815,9),
 (7,'Itapajé',-3.686576,-39.585581,10),
 (8,'Tururu',-3.599536,-39.435876,10),
 (9,'Umirim',-3.68174,-39.347648,10),
 (10,'Uruburetama',-3.623077,-39.514236,10),
 (11,'Apuiarés',-3.947945,-39.431991,11),
 (12,'General Sampaio',-4.042157,-39.455592,11),
 (13,'Pentecoste',-3.792128,-39.26946,11),
 (14,'São Luís do Curu',-3.669015,-39.446448,11),
 (15,'Tejuçuoca',-3.988974,-39.581174,11),
 (16,'Canindé',-4.355676,-39.311455,12),
 (17,'Caridade',-4.225344,-39.205636,12),
 (18,'Itatira',-4.526875,-39.731862,12),
 (19,'Paramoti',-4.099643,-39.241976,12),
 (20,'Acarape',-4.223809,-38.707631,13),
 (21,'Aracoiaba',-4.37352,-38.810717,13),
 (22,'Aratuba',-4.411286,-39.049615,13),
 (23,'Baturité',-4.326222,-38.885853,13),
 (24,'Capistrano',-4.462357,-38.904283,13),
 (25,'Guaramiranga',-4.261799,-38.933177,13),
 (26,'Itapiúna',-4.54909,-38.92891,13),
 (27,'Mulungu',-4.301157,-38.992017,13),
 (28,'Pacoti',-4.225243,-38.921261,13),
 (29,'Palmácia',-4.13794,-38.84245,13),
 (30,'Redenção',-4.224384,-38.729084,13),
 (31,'Barreira',-4.287041,-38.640427,14),
 (32,'Chorozinho',-4.310965,-38.498658,14),
 (33,'Ocara',-4.491435,-38.593894,14),
 (34,'Beberibe',-4.186602,-38.126427,15),
 (35,'Cascavel',-4.133258,-38.242955,15),
 (36,'Pindoretama',-4.028202,-38.305918,15);
COMMIT;
