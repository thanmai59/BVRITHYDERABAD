-- phpMyAdmin SQL Dump
-- version 4.7.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 09, 2021 at 09:42 PM
-- Server version: 10.1.28-MariaDB
-- PHP Version: 7.1.11

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `alumni`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `id` int(11) NOT NULL,
  `email` text NOT NULL,
  `password` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`id`, `email`, `password`) VALUES
(1, 'admin@gmail.com', '123456');

-- --------------------------------------------------------

--
-- Table structure for table `alumni`
--

CREATE TABLE `alumni` (
  `id` int(11) NOT NULL,
  `email` text,
  `password` text,
  `first_name` text,
  `last_name` text,
  `date_of_birth` text,
  `address` text,
  `mobile_number` text,
  `yoj` text,
  `yog` text,
  `present_status` text,
  `job_acquired` text,
  `company` text,
  `college` text,
  `course` text,
  `country` text,
  `job_location` text,
  `designation` text,
  `field_or_technology` text,
  `annual_salary` text,
  `higher_studies1` text,
  `higher_studies2` text,
  `other_higher_studies` text,
  `current_job` text,
  `current_job_location` text,
  `current_company` text,
  `current_designation` text,
  `current_field_or_technology` text,
  `current_annual_salary` text
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `alumni`
--

INSERT INTO `alumni` (`id`, `email`, `password`, `first_name`, `last_name`, `date_of_birth`, `address`, `mobile_number`, `yoj`, `yog`, `present_status`, `job_acquired`, `company`, `college`, `course`, `country`, `job_location`, `designation`, `field_or_technology`, `annual_salary`, `higher_studies1`, `higher_studies2`, `other_higher_studies`, `current_job`, `current_job_location`, `current_company`, `current_designation`, `current_field_or_technology`, `current_annual_salary`) VALUES
(2, 'alumini2@gmail.com', '123456', 'Ramesh', '', '2021-01-01', '', '', '', '2019', 'Job', 'Campus Placement', 'Tesla', '', '', '', '', '', '', '2000', '', '', NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(3, 'alumini3@gmail.com', '123456', 'Mahesh', '', '', '', '', '', '', 'Job', 'Campus Placement', 'HCL', '', '', '', '', '', '', '5000', '', '', NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(4, 'alumini4@gmail.com', '123456', 'Suresh', '', '', '', '', '', '', 'Job', 'Campus Placement', 'HCL', '', '', '', '', '', '', '6000', '', '', NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(5, 'alumini5@gmail.com', '123456', 'Naresh', '', '', '', '', '', '', 'Job', 'Campus Placement', 'TCS', '', '', '', '', '', '', '1500', '', '', NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(6, 'mdsufyan7@gmail.com', '123456', 'Shaik', 'Sufyan', '', 'H.no. 22/61-B, Pagidyala Road', '8498000172', '', '', 'Off Campus Job', 'No', 'Windows', 'GPCET', 'awf', 'India', 'awda', 'Master', 'awdawd', '15000', 'xdcfvgbnm,', 'cvbnm,.', 'New', 'New', 'cvghnjm,l', 'MIR Associates', 'fcgbhnmk', 'fcvgbhnjmk', 'cfvbhnjmk');

-- --------------------------------------------------------

--
-- Table structure for table `event`
--

CREATE TABLE `event` (
  `id` int(11) NOT NULL,
  `event` text,
  `poster` text,
  `event_date` text,
  `time` text,
  `location` text
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `event`
--

INSERT INTO `event` (`id`, `event`, `poster`, `event_date`, `time`, `location`) VALUES
(3, 'Hello', 'uploads/1619589754_daily routine.png', '2021-04-15', 'jasdbja@haksd', 'public_html'),
(5, 'Hello', NULL, '2021-05-20', '10:30 AM', 'KNL'),
(6, 'Hello', NULL, '2021-05-20', '10:30 AM', 'KNL'),
(7, 'Hello', NULL, '2021-05-20', '10:30 AM', 'KNL'),
(8, 'Hello', NULL, '2021-05-20', '10:30 AM', 'KNL'),
(9, 'Hello', NULL, '2021-05-20', '10:30 AM', 'KNL');

-- --------------------------------------------------------

--
-- Table structure for table `event_register`
--

CREATE TABLE `event_register` (
  `id` int(11) NOT NULL,
  `event` int(11) DEFAULT NULL,
  `student` int(11) DEFAULT NULL,
  `team_count` text,
  `team_names` text
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `group_chat`
--

CREATE TABLE `group_chat` (
  `id` int(11) NOT NULL,
  `group_chat` text,
  `student` text,
  `alumni` text
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `job`
--

CREATE TABLE `job` (
  `id` int(11) NOT NULL,
  `job` text,
  `company` text,
  `location` text,
  `salary` text,
  `alumni` text,
  `job_contact` text,
  `link` text
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `job`
--

INSERT INTO `job` (`id`, `job`, `company`, `location`, `salary`, `alumni`, `job_contact`, `link`) VALUES
(2, 'TEACHER IN SCHOOL', 'GFRTG', 'VHJ', '7000', '4', '1234567890', '#');

-- --------------------------------------------------------

--
-- Table structure for table `material`
--

CREATE TABLE `material` (
  `id` int(11) NOT NULL,
  `material` text,
  `file` text,
  `alumni` text
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `message`
--

CREATE TABLE `message` (
  `id` int(11) NOT NULL,
  `message` text,
  `group_chat` int(11) DEFAULT NULL,
  `student` int(11) DEFAULT NULL,
  `alumni` int(11) DEFAULT NULL,
  `date_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `student`
--

CREATE TABLE `student` (
  `id` int(11) NOT NULL,
  `email` text,
  `password` text,
  `first_name` text,
  `last_name` text,
  `date_of_birth` date DEFAULT NULL,
  `address` text,
  `mobile_number` text,
  `yoj` text,
  `yog` text
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `student`
--

INSERT INTO `student` (`id`, `email`, `password`, `first_name`, `last_name`, `date_of_birth`, `address`, `mobile_number`, `yoj`, `yog`) VALUES
(1, 'sufyansk337@gmail.com', '123456', 'Shaik', 'Basha', '2021-04-06', 'H.no. 22/61-B, Pagidyala Road\r\nPagidyala Road', '1234567890', '2015', '2019');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `alumni`
--
ALTER TABLE `alumni`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `event`
--
ALTER TABLE `event`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `event_register`
--
ALTER TABLE `event_register`
  ADD PRIMARY KEY (`id`),
  ADD KEY `student` (`student`),
  ADD KEY `event` (`event`);

--
-- Indexes for table `group_chat`
--
ALTER TABLE `group_chat`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `job`
--
ALTER TABLE `job`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `material`
--
ALTER TABLE `material`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `message`
--
ALTER TABLE `message`
  ADD PRIMARY KEY (`id`),
  ADD KEY `alumni` (`alumni`),
  ADD KEY `student` (`student`),
  ADD KEY `group_chat` (`group_chat`);

--
-- Indexes for table `student`
--
ALTER TABLE `student`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `admin`
--
ALTER TABLE `admin`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `alumni`
--
ALTER TABLE `alumni`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `event`
--
ALTER TABLE `event`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `event_register`
--
ALTER TABLE `event_register`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `group_chat`
--
ALTER TABLE `group_chat`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `job`
--
ALTER TABLE `job`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `material`
--
ALTER TABLE `material`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `message`
--
ALTER TABLE `message`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=46;

--
-- AUTO_INCREMENT for table `student`
--
ALTER TABLE `student`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `event_register`
--
ALTER TABLE `event_register`
  ADD CONSTRAINT `event_register_ibfk_1` FOREIGN KEY (`student`) REFERENCES `student` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `event_register_ibfk_2` FOREIGN KEY (`event`) REFERENCES `event` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `message`
--
ALTER TABLE `message`
  ADD CONSTRAINT `message_ibfk_1` FOREIGN KEY (`alumni`) REFERENCES `alumni` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `message_ibfk_2` FOREIGN KEY (`student`) REFERENCES `student` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `message_ibfk_3` FOREIGN KEY (`group_chat`) REFERENCES `group_chat` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
