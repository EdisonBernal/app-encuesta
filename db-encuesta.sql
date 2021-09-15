/*!40101 SET NAMES utf8 */;
/*!40014 SET FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/ db-encuesta /*!40100 DEFAULT CHARACTER SET utf8mb4 */;
USE db-encuesta;

DROP TABLE IF EXISTS encuesta;
CREATE TABLE `encuesta` (
  `idenc` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(250) NOT NULL,
  `descrip` varchar(250) NOT NULL,
  `imagen` varchar(250) DEFAULT NULL,
  PRIMARY KEY (`idenc`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

DROP TABLE IF EXISTS grupo_trabajo;
CREATE TABLE `grupo_trabajo` (
  `idgrupo` smallint(6) NOT NULL DEFAULT 0,
  `nomgrupo` varchar(250) NOT NULL,
  `codgrupo` varchar(250) NOT NULL,
  PRIMARY KEY (`idgrupo`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

DROP TABLE IF EXISTS preguntas;
CREATE TABLE `preguntas` (
  `idpreg` int(11) NOT NULL AUTO_INCREMENT,
  `tipopreg` char(3) NOT NULL DEFAULT '',
  `pregunta` varchar(2000) NOT NULL,
  PRIMARY KEY (`idpreg`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;

DROP TABLE IF EXISTS respuestas;
CREATE TABLE `respuestas` (
  `idres` int(11) NOT NULL AUTO_INCREMENT,
  `idusu` int(11) NOT NULL,
  `idpreg` int(11) NOT NULL,
  `idenc` int(11) NOT NULL,
  `resp` varchar(2000) NOT NULL,
  PRIMARY KEY (`idres`),
  KEY `FK_resultado_usuario` (`idusu`),
  KEY `FK_resultado_preguntas` (`idpreg`),
  KEY `FK_resultado_encuesta` (`idenc`),
  CONSTRAINT `FK_resultado_encuesta` FOREIGN KEY (`idenc`) REFERENCES `encuesta` (`idenc`),
  CONSTRAINT `FK_resultado_preguntas` FOREIGN KEY (`idpreg`) REFERENCES `preguntas` (`idpreg`),
  CONSTRAINT `FK_resultado_usuario` FOREIGN KEY (`idusu`) REFERENCES `usuario` (`idusu`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

DROP TABLE IF EXISTS usuario;
CREATE TABLE `usuario` (
  `idusu` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(250) NOT NULL,
  `email` varchar(250) NOT NULL,
  `contrasena` varchar(250) NOT NULL,
  PRIMARY KEY (`idusu`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;