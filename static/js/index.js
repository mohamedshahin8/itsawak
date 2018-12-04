


function login(){
    InputUserN = document.getElementById('usrname').value;
    InputPass = document.getElementById('psw').value;
    
    const   UserProgAdmin = "Braheem";
    const   PassProgAdmin = "khalifa";  
        
    if  ( InputPass == PassProgAdmin && InputUserN == UserProgAdmin) {
        location.href="admin-dashboard/index.html"; 
    } else{
        $(".Incorrect").text("خطأ ف الرقم السرى او الإسم ");
    }

};

// --------------------------------- ADS ----------------------------------------

//---------------------------------- Main Page ADS

$("#Main-AD1 > div:gt(0)").hide();
setInterval(function() {
  $('#Main-AD1 > div:first')
    .fadeOut(2000)
    .next()
    .fadeIn(2000)
    .end()
    .appendTo('#Main-AD1');
}, 5000);

$("#Main-AD2 > div:gt(0)").hide();
setInterval(function() {
  $('#Main-AD2 > div:first')
    .fadeOut(2000)
    .next()
    .fadeIn(2000)
    .end()
    .appendTo('#Main-AD2');
}, 5000);


//---------------------------------- ClothesShop ADS

$("#ClothesShop-AD1 > div:gt(0)").hide();
setInterval(function() {
  $('#ClothesShop-AD1 > div:first')
    .fadeOut(2000)
    .next()
    .fadeIn(2000)
    .end()
    .appendTo('#ClothesShop-AD1');
}, 5000);

$("#ClothesShop-AD2 > div:gt(0)").hide();
setInterval(function() {
  $('#ClothesShop-AD2 > div:first')
    .fadeOut(2000)
    .next()
    .fadeIn(2000)
    .end()
    .appendTo('#ClothesShop-AD2');
}, 5000);


$("#ClothesShop-AD3 > div:gt(0)").hide();
setInterval(function() {
  $('#ClothesShop-AD3 > div:first')
    .fadeOut(2000)
    .next()
    .fadeIn(2000)
    .end()
    .appendTo('#ClothesShop-AD3');
}, 5000);

$("#ClothesShop-AD4 > div:gt(0)").hide();
setInterval(function() {
  $('#ClothesShop-AD4 > div:first')
    .fadeOut(2000)
    .next()
    .fadeIn(2000)
    .end()
    .appendTo('#ClothesShop-AD4');
}, 5000);
