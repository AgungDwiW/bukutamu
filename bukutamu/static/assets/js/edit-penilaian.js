$(document).ready(function(){  
        var error;

        $('#EditNilai').on('show.bs.modal', function (event) {
          var id_nilai = $(event.relatedTarget).data('id');
          var id_proposal = $(event.relatedTarget).data('idp');
          var judul = $(event.relatedTarget).data('judul');
          var penilai1 = $(event.relatedTarget).data('penilai1');
          var penilai2 = $(event.relatedTarget).data('penilai2');
          var penilai3 = $(event.relatedTarget).data('penilai3');
          var nilai = $(event.relatedTarget).data('nilai');
          var komentar = $(event.relatedTarget).data('komen');     
          $(this).find("input#editid_nilai").val(id_nilai);
          $(this).find("input#editid_proposal").val(id_proposal);
          $(this).find("span#editjudul_form_nilai").text(judul);    
          $(this).find("input#editnip1").val(penilai1);
          $(this).find("input#editnip2").val(penilai2);
          $(this).find("input#editnip3").val(penilai3);
          $(this).find("input#editnilai").val(nilai);
          $(this).find("#editkomentar").val(komentar);
        });

        $("input#editnip1").focusout(function(){
           var pembimbing = $("#editnip1").val();
           var pembimbing2 = $("#editnip2").val();
           var  same = 0;
           if(pembimbing == pembimbing2 && pembimbing != 0 && pembimbing2 != 0)
           {
              $("span#editvalid_nip1").text('Enter Another NIP');
              $("span#editvalid_nip2").text('Enter Another NIP');
              $("input#editnip1").addClass('is-invalid');
              $("input#editnip2").addClass('is-invalid');
              error = 1;
              same = 1;
           }
           else{
                if(same)
                {
                    $("span#editvalid_nip1").text('');
                    $("span#editvalid_nip2").text('');
                    $("input#editnip1").removeClass('is-invalid is-valid');
                    $("input#editnip2").removeClass('is-invalid is-valid');
                    same = 0;
                    error = 0;
                }
                $.post("<?php echo site_url('SiakadAPI/validationNIP')?>",{
                 nip: pembimbing
                 },function(data){
                    if(data == 0){
                       error = 1;
                       $("span#editvalid_nip1").text('NIP is incorrect or not found');
                       $("input#editnip1").addClass('is-invalid');
                       $("input#editnip1").removeClass('is-valid');
                    }
                    else{
                        error =0;
                        $("span#editvalid_nip1").html(data);
                        $("input#editnip1").addClass('is-valid');
                        $("input#editnip1").removeClass('is-invalid');
                    }     
                });

           }
           
           
        }) ;

        $("input#editnip2").focusout(function(){
           var pembimbing = $("#editnip1").val();
           var pembimbing2 = $("#editnip2").val();
            var  same = 0;
           if(pembimbing == pembimbing2 && pembimbing != 0 && pembimbing2 != 0)
           {
              $("span#editvalid_nip1").text('Enter Another NIP');
              $("span#editvalid_nip2").text('Enter Another NIP');
              $("input#editnip1").addClass('is-invalid');
              $("input#editnip2").addClass('is-invalid');
              error = 1;
              same = 1;
           }
           else{
                if(same)
                {
                    $("span#editvalid_nip1").text('');
                    $("span#editvalid_nip2").text('');
                    $("input#editnip1").removeClass('is-invalid is-valid');
                    $("input#editnip2").removeClass('is-invalid is-valid');
                    same = 0;
                    error = 0;
                }
                $.post("<?php echo site_url('SiakadAPI/validationNIP')?>",{
                 nip: pembimbing2
                 },function(data){
                    if(data == 0){
                       error = 1;
                       $("span#editvalid_nip2").text('NIP is incorrect or not found');
                       $("input#editnip2").addClass('is-invalid');
                       $("input#editnip2").removeClass('is-valid');
                    }
                    else{
                        error =0;
                        $("span#editvalid_nip2").html(data);
                        $("input#editnip2").addClass('is-valid');
                        $("input#editnip2").removeClass('is-invalid');
                    }     
                });

           }
           
           
        }) ;

        $("input#editnip3").focusout(function(){
           var pembimbing = $("#editnip3").val();
           if(pembimbing == 0){
                error = 0
                 $("span#editvalid_nip3").text('');
            
                $("input#editnip3").removeClass('is-invalid');
                $("input#editnip3").removeClass('is-valid');
           }
           else
           {
                $.post("<?php echo site_url('SiakadAPI/validationNIP')?>",{
                 nip: pembimbing
                },function(data){
                  if(data == 0){
                      error = 1;
                      $("span#editvalid_nip3").text('NIP is incorrect or not found');
                      $("input#editnip3").addClass('is-invalid');
                      $("input#editnip3").removeClass('is-valid');
                  }
                  else{
                    error =0;
                    $("span#editvalid_nip3").html(data);

                    $("input#editnip3").removeClass('is-invalid');
                    $("input#editnip3").addClass('is-valid');
                  } 
                });
           }
           
        }) ;
        $("#edit_nilai").click(function(){
            if(error == 1)
            {
                return false;
            }
            return true;
        });


});