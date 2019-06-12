-- Perubahan DB
alter table proposal
add is_anggota1 bit null;

alter table proposal
add is_anggota2 bit null;

alter table dosen
drop column departemen;

alter table skim
add asal_dana varchar(32);

alter table skim
add tanggal_mulai_pengajuan datetime;

alter table skim
add tanggal_akhir_pengajuan datetime;

alter table mahasiswa
drop column angkatan
drop column departemen

--Agar admin dapat menambahkan dan mengubah
alter table skim
add is_active bit 

insert into skim
(nama, tahun, jumlah_termin, asal_dana, tanggal_mulai_pengajuan, tanggal_akhir_pengajua, is_active)
values
('PMW', 2015, 3, 'PMW', '2015-05-01 00:00:00 ', '2015-06-10 23:59:59 ',1),
('BRI', 2015, 3, 'Bank BRI', '2015-05-01 00:00:00 ', '2015-12-27 23:59:59 ',1),
('PMW', 2012, 3, 'APBN', '2015-06-05 00:00:00 ', '2015-12-27 23:59:59 ',0),
('PMW', 2013, 3, 'APBN', '2015-06-05 00:00:00 ', '2015-12-27 23:59:59 ',1),
('PMW', 2014, 3, 'APBN', '2015-06-05 00:00:00 ', '2015-12-27 23:59:59 ',1),
('KKUMKM', 2013, 3, 'KKUMKM', '2015-06-05 00:00:00 ', '2015-12-27 23:59:59 ',1),
('BRI', 2013, 3, 'BRI', '2015-07-07 00:00:00 ', '2015-12-27 23:59:59 ',0),
('BRI', 2014, 3, 'BRI', '2015-07-09 00:00:00 ', '2015-12-27 23:59:59 ',1),
('PMW Sesi 2', 2015, 3, 'APBN', '20150810 00:00:00 ', '2015-09-18 23:59:59 ',1);

alter table mahasiswa
{
	id varchar(64) primary key, "7A628EBB-13DD-407D-9F0D-D02AE0263782"
	nrp varchar (16) not null,
}


-- Foreign key menyebabkan nrp yg tidak ada di database tidak dapat di input, maka
alter table proposal 
drop contraint anggota1 dan anggota 2

alter table proposal 
alter column is_finished bit null;
alter table proposal 
alter column is_active  bit null;

alter table proposal
drop column is_finished;

alter table dosen 
drop column is_admin 

drop table bimbingan.

create table catatam(
	id int identity(0,1) primary key,
	id_proposal int foreign key REFERENCES proposal not null,
	tanggal datetime not null,
	topik isi varchar(128) not null,
	isi varchar(64) not null
);

alter table catatan alter column tanggal date;

--Sini ke Atas Sudah diterapkan pada technology.sql --
create table laporan_kemajuan(
	id int identity(0,1) primary key;
	id_proposal int foreign key REFERENCES proposal not null,
	tanggal datetime not null,
	isi varchar(64) not null

insert into catatan (id_proposal, tanggal, topik, isi) values ('3', '2018-10-31', 'Topik khusus', 'TATATATAA');
insert into catatan (id_proposal, tanggal, topik, isi) values ('3', '2018-10-31', 'Topik 2', 'qwertyuiop');
insert into catatan (id_proposal, tanggal, topik, isi) values ('3', '2018-10-31', 'Topik 3', 'Apapapaa');

alter table Mahasiswa alter column foto_dir varchar(128);

alter table Dosen alter column foto_dir varchar(128);

alter table Petugas alter column foto_dir varchar(128);


-- Perubahan 5 - 1 -2019
-- jumlah termin dari tabel skim pindah ke proposal