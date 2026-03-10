async function loadClients(){

const response = await fetch("http://localhost:5000/clients")

const clients = await response.json()

document.getElementById("clientCount").innerText = clients.length

let table = document.getElementById("clientTable")

table.innerHTML = ""

clients.forEach(c => {

table.innerHTML += `
<tr>
<td>${c.hostname}</td>
<td>${c.ip}</td>
<td>${c.os}</td>
<td>${c.cpu}</td>
<td>${c.ram_gb} GB</td>
<td>${c.process_count}</td>
</tr>
`

})

}