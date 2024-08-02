-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1
-- Généré le : lun. 25 déc. 2023 à 21:55
-- Version du serveur : 10.4.28-MariaDB
-- Version de PHP : 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `employee_management`
--

-- --------------------------------------------------------

--
-- Structure de la table `employee`
--

CREATE TABLE `employee` (
  `MATRICULE` varchar(20) NOT NULL,
  `NOM` varchar(20) NOT NULL,
  `PRENOM` varchar(20) NOT NULL,
  `SALAIRE_MENSUEL` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `employee`
--

INSERT INTO `employee` (`MATRICULE`, `NOM`, `PRENOM`, `SALAIRE_MENSUEL`) VALUES
('emp1', 'mohamed', 'alami', 50000),
('emp2', 'belhedili', 'lamiae', 30000);

-- --------------------------------------------------------

--
-- Structure de la table `paiements`
--

CREATE TABLE `paiements` (
  `ID` int(11) NOT NULL,
  `MATRICULE` varchar(20) NOT NULL,
  `ANNEE` int(11) NOT NULL,
  `MOIS` varchar(20) NOT NULL,
  `JOUR` int(11) NOT NULL,
  `MONTANT` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `paiements`
--

INSERT INTO `paiements` (`ID`, `MATRICULE`, `ANNEE`, `MOIS`, `JOUR`, `MONTANT`) VALUES
(2, 'emp1', 2020, 'Janvier', 5, 20000),
(3, 'emp1', 2020, 'Janvier', 19, 20000),
(4, 'emp1', 2020, 'Janvier', 30, 2020),
(5, 'emp2', 2023, 'Avril', 1, 10000);

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `employee`
--
ALTER TABLE `employee`
  ADD PRIMARY KEY (`MATRICULE`);

--
-- Index pour la table `paiements`
--
ALTER TABLE `paiements`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `FK_MATR` (`MATRICULE`);

--
-- AUTO_INCREMENT pour les tables déchargées
--

--
-- AUTO_INCREMENT pour la table `paiements`
--
ALTER TABLE `paiements`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- Contraintes pour les tables déchargées
--

--
-- Contraintes pour la table `paiements`
--
ALTER TABLE `paiements`
  ADD CONSTRAINT `FK_MATR` FOREIGN KEY (`MATRICULE`) REFERENCES `employee` (`MATRICULE`) ON DELETE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
