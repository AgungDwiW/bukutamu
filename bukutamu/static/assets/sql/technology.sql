 -- Untuk Penggunaan


drop table penilaian;
drop table notifikasi;
drop table berita;
drop table pencairan_dana;
drop table angsuran_mahasiswa;
drop table proposal;
drop table aspek;
drop table skim;
drop table bidang;
drop table petugas;
drop table dosen;
drop table mahasiswa;
drop table laporan_kemajuan;
drop table catatan;


create table mahasiswa(
	id varchar(36) primary key,
	nrp varchar(14) not null unique,
	nama varchar(64) not null,
	foto_dir varchar(128) null
);

create table dosen(
	id char(36) primary key,
	nip char(18) not null unique,
	nama varchar(64) not null,
	foto_dir varchar(128) null
);

create table petugas(
	id char(36) primary key ,
	nip char(18) not null unique,
	nama varchar(64) not null,
	jabatan varchar(64) not null,
	foto_dir varchar(128) null
);

create table bidang(
	id int identity(0,1) primary key,
	nama varchar(64) not null,
	is_active bit not null
);

create table skim(
	id int identity(0,1) primary KEY,
	nama varchar(64) not null,
	tahun int not null,
	asal_dana varchar(32) not null,
	tanggal_mulai_pengajuan datetime,
	tanggal_akhir_pengajuan datetime,
	is_active bit not null
);



create table proposal(
	id int identity(0,1) primary key,
	judul varchar(256) not null,
	file_abstrak varchar(64) not null,
	tanggal_daftar datetime not null,
	tanggal_diterima datetime null,
	tanggal_habis datetime null,
	status_diterima bit null,
	pengajuan_dana int not null,
	dana_disetujui int null,
	jumlah_termin_angsur int null, --ditentukan saat proposal diterima
	file_dir varchar(64) not null,
	laporan_akhir_dir varchar(64) null,
	is_active bit  null,
	ketua varchar(14) foreign key references mahasiswa(nrp) not null,
	anggota1 varchar(14) ,
	anggota2 varchar(14) ,
	pembimbing char(18),
	bidang int foreign key REFERENCES bidang not null,
	skim int FOREIGN KEY REFERENCES skim not null,
	is_anggota1 bit null,
	is_anggota2 bit null
);

create table aspek(
	id int identity(0,1) primary key,
	id_proposal int foreign key references proposal not null,
	aspek_penilaian varchar(64) not null,
	bobot_penilaian int not null,
	keterangan varchar(128) null,
	is_active bit not null
);

create table laporan_kemajuan(
	id int identity (0,1) primary key,
	id_proposal int foreign key references proposal not null,
	tgl_submit date not null,
	file_dir varchar(64) not null,
	termin int not null,
);


create table catatan(
	id int identity(0,1) primary key,
	id_proposal int foreign key REFERENCES proposal not null,
	tanggal date not null,
	topik varchar(128) not null,
	isi varchar(64) not null
);

create table pencairan_dana(
	id int identity(0,1) primary key,
	nip_petugas char(18) foreign key references petugas(nip)not null,
	id_proposal int foreign key references proposal not null,
	tanggal datetime not null,
	jumlah int not null,
	termin int not null,
	keterangan varchar(128) null
);

create table angsuran_mahasiswa(
	id int identity(0,1) primary key,
	nip_petugas char(18) foreign key references petugas(nip) not null,
	id_proposal int foreign key references proposal not null,
	tanggal datetime not null,
	jumlah int not null,
	termin int not null,
	bukti_transfer varchar(64) not null,
	konfirmasi bit null
);

create table berita(
	id int identity(0,1) primary key,
	nip_petugas char(18) foreign key references petugas(nip) not null,
	judul varchar(256) not null,
	konten_dir varchar(64) not null,
	waktu_terbit datetime not null,
	waktu_edit_terakhir datetime not null,
	foto_dir varchar(64) not null,
	file_dir varchar(64) not null
);

create table penilaian(
	id int identity(0,1) primary key,
	penguji char(18) not null,
	id_proposal int foreign key references proposal not null,
	id_aspek int foreign key references aspek not null,
	tanggal datetime not null,
	nilai decimal(4,2) not null,
	komentar varchar(128) null,
	termin int not NULL
);

create table notifikasi(
	id int identity(0,1) primary key,
	tanggal datetime not null,
	keterangan varchar(256) null,
	is_active bit not null,
	id_proposal int foreign key references proposal not null
);




INSERT INTO dosen (id, nip, nama, foto_dir) VALUES
('idd1','196002211984031001', 'Muchammad Husni', NULL),
('idd2','196008111986031001', 'Eko Nurmianto', NULL),
('idd3','198510172015042001', 'Dini Adni Navastara',NULL);


insert into petugas (id, nip, nama, jabatan) values
('idp', '123456789012345678', 'Muhammad Arrafi', 'Developer');


INSERT INTO mahasiswa (id, nrp, nama, foto_dir) VALUES
('081BA8B8-BE83-452E-9484-FD205543510F','5116100158','FARIZ ARDIN ADHIYAKSA', 'https://my.its.ac.id/photo?id=081BA8B8-BE83-452E-9484-FD205543510F' ),
('7A628EBB-13DD-407D-9F0D-D02AE0263782', '5116100043', 'MUHAMMAD ARRAFI' , 'https://my.its.ac.id/photo?id=7A628EBB-13DD-407D-9F0D-D02AE0263782 '  ),
('idm6','05111640000043','Muhammad Arrafi',  'https://my.its.ac.id/photo?id=081BA8B8-BE83-452E-9484-FD205543510F'),
('idm7','05111640000081','Deka',  'https://my.its.ac.id/photo?id=081BA8B8-BE83-452E-9484-FD205543510F'),
('idm1','05111640000001','Dimas',   NULL),
('idm2','05111640000002','Almas', NULL),
('idm3','05111640000003','Fasma' , NULL);

insert into bidang (nama, is_active) values ('Kuliner', '1'),
('Industri Kreatif', '1'), ('Jasa', '1'), ('Kerajinan tangan', '0');

insert into skim
(nama, tahun, asal_dana, tanggal_mulai_pengajuan, tanggal_akhir_pengajuan, is_active)
values
('PMW', 2015, 'PMW', '2015-05-01 00:00:00 ', '2015-06-10 23:59:59 ',1),
('BRI', 2015, 'Bank BRI', '2015-05-01 00:00:00 ', '2015-12-27 23:59:59 ',1),
('PMW', 2012, 'APBN', '2015-06-05 00:00:00 ', '2015-12-27 23:59:59 ',0),
('PMW', 2013, 'APBN', '2015-06-05 00:00:00 ', '2015-12-27 23:59:59 ',1),
('PMW', 2014, 'APBN', '2015-06-05 00:00:00 ', '2015-12-27 23:59:59 ',1),
('KKUMKM', 2013, 'KKUMKM', '2015-06-05 00:00:00 ', '2015-12-27 23:59:59 ',1),
('BRI', 2013, 'BRI', '2015-07-07 00:00:00 ', '2015-12-27 23:59:59 ',0),
('BRI', 2014 , 'BRI', '2015-07-09 00:00:00 ', '2015-12-27 23:59:59 ',1),
('PMW Sesi 2', 2015, 'APBN', '20150810 00:00:00 ', '2015-09-18 23:59:59 ',1);