
//jQuery time
var current_fs, next_fs, previous_fs; //fieldsets
var left, opacity, scale; //fieldset properties which we will animate
var animating; //flag to prevent quick multi-click glitches

$(".next1").click(function(){
    var tahundana = document.getElementById("tahun_dana").value;
    var usulanskim = document.getElementById("skim").value;

    //validation step
    if(tahundana == ""){
        $("#danayear_error").html("*Tahun Sumber Dana is required");
        $("#danayear_error").show();
    }
    if(tahundana != ""){
        $("#danayear_error").hide();
    }

    if(usulanskim == ""){
        $("#usulanskim_error").html("*SKIM is required");
        $("#usulanskim_error").show();
    }
    if(usulanskim != ""){
        $("#usulanskim_error").hide();
    }
    
    if(tahundana != ""  && usulanskim != ""){
            
        if(animating) return false;
        animating = true;

        current_fs = $(this).parent();
        next_fs = $(this).parent().next();

        //activate next step on progressbar using the index of next_fs
        $("#progressbar li").eq($("fieldset").index(next_fs)).addClass("active");

        //show the next fieldset
        next_fs.show(); 
        //hide the current fieldset with style
        current_fs.animate({opacity: 0}, {
            step: function(now, mx) {
                //as the opacity of current_fs reduces to 0 - stored in "now"
                //1. scale current_fs down to 80%
                scale = 1 - (1 - now) * 0.2;
                //2. bring next_fs from the right(50%)
                left = (now * 50)+"%";
                //3. increase opacity of next_fs to 1 as it moves in
                opacity = 1 - now;
                current_fs.css({
            'transform': 'scale('+scale+')',
            'position': 'absolute'
            });
                next_fs.css({'left': left, 'opacity': opacity});
            }, 
            duration: 800, 
            complete: function(){
                current_fs.hide();
                animating = false;
            }, 
            //this comes from the custom easing plugin
            easing: 'easeInOutBack'
        });
        $("#progressbar li").eq($("fieldset").index(current_fs)).removeClass("active");
    }
    
});

$(".next2").click(function(){

    var judulproposal = $("#Judul").val().length;
    var abstrakproposal = $("#Abstrak").val().length;
    var bidangproposal = document.getElementById("bidang").value;
    var danaproposal = $("#dana").val();
    var anggota1proposal = $("#anggota1").val();
    var anggota2proposal = $("#anggota2").val();
    var pembimbingproposal = $("#pembimbing").val();
     var anggota1valid = $("#valid_nrp").val();
     var anggota2valid = $("#valid_nrp2").text();
     var pembimbingvalid = $("#valid_nip").text();


    if(judulproposal == 0){
        $("#judul_error").html("*Judul is required");
        $("#judul_error").show();
    }
    if(judulproposal != 0){
        $("#judul_error").hide();
    }

    if(abstrakproposal == 0){
        $("#abstrak_error").html("*Abstrak is required");
        $("#abstrak_error").show();
    }
    if(abstrakproposal != 0){
        $("#abstrak_error").hide();
    }
    if(bidangproposal == ""){
        $("#bidang_error").html("*Bidang is required");
        $("#bidang_error").show();
    }
    if(bidangproposal != ""){
        $("#bidang_error").hide();
    }

    if(danaproposal == 0){
        $("#pengajuandana_error").html("*Pengajuan Dana is required");
        $("#pengajuandana_error").show();
    }

    if(danaproposal < 0){
        $("#pengajuandana_error").html("*Dana tidak boleh minus");
        $("#pengajuandana_error").show();
    }

    if(danaproposal != 0 && danaproposal > 0){
        $("#pengajuandana_error").hide();
    }

    if(anggota1proposal == 0){
        $("#anggota1_error").html("*Anggota1 is required");
        $("#anggota1_error").show();
    }
    if(anggota1proposal != 0){
        $("#anggota1_error").hide();
    }

    if(anggota2proposal == 0){
        $("#anggota2_error").html("*Anggota2 is required");
        $("#anggota2_error").show();
    }
    if(anggota2proposal != 0){
        $("#anggota2_error").hide();
    }

    if(pembimbingproposal == 0){
        $("#pembimbing_error").html("*Pembimbing is required");
        $("#pembimbing_error").show();
    }
    if(pembimbingproposal != 0){
        $("#pembimbing_error").hide();
    }

    if(anggota1valid)
    {
        $("#pembimbing_error").html("Cek NRP dengan klik kolom input");
    }

    if(judulproposal != 0 && abstrakproposal != 0 && danaproposal != 0 && danaproposal > 0 
        && bidangproposal != ""  && pembimbingproposal != 0 
        && anggota2proposal != 0 && anggota1proposal != 0 && danaproposal > 0
        && error1 == 0 && error2  == 0 && error3 == 0){
        if(animating) return false;
        animating = true;

        current_fs = $(this).parent();
        next_fs = $(this).parent().next();

        //activate next step on progressbar using the index of next_fs
        $("#progressbar li").eq($("fieldset").index(next_fs)).addClass("active");

        //show the next fieldset
        next_fs.show(); 
        //hide the current fieldset with style
        current_fs.animate({opacity: 0}, {
            step: function(now, mx) {
                //as the opacity of current_fs reduces to 0 - stored in "now"
                //1. scale current_fs down to 80%
                scale = 1 - (1 - now) * 0.2;
                //2. bring next_fs from the right(50%)
                left = (now * 50)+"%";
                //3. increase opacity of next_fs to 1 as it moves in
                opacity = 1 - now;
                current_fs.css({
            'transform': 'scale('+scale+')',
            'position': 'absolute'
            });
                next_fs.css({'left': left, 'opacity': opacity});
            }, 
            duration: 800, 
            complete: function(){
                current_fs.hide();
                animating = false;
            }, 
            //this comes from the custom easing plugin
            easing: 'easeInOutBack'
        });
        $("#progressbar li").eq($("fieldset").index(current_fs)).removeClass("active");
    }
});

$(".previous").click(function(){
	if(animating) return false;
	animating = true;
	
	current_fs = $(this).parent();
	previous_fs = $(this).parent().prev();
	
	//de-activate current step on progressbar
	$("#progressbar li").eq($("fieldset").index(current_fs)).removeClass("active");
	
	//show the previous fieldset
	previous_fs.show(); 
	//hide the current fieldset with style
	current_fs.animate({opacity: 0}, {
		step: function(now, mx) {
			//as the opacity of current_fs reduces to 0 - stored in "now"
			//1. scale previous_fs from 80% to 100%
			scale = 0.8 + (1 - now) * 0.2;
			//2. take current_fs to the right(50%) - from 0%
			left = ((1-now) * 50)+"%";
			//3. increase opacity of previous_fs to 1 as it moves in
			opacity = 1 - now;
			current_fs.css({'left': left});
			previous_fs.css({'transform': 'scale('+scale+')', 'opacity': opacity});
		}, 
		duration: 800, 
		complete: function(){
			current_fs.hide();
			animating = false;
		}, 
		//this comes from the custom easing plugin
		easing: 'easeInOutBack'
	});
	$("#progressbar li").eq($("fieldset").index(previous_fs)).addClass("active");
});

// submitform SKIM form validation
$(".submit-skim").click(function(){
	var kodesumber_length = $("#kodesumber").val().length;
	var tahunskim = document.getElementById("tahunskim").value;
	var namasumber_length = $("#namasumber").val().length;
	var skim_length =  $("#skim_id").val().length;
	var tglmulaiskim_length =  $("#tglmulaiskim").val().length;
	var tglselesaiskim_length =  $("#tglselesaiskim").val().length;
	
        if(kodesumber_length == 0){
            $("#sumbercode_error").html("*Kode sumber is required");
            $("#sumbercode_error").show();
		}
		if(kodesumber_length != 0){
            $("#sumbercode_error").hide();
		}
		if(tahunskim == ""){
            $("#year_error").html("*Tahun is required");
            $("#year_error").show();
        }
        if(tahunskim != ""){
            $("#year_error").hide();
		}
		if(namasumber_length == 0){
            $("#sumbername_error").html("*Nama sumber is required");
            $("#sumbername_error").show();
		}
		if(namasumber_length != 0){
            $("#sumbername_error").hide();
		}
		if(skim_length == 0){
            $("#skim_error").html("*SKIM is required");
            $("#skim_error").show();
		}
		if(skim_length != 0){
            $("#skim_error").hide();
		}
		if(tglmulaiskim_length == 0){
            $("#tglmulaiskim_error").html("*Tanggal mulai is required");
            $("#tglmulaiskim_error").show();
		}
		if(tglmulaiskim_length != 0){
            $("#tglmulaiskim_error").hide();
		}
		if(tglselesaiskim_length == 0){
            $("#tglselesaiskim_error").html("*Tanggal selesai is required");
            $("#tglselesaiskim_error").show();
		}
		if(tglselesaiskim_length != 0){
            $("#tglselesaiskim_error").hide();
		}
});

// Auto form validation
$(document).ready(function(){
    $("#sumbercode_error").hide();
    $("#year_error").hide();
    $("#sumbername_error").hide();
    $("#skim_error").hide();
    $("#tglmulaiskim_error").hide();
    $("#tglselesaiskim_error").hide();
    $("#tahundana_error").hide();
    $("#sumberdana_error").hide();
    $("#usulanskim_error").hide();
    $("#judul_error").hide();
    $("#abstrak_error").hide();
    $("#bidang_error").hide();
    $("#pengajuandana_error").hide();
    $("#anggota1_error").hide();
    $("#anggota2_error").hide();
    $("#pembimbing_error").hide();
    $("#file_error").hide();

    var error_sumbername = false;
    var error_year =  false;
    var error_sumbercode = false;
    var error_skim = false;
    var error_tglmulaiskim = false;
    var error_tglselesaiskim = false;

    $("#kodesumber").keyup(function(){
        check_kodesumber();
    });

    $("#namasumber").keyup(function(){
        check_namasumber();
    });

    $("#skim_id").keyup(function(){
        check_skim();
    });

    //
    $("#kodesumber").focusout(function(){
        check_kodesumber();
    });

    $("#tahunskim").focusout(function(){
        check_tahunskim();
    });

    $("#namasumber").focusout(function(){
        check_namasumber();
    });

    $("#skim_id").focusout(function(){
        check_skim();
    });

    $("#file").select(function(){
        fileValidation();
    });
    //

    $("#tglmulaiskim").focusin(function(){
        check_tglmulaiskim();
    });

    $("#tglselesaiskim").focusin(function(){
        check_tglselesaiskim();
    });
    
    $("#tahun_dana").focusout(function(){
        check_tahundana();
    });

    $("#sumber_dana").focusout(function(){
        check_sumberdana();
    });

    $("#skim").focusout(function(){
        check_usulanskim();
    });
    
    // 
    $("#Judul").keyup(function(){
        check_judul();
    });

    $("#Abstrak").keyup(function(){
        check_abstrak();
    });

    $("#bidang").focusout(function(){
        check_bidang();
    });
    
    $("#dana").keyup(function(){
        check_dana();
    });

    $("#anggota1").keyup(function(){
        check_anggota1();
    });

    $("#anggota2").keyup(function(){
        check_anggota2();
    });
    $("#pembimbing").keyup(function(){
        check_pembimbing();
    });
    // 

    function check_kodesumber(){
        var kodesumber_length = $("#kodesumber").val().length;
        if(kodesumber_length == 0){
            $("#sumbercode_error").html("*Kode sumber is required");
            $("#sumbercode_error").show();
        }
        else{
			$("#sumbercode_error").hide();
			error_sumbername = true;
        }
    }

    function check_tahunskim(){
        var tahunskim = document.getElementById("tahunskim").value;
        if(tahunskim == ""){
            $("#year_error").html("*Tahun is required");
            $("#year_error").show();
        }
        else{
			$("#year_error").hide();
			error_year =  true;
        }
    }

    function check_namasumber(){
        var kodesumber_length = $("#namasumber").val().length;
        if(kodesumber_length == 0){
            $("#sumbername_error").html("*Nama sumber is required");
            $("#sumbername_error").show();
        }
        else{
			$("#sumbername_error").hide();
			error_sumbercode = true;
        }
    }

    function check_skim(){
        var skim_length = $("#skim_id").val().length;
        if(skim_length == 0){
            $("#skim_error").html("*SKIM is required");
            $("#skim_error").show();
		}
        else{
			$("#skim_error").hide();
			error_skim = true;
        }
    }

    function check_tglmulaiskim(){
        var tglmulaiskim_length = $("#tglmulaiskim").val().length;
        if(tglmulaiskim_length == 0){
            $("#tglmulaiskim_error").html("*Tanggal mulai is required");
            $("#tglmulaiskim_error").show();
		}
        else{
			$("#tglmulaiskim_error").hide();
			error_tglmulaiskim = true;
        }
    }

    function check_tglselesaiskim(){
        var tglselesaiskim_length = $("#tglselesaiskim").val().length;
        if(tglselesaiskim_length == 0){
            $("#tglselesaiskim_error").html("*Tanggal selesai is required");
            $("#tglselesaiskim_error").show();
		}
        else{
			$("#tglselesaiskim_error").hide();
			error_tglselesaiskim = true;
        }
    }

    function check_tahundana(){
        var tahundana = document.getElementById("tahun_dana").value;
        if(tahundana == ""){
            $("#danayear_error").html("*Tahun Sumber Dana is required");
            $("#danayear_error").show();
        }
        if(tahundana != ""){
            $("#danayear_error").hide();
        }
    }

    function check_sumberdana(){
        var sumberdana = document.getElementById("sumber_dana").value;
        if(sumberdana == ""){
            $("#sumberdana_error").html("*Kode Sumber Dana is required");
            $("#sumberdana_error").show();
        }
        else{
            $("#sumberdana_error").hide();
        }
    }

    function check_usulanskim(){
        var usulanskim = document.getElementById("skim").value;
        if(usulanskim == ""){
            $("#usulanskim_error").html("*SKIM is required");
            $("#usulanskim_error").show();
        }
        else{
            $("#usulanskim_error").hide();
        }
    }

    function check_judul(){
        var judulproposal = $("#Judul").val().length;
        if(judulproposal == 0){
            $("#judul_error").html("*Judul is required");
            $("#judul_error").show();
        }
        else{
            $("#judul_error").hide();
        }
    }

    function check_abstrak(){
        var abstrakproposal = $("#Abstrak").val().length;
        if(abstrakproposal == 0){
            $("#abstrak_error").html("*Abstrak is required");
            $("#abstrak_error").show();
        }
        else{
            $("#abstrak_error").hide();
        }
    }

    function check_bidang(){
        var bidangproposal = document.getElementById("bidang").value;
        if(bidangproposal == ""){
            $("#bidang_error").html("*Bidang is required");
            $("#bidang_error").show();
        }
        else{
            $("#bidang_error").hide();
        }
    }

    function check_dana(){
        var danaproposal = $("#dana").val();
        if(danaproposal == 0){
            $("#pengajuandana_error").html("*Pengajuan Dana is required");
            $("#pengajuandana_error").show();
        }
    
        if(danaproposal < 0){
            $("#pengajuandana_error").html("*Dana tidak boleh minus");
            $("#pengajuandana_error").show();
        }
    
        if(danaproposal != 0 && danaproposal > 0){
            $("#pengajuandana_error").hide();
        }
    }

    function check_anggota1(){
        var anggota1proposal = $("#anggota1").val();
    
        if(anggota1proposal == 0){
            $("#anggota1_error").html("*Anggota1 is required");
            $("#anggota1_error").show();
        }
        if(anggota1proposal != 0){
            $("#anggota1_error").hide();
        }
    }

    function check_anggota2(){
        var anggota2proposal = $("#anggota2").val();
    
        if(anggota2proposal == 0){
            $("#anggota2_error").html("*Anggota2 is required");
            $("#anggota2_error").show();
        }
        if(anggota2proposal != 0){
            $("#anggota2_error").hide();
        }
    }

    function check_pembimbing(){
        var pembimbingproposal = $("#pembimbing").val();
        if(pembimbingproposal == 0){
            $("#pembimbing_error").html("*Pembimbing is required");
            $("#pembimbing_error").show();
        }
        if(pembimbingproposal != 0){
            $("#pembimbing_error").hide();
        }
    }

    function fileValidation(){
        var fileInput = document.getElementById("file");
        var filePath = fileInput.value;
        var extFile = /(\.doc|\.docx|\.pdf)$/i;
        if(!extFile.exec(filePath)){
            $("#file_error").html("*File salah!");
            $("#file_error").show();
        }
        else{
            $("#file_error").hide();
        }
    }
});