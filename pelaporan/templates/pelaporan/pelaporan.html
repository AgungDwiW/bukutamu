{%extends "pelaporan/template.html"%}
{%block title%} Form Pelaporan {%endblock%}
{%block title-table %}
Form Pelaporan                   
{%endblock%}

{%block content%}
<div class="card table-responsive" style="border-radius: 0px !important;">
    <!-- /.card-header -->
    <div class="card-body">
            <!-- Grid -->
        <form id="msform" style="height:auto; width:auto;" method="post" onsubmit="return validateform()" action={% url 'pelaporan:submit'%} >
        <!-- fieldsets -->
        	{% csrf_token %}
            <fieldset>
                
                <div style="margin:auto;">
                    
                    <h4>Data Pelapor</h4>
                    <br>
                    <div class="form-group row" style="padding-bottom:1rem;">
                        <label class="control-label col-sm-2" for="nama">Nama Pelapor:</label>
                        <div class="col-sm-10">
                            <input type="text" name="nama_pelapor" id = "nama_pelapor" class = "form-control inputsm" required placeholder="Nama Pelapor"></div>
                    </div>
                        
                    <div class="form-group row" style="padding-bottom:1rem;"><!-- UID -->
                      <label class="control-label col-sm-2" for="UID">UID Pelapor:</label>
                      <div class="col-sm-7">  
                        <input type="text" required class="form-control inputsm" name="uid_pelapor" id="uid_pelapor" placeholder="UID Pelapor" value =   > 
                      </div>
                      <div class="col-sm-3" style="padding-bottom:1rem;">
                        <select class="form-control inputsm" name="tid_pelapor" id="tid_pelapor" placeholder="Tipe id" >
                            <option>KTP</option>
                            <option selected>Kartu Pegawai</option>
                            <option >SIM</option>
                        </select>
                      </div>
                    </div>  
                    
                    <hr style="display: block;" size="5">
                    <h4>Data Yang dilaporkan</h4>
                    <br>
                        
                    <div class="form-group row" style="padding-bottom:1rem;"><!-- UID -->
                      <label class="control-label col-sm-2" for="UID">UID :</label>
                      <div class="col-sm-7">  
                        <input type="text" class="form-control inputsm" required name="uid_pelaku" id="uid_pelaku"  placeholder="UID Pelaku" value =   > 
                      </div>
                      <div class="col-sm-3">
                        <select class="form-control inputsm" name="tid_pelaku" id="tid_pelaku" placeholder="Tipe id" disabled  value = {{tamu.tipeid}}>
                            <option>KTP</option>
                            <option >Kartu Pegawai</option>
                            <option >SIM</option>
                        </select>
                      </div>
                    </div>  
                    <div class="form-group row" style="padding-bottom:1rem;">
                        <label class="control-label col-sm-2" for="nama">Nama Pelapor:</label>
                        <div class="col-sm-10">
                            <input type = "text" name="nama_pelaku" onchange="get_tamu()"  class = "form-control inputsm" id= "nama" placeholder="Nama Pelanggar" name="nama_pelaku" readonly>
                            	</div>
                    </div>
                    <div class="form-group row" style="padding-bottom:1rem;">
                        <label class="control-label col-sm-2" for="nama">Institusi:</label>
                        <div class="col-sm-10">
                            <input type="text" name="Institusi_pelaku" id = "institusi" readonly class = "form-control inputsm" placeholder="Institusi Pelanggar"></div>
                    </div>
                    <div class="form-group row" style="padding-bottom:1rem;">
                        <label class="control-label col-sm-2" for="nama">No. Handphone:</label>
                        <div class="col-sm-10">
                            <input type="text" name="hp_pelaku" readonly  id = "no_hp" class = "form-control inputsm" placeholder="No. Handphone pelanggar"></div>
                    </div>
                    <div class="form-group row" style="padding-bottom:1rem;">
                        <label class="control-label col-sm-2" for="Tanggalpelanggaran">Tanggal Pelanggaran:</label>
                        <div class="col-sm-10">
                            <select name="tgl_langgar" required disabled class = "form-control inputsm" id = "tgl_langgar">
                                
                            </select>
                        </div>
                    </div>
                    
                    <div class="form-group row" style="padding-bottom:1rem;">
                        <label class="control-label col-sm-2" for="Tanggalpelanggaran">Area</label>
                        <div class="col-sm-10">
                            <select name="area" disabled class = "form-control inputsm" id = "area" >
                                <option>1</option>
                                <option>2</option>
                                <option>3</option>
                                <option>4</option>
                                <option>5</option>
                            </select>
                        </div>
                    </div>
                    <hr style="display: block;" size="5">
                    <div class="form-group row" style="padding-bottom:1rem;">
                        <label class="control-label col-sm-2"  for="nama">Tipe Aktivitas di 12 Basic:</label>
                        <div class="col-sm-10">
                            <select class="form-control inputsm" onchange="get_pelanggaran()" name="aktivitas_12" id="aktivitas_12" placeholder="Tipe id" disabled >
                            <option>Pilih</option>
                            <option >Work at Height</option>
                            <option >Chemical Product</option>
                            <option >Confined Space</option>
                            <option >Hazardous Gases</option>
                            <option >Fire evacuation</option>
                            <option >Equipment safety</option>
                            <option >Forklifts</option>
                            <option >Racks Pallets</option>
                            <option >Truck loading unloading</option>
                            <option >Work permits</option>
                            <option >Hazardous energy</option>
                            <option >Not related 12 basic</option>

                        </select>
                        </div>
                    </div>
                    <div class="form-group row" style="padding-bottom:1rem;">
                        <label class="control-label col-sm-2" for="nama">Sub Kategori:</label>
                        <div class="col-sm-10">
                            <select class="form-control inputsm" disabled onchange="get_pelanggaran()" name="Subkategori" id="Subketegori"   value = {{tamu.tipeid}}>
                            <option selected disabled>Pilih</option>
                            <optgroup label="Reaksi Orang">
                                <option >A1 Menyesuaikan APD</option>
                                <option >A2 Merubah Posisi</option>
                                <option >A3 Membenahi pekerjaan</option>
                                <option >A4 Menghentikan pekerjaan</option>
                                <option >A5 Memasang LOTO atau grounding</option>
                            </optgroup>
                            <optgroup label="Posisi Kerja & Ergonomi">
                                <option >B1 Membentur</option>
                                <option >B2 Terpukul</option>
                                <option >B3 Terjepit</option>
                                <option >B4 Terjatuh</option>
                                <option >B5 Kontak dengan suhu ekstrim</option>
                                <option >B6 Kontak dengan arus listrik</option>
                                <option >B7 Menghirup bahan kimia</option>
                                <option >B8 Bahan Kimia Terserap kulit</option>
                                <option >B9 Bahan Kimia tertelan</option>
                                <option >B10 Posisi Tubuh</option>
                                <option >B11 Jenis dan jumlah gerakan</option>
                                <option >B12 Mengankat beban</option>
                            </optgroup>
                            <optgroup label="APD">
                                <option >C1 Mata dan wajah</option>
                                <option >C2 Telinga</option>
                                <option >C3 Kepala</option>
                                <option >C4 Tangan dan lengan</option>
                                <option >C5 Kaki dan Tungkai</option>
                                <option >C6 Sistem pernafasan</option>
                                <option >C7 Dada dan badan</option>
                                <option >C8 Pakaian yang sesuai</option>
                            </optgroup>
                            <optgroup label="Perkakas dan Perlengkapan">
                                <option >D1 Sesuai dengan jenis pekerjaan</option>
                                <option >D2 Digunakan dengan benar</option>
                                <option >D3 Dalam kondisi aman</option>
                                <option >D4 Desain area kerja</option>
                                <option >D5 Perkakas denga pegangannya</option>
                                <option >D6 Getaran</option>
                                <option >D7 Suhu</option>
                                <option >D8 Pencahayaan</option>
                                <option >D9 Kebisingan</option>
                            </optgroup>
                            <optgroup label="Perkakas dan Perlengkapan">
                                <option >D1 Sesuai dengan jenis pekerjaan</option>
                                <option >D2 Digunakan dengan benar</option>
                                <option >D3 Dalam kondisi aman</option>
                                <option >D4 Desain area kerja</option>
                                <option >D5 Perkakas denga pegangannya</option>
                                <option >D6 Getaran</option>
                                <option >D7 Suhu</option>
                                <option >D8 Pencahayaan</option>
                                <option >D9 Kebisingan</option>
                            </optgroup>
                            <optgroup label="Housekeeping dan Prosedur">
                                <option >E1 Prosedur tidak memadai</option>
                                <option >E2 Prosedur tidak dipahami</option>
                                <option >E3 Prosedur Todak dipatuhi</option>
                                <option >E4 Menjalankan izin kerja</option>
                                <option >E5 Isu housekeeping</option>

                            </optgroup>

                            </select>

                        </div>
                    </div>   
                    <!-- <div class="form-group row" style="padding-bottom:1rem;" id = "hidme" hidden>
                        <div class="table-responsive">
                          <table class="table table-bordered table-hover" id = "table" style=" display: inline-block;
                overflow-y: scroll;
                max-height:250px;">
                            <thead>
                              <tr >
                                <th style="min-width:25%;">Tanggal</th>
                                <th style="min-width:5%;">Area</th>
                                <th style="min-width:70%;">Departemen penanggung jawab</th>
                              </tr>
                            </thead>
                            <tbody>
                            
                          </table>
                        </div>
                    </div> -->
                    <table id="table" class="table table-bordered table-hover"
                                    style="font-size:10pt; text-align:center; vertical-align:middle;" hidden>
                                    <thead>
                                        <th style="min-width:25%;">Tanggal</th>
                                <th style="min-width:5%;">Area</th>
                                <th style="min-width:70%;">Departemen penanggung jawab</th>
                                    </thead>
                                    <tbody>

                                    </tbody>
                            </tfoot>
                            </table>
                    <div class="form-group row" style="padding-bottom:1rem;">
                        <label class="control-label col-sm-2" for="nama">Positif/Negatif</label>
                        <div class="col-sm-10">
                            <select class="form-control inputsm" disabled name="positivity" id="positivity" placeholder="Tipe id"  value = {{tamu.tipeid}}>
                            <option selected value="0">Negatif</option>
                            <option value="1">Positif</option>

                        </select>
                        </div>
                    </div>
                     <div class="form-group row" style="padding-bottom:1rem;">
                        <label class="control-label col-sm-2"  hidden id = "AP1_lab" for="Action plan 1">Action plan 1:</label>
                        <div class="col-sm-10">
                            <input type="text" name="AP1" id = "AP1" hidden  class = "form-control inputsm" placeholder="Action plan 1" hidden></div>
                    </div>

                    <div class="form-group row" style="padding-bottom:1rem;">
                        <label class="control-label col-sm-2" id = "AP2_lab" hidden for="Action plan 2">Action plan 2:</label>
                        <div class="col-sm-10">
                            <input type="text" name="AP2" id = "AP2"  class = "form-control inputsm" placeholder="Action plan 2" hidden></div>
                    </div>
                    <div class="form-group row" style="padding-bottom:1rem;">
                        <label class="control-label col-sm-2" for="Action plan 2">Keterangan:</label>
                        <div class="col-sm-10">
                            <input type="text" name="keterangan" disabled id = "keterangan"  class = "form-control inputsm" placeholder="Keterangan"></div>
                    </div>

                    <div class="col-sm-12 center"> 
                        <input type="submit" name="submit" id = "submit" class="col-sm-12">
                    </div>


                    

                    
        </fieldset>
    </form>
</div>
    <!-- /.card-body -->
</div>
<!-- /.card -->
{%endblock%}

{% block script%}

var item = "{{json}}"
item = item.replace(/&quot;/g, "'")
item = JSON.stringify(eval("(" + item + ")"));
item = JSON.parse(item);
console.log(item)
const tanggal = document.getElementById("tgl_langgar")
const nama = document.getElementById("nama")
const institusi = document.getElementById("institusi")
const no_hp = document.getElementById("no_hp")
const uid = document.getElementById("uid_pelaku")
const tid = document.getElementById("tid_pelaku")
const tipe12 = document.getElementById('aktivitas_12')
const sub = document.getElementById('Subketegori')
const hide = document.getElementById('table')
const table = document.getElementById('table').getElementsByTagName('tbody')[0];
const positif = document.getElementById('positivity')
const ap1 = document.getElementById('AP1')
const ap2 = document.getElementById('AP2')
const ap1_lab = document.getElementById('AP1_lab')
const ap2_lab = document.getElementById('AP2_lab')
const ket = document.getElementById('keterangan')
const area = document.getElementById('area')
var valid = false
function activate(){
    tipe12.disabled = false
    sub.disabled = false
    positif.disabled = false
    ap1.disabled = false
    ap2.disabled = false
    ket.disabled = false
    tanggal.disabled = false
    area.disabled = false
}

function deactivate(){
    tipe12.disabled = true
    sub.disabled = true
    positif.disabled = true
    ap1.disabled = true
    ap2.disabled = true
    ket.disabled = true   
    tanggal.disabled = true
    area.disabled = true
}

function validateform(){
    var str_12 = tipe12.options[tipe12.selectedIndex].text
    var str_sub = sub.options[sub.selectedIndex].text
    if (str_12== "Pilih"  || str_sub== "Pilih"){
        return false
    }
    return valid
    
}

uid.addEventListener("keyup", 
    function (event) {
        var xhttp = new XMLHttpRequest();
        xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            cur = JSON.parse(this.responseText)
            activate()
            valid = true
            get_tamu(cur);

        }
        if (this.readyState == 4 &&this.status == 500) {
            deactivate();
            valid = false
            alert("data tamu tak dapat ditemukan")
        }
        };
        event.preventDefault();
        if (event.which == 13 || event.keyCode == 13) {
           console.log("tamu_ajax/" + uid.value)
            xhttp.open("GET", "/pelaporan/tamu_ajax/" + uid.value, true);
            xhttp.send();
            return false;
    }
    });
function get_tamu(cur){
    console.log(cur)
	institusi.value = cur['perusahaan']
    nama.value = cur['nama']
	no_hp.value = cur['hp']
	if (cur['tid'] == "KTP"){
		tid.options[0].selected = true
		console.log(tid.options[0].selected)
	}
	else{
		tid.options[2].selected = false
	}
    kedatangan  = cur['kedatangan']
	for (key in kedatangan){
        var option = document.createElement("option");
        option.text = kedatangan[key]
        option.value = key
        tanggal.add(option)
    }

};

function get_pelanggaran(){
    
    if (!((uid.value != "") && (tipe12.options[tipe12.selectedIndex].text != "Pilih" && sub.options[sub.selectedIndex].text!="Pilih"))){
        
        return false
    }
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
        cur = JSON.parse(this.responseText)
        console.log(cur);
        pelanggaran(cur);
    }};
    var str_12 = tipe12.options[tipe12.selectedIndex].text
    var str_sub = sub.options[sub.selectedIndex].text
    str_12 = str_12.replace(/ /g, "_");
    str_sub = str_sub.replace(/ /g, "_");
    query = "/pelaporan/pelanggaran_ajax/" +uid.value+"/"+str_12+"/"+ str_sub
    console.log(query)
    xhttp.open("GET", query, true);
    xhttp.send();
}
var flag = 0
function pelanggaran(json){
    content = json.pelanggaran
    ap1.hidden = true
    ap1.readOnly = false
    ap1.required = true
    ap1.value = ""
    ap1_lab.hidden = true
    ap2.hidden =true
    ap2_lab.hidden  = true
    ap2.formNoValidate = true
    if (content.length == 0){
        hide.hidden = true
        ap1_lab.hidden = false
        ap1.hidden = false
        console.log(ap1.hidden)

    }
    else{
        
        count = table.childElementCount
        
        for (a = 0; a<count; a++){
            
            table.deleteRow(0)
        }

        
        for (a = 0; a<content.length;a++)
        {
            console.log(content[a])
            row = table.insertRow(0)
            cell1 = row.insertCell(0)
            cell2 = row.insertCell(1)
            cell3 = row.insertCell(2)
            hide.hidden = false 
            cell1.innerHTML = content[a].tanggal
            cell2.innerHTML = content[a].area
            cell3.innerHTML = content[a].departemen
            if (content[a].ap1!=""){
                ap1.hidden = false
                ap1_lab.hidden = false
                ap1.readOnly = true
                ap1.value = content[a].ap1
                ap1.required = true
                flag = 1
                ap2.hidden = false
                ap2.required = true
                ap2_lab.hidden = false
                ap2.formNoValidate = false
            }
            if (content[a].ap2!=""){
                ap2.value = content[a].ap2
                
                ap2_lab.hidden= false
                ap2.readOnly = true
                
                flag = 2
            }
        }
        
    }
}


$('form input').on('keypress', function(e) {
    return e.which !== 13;
});
{%endblock%}