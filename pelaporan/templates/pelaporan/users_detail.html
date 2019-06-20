{%extends "pelaporan/template.html"%}
{%block title%} Detail Tamu {%endblock%}
{%block head%}
    {% load static %}
    
{%endblock%}

{%block title-table %}
Detail Tamu                 
{%endblock%}

{%block content%}
<div style="margin: auto;">
    <div class="row vertical-align">
        <div class="col-sm-6 center" style="margin: auto" >
            <img src = "{{tamu.image.url}}" width=80%  ></img>
            
            
        </div>
        <div class="col-sm-6 v-divider">
            
              <form action = class = "text-left"  onsubmit="validateForm()">
            

                <div class="form-group row"><!-- UID -->
                  <label class="control-label col-sm-3" for="UID">UID:</label>
                  <div class="col-sm-6">  
                    <input type="text" class="form-control inputsm" name="UID" id="UID" placeholder="UID" value = {{tamu.uid}} readonly > 
                  </div>
                  <div class="col-sm-3">
                    <input class="form-control inputsm" name="TID" id="TID" placeholder="Tipe id"  value = {{tamu.tipeid}} readonly>
                        
                  </div>
                </div>
                
                <br>
                
                <div class="form-group row"> <!-- nama -->
                  <label class="control-label col-sm-3" for="Nama">Nama:</label>
                  <div class="col-sm-9">  
                    <input type="text" class="form-control inputsm" name="Nama" id="Nama"  placeholder="Nama" readonly required  {%if tamu.nama_tamu%} readonly value = {{tamu.nama_tamu}} {%endif%}  >
                  </div>
                </div>
                
                <br>

                <div class="form-group row"> <!-- no HP -->
                  <label class="control-label col-sm-3" for="NoHP">Nomor HP:</label>
                  <div class="col-sm-9">  
                    <input type="number" class="form-control inputsm" name="NoHP" id="NoHP" placeholder="08xxxxxxxxxx" required {%if tamu.no_hp_tamu%} readonly value = {{tamu.no_hp_tamu}} {%endif%} readonly>
                  </div>
                </div>
                
                <br>

                <div class="form-group row"><!-- Jenis kelamin -->
                  <label class="control-label col-sm-3" for="kelamin">Jenis Kelamin:</label>
                  <div class="col-sm-9">  
                    <input class="form-control inputsm" name="Kelamin" id="Kelamin" placeholder="L/P" {%if tamu.jenis_kelamin %} readonly value = {{tamu.jenis_kelamin}} {%endif%} readonly>
                  </div>
                </div>
                
                <br>

                <div class="form-group row"> <!-- Institusi  -->
                  <label class="control-label col-sm-3" for="Institusi">Institusi:</label>
                  <div class="col-sm-9">  
                    <input type="text" class="form-control inputsm" name="Institusi" id="Institusi" placeholder="Institusi" required {% if tamu.perusahaan%} readonly value = {{tamu.perusahaan}} {%endif%} readonly>
                  </div>
                </div>
                
                
            </form>
        </div>
    </div>
</div>
<br>

<div style="margin: auto;">
    <div class="row vertical-align">
        <div class="col-sm-6 center" style="margin: auto" >
            <h3 style="text-align: center;">Data Jam kunjungan</h3>
            <canvas id="djampengunjung"></canvas>
            
        </div>
        <div class="col-sm-6 v-divider">
            <h3 style="text-align: center;">Data kunjungan</h3>
            <canvas id="dpengunjung"></canvas>
              
        </div>
    </div>
</div>
<br>
<div>
    <div class="row">
            <div class="table-responsive col-sm-12" style="overflow-y: scroll;
    max-height:250px;">
              <table id="table" class="table table-bordered table-hover"
                                    style="font-size:10pt; text-align:center; vertical-align:middle;" >
                <thead>
                  <tr >
                    <th class="w-25">Tanggal</th>
                     <th class="w-25">Bertemu dengan</th>
                    <th class="w-50">Keperluan</th>
                  </tr>
                </thead>
                <tbody>
                {%for item in kedatangan%}
                  <tr >
                    <td>{{item.tanggal_keluar}}</td>
                    <td>{{item.bertemu_dengan}}</td>
                    <td>{{item.alasan_kedatangan }}</td>
                  </tr>
                {%endfor%}
                </tbody>
              </table>
            </div>
    </div>
    <br>
    <br>
    <div class="row">
            <div class="table-responsive col-sm-12" style="overflow-y: scroll;
    max-height:250px;">
              <table id="table" class="table table-bordered table-hover"
                                    style="font-size:10pt; text-align:center; vertical-align:middle;" >
                  <tr >
                    <th style="min-width:5%;">Tanggal Pelanggaran</th>
                    <th style="min-width:8%;">12 Basic</th>
                    <th style="min-width:7%;">Sub Kategori</th>
                    <th style="min-width:5%;">+/-</th>
                    <th style="min-width:10%; max-width: 15%">Action Plan 1</th>
                    <th style="min-width:10%; max-width: 15%">Action Plan 2</th>
                    <th style="min-width:15%; max-width: 25%">Keterangan</th>
                  </tr>
                </thead>
                <tbody>
                {% for item in pelanggaran%}
                <tr>
                    <td style="vertical-align:middle;">{{item.tanggal_pelanggaran}}</td>
                    <td style="vertical-align:middle;">{{item.tipe_aktivitas_12}}</td>
                    <td style="vertical-align:middle;">{{item.sub_kategori}}</td>
                    <td style="vertical-align:middle;">{% if item.positif%} + {%else%} - {%endif%}</td>
                    <td style="vertical-align:middle;">{{item.action_plan1}}</td>
                    <td style="vertical-align:middle;">{{item.action_plan2}}</td>
                    <td style="vertical-align:middle;">{{item.keterangan}}</td>
                </tr>
                {%endfor%}
                </tbody>
              </table>
            </div>
    </div>
</div>

{%endblock%}
{%block script %}
var ctxL = document.getElementById("dpengunjung").getContext('2d');
  var mydpengunjung = new Chart(ctxL, {
    type: 'line',
    data: {

      labels: ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli" , "Agustus" , "September", "Oktober","November", "Desember"],
      datasets: [{
          label: "Jumlah kedatangan",
          data: [
            {% for item in bulan%}
            {{item}},
            {%endfor%}
          ],
          backgroundColor: [
            'rgba(105, 0, 132, .2)',
          ],
          borderColor: [
            'rgba(200, 99, 132, .7)',
          ],
          borderWidth: 2
        },
        {
          label: "Jumlah Pelanggaran",
          data: [
          {%for item in bulan_pel%}
          {{item}},
          {%endfor%}
          ],
          backgroundColor: [
            'rgba(0, 137, 132, .2)',
          ],
          borderColor: [
            'rgba(0, 10, 130, .7)',
          ],
          borderWidth: 2
        }
      ]
    },
    options: {
      responsive: true
    }
  });

var ctxL = document.getElementById("djampengunjung").getContext('2d');
  var mydpengunjung = new Chart(ctxL, {
    type: 'line',
    data: {

      labels: ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli" , "Agustus" , "September", "Oktober","November", "Desember"],
      datasets: [{
          label: "Jam kedatangan",
          data: [
            {% for item in bulan_jam%}
            {{item}},
            {%endfor%}
          ],
          backgroundColor: [
            'rgba(105, 0, 132, .2)',
          ],
          borderColor: [
            'rgba(200, 99, 132, .7)',
          ],
          borderWidth: 2
        },
        
      ]
    },
    options: {
      responsive: true
    }
  });
{%endblock%}