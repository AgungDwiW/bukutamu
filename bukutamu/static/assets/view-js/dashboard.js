    $(document).ready(function(){
 
 //Data SKIM
 $('#btn_data_skim').click(function(){
  
  if($.trim($('#tahun_dana').val()).length == 0)
  {
     error_tahun_dana = 'is required';
     $('#error_tahun_dana').text(error_tahun_dana);
     $('#tahun_dana').addClass('has-error');
  }
  else
  {
    error_tahun_dana = '';
    $('#error_tahun_dana').text(error_tahun_dana);
    $('#tahun_dana').removeClass('has-error');
  }
  
  if($.trim($('#sumber_dana').val()).length == 0)
  {
     error_sumber_dana = 'is required';
     $('#error_sumber_dana').text(error_sumber_dana);
     $('#sumber_dana').addClass('has-error');
  }
  else
  {
    error_sumber_dana = '';
    $('#error_sumber_dana').text(error_sumber_dana);
    $('#sumber_dana').removeClass('has-error');
  }

  if($.trim($('#skim').val()).length == 0)
  {
     error_skim = 'is required';
     $('#error_skim').text(error_skim);
     $('#skim').addClass('has-error');
  }
  else
  {
    error_skim = '';
    $('#error_skim').text(error_skim);
    $('#skim').removeClass('has-error');
  }

  //Next and Previous 
  if(error_tahun_dana != '' || error_sumber_dana != '' || 
    error_skim != '' )
  {
     return false;
  }
  else
  {
     $('#list_data_skim').removeClass('active');
     $('#data_skim').removeClass('active');
     $('#list_data_kegiatan').addClass('active');
     $('#data_kegiatan').addClass('active');
  }
 });
 
   $('#previous_btn_data_kegiatan').click(function(){
    $('#list_data_kegiatan').removeClass('active');
    $('#data_kegiatan').removeClass('active');
    $('#list_data_skim').addClass('active');
    $('#data_skim').addClass('active');
   });
 
   


 //Data Kegiatan
 $('#btn_data_kegiatan').click(function(){

  if($.trim($('#judul').val()).length == 0)
  {
   error_judul = 'is required';
   $('#error_judul').text(error_judul);
   $('#judul').addClass('has-error');
  }
  else
  {
   error_judul = '';
   $('#error_judul').text(error_judul);
   $('#judul').removeClass('has-error');
  }


  if($.trim($('#abstrak').val()).length == 0)
  {
   error_abstrak = 'is required';
   $('#error_abstrak').text(error_abstrak);
   $('#abstrak').addClass('has-error');
  }
  else
  {
   error_abstrak = '';
   $('#error_abstrak').text(error_abstrak);
   $('#abstrak').removeClass('has-error');
  }

   if($.trim($('#bidang').val()).length == 0)
  {
   error_bidang = 'is required';
   $('#error_bidang').text(error_bidang);
   $('#bidang').addClass('has-error');
  }
  else
  {
   error_bidang = '';
   $('#error_bidang').text(error_bidang);
   $('#bidang').removeClass('has-error');
  }

  if($.trim($('#dana').val()).length == 0)
  {
   error_dana = 'is required';
   $('#error_dana').text(error_dana);
   $('#dana').addClass('has-error');
  }
  else
  {
   error_dana = '';
   $('#error_dana').text(error_dana);
   $('#dana').removeClass('has-error');
  }
  
  if($.trim($('#anggota1').val()).length == 0)
  {
   error_anggota1 = 'is required';
   $('#error_anggota1').text(error_anggota1);
   $('#anggota1').addClass('has-error');
  }
  else
  {
   error_anggota1 = '';
   $('#error_anggota1').text(error_anggota1);
   $('#anggota1').removeClass('has-error');
  }
  
  if($.trim($('#anggota2').val()).length == 0)
  {
   error_anggota2 = 'is required';
   $('#error_anggota2').text(error_anggota2);
   $('#anggota2').addClass('has-error');
  }
  else
  {
   error_anggota2 = '';
   $('#error_anggota2').text(error_anggota2);
   $('#anggota2').removeClass('has-error');
  }
  
  if($.trim($('#pembimbing1').val()).length == 0)
  {
   error_pembimbing1 = 'is required';
   $('#error_pembimbing1').text(error_pembimbing1);
   $('#pembimbing1').addClass('has-error');
  }
  else
  {
   error_pembimbing1 = '';
   $('#error_pembimbing1').text(error_pembimbing1);
   $('#pembimbing1').removeClass('has-error');
  }

  if($('#anggota1').val() == $('#anggota2').val())
  {
    error_match_nrp = 'Use another NRP';
    $('#error_anggota2').text(error_match_nrp); 
    $('#anggota2').addClass('has-error');
  }
  else
  {
    error_match_nrp = '';
    $('#error_anggota2').text(error_match_nrp);
   $('#anggota2').removeClass('has-error');
  }



  //Next and previous
  if(error_judul != '' || error_abstrak != '' || error_bidang != '' ||  error_dana != '' 
   || error_anggota1 != '' || error_anggota2 != '' || error_pembimbing1!= '' || error >0 
    || error_match_nrp !='' )
  {
   return false;
  }
  else
  {
    $('#list_data_kegiatan').removeClass('active');
     $('#data_kegiatan').removeClass('active');
     $('#list_unggah_proposal').addClass('active');
     $('#unggah_proposal').addClass('active');
  } 
 });
 
 $('#previous_btn_unggah_proposal').click(function(){
    $('#list_unggah_proposal').removeClass('active');
    $('#unggah_proposal').removeClass('active');
    $('#list_data_kegiatan').addClass('active');
    $('#data_kegiatan').addClass('active');
 });

 
 $('#btn_unggah_proposal').click(function(){
  
   //$('#btn_unggah_proposal').attr("disabled", "disabled");
   $(document).css('cursor', 'prgress');
   $("#register_form").submit();  
 });


});