drop table IF EXISTS agenda;
drop table IF EXISTS penilaian;
drop table IF EXISTS angsuran_masuk;
drop table IF EXISTS angsuran_keluar;
drop table IF EXISTS catatan;
drop table IF EXISTS berita;
drop table IF EXISTS proposal;
drop table IF EXISTS skim;
drop table IF EXISTS bidang;
drop table IF EXISTS mahasiswa;
drop table IF EXISTS petugas;
drop table IF EXISTS dosen;
drop table IF EXISTS notifikasi;
drop table IF EXISTS status_proposal;
drop table IF EXISTS aspek;
drop table IF EXISTS angsuran_dari_its;
drop table IF EXISTS angsuran_ke_its;
drop table IF EXISTS bimbingan;
drop table IF EXISTS sumber_dana;

create table skim(
	id int identity(0,1) primary key,
	tahun int not null,
	SKIM varchar(32) not null,
	tgl_mulai date not null,
	tgl_selesai date not null
);

create table agenda(
	id int identity(0,1) primary key,
	id_skim int foreign key references skim not null,
	nama varchar(32),
	tgl_mulai date not null,
	tgl_selesai date not null,
	upload varchar(64) null,
);



create table mahasiswa(
	id varchar(36) primary key,
	nrp varchar(14) not null unique,
	nama varchar(64) not null,
	gender varchar(16)  null,
	-- group_id int not null,
	no_hp varchar(16) null,
	email varchar(32) null,
	alamat varchar(128) null,
	foto varchar(128) null
);

create table dosen(
	id varchar(36) primary key,
	nip char(18) not null unique,
	nama varchar(64) not null,
	gender varchar(16)  null,
	-- group_id int not null,
	no_hp varchar(16) null,
	email varchar(32) null,
	alamat varchar(128) null,
	foto varchar(128) null
);


create table petugas(
	id varchar(36) primary key,
	nip char(18) not null unique,
	nama varchar(64) not null,
	password varchar(64) not null,
	gender varchar(16)  null,
	-- group_id int not null,
	no_hp varchar(16) null,
	email varchar(32) null,
	alamat varchar(128) null,
	foto varchar(128) null
); 



create table bidang(
	id int identity(0,1) primary key,
	nama_bidang varchar(64) not null,
	is_active bit not null
);

create table status_proposal(
	id int primary key,
	stat varchar(32) not null
);

create table proposal(
	id int identity(0,1) primary key,
	judul varchar(256) not null,
	file_abstrak varchar(64) null,
	tgl_daftar datetime not null,
	tgl_diterima datetime  null,
	tgl_selesai datetime  null,
	pengajuan_dana int not null,
	dana_disetujui int null,
	ketua varchar(14) foreign key references mahasiswa(nrp) not null,
	anggota1 varchar(14),
	anggota2 varchar(14),
	pembimbing char(18),
	id_bidang int foreign key references bidang not null,
	id_skim int foreign key references skim not null,
	is_anggota1 bit null,
	is_anggota2 bit null,
	file_dir varchar(64) null,
	id_status int foreign key references status_proposal not null
);


-- Angsur Mahasiswa ke ITS
create table angsuran_masuk(
	id int identity(0,1) primary key,
	id_proposal int foreign key references proposal not null,
	id_skim int foreign key references skim not null,
	nama_pengirim varchar(64) not null,
	jumlah int not null,
	bank varchar(16) not null,
	rekening varchar(32) not null,
	tgl_transfer datetime not null,
	verified_date datetime	null,
	verified_by char(18) foreign key references dosen(NIP) not null,
	verified_stat bit null,
	keterangan varchar(128)null,
	bukti varchar(64) not null
); 

-- Angsur ITS ke Mahasiswa(pendanaan)
create table angsuran_keluar(
	id int identity(0,1) primary key,
	id_proposal int foreign key references proposal not null,
	id_skim int foreign key references skim not null,
	nama_penerima varchar(64) not null,
	bank varchar(16) not null,
	jumlah int not null,
	rekening varchar(32) not null,
	tgl_transfer datetime not null
); 



create table penilaian(
	id_nilai int identity(0,1) primary key,
	--id_skim int foreign key references skim not null,
	proposal int foreign key references proposal not null,
	penilai1 char(18), --foreign key references dosen(NIP) not null,
	penilai2 char(18), --foreign key references dosen(NIP) not null,
	penilai3 char(18), --foreign key references dosen(NIP) not null,
	nilai int not null,
	komentar varchar(256) null,
	tgl_nilai date not null,
	tgl_update date null
);



create table catatan(
	id int identity(0,1) primary key,
	id_proposal int foreign key REFERENCES proposal not null,
	tanggal date not null,
	topik varchar(128) not null,	
	isi varchar(64) not null
);



create table berita(
	id int identity(0,1) primary key,
	judul varchar(128) not null,
	isi varchar(64) not null,
	tgl_buat date not null, 
	tgl_edit date  null,
	foto varchar(64) null,
	file_berita varchar(64) null
);

create table notifikasi(
	id int identity(0,1) primary key,
	penerima varchar(18) not null,
	subjek varchar(128) not null,
	pesan varchar(256) not null,
	tanggal datetime not null,
	redirect varchar(128) null,
	status bit null
);


insert into status_proposal values (0, 'Ditolak'),(2,'Menunggu Konfirmasi Anggota'), (1, 'Anggota Menolak'), (3,'Menunggu Penilaian'),(4, 'Sedang Berjalan'), 
(5, 'Telah Selesai');



INSERT INTO dosen (id, nip, nama, foto, gender) VALUES
('idd1','196002211984031001', 'Muchammad Husni', NULL,'L'),
('idd2','196008111986031001', 'Eko Nurmianto', NULL,'L'),
('idd3','198510172015042001', 'Dini Adni Navastara',NULL,'P');


insert into petugas(id, nip, nama,password, gender) values
('idp', '123456789012345678', 'Muhammad Arrafi','pass','L');


INSERT INTO mahasiswa (id, nrp, nama, foto, gender) VALUES
('idm6','05111640000043','Muhammad Arrafi',  'https://my.its.ac.id/photo?id=081BA8B8-BE83-452E-9484-FD205543510F','L'),
('idm7','05111640000081','Deka',  'https://my.its.ac.id/photo?id=081BA8B8-BE83-452E-9484-FD205543510F','L'),
('idm1','05111640000001','Dimas', NULL,'L'),
('idm2','05111640000002','Almas', NULL,'L'),
('idm3','05111640000003','Fasma', NULL,'L');



insert into bidang (nama_bidang, is_active) values ('Kuliner', '1'),
('Industri Kreatif', '1'), ('Jasa', '1'), ('Kerajinan tangan', '0');

insert into skim(tahun, skim, tgl_mulai, tgl_selesai)
values 
( 2015, 'PMW', '2015-05-01 00:00:00 ', '2015-06-10 23:59:59 '),
( 2015, 'Bank BRI', '2019-02-10 00:00:00 ', '2019-03-11 23:59:59 '),
( 2012, 'APBN', '2015-06-05 00:00:00 ', '2015-12-27 23:59:59 '),
( 2013, 'APBN', '2015-06-05 00:00:00 ', '2015-12-27 23:59:59 '),
( 2014, 'APBN', '2015-06-05 00:00:00 ', '2015-12-27 23:59:59 '),
( 2013 , 'BRI', '2015-07-07 00:00:00 ', '2015-12-27 23:59:59 '),
( 2014 , 'BRI', '2015-07-09 00:00:00 ', '2015-12-27 23:59:59 ');


-- ('081BA8B8-BE83-452E-9484-FD205543510F','5116100158','FARIZ ARDIN ADHIYAKSA', 'https://my.its.ac.id/photo?id=081BA8B8-BE83-452E-9484-FD205543510F' ,'L'),
-- ('7A628EBB-13DD-407D-9F0D-D02AE0263782', '5116100043', 'MUHAMMAD ARRAFI' , 'https://my.its.ac.id/photo?id=7A628EBB-13DD-407D-9F0D-D02AE0263782 ' ,'L' ),