-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 16-04-2025 a las 12:50:31
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `verdepradera`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `asignacioncargos`
--

CREATE TABLE `asignacioncargos` (
  `ID` int(11) NOT NULL,
  `ID_Empleado` int(11) NOT NULL,
  `ID_Cargo` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `campos`
--

CREATE TABLE `campos` (
  `ID` int(11) NOT NULL,
  `NumHoyos` int(11) NOT NULL,
  `ID_Nivel` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `cargo`
--

CREATE TABLE `cargo` (
  `ID` int(11) NOT NULL,
  `Nombre` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `categoria`
--

CREATE TABLE `categoria` (
  `ID` int(11) NOT NULL,
  `Nombre` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `clase`
--

CREATE TABLE `clase` (
  `ID` int(11) NOT NULL,
  `Fecha` date NOT NULL,
  `Duracion` int(11) NOT NULL,
  `ID_Nivel` int(11) NOT NULL,
  `ID_Empleado` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `empleado`
--

CREATE TABLE `empleado` (
  `ID` int(11) NOT NULL,
  `Nombre` varchar(30) NOT NULL,
  `Apellido1` varchar(30) NOT NULL,
  `Apellido2` varchar(30) NOT NULL,
  `Telefono` int(11) NOT NULL,
  `Experiencia` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `factura`
--

CREATE TABLE `factura` (
  `ID` int(11) NOT NULL,
  `Fecha` date NOT NULL,
  `Precio_total` int(11) NOT NULL,
  `ID_Jugador` int(11) NOT NULL,
  `ID_Empleado` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `factura-producto`
--

CREATE TABLE `factura-producto` (
  `ID` int(11) NOT NULL,
  `ID_Factura` int(11) NOT NULL,
  `ID_Producto` int(11) NOT NULL,
  `Cantidad` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `horario`
--

CREATE TABLE `horario` (
  `ID` int(11) NOT NULL,
  `Fecha` date NOT NULL,
  `Hora` time NOT NULL,
  `ID_Empleado` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `hoyo`
--

CREATE TABLE `hoyo` (
  `ID` int(11) NOT NULL,
  `Numero` int(11) NOT NULL,
  `Par` int(11) NOT NULL,
  `Longitud` int(11) NOT NULL,
  `ID_Campo` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `jugador`
--

CREATE TABLE `jugador` (
  `ID` int(11) NOT NULL,
  `Nombre` varchar(30) NOT NULL,
  `Apellido1` varchar(30) NOT NULL,
  `Apellido2` varchar(30) NOT NULL,
  `Fecha_Nac` date NOT NULL,
  `Direccion` varchar(100) NOT NULL,
  `Telefono` int(11) NOT NULL,
  `Correo` varchar(100) NOT NULL,
  `ID_Nivel` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `membresia`
--

CREATE TABLE `membresia` (
  `ID` int(11) NOT NULL,
  `Tipo` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `nivel`
--

CREATE TABLE `nivel` (
  `ID` int(11) NOT NULL,
  `Nombre` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `participantes`
--

CREATE TABLE `participantes` (
  `ID` int(11) NOT NULL,
  `ID_Jugador` int(11) NOT NULL,
  `ID_Torneo` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `producto`
--

CREATE TABLE `producto` (
  `ID` int(11) NOT NULL,
  `Nombre` varchar(100) NOT NULL,
  `Precio` int(11) NOT NULL,
  `Stock` int(11) NOT NULL,
  `ID_Categoria` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `propina`
--

CREATE TABLE `propina` (
  `ID` int(11) NOT NULL,
  `Cantidad` int(11) NOT NULL,
  `ID_Empleado` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `reserva`
--

CREATE TABLE `reserva` (
  `ID` int(11) NOT NULL,
  `Fecha` date NOT NULL,
  `Hora` time NOT NULL,
  `ID_Jugador` int(11) NOT NULL,
  `ID_Horario` int(11) NOT NULL,
  `ID_Campo` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `subscripcion`
--

CREATE TABLE `subscripcion` (
  `ID` int(11) NOT NULL,
  `Fecha_inicio` date NOT NULL,
  `Fecha_vencimiento` date NOT NULL,
  `ID_Jugador` int(11) NOT NULL,
  `ID_Membresia` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `torneo`
--

CREATE TABLE `torneo` (
  `ID` int(11) NOT NULL,
  `Nombre` varchar(30) NOT NULL,
  `Fecha` date NOT NULL,
  `ID_Nivel` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `torneo-campo`
--

CREATE TABLE `torneo-campo` (
  `ID` int(11) NOT NULL,
  `ID_Torneo` int(11) NOT NULL,
  `ID_Campo` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `asignacioncargos`
--
ALTER TABLE `asignacioncargos`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `ID_Empleado` (`ID_Empleado`,`ID_Cargo`),
  ADD KEY `ID_Cargo` (`ID_Cargo`);

--
-- Indices de la tabla `campos`
--
ALTER TABLE `campos`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `ID_Nivel` (`ID_Nivel`);

--
-- Indices de la tabla `cargo`
--
ALTER TABLE `cargo`
  ADD PRIMARY KEY (`ID`);

--
-- Indices de la tabla `categoria`
--
ALTER TABLE `categoria`
  ADD PRIMARY KEY (`ID`);

--
-- Indices de la tabla `clase`
--
ALTER TABLE `clase`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `ID_Nivel` (`ID_Nivel`,`ID_Empleado`),
  ADD KEY `ID_Empleado` (`ID_Empleado`);

--
-- Indices de la tabla `empleado`
--
ALTER TABLE `empleado`
  ADD PRIMARY KEY (`ID`);

--
-- Indices de la tabla `factura`
--
ALTER TABLE `factura`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `ID_Jugador` (`ID_Jugador`,`ID_Empleado`),
  ADD KEY `ID_Empleado` (`ID_Empleado`);

--
-- Indices de la tabla `factura-producto`
--
ALTER TABLE `factura-producto`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `ID_Factura(FK)` (`ID_Factura`,`ID_Producto`),
  ADD KEY `ID_Producto` (`ID_Producto`);

--
-- Indices de la tabla `horario`
--
ALTER TABLE `horario`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `ID_Empleado` (`ID_Empleado`);

--
-- Indices de la tabla `hoyo`
--
ALTER TABLE `hoyo`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `ID_Campo` (`ID_Campo`);

--
-- Indices de la tabla `jugador`
--
ALTER TABLE `jugador`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `ID_Nivel` (`ID_Nivel`);

--
-- Indices de la tabla `membresia`
--
ALTER TABLE `membresia`
  ADD PRIMARY KEY (`ID`);

--
-- Indices de la tabla `nivel`
--
ALTER TABLE `nivel`
  ADD PRIMARY KEY (`ID`);

--
-- Indices de la tabla `participantes`
--
ALTER TABLE `participantes`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `ID_Jugador` (`ID_Jugador`,`ID_Torneo`),
  ADD KEY `ID_Torneo` (`ID_Torneo`);

--
-- Indices de la tabla `producto`
--
ALTER TABLE `producto`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `ID_Categoria` (`ID_Categoria`);

--
-- Indices de la tabla `propina`
--
ALTER TABLE `propina`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `ID_Empleado` (`ID_Empleado`);

--
-- Indices de la tabla `reserva`
--
ALTER TABLE `reserva`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `ID_Jugador` (`ID_Jugador`,`ID_Horario`,`ID_Campo`),
  ADD KEY `ID_Horario` (`ID_Horario`),
  ADD KEY `ID_Campo` (`ID_Campo`);

--
-- Indices de la tabla `subscripcion`
--
ALTER TABLE `subscripcion`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `ID_Jugador` (`ID_Jugador`,`ID_Membresia`),
  ADD KEY `ID_Membresia` (`ID_Membresia`);

--
-- Indices de la tabla `torneo`
--
ALTER TABLE `torneo`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `ID_Nivel` (`ID_Nivel`);

--
-- Indices de la tabla `torneo-campo`
--
ALTER TABLE `torneo-campo`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `ID_Torneo(FK)` (`ID_Torneo`,`ID_Campo`),
  ADD KEY `ID_Campo` (`ID_Campo`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `asignacioncargos`
--
ALTER TABLE `asignacioncargos`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `campos`
--
ALTER TABLE `campos`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `cargo`
--
ALTER TABLE `cargo`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `categoria`
--
ALTER TABLE `categoria`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `clase`
--
ALTER TABLE `clase`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `empleado`
--
ALTER TABLE `empleado`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `factura`
--
ALTER TABLE `factura`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `factura-producto`
--
ALTER TABLE `factura-producto`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `horario`
--
ALTER TABLE `horario`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `hoyo`
--
ALTER TABLE `hoyo`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `jugador`
--
ALTER TABLE `jugador`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `membresia`
--
ALTER TABLE `membresia`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `nivel`
--
ALTER TABLE `nivel`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `participantes`
--
ALTER TABLE `participantes`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `producto`
--
ALTER TABLE `producto`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `propina`
--
ALTER TABLE `propina`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `reserva`
--
ALTER TABLE `reserva`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `subscripcion`
--
ALTER TABLE `subscripcion`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `torneo`
--
ALTER TABLE `torneo`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `torneo-campo`
--
ALTER TABLE `torneo-campo`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `asignacioncargos`
--
ALTER TABLE `asignacioncargos`
  ADD CONSTRAINT `asignacioncargos_ibfk_1` FOREIGN KEY (`ID_Cargo`) REFERENCES `cargo` (`ID`),
  ADD CONSTRAINT `asignacioncargos_ibfk_2` FOREIGN KEY (`ID_Empleado`) REFERENCES `empleado` (`ID`);

--
-- Filtros para la tabla `campos`
--
ALTER TABLE `campos`
  ADD CONSTRAINT `campos_ibfk_1` FOREIGN KEY (`ID_Nivel`) REFERENCES `nivel` (`ID`);

--
-- Filtros para la tabla `clase`
--
ALTER TABLE `clase`
  ADD CONSTRAINT `clase_ibfk_1` FOREIGN KEY (`ID_Empleado`) REFERENCES `empleado` (`ID`),
  ADD CONSTRAINT `clase_ibfk_2` FOREIGN KEY (`ID_Nivel`) REFERENCES `nivel` (`ID`);

--
-- Filtros para la tabla `factura`
--
ALTER TABLE `factura`
  ADD CONSTRAINT `factura_ibfk_1` FOREIGN KEY (`ID_Jugador`) REFERENCES `jugador` (`ID`),
  ADD CONSTRAINT `factura_ibfk_2` FOREIGN KEY (`ID_Empleado`) REFERENCES `empleado` (`ID`);

--
-- Filtros para la tabla `factura-producto`
--
ALTER TABLE `factura-producto`
  ADD CONSTRAINT `factura-producto_ibfk_1` FOREIGN KEY (`ID_Producto`) REFERENCES `producto` (`ID`),
  ADD CONSTRAINT `factura-producto_ibfk_2` FOREIGN KEY (`ID_Factura`) REFERENCES `factura` (`ID`);

--
-- Filtros para la tabla `horario`
--
ALTER TABLE `horario`
  ADD CONSTRAINT `horario_ibfk_1` FOREIGN KEY (`ID_Empleado`) REFERENCES `empleado` (`ID`);

--
-- Filtros para la tabla `hoyo`
--
ALTER TABLE `hoyo`
  ADD CONSTRAINT `hoyo_ibfk_1` FOREIGN KEY (`ID_Campo`) REFERENCES `campos` (`ID`);

--
-- Filtros para la tabla `jugador`
--
ALTER TABLE `jugador`
  ADD CONSTRAINT `jugador_ibfk_1` FOREIGN KEY (`ID_Nivel`) REFERENCES `nivel` (`ID`);

--
-- Filtros para la tabla `participantes`
--
ALTER TABLE `participantes`
  ADD CONSTRAINT `participantes_ibfk_1` FOREIGN KEY (`ID_Jugador`) REFERENCES `jugador` (`ID`),
  ADD CONSTRAINT `participantes_ibfk_2` FOREIGN KEY (`ID_Torneo`) REFERENCES `torneo` (`ID`);

--
-- Filtros para la tabla `producto`
--
ALTER TABLE `producto`
  ADD CONSTRAINT `producto_ibfk_1` FOREIGN KEY (`ID_Categoria`) REFERENCES `categoria` (`ID`);

--
-- Filtros para la tabla `propina`
--
ALTER TABLE `propina`
  ADD CONSTRAINT `propina_ibfk_1` FOREIGN KEY (`ID_Empleado`) REFERENCES `empleado` (`ID`);

--
-- Filtros para la tabla `reserva`
--
ALTER TABLE `reserva`
  ADD CONSTRAINT `reserva_ibfk_1` FOREIGN KEY (`ID_Jugador`) REFERENCES `jugador` (`ID`),
  ADD CONSTRAINT `reserva_ibfk_2` FOREIGN KEY (`ID_Horario`) REFERENCES `horario` (`ID`),
  ADD CONSTRAINT `reserva_ibfk_3` FOREIGN KEY (`ID_Campo`) REFERENCES `campos` (`ID`);

--
-- Filtros para la tabla `subscripcion`
--
ALTER TABLE `subscripcion`
  ADD CONSTRAINT `subscripcion_ibfk_1` FOREIGN KEY (`ID_Jugador`) REFERENCES `jugador` (`ID`),
  ADD CONSTRAINT `subscripcion_ibfk_2` FOREIGN KEY (`ID_Membresia`) REFERENCES `membresia` (`ID`);

--
-- Filtros para la tabla `torneo`
--
ALTER TABLE `torneo`
  ADD CONSTRAINT `torneo_ibfk_1` FOREIGN KEY (`ID_Nivel`) REFERENCES `nivel` (`ID`);

--
-- Filtros para la tabla `torneo-campo`
--
ALTER TABLE `torneo-campo`
  ADD CONSTRAINT `torneo-campo_ibfk_1` FOREIGN KEY (`ID_Torneo`) REFERENCES `torneo` (`ID`),
  ADD CONSTRAINT `torneo-campo_ibfk_2` FOREIGN KEY (`ID_Campo`) REFERENCES `campos` (`ID`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
