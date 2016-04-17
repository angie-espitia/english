-- phpMyAdmin SQL Dump
-- version 3.0.1.1
-- http://www.phpmyadmin.net
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 11-03-2016 a las 23:19:40
-- Versión del servidor: 5.1.30
-- Versión de PHP: 5.2.7

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Base de datos: `proyecto`

create database proyecto;
use proyecto;
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `calificacion`
--

CREATE TABLE `calificacion` (
  `id` int(20) NOT NULL AUTO_INCREMENT,
  `estudiante_id` int(20) NOT NULL,
  `nota` float NOT NULL,
  `modulo_estudiante` int(10) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=4 ;

--
-- Volcar la base de datos para la tabla `calificacion`
--

INSERT INTO `calificacion` (`id`, `estudiante_id`, `nota`, `modulo_estudiante`) VALUES
(1, 2, 4.1, 1),
(2, 2, 4.5, 1),
(3, 3, 3.4, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `curso`
--

CREATE TABLE `curso` (
  `id` int(20) NOT NULL AUTO_INCREMENT,
  `profesores_id` int(20) NOT NULL,
  `Nombre` varchar(20) COLLATE utf8_unicode_ci NOT NULL,
  `Fecha_inicio` date NOT NULL,
  `Fecha_fin` date NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=4 ;

--
-- Volcar la base de datos para la tabla `curso`
--

INSERT INTO `curso` (`id`, `profesores_id`, `Nombre`, `Fecha_inicio`, `Fecha_fin`) VALUES
(1, 1, 'Ingles', '2016-02-02', '2016-05-05'),
(2, 2, 'Español', '2016-02-02', '2016-05-05'),
(3, 1, 'fisica', '2016-03-01', '2016-03-31');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `diag_estudiante`
--

CREATE TABLE `diag_estudiante` (
  `id` int(20) NOT NULL AUTO_INCREMENT,
  `estudiante_id` int(20) NOT NULL,
  `curso_id` int(20) NOT NULL,
  `modulo_id` int(20) NOT NULL,
  `estado_id` int(20) NOT NULL,
  `calificacion_id` float NOT NULL,
  `detalle` text COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=2 ;

--
-- Volcar la base de datos para la tabla `diag_estudiante`
--

INSERT INTO `diag_estudiante` (`id`, `estudiante_id`, `curso_id`, `modulo_id`, `estado_id`, `calificacion_id`, `detalle`) VALUES
(1, 2, 1, 1, 1, 4.3, 'paso raspado');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `estado`
--

CREATE TABLE `estado` (
  `id` int(20) NOT NULL AUTO_INCREMENT,
  `descripcion` varchar(20) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=5 ;

--
-- Volcar la base de datos para la tabla `estado`
--

INSERT INTO `estado` (`id`, `descripcion`) VALUES
(1, 'En curso'),
(2, 'Finalizado'),
(3, 'Repitiendo'),
(4, 'test');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `estudiante`
--

CREATE TABLE `estudiante` (
  `id` int(20) NOT NULL AUTO_INCREMENT,
  `Nombre` varchar(20) COLLATE utf8_unicode_ci NOT NULL,
  `Apellido` varchar(20) COLLATE utf8_unicode_ci NOT NULL,
  `Email` varchar(20) COLLATE utf8_unicode_ci NOT NULL,
  `Tel` int(10) NOT NULL,
  `Clave` int(10) NOT NULL,
  `Direccion` varchar(20) COLLATE utf8_unicode_ci NOT NULL,
  `Sexo` char(1) COLLATE utf8_unicode_ci NOT NULL,
  `Fecha Nacimiento` date NOT NULL,
  `Cedula` varchar(10) COLLATE utf8_unicode_ci NOT NULL,
  `Foto` text COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=4 ;

--
-- Volcar la base de datos para la tabla `estudiante`
--

INSERT INTO `estudiante` (`id`, `Nombre`, `Apellido`, `Email`, `Tel`, `Clave`, `Direccion`, `Sexo`, `Fecha Nacimiento`, `Cedula`, `Foto`) VALUES
(1, 'angie', 'espitia', 'angie@example.com', 2222222, 12345, 'Mz 20 -- 3', '0', '1995-03-07', '1111111111', 'simone_simons_by_alarexai-d56tje3.jpg'),
(2, 'johanna', 'salazar', 'johanna@example.com', 33333333, 12345, 'Mz 10 -- 1', '0', '1993-02-22', '0000000099', 'E5C.jpg'),
(3, 'Juan', 'Juan', 'Juan@example.com', 12345, 12345, 'Mz 10 -- 1', '1', '1988-03-22', '1231231231', 'lunas-y-estrellas.gif');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `modulo`
--

CREATE TABLE `modulo` (
  `id` int(20) NOT NULL AUTO_INCREMENT,
  `curso_id` int(20) NOT NULL,
  `Nombre` varchar(20) COLLATE utf8_unicode_ci NOT NULL,
  `Fecha` date NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=6 ;

--
-- Volcar la base de datos para la tabla `modulo`
--

INSERT INTO `modulo` (`id`, `curso_id`, `Nombre`, `Fecha`) VALUES
(1, 1, 'Ingles Basico', '2016-02-02'),
(2, 1, 'Ingles Medio', '2016-02-02'),
(3, 2, 'Español 1', '2016-02-02'),
(4, 2, 'Español 2', '2016-02-02'),
(5, 1, 'Ingles Avanzado', '2016-02-02');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `profesores`
--

CREATE TABLE `profesores` (
  `id` int(20) NOT NULL AUTO_INCREMENT,
  `Nombre` varchar(45) COLLATE utf8_unicode_ci NOT NULL,
  `Apellido` varchar(45) COLLATE utf8_unicode_ci NOT NULL,
  `Email` varchar(20) COLLATE utf8_unicode_ci NOT NULL,
  `Tel` int(10) NOT NULL,
  `Clave` int(10) NOT NULL,
  `Direccion` varchar(20) COLLATE utf8_unicode_ci NOT NULL,
  `Sexo` char(1) COLLATE utf8_unicode_ci NOT NULL,
  `Fecha Nacimiento` date NOT NULL,
  `Cedula` varchar(10) COLLATE utf8_unicode_ci NOT NULL,
  `Foto` text COLLATE utf8_unicode_ci NOT NULL,
  `Profesion` varchar(20) COLLATE utf8_unicode_ci NOT NULL,
  `Especialidad` varchar(20) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=3 ;

--
-- Volcar la base de datos para la tabla `profesores`
--

INSERT INTO `profesores` (`id`, `Nombre`, `Apellido`, `Email`, `Tel`, `Clave`, `Direccion`, `Sexo`, `Fecha Nacimiento`, `Cedula`, `Foto`, `Profesion`, `Especialidad`) VALUES
(1, 'Lidia', 'Cuenca', 'Lidia@example.com', 123123, 12345, 'Mz 12 -12', '0', '2012-12-12', '111111113', 'foto', 'profesor', 'ingles'),
(2, 'Jose', 'Suarez', 'jose@example.com', 123123, 12345, 'Mz 90 -- 1', '0', '2012-12-12', '123123123', 'foto', 'Docente', 'Español');
