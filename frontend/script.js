const form = document.getElementById('uploadForm');
form.addEventListener('submit', async e => {
  e.preventDefault();
  const file = form.foto.files[0];
  const data = new FormData();
  data.append('foto', file);
  await fetch('https://TUO_BACKEND_URL/upload', { method:'POST', body:data });
  alert('Foto inviata!');
});
