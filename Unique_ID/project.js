
function func(){
    let user = document.getElementById('user').value;
    let time = new Date();
    let uniq_id = user + '_' + (Math.floor(Math.random() * (10000 - 999 ) ) + 1000).toString();
    document.getElementById('output').style.display="block"; 
    document.getElementById('output').innerHTML = '<B>Unique ID :</B> ' + uniq_id+'<br><br> <B>Username :</B> '+user +'<br><br> <B>Time :</B> ' + time;
}
