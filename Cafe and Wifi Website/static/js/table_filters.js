// filters.js
function filterTable() {
  var table, tr, i, j, td, txtValue;
  var filters = {
    location: document.getElementById('locationFilter').value,
    sockets: document.getElementById('socketsFilter').value,
    toilet: document.getElementById('toiletFilter').value,
    wifi: document.getElementById('wifiFilter').value,
    calls: document.getElementById('callsFilter').value,
    seats: document.getElementById('seatsFilter').value
  };

  table = document.getElementById("cafesTable");
  tr = table.getElementsByTagName("tr");

  for (i = 2; i < tr.length; i++) {
    var showRow = true;

    for (var key in filters) {
      if (filters[key]) {
        var columnIndex;
        switch (key) {
          case 'location':
            columnIndex = 1;
            break;
          case 'sockets':
            columnIndex = 2;
            break;
          case 'toilet':
            columnIndex = 3;
            break;
          case 'wifi':
            columnIndex = 4;
            break;
          case 'calls':
            columnIndex = 5;
            break;
          case 'seats':
            columnIndex = 6;
            break;
        }

        td = tr[i].getElementsByTagName("td")[columnIndex];
        if (td) {
          txtValue = td.textContent || td.innerText;
          if (filters[key] !== "" && txtValue !== filters[key]) {
            showRow = false;
            break;
          }
        }
      }
    }

    tr[i].style.display = showRow ? "" : "none";
  }
}



function resetFilters() {
  document.getElementById('locationFilter').value = "";
  document.getElementById('socketsFilter').value = "";
  document.getElementById('toiletFilter').value = "";
  document.getElementById('wifiFilter').value = "";
  document.getElementById('callsFilter').value = "";
  document.getElementById('seatsFilter').value = "";
  filterTable();
}


document.getElementById('locationFilter').addEventListener('change', filterTable);
document.getElementById('socketsFilter').addEventListener('change', filterTable);
document.getElementById('toiletFilter').addEventListener('change', filterTable);
document.getElementById('wifiFilter').addEventListener('change', filterTable);
document.getElementById('callsFilter').addEventListener('change', filterTable);
document.getElementById('seatsFilter').addEventListener('change', filterTable);
