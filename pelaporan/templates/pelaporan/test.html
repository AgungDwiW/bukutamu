<input type="text" name="uid" id = "uid">

<div class="form-group row" style="padding-bottom:1rem;">
                        <label class="control-label col-sm-2" for="nama">Tipe Aktivitas di 12 Basic:</label>
                        <div class="col-sm-10">
                            <select class="form-control inputsm" name="aktivitas_12" id="aktivitas_12" placeholder="Tipe id"  onchange="get_pelanggaran()" value = {{tamu.tipeid}}>
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
                            <select class="form-control inputsm" name="Subkategori" id="Subketegori"  onchange="get_pelanggaran()"  value = {{tamu.tipeid}}>
                            <option selected disabled>Pilih</option>
                            <optgroup label="Reaksi Orang">
                                <option >A1 Menyesuaikan APD</option>
                                <option >A2 Merubah Posisi</option>
                                <option >A3 Membenahi pekerjaan</option>
                                <option >A4 Menghentikan pekerjaan</option>
                                <option >A5 Memasang LOTO / grounding</option>
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
                    <div hidden id= "hidme"> Pelanggaran yang sama :
                    	<div class="row">
            <div class="table-responsive col-sm-12">
              <table class="table " id ="table" style=" overflow-y: scroll;
    max-height:250px;">
                <thead>
                  <tr >
                    <th class="w-25">Tanggal</th>
                     <th class="w-25">Area</th>
                    <th class="w-50">Departemen penanggung jawab</th>
                  </tr>
                </thead>
                <tbody>
                
                </tbody>
              </table>
            </div>
   					 </div>
                    </div>
<script type="text/javascript">
	const uid = document.getElementById('uid')
	const tipe12 = document.getElementById('aktivitas_12')
	const sub = document.getElementById('Subketegori')
	const hide = document.getElementById('hidme')
	const table = document.getElementById('table')
	uid.addEventListener("keyup", 
	function (event) {
		var xhttp = new XMLHttpRequest();
		xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
        	cur = JSON.parse(this.responseText)
            console.log(cur);
            
        }
    	};
		event.preventDefault();
	    if (event.which == 13 || event.keyCode == 13) {
	       console.log("ajax/" + uid.value)
	        xhttp.open("GET", "/pelaporan/tamu_ajax/" + uid.value, true);
			xhttp.send();
	        return false;
    }
	});
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
	function pelanggaran(json){
		content = json.pelanggaran
		if (content.length == 0){
			hide.hidden = true
			return false
		}
		else{
			for (a = 0; a<content.length;a++)
			{
				console.log(content[a])
				row = table.insertRow(1)
				cell1 = row.insertCell(0)
				cell2 = row.insertCell(1)
				cell3 = row.insertCell(2)
				hide.hidden = false	
				cell1.innerHTML = content[a].tanggal
				cell2.innerHTML = content[a].area
				cell3.innerHTML = content[a].departemen
			}
			
		}
	}
</script>
