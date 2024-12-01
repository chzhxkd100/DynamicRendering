let displayedData = new Set();

async function fetchRequestWithError() {
  try {
    const url = `http://34.64.115.78:8080/pastebin/api/pastes/`;
    const response = await fetch(url);
    if (response.status >= 200 && response.status < 400) {
      const data = await response.json();
      for (var key in data) {
	const paste = data[key];
	if(!displayedData.has(paste['id'])){
          ndiv = document.createElement('div');
          ndiv.innerHTML = `<h3> ${data[key]['title']} </h3><p> ${data[key]['content']}</p><hr>`;
          pdiv = document.getElementById('pastes');
          pdiv.insertBefore(ndiv, pdiv.firstChild);
 	  displayedData.add(paste['id']);
	    if (pdiv.children.length > 10){
	      pdiv.removeChild(pdiv.lastChild);
	    }
	}

      }
    } else {
      console.log(`${response.statusText}: ${response.status} error`);
    }
  } catch (error) {
    console.log(error);
  }
}

fetchint = setInterval(fetchRequestWithError, 3*1000);

