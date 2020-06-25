function changeTheme() {
  arr = ['#F7D52C', '#D6CA27', '#D8ED37', '#84D627', '#52F72C']
  color = arr[Math.floor(Math.random() * 5)]
  document.getElementById("change").style.backgroundColor = color;
}

