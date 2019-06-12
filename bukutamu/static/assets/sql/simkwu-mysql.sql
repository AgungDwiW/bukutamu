-- phpMyAdmin SQL Dump
-- version 4.8.0.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Aug 01, 2018 at 12:27 PM
-- Server version: 10.1.32-MariaDB
-- PHP Version: 7.2.5

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `simkwu`
--

-- --------------------------------------------------------

--
-- Table structure for table `anggota`
--

CREATE TABLE `anggota` (
  `id` int(11) NOT NULL,
  `id_temp` varchar(32) DEFAULT NULL,
  `id_proposal` int(11) NOT NULL,
  `nrp_anggota` char(14) NOT NULL,
  `is_ketua` bit(1) NOT NULL,
  `is_setuju` bit(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `angsuran`
--

CREATE TABLE `angsuran` (
  `id` int(11) NOT NULL,
  `id_temp` varchar(32) DEFAULT NULL,
  `nip_petugas` char(18) NOT NULL,
  `id_proposal` int(11) NOT NULL,
  `tanggal` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `jumlah` int(11) NOT NULL,
  `status_persetujuan` bit(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `berita`
--

CREATE TABLE `berita` (
  `id` int(11) NOT NULL,
  `id_temp` varchar(32) DEFAULT NULL,
  `nip_petugas` char(18) NOT NULL,
  `judul` varchar(256) NOT NULL,
  `konten_dir` varchar(64) NOT NULL,
  `waktu_terbit` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `waktu_edit_terakhir` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00',
  `foto_dir` varchar(64) NOT NULL,
  `file_dir` varchar(64) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `bimbingan`
--

CREATE TABLE `bimbingan` (
  `id` int(11) NOT NULL,
  `id_temp` varchar(32) DEFAULT NULL,
  `id_pembimbing` int(11) NOT NULL,
  `tanggal` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `isi_bimbingan` varchar(64) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `dosen`
--

CREATE TABLE `dosen` (
  `nip` char(18) NOT NULL,
  `nama` varchar(64) NOT NULL,
  `departemen` varchar(64) NOT NULL,
  `foto_dir` varchar(64) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `dosen`
--

INSERT INTO `dosen` (`nip`, `nama`, `departemen`, `foto_dir`) VALUES
('195102221985022001', 'Endah Yuswarini', 'Teknik Sipil ', NULL),
('195410081980031003', 'R. Adi Wardoyo', 'Desain Interior', NULL),
('196002211984031001', 'Muchammad Husni', 'Teknik Informatika', NULL),
('196008111986031001', 'Eko Nurmianto', 'Teknik Industri', NULL),
('196104041991021001', 'Bachtera Indarto', 'Fisika', NULL),
('196204181990031004', 'Tasripa', 'Teknik Elektro ', NULL),
('196301271990021003', 'Yoyok Cahyono', 'Fisika', NULL),
('196307261989031003', 'Muhammad Sigit Darmawa', 'Teknik Sipil', NULL),
('196401301990021001', 'Mochamad Zainuri', 'Fisika', NULL),
('196406081991021001', 'Sumarno', 'Teknik Kimia', NULL),
('196509191990031003', 'Bambang Sampurno', 'Teknik Mesin', NULL),
('196511011985101001', 'Tri Laksmi Budi Wicaksono', '', NULL),
('196809302000031001', 'Sungging Pintowantoro', 'Teknik Material dan Metalurgi', NULL),
('196906141998021001', 'Muchammad Nurif', 'M K U', NULL),
('197001221995121002', 'Andhika Estiyono', 'Desain Produk Industri', NULL),
('197004211998021001', 'Aries Rohiyanto', '', NULL),
('197103132009121001', 'Sholiq', 'Sistem Informasi', NULL),
('197107231995121001', 'Suntoyo', 'Teknik Kelauta', NULL),
('197207151998022001', 'Alvida Mustika Rukmi', 'Matematika ', NULL),
('197208091995121001', 'Agus Zainal Arifi', 'Teknik Informatika', NULL),
('197609182003122002', 'Lailatul Qadariyah', 'Teknik Kimia', NULL),
('197906202006042001', 'Dr. Widyastuti', 'Teknik Material dan Metalurgi', NULL),
('197906262005012002', 'Umi Laili Yuhana', 'Teknik Informatika', NULL),
('198101052005011004', 'Suwito', 'Teknik Elektro ', NULL),
('198101052010051200', 'Bayu S.', 'Fisika', NULL),
('198102102014042001', 'Dwi Indriyani', 'Teknik Sipil', NULL),
('198102242014041001', 'Imam Safawi Ahmad, S.Si., M.Si.', 'Statistika  ', NULL),
('198410162008121002', 'Radityo Anro ', 'Teknik Informatika', NULL),
('198501082007061300', 'Panji R.', 'Informatika', NULL),
('19860312201212204', 'Wijayanti Nurul Khotimah', 'Tek;nik Informatika', NULL),
('198802252014041001', 'Berto Mulia Wibawa', 'Manajemen Bisnis', NULL),
('199001042014041001', 'Erik Sugianto', 'Transportasi Laut', NULL),
('199001052011121001', 'Syauki A.', 'Matematika', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `list_aspek`
--

CREATE TABLE `list_aspek` (
  `id` int(11) NOT NULL,
  `aspek` varchar(64) NOT NULL,
  `bobot` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `mahasiswa`
--

CREATE TABLE `mahasiswa` (
  `nrp` char(14) NOT NULL,
  `nama` varchar(64) NOT NULL,
  `departemen` varchar(64) NOT NULL,
  `foto_dir` varchar(64) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `mahasiswa`
--

INSERT INTO `mahasiswa` (`nrp`, `nama`, `departemen`, `foto_dir`) VALUES
('05111440000067', 'Dzaky Z.', 'Kimia', NULL),
('05111440000137', 'Anwar H.', 'Informatika', NULL),
('05111440000153', 'Andreas G.', 'Matematika', NULL),
('05111640000001', 'Dimas', 'Kimia', NULL),
('05111640000002', 'Almas', 'Matematika', NULL),
('05111640000003', 'Fasma', 'Matematika', NULL),
('05111640000004', 'Nada', 'Matematika', NULL),
('05111640000005', 'Nida', 'Kimia', NULL),
('05111640000043', 'Rafi', 'Informatika', NULL),
('05111640000081', 'Deka', 'Informatika', NULL),
('05111640000134', 'Alam', 'Informatika', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `pembimbing`
--

CREATE TABLE `pembimbing` (
  `id` int(11) NOT NULL,
  `id_temp` varchar(32) DEFAULT NULL,
  `nip_pembimbing` char(18) NOT NULL,
  `id_proposal` int(11) NOT NULL,
  `is_setuju` bit(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `penilaian`
--

CREATE TABLE `penilaian` (
  `id` int(11) NOT NULL,
  `id_temp` varchar(32) DEFAULT NULL,
  `nip_penguji` char(18) NOT NULL,
  `id_aspek` int(11) NOT NULL,
  `id_proposal` int(11) NOT NULL,
  `tanggal` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `nilai` int(11) NOT NULL,
  `komentar_dir` varchar(64) DEFAULT NULL,
  `jenis_penilaian` varchar(64) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `petugas`
--

CREATE TABLE `petugas` (
  `nip` char(18) NOT NULL,
  `nama` varchar(64) NOT NULL,
  `jabatan` varchar(64) NOT NULL,
  `fotodir` varchar(64) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `proposal`
--

CREATE TABLE `proposal` (
  `id` int(11) NOT NULL,
  `id_temp` varchar(32) DEFAULT NULL,
  `judul` varchar(256) NOT NULL,
  `abstrak` varchar(64) NOT NULL,
  `bidang` varchar(64) NOT NULL,
  `tanggal_daftar` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `tanggal_diterima` timestamp NULL DEFAULT NULL,
  `tanggal_habis` timestamp NULL DEFAULT NULL,
  `status_diterima` bit(1) DEFAULT NULL,
  `pengajuan_dana` int(11) NOT NULL,
  `dana_disetujui` int(11) DEFAULT NULL,
  `file_dir` varchar(64) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `anggota`
--
ALTER TABLE `anggota`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_proposal` (`id_proposal`),
  ADD KEY `nrp_anggota` (`nrp_anggota`);

--
-- Indexes for table `angsuran`
--
ALTER TABLE `angsuran`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_proposal` (`id_proposal`),
  ADD KEY `nip_petugas` (`nip_petugas`);

--
-- Indexes for table `berita`
--
ALTER TABLE `berita`
  ADD PRIMARY KEY (`id`),
  ADD KEY `nip_petugas` (`nip_petugas`);

--
-- Indexes for table `bimbingan`
--
ALTER TABLE `bimbingan`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_pembimbing` (`id_pembimbing`);

--
-- Indexes for table `dosen`
--
ALTER TABLE `dosen`
  ADD PRIMARY KEY (`nip`);

--
-- Indexes for table `list_aspek`
--
ALTER TABLE `list_aspek`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `mahasiswa`
--
ALTER TABLE `mahasiswa`
  ADD PRIMARY KEY (`nrp`);

--
-- Indexes for table `pembimbing`
--
ALTER TABLE `pembimbing`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_proposal` (`id_proposal`),
  ADD KEY `nip_pembimbing` (`nip_pembimbing`);

--
-- Indexes for table `penilaian`
--
ALTER TABLE `penilaian`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_aspek` (`id_aspek`),
  ADD KEY `id_proposal` (`id_proposal`),
  ADD KEY `nip_penguji` (`nip_penguji`);

--
-- Indexes for table `petugas`
--
ALTER TABLE `petugas`
  ADD PRIMARY KEY (`nip`);

--
-- Indexes for table `proposal`
--
ALTER TABLE `proposal`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `anggota`
--
ALTER TABLE `anggota`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `angsuran`
--
ALTER TABLE `angsuran`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `berita`
--
ALTER TABLE `berita`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `bimbingan`
--
ALTER TABLE `bimbingan`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `list_aspek`
--
ALTER TABLE `list_aspek`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `pembimbing`
--
ALTER TABLE `pembimbing`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `penilaian`
--
ALTER TABLE `penilaian`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `proposal`
--
ALTER TABLE `proposal`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `anggota`
--
ALTER TABLE `anggota`
  ADD CONSTRAINT `anggota_ibfk_1` FOREIGN KEY (`id_proposal`) REFERENCES `proposal` (`id`),
  ADD CONSTRAINT `anggota_ibfk_2` FOREIGN KEY (`nrp_anggota`) REFERENCES `mahasiswa` (`nrp`);

--
-- Constraints for table `angsuran`
--
ALTER TABLE `angsuran`
  ADD CONSTRAINT `angsuran_ibfk_1` FOREIGN KEY (`id_proposal`) REFERENCES `proposal` (`id`),
  ADD CONSTRAINT `angsuran_ibfk_2` FOREIGN KEY (`nip_petugas`) REFERENCES `petugas` (`nip`);

--
-- Constraints for table `berita`
--
ALTER TABLE `berita`
  ADD CONSTRAINT `berita_ibfk_1` FOREIGN KEY (`nip_petugas`) REFERENCES `petugas` (`nip`);

--
-- Constraints for table `bimbingan`
--
ALTER TABLE `bimbingan`
  ADD CONSTRAINT `bimbingan_ibfk_1` FOREIGN KEY (`id_pembimbing`) REFERENCES `pembimbing` (`id`);

--
-- Constraints for table `pembimbing`
--
ALTER TABLE `pembimbing`
  ADD CONSTRAINT `pembimbing_ibfk_1` FOREIGN KEY (`id_proposal`) REFERENCES `proposal` (`id`),
  ADD CONSTRAINT `pembimbing_ibfk_2` FOREIGN KEY (`nip_pembimbing`) REFERENCES `dosen` (`nip`);

--
-- Constraints for table `penilaian`
--
ALTER TABLE `penilaian`
  ADD CONSTRAINT `penilaian_ibfk_1` FOREIGN KEY (`id_aspek`) REFERENCES `list_aspek` (`id`),
  ADD CONSTRAINT `penilaian_ibfk_2` FOREIGN KEY (`id_proposal`) REFERENCES `proposal` (`id`),
  ADD CONSTRAINT `penilaian_ibfk_3` FOREIGN KEY (`nip_penguji`) REFERENCES `dosen` (`nip`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
